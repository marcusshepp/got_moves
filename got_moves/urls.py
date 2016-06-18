from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login

from rest_framework.routers import DefaultRouter

from main import viewsets


router = DefaultRouter()
router.register("categories", viewsets.DefaultCategoryViewset)
router.register("classic_moves", viewsets.ClassicMoveViewset)

urlpatterns = [
    url(r'^foo/', admin.site.urls),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
