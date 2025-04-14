from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=200) # Indicates text
    description = models.TextField(blank=True) # Large texts
    done = models.BooleanField(default=False) # This is like an status flag that indicates whether the task is done or not
    def __str__(self):  # To watch the title of the task in the admin panel of the default server.
        return self.title
    