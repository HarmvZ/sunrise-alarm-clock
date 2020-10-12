import time

# import pygame
import numpy as np
# from gtts import gTTS
from rpi_ws281x import Color
from settings import LED_DITHERING_STEPS
# from utils.alarm_text import create_text
from utils.stoppable_thread import StoppableThread


class AlarmThread(StoppableThread):
    def __init__(self, strip, **kwargs):
        super().__init__(strip)
        self.steps = kwargs["steps"]
        self.timestep = kwargs["timestep"]

    def run(self):
        """
        Transition all leds to white
        :param steps: number of steps in transition
        :param timestep: time that one step takes in ms
        """
        def transition(start_color, final_color, steps):
            """ Transition with dithering """
            color_delta = final_color - start_color
            for i in range(self.steps):
                # create linear i in range 0 to 100
                lin_range = i / (self.steps - 1) * 100
                color_rgb = start_color + color_delta * lin_range / 100
                color = Color(
                    int(color_rgb[0]),
                    int(color_rgb[1]),
                    int(color_rgb[2])
                )
                for i in range(4):
                    for j in range(
                        0,
                        self.strip.numPixels(),
                        LED_DITHERING_STEPS
                    ):
                        self.strip.setPixelColor(j + i, color)
                    self.strip.show()

                    if self.stopped():
                        return False
                    time.sleep(self.timestep / (LED_DITHERING_STEPS * 1000))
            return True

        final_color = np.array([214, 108, 0])
        start_color = np.array([0, 0, 0])
        if not transition(start_color, final_color, int(self.steps / 2)):
            return

        start_color = np.array([214, 108, 0])
        final_color = np.array([255, 255, 255])
        if not transition(start_color, final_color, int(self.steps / 2)):
            return


        # alarm_text = create_text()
        # if self.stopped():
        #     return

        # tts = gTTS(alarm_text, lang="nl")
        # tts.save(SOUND_FILE_PATH)

        # if self.stopped():
        #     return

        # pygame.mixer.init()
        # pygame.mixer.music.load(SOUND_FILE_PATH)
        # while pygame.mixer.get_busy():
        #     pygame.mixer.music.get_pos()
        #     if self.stopped():
        #         pygame.mixer.quit()
        #         return
