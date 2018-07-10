from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from tasks.models import Task
import datetime

class Command(BaseCommand):
    help = 'Lists unfinished tasks for the day'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        incomplete_recurring = Q(
                ~Q(completion__create_date__date=datetime.date.today()),
                recurring=True
        )
        incomplete_adhoc = Q(recurring=False, completion__isnull=True)

        tasks = Task.objects \
                .prefetch_related('completion_set') \
                .filter(incomplete_recurring | incomplete_adhoc)

        print('\n'.join(map(lambda t: str(t), tasks)))
