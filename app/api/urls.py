from django.urls import path

from api.views import ShortUrlCreateAPIView, RedirectToLongUrl, MainView

app_name = 'api'

urlpatterns = [
    path('api/short_url/', ShortUrlCreateAPIView.as_view()),
    path('<str:short_url>/', RedirectToLongUrl.as_view()),
    path('', MainView.as_view()),
]
