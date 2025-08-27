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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, ProjectViewSet, TagViewSet, ApiTestView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-test/', ApiTestView.as_view(), name='api-test'),
]
