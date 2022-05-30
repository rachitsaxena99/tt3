from django.forms import ModelForm
from testroom.models import *
class NwTst(ModelForm):
    class Meta:
        model= Test
        fields = ['start_dat']