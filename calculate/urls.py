from django.urls import path
from . import views

app_name = 'calculate'

urlpatterns = [
    path('', views.index, name='index'),
    #ファイルアップロード
    path('new_file', views.new_file, name='new_file'),
]