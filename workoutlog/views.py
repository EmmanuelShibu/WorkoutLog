from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,View,FormView,TemplateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

from workoutlog.models import Category,Exercise,Workout
from workoutlog.forms import RegistrationForm,SigninForm,CategoryForm,ExerciseForm,WorkoutForm

# Create your views here.

class RegistrationView(CreateView):
    form_class=RegistrationForm
    model=User
    template_name='register.html'
    success_url=reverse_lazy('signin')

class SigninView(FormView):
    form_class=SigninForm
    template_name='signin.html'
    success_url=reverse_lazy('workoutlog-home')


    def post(self,request,*args,**kwargs):
        form=SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('workoutlog-home')
        else:
            return render(request, self.template_name, {'form': form})

class WorkoutLogIndexView(TemplateView):
    template_name='workoutlog-home.html'

class CategoryIndexView(TemplateView):
    template_name='category-home.html'

class CategoryCreateView(CreateView):
    model=Category
    form_class=CategoryForm
    template_name='category-add.html'
    success_url=reverse_lazy('category-list')

class CategoryListView(ListView):
    model=Category
    context_object_name='categories'
    template_name='category-list.html'

def category_delete_view(request,*args,**kwargs):
    id=kwargs.get('pk')
    Category.objects.get(id=id).delete()
    return redirect('category-list')

class CategoryUpdateView(UpdateView):
    model=Category
    form_class=CategoryForm
    template_name='category-update.html'
    success_url=reverse_lazy('category-list')

class ExerciseHomeView(TemplateView):
    template_name='exercise-home.html'

class ExerciseCreateView(CreateView):
    model=Exercise
    form_class=ExerciseForm
    template_name='exercise-add.html'
    success_url=reverse_lazy('exercise-list')

class ExerciseListView(ListView):
    model=Exercise
    context_object_name='exercises'
    template_name='exercise-list.html'

def exercise_delete_view(request,*args,**kwargs):
    id=kwargs.get('pk')
    Exercise.objects.get(id=id).delete()
    return redirect('exercise-list')

class ExerciseUpdateView(UpdateView):
    model=Exercise
    form_class=ExerciseForm
    template_name='exercise-update.html'
    success_url=reverse_lazy('exercise-list')

class WorkoutHomeView(TemplateView):
    template_name='workout-home.html'

class WorkoutCreateView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout-add.html'
    success_url = reverse_lazy('workout-list')



class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout-list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get the filter parameters from the request
        date = self.request.GET.get('date')
        
        # Apply filters if they exist
        if date:
            queryset = queryset.filter(date=date)
        
        return queryset


