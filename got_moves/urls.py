from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login

from rest_framework.routers import DefaultRouter

from main import views


router = DefaultRouter()
router.register("categories", views.MoveCategoryViewset)
router.register("classic_moves", views.ClassicMoveViewset)
router.register("classic_move_performances", views.ClassicMovePerformanceViewset)

urlpatterns = [
    url(r'^foo/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/classic_move_search', views.ClassicMoveFilterListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
