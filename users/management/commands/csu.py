from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test_test@test.ru',
            first_name='admin',
            last_name='admin'
        )

        user.set_password('123098Olga')
        user.save()
