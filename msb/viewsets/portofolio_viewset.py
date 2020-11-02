from rest_framework import viewsets

from msb.models.portofolio_model import Portofolio

from msb.serializers.portofolio_serializer import PortofolioSerializer

class PortofolioViewSet(viewsets.ModelViewSet):
	queryset = Portofolio.objects.all()
	serializer_class = PortofolioSerializer