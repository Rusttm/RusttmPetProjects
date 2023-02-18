from django.db import models

# Create your models here.

from django.forms import ModelForm

class Equations(models.Model):
    function_string = models.CharField(help_text="Please b", max_length=100, default="sin(x)")
    left_edge = models.IntegerField(default=-10)
    right_edge = models.IntegerField(default=10)
    accuracy = models.IntegerField(default=3)
    date_field = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.function_string

class EquationForm(ModelForm):
    class Meta:
        model = Equations
        fields = ['function_string', 'left_edge', 'right_edge', 'accuracy']



