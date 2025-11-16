from django.urls import path
from .views import HomePageView
from .views import HomePageView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]