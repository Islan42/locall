from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('b/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('b/<int:pk>/create/', views.CreateCommentView.as_view(), name='comment-create'),
    path('bloggers/', views.AuthorListView.as_view(), name='blog-author-list'),
    path('blogger/<int:pk>/', views.AuthorDetailView.as_view(), name='blog-author-detail'),
]
