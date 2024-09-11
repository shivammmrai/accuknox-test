#question 1 Answer
#By default, Django signals are executed synchronously. That means when a signal is sent, all connected receivers are called immediately before 
# the flow of control is returned to the code after the signal is sent.

#Code to demonstrate synchronous execution:

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received, starting process...")
    time.sleep(5)  # Simulate a time-consuming task
    print("Signal processing complete.")

# Trigger the signal by saving a user
user = User.objects.create(username='testuser')

# Output will clearly show the synchronous nature due to the delay from time.sleep()




