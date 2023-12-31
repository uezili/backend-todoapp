from django.urls import path
from .views import CreateUserView, UserDetailsView, CustomAuthToken,TaskListCreateView, TaskDetailView


# urls.py

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='user_details'),

]
