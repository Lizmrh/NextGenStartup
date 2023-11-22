from typing import Any
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# class Home(View):
#     def get(self, request):
#         return HttpResponse("Prova")

class Home(TemplateView):
    template_name = "home.html"

class About_OurMission(TemplateView):
    template_name = "About_OurMission.html"

class About_EducationalPods(TemplateView):
    template_name = "About_EducationalPods.html"

class About_Schools(TemplateView):
    template_name = "About_Schools.html"

class About_ForParents(TemplateView):
    template_name = "About_ForParents.html"

class About_MainGallery(TemplateView):
    template_name = "About_MainGallery.html"


class OurProgram_AfterSchoolClasses(TemplateView):
    template_name = "OurProgram_AfterSchoolClasses.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = courses
        return context
    
class OurProgram_VacationCamps(TemplateView):
    template_name = "OurProgram_VacationCamps.html"

class OurProgram_PrivateSessions(TemplateView):
    template_name = "OurProgram_PrivateSessions.html"


class Course:
    def __init__(self, name, image, description, grades):
        self.name = name
        self.image = image
        self.description = description
        self.grades = grades

courses = [
    Course("ChimiLab", "https://i.ibb.co/SJ3QdMc/01-01.png", "Students will learn how titan companies have exploded into the market by using chemistry! Whether it's cosmetics, cologne, household detergents or a variety of other products we use daily, chemistry is all around us. Students will learn how to become the next big entrepreneur through science!", "K-6th"),
    Course("DigiLab", "https://i.ibb.co/CHYFJfV/Yellow-Black-Playful-Lamp-Bulb-Idea-Company-Logo.png", "From designing blogs, to creating e-commerce sites or brand-building sites kids will learn about structure, content, layout, typography and design. Our tech savvy students will be designing and building web pages using HTML and CSS. Kids will take on “business missions” for potential clients in different fields and create mock websites for their clients. Throughout the class, students will learn about design flow and functionality and by the end of class students will have completed a website of their own.", "K-6th"),
    Course("APPrentice", "https://i.ibb.co/ccWS1sx/digilab.png", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Little Big Investors", "https://i.ibb.co/0JLYnM4/littlebiginvestor.png", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Craft Your Brand", "https://i.ibb.co/1RqRYNr/crafturbrand.png", "Turn your love of fun craft projects into a profitable company! Learn how entrepreneurs have made a living through selling their do it yourself projects and understand how using technology and media can play a huge part in the success of your business.", "K-6th"),
    Course("Printing Profits", "https://i.ibb.co/ygYRmVn/printingprfts.png", "Using different mediums learn how to easily design shirts, totes, and other textiles. Then use your unique designs to market and pitch your brand.", "K-6th"),
    Course("Build Your Class", "https://i.ibb.co/3BSc9Hn/buildurclass.png", "Put together a class for yourself. Is there a specific class that you want to take", "K-6th"),
]