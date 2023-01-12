from django.db.models.signals import post_save
from meet.models import Room
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender = Room )
def send_mail(sender,instance,created, **kwargs):
    if created:
     send_mail(
    'CHAT REQUEST ACCEPTED',      #got SMTPAuthenticationError
    'YOU CAN NOW CHAT WITH USER. CHAT ROOM ='+ instance.name, 
    'd91771639@gmail.com',
    ['sameersingla400@gmail.com'],
    fail_silently=False,
)

