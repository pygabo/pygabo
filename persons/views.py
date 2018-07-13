from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person
from .forms import PersonForm


class PersonListView(LoginRequiredMixin,ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context.update({
            'name': 'List Person',
            'icon':'home',
        })
        return context
    def get_queryset(self):
        results = Person.objects.filter(owner=self.request.user)
        return results

class PersonCreateView(LoginRequiredMixin, CreateView):
    form_class = PersonForm

    def form_valid(self, form):
        furmulario = form.save(commit=False)
        furmulario.owner = self.request.user
        furmulario.save()
        self.object = furmulario
        return redirect('persons:index')

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context.update({
            'name': 'Create Person',
            'icon': 'plus-square-o'
        })
        return context



class PersonUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PersonForm
    model = Person

    def form_valid(self, form):
        furmulario = form.save(commit=False)
        furmulario.owner = self.request.user
        furmulario.save()
        self.object = furmulario
        return redirect('persons:index')

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        context.update({
            'name': 'Update Person',
            'icon':'edit',
        })
        return context


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('persons:index')

    def get_context_data(self, **kwargs):
        context = super(PersonDeleteView, self).get_context_data(**kwargs)
        context.update({
            'name': 'Delete Person',
            'icon': 'trash-o',
        })
        return context
