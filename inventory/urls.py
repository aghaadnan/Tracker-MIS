from django.urls import path
from .views import (
    InventoryListView,
    TrackerDeviceListView,
    TrackerDeviceCreateView,
    TrackerDeviceDetailView,
    TrackerDeviceUpdateView,
    TrackerDeviceDeleteView,
    SimListView,
    SimCreateView,
    SimDetailView,
    SimUpdateView,
    SimDeleteView,
)

app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('trackerdevices/', TrackerDeviceListView.as_view(), name='trackerdevice-list'),
    path('trackerdevices/create/', TrackerDeviceCreateView.as_view(), name='trackerdevice-create'),
    path('trackerdevices/<int:pk>/', TrackerDeviceDetailView.as_view(), name='trackerdevice-detail'),
    path('trackerdevices/<int:pk>/update/', TrackerDeviceUpdateView.as_view(), name='trackerdevice-update'),
    path('trackerdevices/<int:pk>/delete/', TrackerDeviceDeleteView.as_view(), name='trackerdevice-delete'),
    path('sims/', SimListView.as_view(), name='sim-list'),
    path('sims/create/', SimCreateView.as_view(), name='sim-create'),
    path('sims/<int:pk>/', SimDetailView.as_view(), name='sim-detail'),
    path('sims/<int:pk>/update/', SimUpdateView.as_view(), name='sim-update'),
    path('sims/<int:pk>/delete/', SimDeleteView.as_view(), name='sim-delete'),
]
