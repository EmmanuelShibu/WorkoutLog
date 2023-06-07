from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from workoutlog.models import Category,Exercise,Workout

import datetime

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1','password2']

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model=Exercise
        fields=['name','category']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise', 'reps', 'best_weight', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
