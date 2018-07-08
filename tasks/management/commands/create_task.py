from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task

class Command(BaseCommand):
    help = 'Creates a task'

    def add_arguments(self, parser):
        parser.add_argument('title')

        parser.add_argument(
            '--description',
            '-D',
            nargs=1,
            dest='description',
            help='Add a description to a task',
        )

        parser.add_argument(
            '--recurring',
            '-R',
            action='store_true',
            dest='recurring',
            help='Make a task recurring',
        )

    def handle(self, *args, **options):
        task = Task(
                title=options['title'],
                description=options['description'],
                recurring=options['recurring'],
        )

        print('Creating task:', task.title)

        task.save()

        print('Done!')
