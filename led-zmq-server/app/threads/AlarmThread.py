import time

import pygame
import numpy as np
from gtts import gTTS
from rpi_ws281x import Color
from settings import SOUND_FILE_PATH
from utils.alarm_text import create_text
from utils.core_actions import color_wipe
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
            color_wipe(
                self.strip,
                Color(
                    int(color[0]),
                    int(color[1]),
                    int(color[2])
                )
            )
            if self.stopped():
                return
            time.sleep(self.timestep / 1000)

            # TODO add dithering, color from black -> deep orange ->  white

        alarm_text = create_text()
        if self.stopped():
            return

        tts = gTTS(alarm_text, lang="nl")
        tts.save(SOUND_FILE_PATH)

        if self.stopped():
            return

        pygame.mixer.init()
        pygame.mixer.music.load(SOUND_FILE_PATH)
        while pygame.mixer.get_busy():
            pygame.mixer.music.get_pos()
            if self.stopped():
                pygame.mixer.quit()
                return
