import time

# import pygame
import numpy as np

# from gtts import gTTS
from rpi_ws281x import Color
from settings import LED_DITHERING_STEPS

# from utils.alarm_text import create_text
from utils.stoppable_thread import StoppableThread
from mpd import MPDClient


class AlarmThread(StoppableThread):
    def __init__(self, strip, **kwargs):
        super().__init__(strip)
        self.duration = kwargs["duration"]
        self.colors = kwargs["colors"]
        self.playlist = kwargs["playlist"]
        self.volumes = kwargs["volumes"]

        self.timestep = 0.2  # duration of each step in seconds
        self.steps = self.duration / self.timestep  # nr of steps

    def run(self):
        """
        Transition all leds to white
        :param steps: number of steps in transition
        :param timestep: time that one step takes in ms
        """

        def transition(start_color, final_color, steps):
            """ Transition with dithering """
            color_delta = final_color - start_color
            for i in range(steps):
                # create linear i in range 0 to 100
                lin_range = i / (steps - 1) * 100
                color_rgb = start_color + color_delta * lin_range / 100
                color = Color(int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))
                for i in range(4):
                    for j in range(0, self.strip.numPixels(), LED_DITHERING_STEPS):
                        self.strip.setPixelColor(j + i, color)
                    self.strip.show()

                    if self.stopped():
                        return False
                    time.sleep(self.timestep / LED_DITHERING_STEPS)
            return True

        start_time = time.time()
        nr_of_color_transitions = len(self.colors) - 1

        # TODO start music, progress volume
        # client = MPDClient(use_unicode=True)
        # client.connect('localhost', 6690) # TODO
        # for entry in client.lsinfo("/"):
        #     pass

        for color_idx in range(nr_of_color_transitions):
            start_color = np.array(self.colors[color_idx])
            finish_color = np.array(self.colors[color_idx + 1])
            if not transition(
                start_color, finish_color, int(self.steps / nr_of_color_transitions)
            ):
                return
