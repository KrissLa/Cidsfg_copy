from django.core.management import BaseCommand
from loguru import logger

from backend.apps.products.models import House, Series


class Command(BaseCommand):
    houses = House.objects.all()

    def update_prices(self):
        for h in self.houses:
            h.get_price()

    def update_main_picture(self):
        for h in self.houses:
            h.save_main_picture()

    def update_series_count(self):
        series = Series.objects.all()
        for s in series:
            s.get_active_houses_count()

    def handle(self, **options):
        self.update_prices()
        self.update_series_count()
        self.update_main_picture()
