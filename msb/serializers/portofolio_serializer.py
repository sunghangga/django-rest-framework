from msb.models.portofolio_model import Portofolio

from rest_framework import serializers

class PortofolioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portofolio
		fields = '__all__'