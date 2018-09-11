from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'', views.index, name='index'),
    re_path(r'<int:question_id>', views.detail, name='detail'),
    re_path(r'<int:question_id>/results/', views.results, name='results'),
    re_path(r'<int:question_id>/votes/', views.vote, name='vote'),
]
