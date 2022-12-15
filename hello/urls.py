from django.urls import path
from .views import HelloViewSet, HelloDetailView

urlpatterns = [
    path('list', HelloViewSet.as_view(), name='hello'),
    path('<int:pk>', HelloDetailView.as_view(), name='hello_detail'),
]