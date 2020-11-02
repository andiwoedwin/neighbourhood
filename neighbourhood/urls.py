from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   # path('mitaa/', views.index, name='index'), 
   path('ongeza_mtaa/', views.add_mtaa, name='add_mtaa'),
   path('post/<mtaa_id>', views.create_post, name='add_post'),
   path('', views.mitaa, name='mitaa_zote'),
   path('mtaa/<mtaa_id>', views.mtaa, name='mtaa'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)