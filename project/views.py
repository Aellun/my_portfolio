from django.shortcuts import render, redirect
from django.contrib import messages
from project.models import Contact, Resume, Project 
def project_view(request):
    return render(request, 'project.html')

def resume_view(request):
    return render(request, 'resume.html')
    
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        return redirect('/contact')

    return render(request, 'contact.html')
