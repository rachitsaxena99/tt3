from django.db import models
from django.contrib.auth.models import User


class Doubt(models.Model):
    ques = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(null=True , blank=True)
    date = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    comments = models.ManyToManyField('Comment' , blank=True , related_name="comments")
    def __str__(self):
        return str(self.ques + ' ' + self.user.username)


class Comment(models.Model):
    body = models.CharField(max_length=1000 )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    doubt = models.ForeignKey(Doubt , on_delete=models.CASCADE)
    subComment = models.ManyToManyField('subComment' , blank=True)
    def __str__(self):
        return self.body


class subComment(models.Model):
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doubt = models.ForeignKey(Doubt , on_delete=models.CASCADE)
    def __str__(self):
        return self.body
