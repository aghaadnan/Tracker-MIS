from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DeleteView, DetailView,
                CreateView,UpdateView
                                  )
from .models import Lead, Agent
from agent.mixins import OrganisorandLoginRequiredMixin
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
# Create your views here.
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/home_page.html"
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        print(user.is_organisor)
        if user.is_organisor:
            queryset = Lead.objects.all()
            #queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            #queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
        return queryset

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    
    context_object_name = 'lead'
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
            return queryset

class LeadCreatView(OrganisorandLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')
class LeadUpdateView(OrganisorandLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_create.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    '''
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)
        '''

    def get_success_url(self):
        return reverse('leads:lead-list')
class LeadDeleteView(OrganisorandLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)
    def get_success_url(self):
        return reverse('leads:lead-list')


def landin_page(request):
    return render(request, "landing_page.html")

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "leads\home_page.html", context)

def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads\lead_detail.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads/all/")
    context ={
        "form" : form
    }
    return render(request, "leads\lead_create.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads/all/")
    context ={
        "lead" : lead,
        "form" : form
    }
    return render(request, "leads\lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads/all/")
    '''
def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads/all/")
    context ={
        "form" : form
    }
    return render(request, "leads\lead_create.html", context)

    '''