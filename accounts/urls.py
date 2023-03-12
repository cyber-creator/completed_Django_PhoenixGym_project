from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views


urlpatterns = [
    path('', views.account_options, name='account_options'),
    path('register/', views.account_register, name='account_register'),
    path('password_change/', authentication_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', authentication_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', authentication_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', authentication_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', authentication_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', views.account_profile, name='account_profile'),
    path('inform_page/', views.account_inform, name='account_inform'),
    path("profile/edit-<slug:slug>/", views.BlogEdit.as_view(), name='profile_blog_edit'),
    path("profile/blog_create/", views.BlogCreate.as_view(), name='profile_blog_create'),
    path('profile/blog_delete/<int:pk>', views.BlogDelete.as_view(), name='delete_blog'),
    path('logout/', views.logout_user, name='account_logout'),
]
