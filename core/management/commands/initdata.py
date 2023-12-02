from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Init data for project"

    def handle(self, *args, **options):
        pass
