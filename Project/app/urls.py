from django.urls import path
from .views import HomePageView
from .views import HomePageView, PostCreateView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]