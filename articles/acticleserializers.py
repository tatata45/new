from rest_framework import serializers
from .models import Acticle


class ActicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acticle
        fields = ( 'name', 'description', 'category_id')