from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhoenixHomePage.as_view(), name='index'),
    path("all_blogs/", views.BlogList.as_view(), name='blog-list'),
    path("search/", views.BlogSearch.as_view(), name='search'),
    path("<slug:slug>/", views.SingleBlog.as_view(), name='single_blog'),
    path("category/<slug:slug>/", views.BlogByCategory.as_view(), name='category'),
    path("authors_blog/<str:name>/", views.AuthorsBlog.as_view(), name='authors_blog'),
]


