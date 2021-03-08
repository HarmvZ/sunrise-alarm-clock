from alarms.utils.mopidy_client import MopidyClient
from alarms.utils.stoppable_thread import StoppableThread
from alarms.threads import AlarmThread
from alarms.utils.wled_client import WledClient


# Singleton class as defined in:
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
class AlarmControlSingleton:
    class __AlarmControlSingleton:
        def __init__(self):
            self.thread = None

        def start_alarm(self, **kwargs):
            self.stop_thread()
            self.thread = AlarmThread(**kwargs)
            self.thread.start()
            return self.thread

        def stop_thread(self):
            if (
                issubclass(type(self.thread), StoppableThread)
                and self.thread.is_alive()
                and not self.thread.stopped()
            ):
                self.thread.stop()
                self.thread.join()

        def stop_alarm(self):
            self.stop_thread()
            mopidy_client = MopidyClient()
            mopidy_client.stop_playback()
            wled_client = WledClient()
            wled_client.power_off()

    instance = None

    def __init__(self):
        if not AlarmControlSingleton.instance:
            AlarmControlSingleton.instance = (
                AlarmControlSingleton.__AlarmControlSingleton()
            )

    def __getattr__(self, name):
        return getattr(self.instance, name)