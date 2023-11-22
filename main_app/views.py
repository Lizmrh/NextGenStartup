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
    Course("ChimiLab", "https://i.ibb.co/SJ3QdMc/01-01.png", "Get ready for an explosive adventure in our after-school class where young minds discover the magical world where chemistry meets business brilliance! 🌟 Dive into the secrets behind titan companies that have rocked the market with products we use every day, from dazzling cosmetics to household superheroes like detergents.  Join us as we unravel the chemistry woven into the fabric of our daily lives and cultivate essential skills for leadership and entrepreneurship. 🌟 Develop the knack for innovation, hone problem-solving abilities, and ignite creativity—the perfect recipe for young leaders of the future! Join us for a journey of discovery and skill-building that goes beyond the classroom. 🔬💡✨", "K-6th"),
    Course("DigiLab", "https://i.ibb.co/CHYFJfV/Yellow-Black-Playful-Lamp-Bulb-Idea-Company-Logo.png", "Get set for an after-school adventure that's all about crafting amazing websites! 🚀 From bringing blogs to life to crafting cool online spaces, kids will explore the art of structure, content, layout, typography, and design in the digital realm.  Our tech-savvy crew will dive into the world of coding using HTML and CSS, turning imaginative ideas into web wonders! 🖥️🎨 But this class is not just about learning; it's about becoming design heroes on 'business missions' for exciting clients in different fields. Picture creating mock websites that showcase your skills and creativity!  Throughout this digital journey, we'll uncover the secrets of design flow and functionality, and by the end of the class, you'll proudly unveil your very own website masterpiece. 🌐💻 Get ready to unleash your inner web wizard in the most exciting after-school class ever! ✨", "K-6th"),
    Course("APPrentice", "https://i.ibb.co/ccWS1sx/digilab.png", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Little Big Investors", "https://i.ibb.co/0JLYnM4/littlebiginvestor.png", "Have you ever wanted to build a mobile app? In this class, students learn how to make their ideas happen through app building. Using the Thunkable app making platform, kids learn how to make applications that can be used in real-life situations. Problem solving skills are honed as they work through real world business problems and use their critical thinking to come up with solutions. All creative thinkers are encouraged to sign up for the fun!", "K-6th"),
    Course("Craft Your Brand", "https://i.ibb.co/1RqRYNr/crafturbrand.png", "Embark on a creative journey that goes beyond crafts - turn your hobby into a superpower! 🚀 Discover how cool DIY projects can teach you essential skills for leadership and entrepreneurship. Dive into the stories of imaginative minds who've turned their passions into something extraordinary.  In this after-school class, we'll show you how technology and media play a vital role in unleashing your creative potential. Get ready to sharpen your problem-solving skills, ignite your innovative spark, and become a leader in your own right! 🌟 Let's turn your DIY dreams into a reality, with a sprinkle of creativity and a dash of business magic! 🎨✨💼", "K-6th"),
    Course("Printing Profits", "https://i.ibb.co/ygYRmVn/printingprfts.png", "Get ready for a blast of creativity in the coolest after-school class ever! 🎨 Dive into the world of design and transform ordinary shirts, totes, and textiles into your very own masterpieces using a variety of awesome mediums.  But that's not all - we'll guide you through the process of showcasing your designs and pitching your own brand. It's a practical hands-on experience that goes beyond art, helping you develop skills in marketing and presentation.  Throughout this creative journey, you'll not only master the art of design but also develop skills that go beyond the canvas. Get ready to discover the secrets of leadership and entrepreneurship as you embark on a colorful adventure in our after-school design haven! 🌈✨", "K-6th"),
    Course("Build Your Class", "https://i.ibb.co/3BSc9Hn/buildurclass.png", "Welcome to 'Imagineer: The Ultimate Learning Adventure', where imagination takes the lead, and learning becomes a self-crafted quest! 🚀 In this unique class, children and parents team up to create a customized and themed learning experience, blending elements of science, engineering, technology, arts, mathematics, with a touch of entrepreneurship. It is a dynamic class where you and your child collaborate to design a curriculum that aligns with your interests and passions. Dive into the wonders of science experiments, explore the realms of technology, unleash your creativity in arts and crafts, and delve into the fascinating world of mathematics.   Feel the excitement as you incorporate elements of entrepreneurship into your tailored class. Learn to pitch creative ideas, design products, or even explore business missions together. Unleash your creativity, ignite curiosity, and embark on a personalized educational journey like never before! 🌈🔧💻🎨📐💡", "K-6th"),
]