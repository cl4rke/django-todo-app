from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task
import datetime

class Command(BaseCommand):
    help = 'Lists unfinished tasks for the day'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        tasks = Task.objects.filter(
                completion__isnull=True
        ).exclude(
                completion__create_date__date=datetime.date.today()
        )
        print('\n'.join(map(lambda t: str(t), tasks)))
