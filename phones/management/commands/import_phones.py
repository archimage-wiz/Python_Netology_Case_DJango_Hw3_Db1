import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for xphone in phones:
            
            Phone(
                id=xphone["id"],
                name=xphone["name"],
                price=xphone["price"],
                release_date=xphone["release_date"],
                lte_exists=xphone["lte_exists"],
                image=xphone["image"],
            ).save()
