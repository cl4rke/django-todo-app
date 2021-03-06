from django.db import models
from django.utils import timezone
import datetime


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    recurring = models.BooleanField()

    def __str__(self):
        completed = self.completed()
        completion = '✓' if completed else '✗'
        basic_info = "%s [%d] %s" % (completion, self.id, self.title)

        if completed:
            if self.description:
                return '%s: %s' % (basic_info, self.description)
            return basic_info

        last_touch_date = self.create_date

        if self.completion_set.exists():
            last_touch_date = self.completion_set.last().create_date

        days_old = (timezone.now() - last_touch_date).days
        day_unit = ('day' if days_old == 1 else 'days') + ' old'
        age_info = '(%s %s)' % (days_old, day_unit) \
                if days_old else ''

        if self.description:
            return '%s: %s %s' % (
                    basic_info,
                    self.description,
                    age_info
            )
        return '%s %s' % (basic_info, age_info)

    def completed(self):
        if self.recurring:
            return self.completion_set \
                    .filter(create_date__date=datetime.date.today()) \
                    .exists()

        return len(self.completion_set.all()) > 0


class Completion(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.task, self.create_date)
