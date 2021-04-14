from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import View
from loguru import logger

from .models import HomeDecorationCategory, HomeDecorationSubCategory, HomeDecorationType, HomeDecoration


class HomeDecorationsListView(ListView):
    """ Вывод списка категорий """
    model = HomeDecorationCategory
    template_name = 'home_decorations/home_decorations_list.html'
    queryset = HomeDecorationCategory.objects.filter(hd_active=True).order_by('id')
    context_object_name = 'home_decorations'


class HomeDecorationsCategoryDetailView(DetailView):
    """ Вывод списка подкатегорий по выбранной категории на страницу """
    model = HomeDecorationCategory
    slug_field = 'hd_slug'
    template_name = 'home_decorations/home_decorations_category_detail.html'
    context_object_name = 'hd_category'

    def get_object(self, **kwargs):
        category_slug = self.kwargs.get('slug', '')
        category = get_object_or_404(HomeDecorationCategory, hd_slug=category_slug, hd_active=True)
        return category


class HomeDecorationsSubCategoryDetailView(DetailView):
    """ Вывод списка типов по выбранной подкатегории на страницу"""
    model = HomeDecorationSubCategory
    slug_field = 'slug'
    template_name = 'home_decorations/home_decorations_subcategory_detail.html'
    context_object_name = 'hd_category'

    def get_object(self, **kwargs):
        category_slug = self.kwargs.get('category_slug', '')
        category = get_object_or_404(HomeDecorationCategory, hd_slug=category_slug, hd_active=True)
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug', '')
        sub_category_slug = self.kwargs.get('slug', '')
        sub_category = get_object_or_404(HomeDecorationSubCategory, active=True, category__hd_slug=category_slug,
                                         slug=sub_category_slug)

        context['sub_category'] = sub_category
        logger.info(context['sub_category'])
        return context


class HomeDecorationsTypeDetailView(DetailView):
    """ Вывод списка типов по выбранной подкатегории на страницу"""
    model = HomeDecorationSubCategory
    slug_field = 'slug'
    template_name = 'home_decorations/home_decorations_type_detail.html'
    context_object_name = 'hd_category'

    def get_object(self, **kwargs):
        category_slug = self.kwargs.get('category_slug', '')
        category = get_object_or_404(HomeDecorationCategory, hd_slug=category_slug, hd_active=True)
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug', '')
        sub_category_slug = self.kwargs.get('subcategory_slug', '')
        type_slug = self.kwargs.get('slug', '')
        hd_type = get_object_or_404(HomeDecorationType, active=True, sub_category__category__hd_slug=category_slug,
                                    sub_category__slug=sub_category_slug, slug=type_slug)

        context['hd_type'] = hd_type
        return context


# class HomeDecorationsListView(TemplateView):
#     """ Страница с каталогом отделок """
#     template_name = 'home_decorations/home_decorations_list.html'


class HomeDecorationsDetailView(TemplateView):
    """ Страница с подробным отписание об отделке """
    template_name = 'home_decorations/home_decorations_detail.html'
