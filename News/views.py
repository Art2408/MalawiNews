from django.shortcuts import render ,redirect

from .models import Cartegory ,LatestNews,NewsContent
from Account.models import Profile , Subscriber
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def HomePage (request):

    if request.method == "POST":
        username = request.POST.get("username")
        user_email = request.POST.get("user_email")
        if username and user_email:
            subcriber = Subscriber.objects.create(
                username = username,
                email = user_email
            )
            print("form is called")

    latest = LatestNews.objects.all()
    news = NewsContent.objects.all()

    context={
        "latest":latest,
        "news":news
    }
    return render(request,"pages/home-page.html",context)

def LatestPage(request):
    if request.method=="POST":
        query = request.POST.get("query")
        if query:
            latest = LatestNews.objects.filter(Title__icontains=query)

    latest = LatestNews.objects.all()
    
    context={
        "latest":latest 
    }
    return render(request,"pages/latest-page.html",context)


def News_Story_Page(request):
    news = NewsContent.objects.all()
    context = {
        "news":news
    }
    return render(request,"pages/news-story-page.html",context)


def CartegoryPage(request):
    cartegory = Cartegory.objects.all()
    news = NewsContent.objects.all()
    context ={
        "cartegory":cartegory,
        "news":news
    }
    return render(request,"pages/cartegory-page.html",context)

def CartegoryNews(request,pk):
    cart = Cartegory.objects.get(id=pk)
    cartegory = Cartegory.objects.all()
    news = NewsContent.objects.filter(Cartegory=cart)
    context ={
        "cartegory":cartegory,
        "news":news
    }
    return render(request,"pages/cartegory-page.html",context)

def StoryPage(request,pk):
    news = NewsContent.objects.get(id=pk)
    related_news = NewsContent.objects.filter(Cartegory=news.Cartegory)

    context ={
        "news":news,
        "related_news":related_news
    }
    return render(request,"pages/story-page.html",context)

def LatestStory(request,pk):
    news = LatestNews.objects.get(id=pk)
    related_news = LatestNews.objects.filter(Cartegory=news.Cartegory)
    context ={
        "news":news,
        "related_news":related_news
    }
    return render(request,"pages/story-page.html",context)

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = Profile.objects.filter(email=email)

        if user:
            print("user already created")

        else:
            if password1==password2:
                user = Profile.objects.create(
                    username = username,
                    email = email,
                    password = make_password(password1)
                )
                login(request,user)
                return redirect("profile")
                
    return render(request,"Auth/sign-up.html")

def LogIn(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email,password=password)
        # print(user)
        if user:
            login(request,user)
            return redirect("profile")
            print("log in successfully")
        print("user is not found")
    return render(request,"Auth/log-in.html")

def LogOut(request):
    logout(request)
    return redirect("home")
    
@login_required(login_url="log-in")
def ProfilePage(request):
    user = request.user
    latest = LatestNews.objects.filter(Host=user)
    news = NewsContent.objects.filter(Host=user)

    if request.method=="POST":
        username = request.POST.get("username")
        user_avatar = request.FILES["avatar"]
        if username is not None:
            user.username=username
            print("username is changed")
            user.save()
            
        if user_avatar is not None:
            user.Avatar=user_avatar
            print("avatar is changed")
            print(user_avatar)
            user.save()
    context={
        "latest":latest,
        "news":news
    }
    return render(request,"Profile/profile-page.html",context)

def ChooseNewsCart(request):
    if request.method == "POST":
        cart = request.POST.get("cartegory")
        cartegory = Cartegory.objects.filter(cartegory = cart)
        if cartegory:
            print("the cartegory already created")

        else:
            cartegory =Cartegory.objects.create(
                cartegory = cart
            )
            return redirect(f"/create-news/{cartegory.id}")

    cartegories = Cartegory.objects.all()
    print(cartegories)
    context = {
        "cartegories":cartegories
    }
    return render(request,"Profile/choose-cartegory.html" , context)

def ChooseLatestCart(request):
    if request.method == "POST":
        cart = request.POST.get("cartegory")
        cartegory = Cartegory.objects.filter(cartegory = cart)
        if cartegory:
            print("the cartegory already created")

        else:
            cartegory =Cartegory.objects.create(
                cartegory = cart
            )
            return redirect(f"/create-latest/{cartegory.id}")

    cartegories = Cartegory.objects.all()
    print(cartegories)
    context = {
        "cartegories":cartegories
    }
    return render(request,"Profile/choose-cartegory-latest.html",context)

def CreateNews(request,pk):
    cartegory = Cartegory.objects.get(id=pk)
    user = request.user
    
    if request.method == "POST":
        picture = request.FILES.get("image")

        news =  NewsContent.objects.create(
            Cartegory = cartegory,
            Host = user,
            Title = request.POST.get("title"),
            Story = request.POST.get("story"),
        )
        if picture is not None:
            news.Picture = picture
            news.save()
        print("news story created")
        return redirect("profile")
    return render(request,"Profile/create-news.html")

def CreateLatestNews(request,pk):
    cartegory = Cartegory.objects.get(id=pk)
    user = request.user

    if request.method == "POST":
        picture = request.FILES.get("image")
        latest =  LatestNews.objects.create(
            Cartegory = cartegory,
            Host = user,
            Title = request.POST.get("title"),
            Story = request.POST.get("story"),
        )
        if picture is not None:
            latest.Picture = picture
            latest.save()
        print("news latest story created")
        return redirect("profile")
    return render(request,"Profile/create-latest.html")


def SubcriberingForm(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user_email = request.POST.get("user_email")
        if username and user_email:
            subcriber = Subscriber.objects.create(
                username = username,
                email = user_email
            )
            print("form is called")
    return render(request,"constants/footer.html")


def DeleteNews(request,pk):
    news = NewsContent.objects.get(id=pk)

    if request.method == "POST":
        news.delete()
        print("news deleted successfully")
        return redirect("profile")
    
    context = {
        "news":news    }
    return render(request,"Profile/delete-news.html",context)

def DeleteLatestNews(request,pk):
    news = LatestNews.objects.get(id=pk)

    if request.method == "POST":
        news.delete()
        print("news deleted successfully")
        return redirect("profile")
    
    context = {
        "news":news    }
    return render(request,"Profile/delete-news.html",context)
