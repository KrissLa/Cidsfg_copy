from loguru import logger
from rest_framework.filters import BaseFilterBackend


# http://127.0.0.1:8000/api/v1/home_decorations/?categories=&sub_categories=&type=&ordering=

class CategoryFilter(BaseFilterBackend):
    """
    Фильтр по категориям
    """
    def filter_queryset(self, request, queryset, view):
        categories = request.query_params.get('categories', None)
        logger.info(categories)
        if categories:
            categories = categories.split(',')
            logger.info(categories)
            queryset = queryset.filter(category__in=categories).distinct()
        logger.info(queryset)
        return queryset


class SeriesFilter(BaseFilterBackend):
    """
    Фильтр по сериям
    """
    def filter_queryset(self, request, queryset, view):
        series = request.query_params.get('series', None)
        logger.info(series)
        if series:
            series = series.split(',')
            logger.info(series)
            queryset = queryset.filter(series__in=series).distinct()
        logger.info(queryset)
        return queryset

