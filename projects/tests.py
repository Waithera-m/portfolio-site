from django.test import TestCase
from .models import Repo
import datetime
from django.utils import timezone
from django.urls import reverse

class RepoModelTests(TestCase):

    """
    class facilitates the creation of repo objects
    """
    def setUp(self):

        """
        method runs before all tests
        """
        self.repo = Repo('Partage','Partage is a simple flask application that allows users to view and comment on posts. Users can also use provided links to add new posts, update and delete existing posts','2020-05-21','https://github.com/Waithera-m/partage')

    def test_init(self):

        """
        method checks if objects are initialized properly
        """
        self.assertTrue(isinstance(self.repo,Repo))
    
    def test_was_added_recently(self):

        """
        method tests if class' was_added_recently() returns true if a project with a pub_date that is less than a day is published
        """
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59)
        recent_project = Repo(pub_date=time)
        self.assertIs(recent_project.was_added_recently(),True)

