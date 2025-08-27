from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Urgent'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='todos')
    tags = models.ManyToManyField(Tag, blank=True, related_name='todos')

    title = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    due_date = models.DateTimeField(null=True, blank=True)
    recurrence = models.CharField(max_length=100, null=True, blank=True)  # e.g., 'daily', 'weekly', 'monthly'
    metadata = models.JSONField(default=dict, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
