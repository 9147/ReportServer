from django.test import TestCase
from django.utils import timezone
from models import Commit
# Create a new Commit object
new_commit = Commit.objects.create(
    admission_no="New commit message",
)
print(new_commit)
