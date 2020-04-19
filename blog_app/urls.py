from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog_app'
urlpatterns = [
    ## So re-initialize(D) urls.py in blogs to handle different blog paths ||
    ## ## blog Home ||
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    #               detail = nickname of dynamic/ Specific blog calling
]
# to upload Media to a global root/media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings)