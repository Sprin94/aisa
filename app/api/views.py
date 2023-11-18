from django.shortcuts import redirect, render
from django.conf import settings
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ShortUrlCreateSerialize
from api.models import ShortUrl


class ShortUrlCreateAPIView(CreateAPIView):
    """Создание ShortUrl"""
    serializer_class = ShortUrlCreateSerialize
    queryset = ShortUrl.objects.all()

    def create(self, request, *args, **kwargs):
        instance = ShortUrl.objects.filter(url=request.data.get('url'))
        if instance:
            serializer = self.get_serializer(instance=instance[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs)


class RedirectToLongUrl(RetrieveAPIView):
    """Редирект с короткой на длинный URL"""
    serializer_class = ShortUrlCreateSerialize
    queryset = ShortUrl.objects.all()
    lookup_field = 'short_url'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        url = serializer.data["url"]
        return redirect(url)


class MainView(APIView):
    def get(self, request):
        host = settings.HOST
        return render(request, 'base.html', {"host": host})
