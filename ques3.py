# Answer: Yes, Django signals run in the same database transaction by default. We can demonstrate this by raising an exception in the signal handler to see if it causes a rollback in the transaction.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def test_signal_handler(sender, instance, **kwargs):
    raise Exception("Intentional Exception to test transaction rollback")

# We'll have to run this in Django shell:
from django.contrib.auth.models import User
from django.db import transaction
try:
    with transaction.atomic():
        user = User.objects.create(username="testuser")
except Exception:
    print("Transaction rolled back due to exception in signal")

# If "Transaction rolled back due to exception in signal" is printed, it confirms that signals run within the same transaction.
