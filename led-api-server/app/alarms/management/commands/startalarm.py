from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from api.zmq_client import ZMQClient


class Command(BaseCommand):
    help = "Triggers alarm scripts on zmq server"

    def log(self, msg):
        dt = datetime.now()
        self.stdout.write("{} - {}".format(dt, msg))

    def handle(self, *args, **options):

        self.log("Starting alarm")
        try:
            zmqc = ZMQClient()
            zmqc.perform_request("start_alarm")
        except Exception as e:
            self.log(str(e))
            raise CommandError(str(e))
        self.log("Alarm successfully started")
