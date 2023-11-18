from uuid import uuid4
from urllib.parse import urljoin

from django.conf import settings
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import ShortUrl


class ShortUrlCreateSerialize(ModelSerializer):
    short_url = SerializerMethodField()

    class Meta:
        model = ShortUrl
        fields = ('url', 'short_url')
        read_only_fields = (
            'id',
            'short_url',
        )

    def get_short_url(self, obj) -> str:
        return urljoin(settings.HOST, obj.short_url)

    def create(self, validated_data):
        validated_data['short_url'] = str(uuid4())[:6]
        return super().create(validated_data)
