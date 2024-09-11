#question 3 Answer
#By default, Django signals are executed within the same transaction as the code that triggered them. 
# This is especially true for signals like post_save, which run after the database commit. 
# If a transaction is rolled back, signal-related changes 
# (like database operations within the signal handler) are also rolled back.

#Code to demonstrate signals running within the same transaction:

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    instance.first_name = 'Updated'
    instance.save()
    print(f"Signal handler executed, first name updated to {instance.first_name}")

# Transaction block to trigger rollback
try:
    with transaction.atomic():
        user = User.objects.create(username='testuser')
        raise Exception("Rolling back transaction")
except Exception as e:
    pass

# Check if the user exists and if the first name was updated (it should not be)
try:
    user = User.objects.get(username='testuser')
    print(f"User first name: {user.first_name}")  # If rollback worked, this line won't run
except User.DoesNotExist:
    print("Transaction rolled back, no user created.")


#Since the transaction is rolled back, no user will be created, and the signal's attempt to update the user’s first name will not persist.
