from django.db import models

# Create your models here.
class Task (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField(blank=True,null=True)
    priority=models.IntegerField(default=1)    
    def __str__(self):
        return f"{self.title}(Priority: {self.priority})"    