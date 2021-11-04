from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


def home(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1=request.POST['password2']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save();
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('post_view')
        else:
            messages.info(request,'invaild userid or password')
            return redirect('login')
    else:
        return  render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post_view(request):
    obj1=Post.objects.all()
    if request.method=="POST":
        name=request.POST.get('post_name')
        post=request.POST.get('post')
        date=request.POST.get('date')
        obj=Post(post_name=name,post=post,date=date)
        obj.save();
    return render(request,'post.html',{'obj1':obj1})


class TaskDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('post_name','post','date')
    def get_success_url(self):
        return reverse_lazy('post_view')
        # return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url=reverse_lazy('post_view')