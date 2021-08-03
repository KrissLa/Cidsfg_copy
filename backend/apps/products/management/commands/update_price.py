from django.core.management import BaseCommand
from loguru import logger

from backend.apps.products.models import House


class Command(BaseCommand):
    def handle(self, **options):
        houses = House.objects.all()
        for h in houses:
            h.get_price()
