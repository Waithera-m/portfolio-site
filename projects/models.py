from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Languages(models.Model):
    """
    class facilitates the creation of language objects
    """
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Repo(models.Model):

    """
    class facilitates the creation of project objects
    """
    project_name = models.CharField(max_length=70)
    description = models.TextField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='projects/%Y/%m%d',null=True)
    languages = models.ManyToManyField(Languages)

    def __str__(self):
        return self.project_name

    def was_added_recently(self):

        """
        method return recently added projects
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
