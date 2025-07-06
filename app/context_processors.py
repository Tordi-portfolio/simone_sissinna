from .models import PrivateChat

def unread_message_count(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            count = PrivateChat.objects.filter(recipient=request.user, is_read=False).count()
            return {'admin_unread_count': count}
        else:
            count = PrivateChat.objects.filter(recipient=request.user, is_read=False).count()
            return {'user_unread_count': count}
    return {}
