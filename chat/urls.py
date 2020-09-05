from django.urls import path
from chat import views

urlpatterns = [
    path('chatroom/<str:room_name>/', views.RoomView.as_view(), name='chatroom')
]
