from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('courses/', views.CourseList.as_view(), name="course_list"),
    path('about/OurMission', views.About_OurMission.as_view(), name="About_OurMission"),
    path('about/EducationalPods', views.About_EducationalPods.as_view(), name="About_EducationalPods"),
    path('about/Schools', views.About_Schools.as_view(), name="About_Schools"),
    path('about/ForParents', views.About_ForParents.as_view(), name="About_ForParents"),
    path('about/MainGallery', views.About_MainGallery.as_view(), name="course_About_MainGallery"),
]