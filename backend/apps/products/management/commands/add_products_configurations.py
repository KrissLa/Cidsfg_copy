from django.core.management.base import BaseCommand
from loguru import logger
from django.db.utils import IntegrityError

from backend.apps.products.models import HouseAdditionCategory, HouseAddition, Configuration, ConfigurationInHouses, \
    House


class Command(BaseCommand):
    def create_house_addition_category(self):
        addition_categories = [
            {'name': 'ДОМОКОМПЛЕКТ',
             'house_addition': ['силовой каркас дома выполнен из клеенного бруса хвойных пород',
                                'утепление 150 мм базальтовые плиты (200 мм на выбор)',
                                'кровля фальцевая (или металлочерепица)',
                                'полы из 16 мм ЦСП (цементно-стружечная плита)',
                                'стены снаружи имитация бруса (или планкен)',
                                'стены и потолок внутри из 12 мм ГСП (гипсо-стружечная плита)',
                                'крыльцо (лестница, терраса 1,5х1,2 м, козырек)']},

            {'name': 'ОТДЕЛКА',
             'house_addition': [
                 'внутренняя отделка: потолок и стены - покраска, цвет на выбор, полы – ламинат Дуб Долтон 34 класс',
                 'межкомнатные двери белого цвета',
                 'ванная комната: мозаика и массив дерева']},

            {'name': 'ОСТЕКЛЕНИЕ И ДВЕРИ',
             'house_addition': ['окна (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                                'входные двери (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                                'панорамное остекление (двухкамерные стеклопакеты толщиной 38 мм)']},

            {'name': 'КОММУНИКАЦИИ',
             'house_addition': ['разводка водопровода и канализации',
                                'разводка электрики в лотках под домом, силовой электрощит',
                                'наружное и внутреннее освещение',
                                'вентиляция - вентиляционные клапаны',
                                'отопление - электрические конвекторы Ballu Enzo']},

            {'name': 'ОБОРУДОВАНИЕ И САНТЕХНИКА',
             'house_addition': ['тёплые полы в ванной комнате',
                                'ванная комната: умывальник, душевая кабина, смесители, унитаз',
                                'бойлер на 100 литров',
                                'снегозадержатели и водосточная система']},

            {'name': 'МОНТАЖ',
             'house_addition': ['полная сборка дома из панелей на расстоянии до 100 км от Москвы']},

            {'name': 'РАЗНОЕ',
             'house_addition': ['монтаж дома',
                                'отделка',
                                'коммуникации',
                                'оборудование и сантехника',
                                'выезд монтажной бригады далее 100 км от Москвы',
                                'доставка домокомплекта (стоимость доставки)',
                                'фундамент',
                                'мебель и бытовая техника',
                                'большая терраса']},
        ]
        for cat in addition_categories:
            try:
                category = HouseAdditionCategory.objects.get_or_create(name=cat['name'])
                logger.success(f'Категория {category} успешно добавлена')
            except Exception as e:
                logger.error(f'ОШИБКА: {e}')
            for addition in cat['house_addition']:
                try:
                    addit = HouseAddition.objects.create(category=category[0], body=addition)
                    logger.success(f'Доп штука {addit} успешно добавлена')
                except Exception as e:
                    logger.error(f'{e}')

    def get_delivery_additions_include(self):
        return list(HouseAddition.objects.filter(
            body__in=['окна (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                      'входные двери (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                      'панорамное остекление (двухкамерные стеклопакеты толщиной 38 мм)',
                      'силовой каркас дома выполнен из клеенного бруса хвойных пород',
                      'утепление 150 мм базальтовые плиты (200 мм на выбор)',
                      'кровля фальцевая (или металлочерепица)',
                      'полы из 16 мм ЦСП (цементно-стружечная плита)',
                      'стены снаружи имитация бруса (или планкен)',
                      'стены и потолок внутри из 12 мм ГСП (гипсо-стружечная плита)',
                      ]))

    def get_delivery_additions_not_include(self):
        return list(HouseAddition.objects.filter(
            body__in=['монтаж дома',
                      'отделка',
                      'коммуникации',
                      'оборудование и сантехника',
                      'выезд монтажной бригады далее 100 км от Москвы',
                      'доставка домокомплекта (стоимость доставки)',
                      'фундамент',
                      'мебель и бытовая техника',
                      'большая терраса'
                      ]))

    def get_for_finishing_additions_include(self):
        return list(HouseAddition.objects.filter(
            body__in=['полная сборка дома из панелей на расстоянии до 100 км от Москвы',
                      'силовой каркас дома выполнен из клеенного бруса хвойных пород',
                      'утепление 150 мм базальтовые плиты (200 мм на выбор)',
                      'кровля фальцевая (или металлочерепица)',
                      'полы из 16 мм ЦСП (цементно-стружечная плита)',
                      'стены снаружи имитация бруса (или планкен)',
                      'стены и потолок внутри из 12 мм ГСП (гипсо-стружечная плита)',
                      'крыльцо (лестница, терраса 1,5х1,2 м, козырек)',
                      'окна (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                      'входные двери (деревянные рамы, двухкамерные стеклопакеты толщиной 38 мм)',
                      'панорамное остекление (двухкамерные стеклопакеты толщиной 38 мм)'
                      ]))

    def get_for_finishing_additions_not_include(self):
        return list(HouseAddition.objects.filter(
            body__in=['отделка',
                      'коммуникации',
                      'оборудование и сантехника',
                      'выезд монтажной бригады далее 100 км от Москвы',
                      'доставка домокомплекта (стоимость доставки)',
                      'фундамент',
                      'мебель и бытовая техника',
                      'большая терраса'
                      ]))

    def get_turnkey_additions_include(self):
        return list(HouseAddition.objects.exclude(
            body__in=['монтаж дома',
                      'отделка',
                      'коммуникации',
                      'оборудование и сантехника',
                      'выезд монтажной бригады далее 100 км от Москвы',
                      'доставка домокомплекта (стоимость доставки)',
                      'фундамент',
                      'мебель и бытовая техника',
                      'большая терраса'
                      ]))

    def get_turnkey_additions_not_include(self):
        return list(HouseAddition.objects.filter(
            body__in=['выезд монтажной бригады далее 100 км от Москвы',
                      'доставка домокомплекта (стоимость доставки)',
                      'фундамент',
                      'мебель и бытовая техника',
                      'большая терраса'
                      ]))

    def create_configurations(self):
        configuration = Configuration.objects.get_or_create(name='Поставка с завода',
                                                            description='Домокомплект из упакованных панелей с крепежом'
                                                                        ' для монтажа. Без доставки.')
        configuration[0].included_in_price.add(*self.get_delivery_additions_include())
        configuration[0].not_included_in_price.add(*self.get_delivery_additions_not_include())
        configuration_1 = Configuration.objects.get_or_create(name='Под ключ',
                                                              description='Дом с окнами, входной дверью и перегородками'
                                                                          ' смонтированный на участке. Без доставки.')
        configuration_1[0].included_in_price.add(*self.get_for_finishing_additions_include())
        configuration_1[0].not_included_in_price.add(*self.get_for_finishing_additions_not_include())

        configuration_2 = Configuration.objects.get_or_create(name='Под мебель',
                                                              description='Полностью готовый дом, включая внутреннюю и '
                                                                          'наружную отделку.')
        configuration_2[0].included_in_price.add(*self.get_turnkey_additions_include())
        configuration_2[0].not_included_in_price.add(*self.get_turnkey_additions_not_include())

    def add_configurations_to_houses(self):
        houses = House.objects.all()
        # houses.update(configurations=Configuration.objects.all()[0])
        configurations = Configuration.objects.all()
        for house in houses:
            for conf in configurations:
                configurations_in_house = ConfigurationInHouses.objects.create(house=house, configuration=conf)



            # logger.info(house)
            # logger.info(house.configurations)
            # # logger.info((list(Configuration.objects.all())))
            # house.configurations.set(list(Configuration.objects.all()))
            # house.save()

    def handle(self, **options):
        self.create_house_addition_category()
        self.create_configurations()
        self.add_configurations_to_houses()
