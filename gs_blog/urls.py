from django.urls import path
from . import views

#path('', views.home,name='blog-home'),
#path('',views.about,name='blog-about'),
urlpatterns = [

    path('',views.PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('lgin/',views.lgin,name='blog-lgin'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/new/',views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete'),

]
