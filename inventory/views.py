from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TrackerDevice, Sim


# TrackerDevice views
class InventoryListView(TemplateView):
    template_name = "inventory/inventory_list.html"

class TrackerDeviceListView(ListView):
    model = TrackerDevice
    template_name = "inventory/trackerdevice_list.html"

class TrackerDeviceCreateView(CreateView):
    model = TrackerDevice
    fields = ['model_number', 'vendor', 'price', 'imei']
    template_name = "inventory/trackerdevice_create.html"
    success_url = reverse_lazy('inventory:trackerdevice-list')

class TrackerDeviceDetailView(DetailView):
    model = TrackerDevice
    template_name = "inventory/trackerdevice_detail.html"

class TrackerDeviceUpdateView(UpdateView):
    model = TrackerDevice
    fields = ['model_number', 'vendor', 'price', 'imei']
    template_name = "inventory/trackerdevice_update.html"
    success_url = reverse_lazy('inventory:trackerdevice-list')

class TrackerDeviceDeleteView(DeleteView):
    model = TrackerDevice
    template_name = "inventory/trackerdevice_delete.html"
    success_url = reverse_lazy('inventory:trackerdevice-list')

# Sim views
class SimListView(ListView):
    model = Sim
    template_name = "inventory/sim_list.html"

class SimCreateView(CreateView):
    model = Sim
    fields = ['MSISDN', 'ICC_ID', 'OPERATOR', 'PACKAGE']
    template_name = "inventory/sim_create.html"
    success_url = reverse_lazy('inventory:sim-list')

class SimDetailView(DetailView):
    model = Sim
    template_name = "inventory/sim_detail.html"

class SimUpdateView(UpdateView):
    model = Sim
    fields = ['MSISDN', 'ICC_ID', 'OPERATOR', 'PACKAGE']
    template_name = "inventory/sim_update.html"
    success_url = reverse_lazy('inventory:sim-list')

class SimDeleteView(DeleteView):
    model = Sim
    template_name = "inventory/sim_confirm_delete.html"
    success_url = reverse_lazy('inventory:sim-list')
