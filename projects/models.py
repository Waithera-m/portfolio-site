from django.db import models
import datetime

# Create your models here.
class Repo(models.Model):

    """
    class facilitates the creation of project objects
    """
    project_name = models.CharField(max_length=70)
    description = models.TextField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

    