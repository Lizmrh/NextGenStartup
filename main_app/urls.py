from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('courses/', views.CourseList.as_view(), name="course_list")
]