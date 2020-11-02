from rest_framework import routers
from django.urls import path
from msb.views import dashboard_view

from msb.viewsets.portofolio_viewset import PortofolioViewSet

# for api
router = routers.DefaultRouter()
router.register('api/portofolio', PortofolioViewSet)

urlpatterns = [
	path('', dashboard_view.dashboard, name='dashboard'),
]

urlpatterns += router.urls