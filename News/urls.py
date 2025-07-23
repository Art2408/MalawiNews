from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePage , name="home"),
    path("latest-news/",views.LatestPage , name="latest-news"),
    path("news-cartegories/" ,views.CartegoryPage ,name="cartegory"),
    path("news-cartegories/<str:pk>" ,views.CartegoryNews ,name="cartegory-news"),
    path("news-story/" ,views.News_Story_Page ,name="news-story"),
    path("news-story/<str:pk>",views.StoryPage,name="story-news"),
    path("latest-story/<str:pk>",views.LatestStory,name="latest-story"),

    path("sign-up/",views.SignUp,name="sign-up"),
    path("log-in/",views.LogIn,name="log-in"),
    path("log-out/",views.LogOut , name="log-out"),

    path("profile/",views.ProfilePage ,name="profile"),
    path("choose-cartegory/",views.ChooseNewsCart,name="choose-cart"),
    path("create-news/<str:pk>/",views.CreateNews,name="create-news"),
    path("choose-cart-latest/",views.ChooseLatestCart,name="choose-cart-latest"),
    path("create-latest/<str:pk>/",views.CreateLatestNews,name="create-latest"),
    path("delete-news/<str:pk>",views.DeleteNews,name="delete-news"),
    path("delete-latest-news/<str:pk>",views.DeleteLatestNews,name="delete-latest"),
]
