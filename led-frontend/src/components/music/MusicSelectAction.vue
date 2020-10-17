<template>
  <div>
    <MusicSearch
      @track-clicked="openTrackActions"
    />
    <q-dialog
      v-model="trackActions"
      dark
    >
      <q-card dark>
        <q-card-section
          class="q-pt-none q-mx-none scroll"
          style="max-height: 50vh"
        >
          <q-markup-table
            dark
            dense
            class="text-left"
          >
            <tbody>
              <tr
                v-for="track in tracks"
                :key="track.uri"
              >
                <td>
                  <slot :track="track">
                    <q-btn-group>
                      <q-btn
                        icon="play_arrow"
                        dense
                        color="primary"
                        @click="$emit('play-now', track.uri)"
                      />
                      <q-btn
                        icon="playlist_add"
                        dense
                        color="secondary"
                        @click="$emit('add-to-playlist', track.uri)"
                      />
                    </q-btn-group>
                  </slot>
                </td>
                <td>
                  <img
                    v-if="track.uri in trackImageUris"
                    :src="trackImageUris[track.uri][0].uri"
                    style="max-height: 3em"
                  >
                </td>
                <td>
                  <div class="text-weight-bold">
                    {{ track.name }}
                  </div>
                  <div>{{ track.artists.map(a => a.name).join(', ') }}</div>
                </td>
              </tr>
            </tbody>
          </q-markup-table>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import MusicSearch from 'components/music/MusicSearch';

export default {
  components: { MusicSearch },
  data () {
    return {
      status: window.mopidyStatus,
      mopidy: window.mopidy,
      trackActions: false,
      tracks: [],
      trackImageUris: {},
    };
  },
  methods: {
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

  },
};
</script>
