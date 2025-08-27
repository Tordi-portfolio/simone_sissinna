from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PrivateChat
from .forms import MessageForm, RegisterForm


# ---------------- Home Page ----------------

def home(request):
    return render(request, 'home.html')


# ---------------- Authentication ----------------

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=full_name
                )
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'logins/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'logins/login.html')


@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')


# ---------------- Chat System ----------------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from .models import PrivateChat
from .forms import MessageForm

# USER CHATS WITH ADMIN
@login_required
def chat_with_admin(request):
    admin = User.objects.filter(is_staff=True).first()
    if not admin:
        messages.error(request, "Admin not available.")
        return redirect('home')

    PrivateChat.objects.filter(sender=admin, recipient=request.user, is_read=False).update(is_read=True)

    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        file = request.FILES.get('file')

        if message_text or file:
            PrivateChat.objects.create(
                sender=request.user,
                recipient=admin,
                message=message_text,
                file=file
            )
            return redirect('chat_with_admin')

    chats = PrivateChat.objects.filter(
        Q(sender=request.user, recipient=admin) | Q(sender=admin, recipient=request.user)
    ).order_by('timestamp')

    return render(request, 'chat/chat_user.html', {
        'messages': chats,
        'admin': admin
    })



# ADMIN SEES LIST OF USERS
@login_required
def admin_user_list(request):
    if not request.user.is_staff:
        return redirect('home')

    users = User.objects.filter(is_staff=False)
    return render(request, 'chat/admin_user_list.html', {'users': users})


# ADMIN CHATS WITH SPECIFIC USER
@login_required
def admin_chat_view(request, user_id):
    if not request.user.is_staff:
        return redirect('home')
    
    user = get_object_or_404(User, id=user_id)
    PrivateChat.objects.filter(sender=user, recipient=request.user, is_read=False).update(is_read=True)

    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        file = request.FILES.get('file')

        if message_text or file:
            PrivateChat.objects.create(
                sender=request.user,
                recipient=user,
                message=message_text,
                file=file
            )
            return redirect('admin_chat_view', user_id=user.id)

    chats = PrivateChat.objects.filter(
        Q(sender=request.user, recipient=user) | Q(sender=user, recipient=request.user)
    ).order_by('timestamp')

    return render(request, 'chat/chat_admin.html', {
        'messages': chats,
        'user': user
    })

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import PrivateChat

@login_required
def get_new_messages(request):
    if request.user.is_staff:
        unread_count = PrivateChat.objects.filter(is_read=False).exclude(sender=request.user).count()
        latest_message = PrivateChat.objects.filter(is_read=False).exclude(sender=request.user).order_by('-timestamp').first()
    else:
        unread_count = PrivateChat.objects.filter(recipient=request.user, is_read=False).count()
        latest_message = PrivateChat.objects.filter(recipient=request.user, is_read=False).order_by('-timestamp').first()

    message_text = latest_message.message if latest_message else ""

    return JsonResponse({
        'unread_count': unread_count,
        'latest_message': message_text
    })


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import PrivateChat  # Import your model

@login_required
def get_unread_count(request):
    count = PrivateChat.objects.filter(recipient=request.user, is_read=False).count()
    return JsonResponse({'unread_count': count})


def diana(request):
    return render(request, 'fans/diana.html')

def fanspage(request):
    return render(request, 'fans/fanspage.html')