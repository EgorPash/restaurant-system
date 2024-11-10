from django.core.management import BaseCommand

from service.models import Table, TimeSection


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        tables_list = [
            {"number": 1, "seats": 4},
            {"number": 2, "seats": 2},
            {"number": 3, "seats": 6},
        ]

        prepare_to_fill_tables_list = []
        for table_data in tables_list:
            table = Table.objects.create(**table_data)
            table.times.set(TimeSection.objects.all())