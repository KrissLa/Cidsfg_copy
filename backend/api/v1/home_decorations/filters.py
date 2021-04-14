from loguru import logger
from rest_framework.filters import BaseFilterBackend


# http://127.0.0.1:8000/api/v1/home_decorations/?categories=&sub_categories=&type=&ordering=

class HomeDecorationsFilter(BaseFilterBackend):
    """
    Фильтр отделок и коммуникаций по категориям
    """

    def filter_queryset(self, request, queryset, view):
        categories = request.query_params.get('categories', None)
        sub_categories = request.query_params.get('sub_categories', None)
        types = request.query_params.get('types', None)
        logger.info(sub_categories)
        logger.info(categories)
        logger.info(types)
        if categories:
            categories = categories.split(',')
            logger.info(categories)
            queryset = queryset.filter(type__sub_category__category__id__in=categories).distinct()
            logger.info(queryset)
            logger.info(queryset.count())
        if sub_categories:
            sub_categories = sub_categories.split(',')
            logger.info(sub_categories)
            queryset = queryset.filter(type__sub_category__id__in=sub_categories).distinct()
            logger.info(queryset)
            logger.info(queryset.count())
        if types:
            types = types.split(',')
            logger.info(types)
            queryset = queryset.filter(type__id__in=types).distinct()
            logger.info(queryset)
            logger.info(queryset.count())
        logger.info(queryset)
        logger.info(queryset.count())
        return queryset
