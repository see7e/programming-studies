from django.db import models
from register_login.models import CustomUser

TASK_CHOICES = [
    ("pending", "Pending"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
]
TASK_TYPES = [
    # ('receiving', 'Receiving'), # Inbound
    # ('putaway', 'Putaway'), # Inbound
    ("picking", "Picking"),  # Outbound
    ("packing", "Packing"),  # Outbound
    ("shipping", "Shipping"),  # Outbound
]

# Following the EDA
class Event(models.Model):
    description = models.TextField()
    application = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    type = models.CharField(max_length=50, choices=TASK_TYPES)
    status = models.CharField(max_length=20, choices=TASK_CHOICES, default="pending")
    created_by = models.ForeignKey(
        CustomUser, related_name="created_by", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        CustomUser, related_name="updated_by", on_delete=models.CASCADE
    )
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     created = not self.pk
    #     super().save(*args, **kwargs)
    #     if created:
    #         # Emit event when a new task is created
    #         Event.objects.create(name='TaskCreated', description=f'Task {self.id} created')
    #     else:
    #         # Emit event when a task is updated
    #         Event.objects.create(name='TaskUpdated', description=f'Task {self.id} updated')

    # def complete(self):
    #     # Mark task as completed and emit event
    #     self.status = 'completed'
    #     self.save()
    #     Event.objects.create(name='TaskCompleted', description=f'Task {self.id} completed')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.type} - {self.status} - {self.start_date} - {self.due_date}"
