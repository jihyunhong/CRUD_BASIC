from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
    path('create/', view=views.create_post, name='create'),
]
