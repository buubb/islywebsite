from django.core.management.base import BaseCommand
from django.utils import timezone
from axes.models import AccessLog

class Command(BaseCommand):
    help = 'Delete access logs older than 30 days'

    def handle(self, *args, **kwargs):
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        deleted_count, _ = AccessLog.objects.filter(attempt_time__lte=thirty_days_ago).delete()
        self.stdout.write(f'Successfully deleted {deleted_count} old access logs')
