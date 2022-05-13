from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    units = models.ManyToManyField('Unit', blank=True, related_name='units')
    img = models.ImageField(null=True , blank=True)
    def __str__(self):
        return self.name




class Unit(models.Model):
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    unitNo = models.IntegerField(default=1)
    file = models.FileField(null=True, blank=True)
    def __str__(self):
        return str((self.subject.name) + ' ' + str(self.unitNo))

    class Meta:
        unique_together = ('unitNo','subject')
        ordering = ['unitNo']