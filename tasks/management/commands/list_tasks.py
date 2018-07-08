from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task

class Command(BaseCommand):
    help = 'Creates a task'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        tasks = filter(
                lambda t: not t.completed(),
                Task.objects.filter(completion__isnull=True)
        )
        print('\n'.join(map(lambda t: str(t), tasks)))
