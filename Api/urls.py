from django.urls import path
from .views import Home,HomeDetail,UserDetails,UserList

urlpatterns=[
    path('api/',Home.as_view(),name='home'),
    path('api/<int:pk>',HomeDetail.as_view(),name='detail'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/',UserDetails.as_view()),
]