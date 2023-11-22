from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/OurMission', views.About_OurMission.as_view(), name="About_OurMission"),
    path('about/EducationalPods', views.About_EducationalPods.as_view(), name="About_EducationalPods"),
    path('about/Schools', views.About_Schools.as_view(), name="About_Schools"),
    path('about/ForParents', views.About_ForParents.as_view(), name="About_ForParents"),
    path('about/MainGallery', views.About_MainGallery.as_view(), name="course_About_MainGallery"),
    
    path('ourProgram/AfterSchoolClasses', views.OurProgram_AfterSchoolClasses.as_view(), name="OurProgram_AfterSchoolClasses.html"),
    path('ourProgram/VacationCamps', views.OurProgram_VacationCamps.as_view(), name="OurProgram_VacationCamps.html"),
    path('ourProgram/PrivateSessions', views.OurProgram_PrivateSessions.as_view(), name="OurProgram_PrivateSessions.html"),
]