from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    ## So re-initialize(D) urls.py in blogs to handle different blog paths ||
    ## ## blog Home ||
    path('',views.all_blogs,name='all_blogs'),
]
# to upload Media to a global root/media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings)