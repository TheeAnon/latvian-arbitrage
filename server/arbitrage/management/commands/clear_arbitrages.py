from django.core.management.base import BaseCommand
from arbitrage.models import ArbitrageOpportunity

class Command(BaseCommand):
    help = 'Clears all entries from the ArbitrageOpportunity model'

    def handle(self, *args, **kwargs):
        try:
            ArbitrageOpportunity.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully cleared all ArbitrageOpportunity entries'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to clear ArbitrageOpportunity entries: {str(e)}'))
