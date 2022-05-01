from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    publish_choice = (
        ('yes','yes'),
        ('no','no')
    )

    user = models.ForeignKey(User , on_delete=models.CASCADE)

    heading = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    meta = models.CharField(max_length=200 , blank=True,null=True)
    content = models.TextField()

    tags = models.ManyToManyField(Tag , blank=True)
    published = models.CharField(max_length=10 , choices=publish_choice , default='no')

    def __str__(self):
        return self.heading


class CommentArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True , blank=True , null=True)
    reaction = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return str(self.article.heading + ' ' +self.reaction)

class RelationArticle(models.Model):

    reaction_choic = (
        ('nothing','nothing'),
        ('dislike','dislike'),
        ('like','like')
    )
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    reaction = models.CharField(max_length=100 ,choices=reaction_choic , default='nothing')

    def __str__(self):
        return str(self.article.heading + ' ' +self.reaction)

