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

class CourseList(TemplateView):
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = courses
        return context

class Course:
    def __init__(self, name, image, description, grades):
        self.name = name
        self.image = image
        self.description = description
        self.grades = grades

courses = [
    Course("ChimiLab", "https://ibb.co/JqstCgc", "Students will learn how titan companies have exploded into the market by using chemistry! Whether it's cosmetics, cologne, household detergents or a variety of other products we use daily, chemistry is all around us. Students will learn how to become the next big entrepreneur through science!", "K-6th"),
    Course("DigiLab", "https://ibb.co/JqstCgc", "From designing blogs, to creating e-commerce sites or brand-building sites kids will learn about structure, content, layout, typography and design. Our tech savvy students will be designing and building web pages using HTML and CSS. Kids will take on “business missions” for potential clients in different fields and create mock websites for their clients. Throughout the class, students will learn about design flow and functionality and by the end of class students will have completed a website of their own.", "K-6th"),
    Course("APPrentice", "https://ibb.co/JqstCgc", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Little Big Investors", "https://ibb.co/JqstCgc", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Craft Your Brand", "https://ibb.co/JqstCgc", "Turn your love of fun craft projects into a profitable company! Learn how entrepreneurs have made a living through selling their do it yourself projects and understand how using technology and media can play a huge part in the success of your business.", "K-6th"),
    Course("Printing Profits", "https://ibb.co/JqstCgc", "Using different mediums learn how to easily design shirts, totes, and other textiles. Then use your unique designs to market and pitch your brand.", "K-6th"),
    Course("Build Your Class", "https://ibb.co/JqstCgc", "Put together a class for yourself. Is there a specific class that you want to take", "K-6th"),
]