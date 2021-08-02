from loguru import logger

from backend.apps.products.models import HouseAdditionCategory


def run_shell():
    cat = HouseAdditionCategory.objects.all()
    logger.info(cat)
