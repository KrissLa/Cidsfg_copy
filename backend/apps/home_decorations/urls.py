from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeDecorationsListView.as_view(), name='home_decorations_list'),
    path("<slug:slug>/", views.HomeDecorationsCategoryDetailView.as_view(), name='home_decorations_subcategories'),
    path("<slug:category_slug>/<slug:slug>/", views.HomeDecorationsSubCategoryDetailView.as_view(),
         name='home_decorations_subcategory_detail'),
    path("<slug:category_slug>/<slug:subcategory_slug>/<slug:slug>", views.HomeDecorationsTypeDetailView.as_view(),
         name='home_decorations_type_detail'),
]
