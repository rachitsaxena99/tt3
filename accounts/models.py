from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from question.models import Company
class Profile(models.Model):
    profession = (
        ('student','student'),
        ('teacher','teacher'),
        ('other','other'),
    )
    user = models.OneToOneField(User , related_name='profile' , on_delete=models.CASCADE)
    profession = models.CharField(max_length=100 , default='other')
    about = models.TextField(blank=True)
    experience = models.ManyToManyField('Experience' , blank=True)
    # connections = models.ManyToManyField('Connection' , blank=True, related_name='connection')
    def __str__(self):
        return self.user.username

class Connection(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Experience(models.Model):
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    designation = models.CharField(max_length=1000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

@receiver(post_save , sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

