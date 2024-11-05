# Answer: By default, Django signals are executed synchronously, meaning they run in the same thread as the code that triggers them and wait for the signal handler to complete before proceeding.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def test_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")

# We'll have to run this in Django shell:
from django.contrib.auth.models import User
user = User.objects.create(username="testuser")

# The code will pause for 5 seconds as it waits for the signal handler to complete, indicating synchronous execution.