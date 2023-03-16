from django.shortcuts import render
from django.views.generic import ListView, DetailView

from device.models import Category, Marques, Appareils


def index(request):
    categories = Category.objects.all()
    marques = Marques.objects.all()
    context = {
        'categories': categories,
        'marques': marques,
    }
    return render(request, 'device/index.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'device/categorie_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appareils'] = Appareils.objects.all()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'device/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alug = self.kwargs.get('slug')  # Récupère le slug de la catégorie dans l'URL
        context['appareils'] = Appareils.objects.filter(category__slug=alug)
        return context


class AppareilsListView(ListView):
    model = Appareils
    template_name = 'device/appareils_list.html'
    context_object_name = 'appareils'


class AppareilsDetailView(DetailView):
    model = Appareils
    template_name = 'device/appareils_detail.html'
    context_object_name = 'appareil'
