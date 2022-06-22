from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('<slug:slug>/', views.post, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
