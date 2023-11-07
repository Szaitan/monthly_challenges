from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.monthly_challenges_all, name="month-challenges"),
    path("<int:month>", views.monthly_challenge_by_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
