from django.urls import path, include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')
url_patterns = [
    path('api/v1', include(router.urls))
]

# All of this code is equivalent to DELETE, POST, GET, PUT, ...