from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email='sebastian@maachi.com').exists():
            user = User()
            user.email = 'sebastian@maachi.com'
            user.set_password('lascortinascerradas')
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True 
            user.save()