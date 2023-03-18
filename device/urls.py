from django.urls import path
from device.views import index, AppareilsListView, AppareilsDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('', index, name='index'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    # path('appareils/', AppareilsListView.as_view(), name='appareils_list'),
    path('appareils/<slug:slug>/', AppareilsDetailView.as_view(), name='appareils_detail'),
]
