from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from question.models import  Category

class Doubt(models.Model):
    heading = models.CharField(max_length=200,blank=True,null=True)
    ques = models.TextField()
    meta = models.CharField(max_length=100, blank=True , null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    comments = models.ManyToManyField('Comment' , blank=True , related_name="comments")
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null=True , blank=True )
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


@receiver(post_save , sender=Doubt)
def create_meta(sender,instance,created, **kwargs):
    if created:
        ques = str(instance.ques)
        if len(ques)<100:
            instance.meta = ques[:len(ques)]
        else:
            instance.meta = ques[:99]
        instance.save()