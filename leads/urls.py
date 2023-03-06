from django.urls import path
from .views import (
    lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreatView, LeadDeleteView, LeadUpdateView
)
app_name = "leads"
urlpatterns = [
    path("all/", LeadListView.as_view(), name='lead-list'),
    path("create/", LeadCreatView.as_view(), name='lead-create'),
    path("<int:pk>/", LeadDetailView.as_view(), name='lead-detail'),
    path("<int:pk>/update/", LeadUpdateView.as_view(), name='lead-update'),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name='lead-delete')
]
