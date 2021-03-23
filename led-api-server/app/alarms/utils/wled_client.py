import os
import requests


class WledClient:
    def __init__(self):
        self.url = os.environ.get("WLED_API")
        self.connected = True
        self.default_state = {
            "on": True,
            "bri": 255,
            "transition": 0,
            "ps": -1,
            "pl": -1,
            "nl": {
                "on": False,
            },
            "udpn": {"send": True, "recv": True},
        }

        r = self._get()
        if not self.connected:
            return
        state = r["state"]
        self.main_seg = state["mainseg"]
        self.default_state["seg"] = state["seg"]

    def __request(self, method, **kwargs):
        if not self.connected:
            return
        try:
            r = requests.request(method, self.url, **kwargs)
            self.connected = True
            return r.json()
        except Exception as e:
            self.connected = False
            print(str(e))
            raise e  # TODO remove/log?

    def _get(self):
        return self.__request(method="GET")

    def _post(self, json):
        return self.__request(method="POST", json=json)

    def set_color(self, color):
        if not self.connected:
            return
        new_state = dict(self.default_state)
        new_state["seg"][self.main_seg] = {
            "col": [color, color, color],
            "fx": 0,
            "pal": 0,
            "on": True,
            "bri": 255,
        }
        self._post(json=new_state)

    def power_off(self):
        if self.connected:
            self._post(json={"on": False})
