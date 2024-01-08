from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.fill_verification_code_types()

    def fill_verification_code_types(self):
        call_command("loaddata", "verification_code_types")
