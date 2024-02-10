from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.html import escape

from .models import Task, TaskGroup


def refresh_app(request, /, active_group=None):
    if not active_group:
        active_group = TaskGroup.get_default_group(request=request)

    tasks = request.user.tasks.filter(group_id=active_group.pk).order_by('done', '-creation_date')
    groups = request.user.task_groups.order_by('creation_date')

    return render(request, 'task_manager/partials/app_container.html',
                  {'task_list': tasks, 'group_list': groups, 'active_groupe': active_group})


def refresh_tasks(request, /, active_group=None):
    if not active_group:
        active_group = TaskGroup.get_default_group(request=request)

    tasks = request.user.tasks.filter(group_id=active_group.pk).order_by('done', '-creation_date')

    return render(request, 'task_manager/partials/task_list.html',
                  {'task_list': tasks, 'active_groupe': active_group})


@login_required
def home(request):
    active_group = TaskGroup.get_default_group(request=request)
    tasks = request.user.tasks.filter(group_id=active_group.pk).order_by('done', '-creation_date')
    groups = request.user.task_groups.order_by('creation_date')

    return render(request, 'task_manager/index.html',
                  {'task_list': tasks, 'group_list': groups, 'active_groupe': active_group})


@login_required
@require_http_methods(['POST'])
def add_task(request, group_id):
    content = escape(request.POST['add-task-input'])
    active_group = TaskGroup.objects.get(id=group_id)
    Task.objects.create(content=content, owner=request.user, group=active_group)

    return refresh_tasks(request, active_group=active_group)


@login_required
@require_http_methods(['DELETE'])
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    active_group = task.group
    task.delete()

    return refresh_tasks(request, active_group=active_group)


@login_required
@require_http_methods(['POST'])
def switch_task_state(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = not task.done
    task.save()
    active_group = task.group

    return refresh_tasks(request, active_group=active_group)


@login_required
@require_http_methods(['POST'])
def add_group(request):
    name = escape(request.POST['add-group-input'])
    active_group = TaskGroup.objects.create(name=name, owner=request.user)

    return refresh_app(request, active_group=active_group)


@login_required
def change_group(request, group_id):
    active_group = TaskGroup.objects.get(pk=group_id)

    return refresh_app(request, active_group=active_group)


@login_required
@require_http_methods(['DELETE'])
def delete_group(request, group_id):
    group = TaskGroup.objects.get(pk=group_id)
    group.delete()
    active_group = TaskGroup.get_default_group(request=request)

    return refresh_app(request, active_group=active_group)


def sort_group(request):
    return None