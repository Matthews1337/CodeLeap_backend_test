from django.urls import path
from testsite import views



urlpatterns = [
    path('user/', views.user_list, name='user'),
    path('user/<str:id>/', views.user_detail, name='detail')
]