import os
import requests


class MopidyClient:
    def __init__(self):
        self.url = os.environ.get("MOPIDY_API")
        self.connected = True

    def __request(self, method, params=None):
        if not self.connected:
            return
        try:
            data = {"jsonrpc": "2.0", "id": 1, "method": method}
            if params is not None:
                data["params"] = params
            r = requests.request(
                "POST",
                self.url,
                json=data,
            )
            self.connected = True
            return r.json()["result"]
        except Exception as e:
            self.connected = False
            print(str(e))
            raise e

    def start_playlist(self, playlist_uri, start_volume):
        self.stop_playback()
        playlist = self.__request("core.playlists.lookup", params={"uri": playlist_uri})
        uris = [t["uri"] for t in playlist.get("tracks", [])]
        self.__request("core.tracklist.add", params={"uris": uris})
        self.__request("core.mixer.set_volume", params={"volume": start_volume})
        self.__request("core.playback.play")

    def set_volume(self, volume):
        self.__request("core.mixer.set_volume", params={"volume": volume})

    def stop_playback(self):
        self.__request("core.playback.stop")
        self.__request("core.tracklist.clear")
