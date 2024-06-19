from django.core.management.base import BaseCommand
from mainapp.models import UniqueGroupId

class Command(BaseCommand):
    help = 'Update group_id of all UniqueGroupId instances'

    def handle(self, *args, **options):
        for unique_group_id in UniqueGroupId.objects.all():
            unique_group_id.group_id = unique_group_id.generate_unique_code()
            unique_group_id.save()