from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('<int:pk>/', views.DetailView.as_view(), name="details"),
    path('skills', views.skills, name='skills'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)