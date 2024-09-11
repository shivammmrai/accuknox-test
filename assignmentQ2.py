#question 2 Answer
#Yes, Django signals run in the same thread as the caller. To prove this, we can print the current thread ID in both the signal 
# handler and the code that triggers the signal.
# Code to demonstrate signal running in the same thread:

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()}")


print(f"Main code running in thread: {threading.get_ident()}")
user = User.objects.create(username='testuser')



#In the output, both the main code and the signal handler will print the same thread ID, 
# proving that signals run in the same thread as the caller.
