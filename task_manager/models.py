from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True,
                              blank=True, related_name='task_groups')
    creation_date = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_default_group(cls, request):
        group, _ = cls.objects.get_or_create(name='Default', owner=request.user)
        return group

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=300)
    creation_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              null=True, blank=True, related_name='tasks')
    group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name='tasks',
                              null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content
