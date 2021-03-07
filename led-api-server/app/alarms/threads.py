import time
from alarms.utils.mopidy_client import MopidyClient

from alarms.utils.stoppable_thread import StoppableThread
from alarms.utils.wled_client import WledClient


class AlarmThread(StoppableThread):
    def __init__(self, **kwargs):
        super().__init__()

        self.timestep = 0.2  # duration of each step in seconds
        self.mopidy_client = MopidyClient()
        self.volume = 0

        self.wled_client = WledClient()

        self.duration = kwargs["duration"]
        self.colors = kwargs["colors"]
        self.playlist = kwargs["playlist"]
        self.volumes = kwargs["volumes"]

        self.start_time = time.time()
        self.steps = self.duration / self.timestep  # nr of steps
        self.nr_of_color_transitions = len(self.colors) - 1
        self.steps_per_color = self.steps / self.nr_of_color_transitions
        self.start_volume = self.volumes[0][1]
        self.end_volume = self.volumes[-1][1]

    def run(self):
        """
        Transition all leds to white
        :param steps: number of steps in transition
        :param timestep: time that one step takes in ms
        """

        def step_color(step_nr):
            color_from = self.colors[int(step_nr / self.steps_per_color)]
            color_to = self.colors[int(step_nr / self.steps_per_color) + 1]
            color_delta = [c0 - c1 for c0, c1 in zip(color_to, color_from)]
            step_slope = (step_nr % self.steps_per_color) / self.steps_per_color
            color_rgb = [
                int(c0 + step_slope * c1) for c0, c1 in zip(color_from, color_delta)
            ]

            return color_rgb

        def step_volume(step_nr):
            step_ratio = step_nr / self.steps
            volume_delta = self.end_volume - self.start_volume
            volume = int(self.start_volume + step_ratio * volume_delta)
            print("step volume", volume)
            if self.volume != volume:
                self.mopidy_client.set_volume(volume)
                self.volume = volume

        if self.playlist != "":
            self.mopidy_client.start_playlist(self.playlist, self.start_volume)

        step = 0
        while step < self.steps:
            self.wled_client.set_color(step_color(step))
            step_volume(step)

            time.sleep(self.timestep)

            expected_time = self.start_time + step * self.timestep
            actual_time = time.time()
            time_delta = actual_time - expected_time
            step_correction = time_delta / self.timestep
            step += step_correction + 1

            if self.stopped():
                return False
