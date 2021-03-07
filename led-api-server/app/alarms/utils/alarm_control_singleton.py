from alarms.utils.stoppable_thread import StoppableThread
from alarms.threads import AlarmThread


# Singleton class as defined in:
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
class AlarmControlSingleton:
    class __AlarmControlSingleton:
        def __init__(self):
            self.thread = None

        def start_alarm(self, **kwargs):
            self.stop_alarm()
            self.thread = AlarmThread(**kwargs)
            self.thread.start()
            return self.thread

        def stop_alarm(self):
            if (
                issubclass(type(self.thread), StoppableThread)
                and self.thread.is_alive()
                and not self.thread.stopped()
            ):
                self.thread.stop()
                self.thread.join()

    instance = None

    def __init__(self):
        if not AlarmControlSingleton.instance:
            AlarmControlSingleton.instance = (
                AlarmControlSingleton.__AlarmControlSingleton()
            )

    def __getattr__(self, name):
        return getattr(self.instance, name)