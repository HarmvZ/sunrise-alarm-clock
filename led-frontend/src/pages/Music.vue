<template>
  <q-page class="q-px-md">
    <div
      v-if="status === 0"
      class="col-12 text-center"
    >
      <q-spinner
        color="primary"
        size="6em"
        :thickness="2"
        class="q-ma-xl"
      />
    </div>
    <div
      v-if="status === 1"
      class="col-12"
    >
      <Audio :mopidy="mopidy" />
      <Volume :mopidy="mopidy" />
      <card title="Music search">
        <MusicSearch @track-clicked="openTrackActions" />
        <q-dialog
          v-model="trackActions"
        >
          <q-card>
            <q-card-section class="q-pt-none">
              <q-markup-table>
                <thead>
                  <tr>
                    <th class="text-right">
                      Action
                    </th>
                    <th class="text-left">
                      Song
                    </th>
                    <th class="text-left">
                      Artists
                    </th>
                    <th class="text-left">
                      Album
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="track in tracks"
                    :key="track.uri"
                  >
                    <td class="text-right">
                      <q-btn
                        icon="play_arrow"
                        @click="playTrack(track.uri)"
                      />
                    </td>
                    <td class="text-left">
                      {{ track.name }}
                    </td>
                    <td class="text-left">
                      {{ track.artists.map(a => a.name).join(', ') }}
                    </td>
                    <td class="text-left">
                      {{ track.album.name }}
                    </td>
                  </tr>
                </tbody>
              </q-markup-table>
            </q-card-section>

            <q-card-actions
              align="right"
              class="bg-white text-teal"
            >
              <q-btn
                v-close-popup
                flat
                label="OK"
              />
            </q-card-actions>
          </q-card>
        </q-dialog>
      </card>
      <card title="Mopidy Iris">
        <q-card-section class="column items-center q-mt-md">
          <q-btn
            color="primary"
            @click="openURL(`http://${hostname}:6680/iris/`)"
          >
            Open Mopidy Iris&nbsp;
            <q-icon name="open_in_new" />
          </q-btn>
        </q-card-section>
      </card>
    </div>
    <div
      v-if="status === 2"
      class="col-12"
    >
      <q-card
        class="col-12 bg-grey-9 text-center q-mt-md"
      >
        <q-card-section class="">
          <div class="">
            MPD server connection failure
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import { openURL } from 'quasar';
import Audio from 'components/Audio';
import Volume from 'components/Volume';
import MusicSearch from 'components/music/MusicSearch';

export default {
  name: 'Music',
  components: { Audio, Volume, MusicSearch },
  data () {
    return {
      status: window.mopidyStatus,
      mopidy: window.mopidy,
      hostname: process.env.HOSTNAME,
      trackActions: false,
      tracks: [],
      trackImageUris: {},
    };
  },
  methods: {
    openURL,
    openTrackActions (uri) {
      window.mopidy.library.lookup({ uris: [uri] }).then(tracks => {
        this.tracks = [];
        for (const ts of Object.values(tracks)) {
          this.tracks.push(...ts);
        }
        const uris = this.tracks.map(t => t.uri);
        window.mopidy.library.getImages([uris]).then(images => {
          for (const [uri, image] of Object.entries(images)) {
            this.trackImageUris[uri] = image;
          }
          this.trackActions = true;
        });
      });
    },
    playTrack (uri) {
      window.mopidy.tracklist.add({ uris: [uri], at_position: 1 }).then(tlTracks => {
        window.mopidy.playback.play({ tl_track: tlTracks[tlTracks.length - 1] });
      });
    },
  },
};
</script>
