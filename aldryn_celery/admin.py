from django.contrib import admin
import djcelery.models
import celery


# hide unused Tables from admin
# these would require the obsolete ``manage.py celerycam`` to be running.
try:
    admin.site.unregister(djcelery.models.TaskState)
except Exception as e:
    print e
try:
    admin.site.unregister(djcelery.models.WorkerState)
except Exception as e:
    print e


# show task results from the database result backend
class TaskMetaAdmin(admin.ModelAdmin):
    detail_title = 'Task Result'
    detail_title = 'Task Results'
    list_display = (
        'task_id',
        'status',
        'date_done',
        'hidden',
    )
    date_hierarchy = ''
    readonly_fields = (
        'result',
    )


admin.site.register(djcelery.models.TaskMeta, TaskMetaAdmin)
