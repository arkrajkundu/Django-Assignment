# Answer: Yes, Django signals run in the same thread as the caller by default. This can be demonstrated by comparing the thread IDs of the caller and the signal handler.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def test_signal_handler(sender, instance, **kwargs):
    print("Signal handler thread:", threading.current_thread().ident)

# We'll have to run this in Django shell:
from django.contrib.auth.models import User
import threading
print("Main thread:", threading.current_thread().ident)
user = User.objects.create(username="testuser")

# You should see that the thread IDs printed are the same, proving that the signal handler runs in the same thread.
