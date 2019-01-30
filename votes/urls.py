from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:candidate_id>/', views.detail, name='detail'),
    path('<int:candidate_id>/update', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('poscreate/', views.poscreate, name='poscreate'),
]
