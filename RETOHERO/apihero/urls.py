from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apihero.views import HeroViewSet

router = SimpleRouter()
router.register('hero', HeroViewSet, 'hero')


urlpatterns = [
    path('', include(router.urls))
]
