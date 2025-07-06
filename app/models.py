from django.db import models
from django.contrib.auth.models import User

class PrivateChat(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    file = models.FileField(upload_to='chat_uploads/', blank=True, null=True)  # Supports images/videos
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.username} to {self.recipient.username}: {self.message[:20]}'
