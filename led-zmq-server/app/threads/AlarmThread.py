import numpy as np
import time
from rpi_ws281x import Color
from utils.stoppable_thread import StoppableThread


class AlarmThread(StoppableThread):
    def __init__(self, strip, **kwargs):
        super().__init__(strip)
        self.steps = kwargs["steps"]
        self.timestep = kwargs["timestep"]
        self.music_thread = None

    def run(self):
        """
        Transition all leds to white
        :param steps: number of steps in transition
        :param timestep: time that one step takes in ms
        """
        final_color = np.array([255, 255, 255])
        start_color = np.array([0, 0, 0])
        color_delta = final_color - start_color
        for i in range(self.steps):
            # create linear i in range 0 to 100
            lin_range = i / (self.steps - 1) * 100
            # create exponential range from 1 to exp(100)
            log_range = np.exp(lin_range)
            # create exponential range from 0 to 1
            log_range = (log_range - 1) / (np.exp(100) - 1)
            color = start_color + color_delta * lin_range / 100  # log_range
            self.color_wipe(Color(int(color[0]), int(color[1]), int(color[2])))
            if self.stopped():
                return
            time.sleep(self.timestep / 1000)

            # TODO add dithering, color from black -> deep orange ->  white

