from datetime import datetime as now, timedelta
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=2048)
    datetime = models.DateTimeField(auto_created=True, default=now.now())
    deadline = models.DateTimeField(auto_created=False, default=now.now()+timedelta(days=30))
    done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["done", "-datetime"]


