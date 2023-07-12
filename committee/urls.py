from django.urls import path
from .views import CommitteeListView, CommitteeDetailView

urlpatterns = [
    path('', CommitteeListView.as_view()),
    path('<int:pk>/', CommitteeDetailView.as_view())
]