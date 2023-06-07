from django.urls import path

from workoutlog import views

urlpatterns=[
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('signin/',views.SigninView.as_view(),name='signin'),
    path('home/',views.WorkoutLogIndexView.as_view(),name='workoutlog-home'),
    path('categories/home/',views.CategoryIndexView.as_view(),name='category-home'),
    path('categories/add/',views.CategoryCreateView.as_view(),name='category-add'),
    path('categories/all/',views.CategoryListView.as_view(),name='category-list'),
    path('category/remove/<int:pk>',views.category_delete_view,name='category-remove'),
    path('category/change/<int:pk>',views.CategoryUpdateView.as_view(),name='category-update'),
    path('exercises/home/',views.ExerciseHomeView.as_view(),name='exercise-home'),
    path('exercises/add/',views.ExerciseCreateView.as_view(),name='exercise-add'),
    path('exercises/all/',views.ExerciseListView.as_view(),name='exercise-list'),
    path('exercise/remove/<int:pk>/',views.exercise_delete_view,name='exercise-remove'),
    path('exercise/change/<int:pk>/',views.ExerciseUpdateView.as_view(),name='exercise-update'),
    path('workouts/home/',views.WorkoutHomeView.as_view(),name='workout-home'),
    path('workouts/add/',views.WorkoutCreateView.as_view(),name='workout-add'),
    path('workouts/all/',views.WorkoutListView.as_view(),name='workout-list'),
    ]