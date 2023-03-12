from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('users', views.UsersAPIViewsSets, basename='users')
router.register('', views.BlogsAPIViewSets, basename='blogs')


urlpatterns = router.urls


# urlpatterns += [
#     path('', views.BlogsAPIView.as_view()),
#     path('<int:pk>/', views.BlogDetailAPIView.as_view()),
#     path('create/', views.BlogCreateAPIView.as_view()),
#     path('process/<int:pk>/', views.BlogProcessAPIView.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

