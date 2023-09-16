from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def posts(request):
    posts = [
        {
            'headline': 'Laboratory Management System',
            'sub_headline': 'Designed Built & maintained the lab management system'
        },

        {
            'headline': 'Online Store',
            'sub_headline': 'Online store with paypal payments integration'
        },

        {
            'headline': 'Membership Website',
            'sub_headline': 'Modulized guide for online courses'
        },

    ]
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')