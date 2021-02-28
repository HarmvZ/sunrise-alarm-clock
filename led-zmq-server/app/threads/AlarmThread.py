import time

import numpy as np
from mopidy_json_client import MopidyClient
from rpi_ws281x import Color

from utils.stoppable_thread import StoppableThread


class AlarmThread(StoppableThread):
    def __init__(self, strip, **kwargs):
        super().__init__(strip)

        self.timestep = 0.2  # duration of each step in seconds
        self.mopidy = False
        self.volume = 0

        self.duration = kwargs["duration"]
        self.colors = kwargs["colors"]
        self.playlist = kwargs["playlist"]
        self.volumes = kwargs["volumes"]

        self.n_pixels = self.strip.numPixels()
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

        # def transition(start_color, final_color, steps):
        #     """ Transition with dithering """
        #     color_delta = final_color - start_color
        #     for i in range(steps):
        #         # create linear i in range 0 to 100
        #         lin_range = i / (steps - 1) * 100
        #         color_rgb = start_color + color_delta * lin_range / 100
        #         color = Color(int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))
        #         for i in range(4):
        #             for j in range(0, self.strip.numPixels(), LED_DITHERING_STEPS):
        #                 self.strip.setPixelColor(j + i, color)
        #             self.strip.show()

        #             if self.stopped():
        #                 return False
        #             time.sleep(self.timestep / LED_DITHERING_STEPS)
        #     return True

        # for color_idx in range(nr_of_color_transitions):
        #     start_color = np.array(self.colors[color_idx])
        #     finish_color = np.array(self.colors[color_idx + 1])
        #     if not transition(
        #         start_color, finish_color, int(self.steps / nr_of_color_transitions)
        #     ):
        #         return

        def on_mopidy_connected(connection_status):
            print("connecting mopidy triggered", connection_status)

            if connection_status:
                print("starting mopidy requests")

                playlist = self.mopidy.playlists.lookup(self.playlist)
                uris = [t["uri"] for t in playlist["tracks"]]
                self.mopidy.playback.stop()
                self.mopidy.tracklist.clear()
                self.mopidy.tracklist.add(uris=uris)
                self.mopidy.mixer.set_volume(self.start_volume)
                self.volume = self.start_volume
                self.mopidy.playback.play()
                print(" mopidy requests play")

        def step_color(step_nr):
            color_from = np.array(self.colors[int(step_nr / self.steps_per_color)])
            color_to = np.array(self.colors[int(step_nr / self.steps_per_color) + 1])
            color_delta = color_to - color_from

            color_rgb = (
                color_from
                + ((step_nr % self.steps_per_color) / self.steps_per_color)
                * color_delta
            )
            color = Color(*[int(c) for c in color_rgb])
            # TODO dithering
            for i in range(self.n_pixels):
                self.strip.setPixelColor(i, color)
            self.strip.show()

        def step_volume(step_nr):
            step_ratio = step_nr / self.steps
            volume_delta = self.end_volume - self.start_volume
            volume = int(self.start_volume + step_ratio * volume_delta)
            if self.volume != volume:
                self.mopidy.mixer.set_volume(volume)
                self.volume = volume

        print("starting alarmthread")
        if self.playlist != "":
            self.mopidy = MopidyClient(
                ws_url="ws://raspberrypi:6680/mopidy/ws",
                error_handler=lambda e: print("ws error", e),
                connection_handler=on_mopidy_connected,
                autoconnect=False,
                retry_max=10,
                retry_secs=10,
            )
            print("connecting mopidy")

            self.mopidy.connect()
            print("connecting mopidy 1")

        step = 0
        while step < self.steps:
            step_color(step)
            if self.mopidy:
                step_volume(step)

            time.sleep(self.timestep)

            expected_time = self.start_time + step * self.timestep
            actual_time = time.time()
            time_delta = actual_time - expected_time
            step_correction = time_delta / self.timestep
            step += step_correction + 1

            if self.stopped():
                return False
