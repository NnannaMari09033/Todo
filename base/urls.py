from django.urls import path
from django.shortcuts import redirect
from .views import CustomLoginView, CustomLogoutView, RegisterPage, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskReorder

urlpatterns = [
    path('', lambda request: redirect('tasks'), name='home'),  # Redirect root URL to 'tasks'
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('tasks/reorder/', TaskReorder.as_view(), name='task-reorder'),
]
