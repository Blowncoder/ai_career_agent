from django.db import models

class ChatLog(models.Model):
    user_message = models.TextField(null=True, blank=True)
    ai_response = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: {self.user_message[:20]}..."