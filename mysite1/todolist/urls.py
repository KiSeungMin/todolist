from django.urls import path

from . import views

app_name='todolist'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:diary_id>/', views.detail, name='detail'),
    path('comment/create/<int:diary_id>/', views.comment_create, name='comment_create'),
    path('diary/create/', views.diary_create, name="diary_create")
]