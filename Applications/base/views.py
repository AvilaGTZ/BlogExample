import random
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.core.paginator import Paginator
from .models import Post, Category, SocialNetworks, Web
from .utils import *
from .forms import ContactForms

class Main(ListView):
    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.filter(
            state = True,
            published = True
        ).values_list('id', flat=True))
        MainPost = random.choice(posts)
        posts.remove(MainPost)
        MainPost = Consult(MainPost)

        post1 = random.choice(posts)
        posts.remove(post1)

        post2 = random.choice(posts)
        posts.remove(post2)

        post3 = random.choice(posts)
        posts.remove(post3)

        post4 = random.choice(posts)
        posts.remove(post4)

    #Retreiving the last posts of each category ----------------------#
        try:
            PostPrograming = Post.objects.filter(
                state = True,
                published = True,
                category = Category.objects.get(name = 'Programing')
            ).latest('publishDate')
        except:
            PostPrograming = None

        try:
            print("Llegue")
            PostMain = Post.objects.filter(
                state = True,
                published = True,
                category = Category.objects.get(name = 'Main')
            ).latest('publishDate')
        except:
            PostMain = None

        
    #-----------------------------------------------------------------#

        Context = {
            'Main':MainPost,
            'post1':Consult(post1),
            'post2':Consult(post2),
            'post3':Consult(post3),
            'post4':Consult(post4),
            'MainPost':PostMain,
            'ProgramingPost':PostPrograming,
            'Socials':GetSocial,
            'Web':GetWeb
        }
        return render(request, 'index.html',Context)

class GlobalListing(ListView):
    def get(self, request, categoryName, *args, **kwargs):
        Context = GenCategory(categoryName,request)
        return render(request,'category.html',Context)

class ContactForm(View):
    def get(self, request,*args, **kwargs):
        form = ContactForms()
        Context = {
            'Socials':GetSocial,
            'Web':GetWeb,
            'Form':form
        }
        return render(request,'contact.html',Context)

    def post(self, request,*args, **kwargs):
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            Context = {
                'Form': form,
            }
            return render(request,'contact.html',Context)
    
        

'''class MainListing(ListView):

    def get(self, request, *args, **kwargs):
        Context = GenCategory('Main',request)

        return render(request,'category.html',Context)

class ProgramingListing(ListView):

    def get(self, request, *args, **kwargs):
        Context = GenCategory('Programing',request)

        return render(request,'category.html',Context)'''
