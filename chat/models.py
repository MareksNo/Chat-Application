from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    content = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def last_15_messages(cls):
        messages = cls.objects.order_by('-posting_date').all()[:15]
        return reversed(messages)
    
    @classmethod
    def create_message(cls, content, user):
        message = cls(content=content, user=user)
        message.save()

        return message
