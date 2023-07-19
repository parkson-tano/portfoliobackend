from rest_framework.routers import SimpleRouter
from .views import PortfolioViewSet 
from django.urls import include,path

router = SimpleRouter()

router.register('portfolios',PortfolioViewSet,basename="portfolio-view")

urlpatterns = [
    path('api/v1/',include(router.urls))
]




