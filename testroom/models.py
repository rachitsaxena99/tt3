from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    deadline = models.DateField(null=True,blank=True)
    question = models.TextField()
    heading = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    input = models.TextField()
    output = models.TextField()
    status = models.BooleanField(default=True)
    entries = models.ManyToManyField('TestCase', blank=True)
    def __str__(self):
        return self.heading

# class Example(models.Model):
#

class TestCase(models.Model):
    user = models.ForeignKey(User , models.CASCADE)
    code = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    output = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.user.username

