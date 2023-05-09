from django.conf import settings
from django.urls import path, re_path
from .import views

from django.views.static import serve


urlpatterns = [

    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('contacts/success/', views.contact_success, name='contact_success'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('feedback/view_my/', views.view_feedback_my, name='view_feedback_my'),
    path('feedback/view/', views.view_feedback, name='view_feedback'),
    path('contacts/posts_list', views.post_list, name='posts'),
    path('contacted/', views.AdminContactView.as_view(), name='contact'),
    path('search', views.search, name='search'),
    path('post/<int:id>/', views.post, name='post'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]


