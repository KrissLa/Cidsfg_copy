from django.core.management import BaseCommand
from loguru import logger

from backend.apps.products.models import House, Series


class Command(BaseCommand):
    def update_prices(self):
        houses = House.objects.all()
        for h in houses:
            h.get_price()

    def update_series_count(self):
        series = Series.objects.all()
        for s in series:
            s.get_active_houses_count()

    def handle(self, **options):
        self.update_prices()
        self.update_series_count()
