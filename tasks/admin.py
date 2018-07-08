from django.contrib import admin

from .models import Task, Completion

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        'create_date',
        'modify_date',
    )

class CompletionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'create_date',
        'modify_date',
    )

admin.site.register(Task, TaskAdmin)
admin.site.register(Completion, CompletionAdmin)
