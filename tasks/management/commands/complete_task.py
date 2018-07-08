from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task, Completion

class Command(BaseCommand):
    help = 'Completes a task'

    def add_arguments(self, parser):
        parser.add_argument('task_pk', type=int)

    def handle(self, *args, **options):
        try:
            task = Task.objects.get(pk=options['task_pk'])
        except Task.DoesNotExist:
            raise CommandError('Task "%s" does not exist' % poll_id)
        
        print('Completing task:', task)

        Completion(task=task).save()

        print('Done')
