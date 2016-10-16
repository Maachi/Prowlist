from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@maachi.com").exists():
            User.objects.create_superuser("admin@maachi.com", "lascortinascerradas")
