import django.dispatch

task_created = django.dispatch.Signal(providing_args=['task'])
task_error = django.dispatch.Signal(providing_args=['task'])
task_rescheduled = django.dispatch.Signal(providing_args=['task'])
task_failed = django.dispatch.Signal(providing_args=['task_id', 'completed_task'])
task_successful = django.dispatch.Signal(providing_args=['task_id', 'completed_task'])