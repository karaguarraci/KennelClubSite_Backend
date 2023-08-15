from django.urls import path
from .views import PhotoListView, PhotoDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PhotoListView.as_view()),
    path('<int:pk>/', PhotoDetailView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)