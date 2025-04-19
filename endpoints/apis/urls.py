from django.urls import path
from apis import views
from endpoints import settings
from django.conf.urls.static import static


urlpatterns = [
    path('students/', views.student, name='student'),
    path('subjects/', views.subject, name='subject')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_URL)