import random
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DeleteView, DetailView,
                CreateView,UpdateView
                                  )
from leads.models import Agent
from .mixins import OrganisorandLoginRequiredMixin
from .forms import AgentFormModel

class AgentListView(OrganisorandLoginRequiredMixin, ListView):
    template_name = "agent\gent_list.html"
    
    def get_queryset(self):
        organisation =self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
class AgentCreateView(OrganisorandLoginRequiredMixin, CreateView):
    template_name = 'agent/agent_create.html'
    form_class = AgentFormModel

    def get_success_url(self):
        return reverse('agent:agent-list')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.password= "aghabro123"
        #user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )
        #agent.organisation = self.request.user.userprofile
        #agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganisorandLoginRequiredMixin, DetailView):
    template_name = "agent/agent_detail.html"
    context_object_name = 'agent'
    def get_queryset(self):
        organisation =self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
class AgentUpdateView(OrganisorandLoginRequiredMixin, UpdateView):
    template_name = 'agent/agent_update.html'
    queryset = Agent.objects.all()
    form_class = AgentFormModel
    def get_success_url(self):
        return reverse('agent:agent-list')
class AgentDeleteView(OrganisorandLoginRequiredMixin, DeleteView):
    template_name = "agent/agent_delete.html"
    queryset = Agent.objects.all()
    def get_success_url(self):
        return reverse('agent:agent-list')
    def get_queryset(self):
        organisation =self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
