from django.db import models

from datetime import datetime

# Create your models here.
class Task(models.Model):
    """
    Stores a Task
    """
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    created_by = models.CharField(max_length=200)
    created_on = models.DateField(default=datetime.today)
    due_date = models.DateField(default=datetime.today)

    class Meta:
        db_table = 'task'
        ordering = ['id']
    
    def __str__(self):
        return self.title