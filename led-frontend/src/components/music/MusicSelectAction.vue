<template>
  <div>
    <MusicSearch
      @track-clicked="openTrackActions"
    />
    <q-dialog
      ref="dialog"
      v-model="trackActions"
      dark
      content-class="bg-secondary"
    >
      <q-markup-table
        dark
        dense
        class="text-left "
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
                    color="accent"
                    @click="onPlayClick(track.uri)"
                  />
                  <q-btn
                    icon="playlist_add"
                    dense
                    color="primary"
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
    </q-dialog>

    <q-inner-loading
      dark
      :showing="loading"
    >
      <q-spinner
        size="50px"
        color="primary"
      />
    </q-inner-loading>
  </div>
</template>

<script>
import MusicSearch from 'components/music/MusicSearch';

export default {
  components: { MusicSearch },
  data () {
    return {
      loading: false,
      trackActions: false,
      tracks: [],
      trackImageUris: {},
    };
  },
  methods: {
    openTrackActions (uri) {
      this.loading = true;
      this.$mopidy.library.lookup({ uris: [uri] }).then(tracks => {
        this.tracks = [];
        for (const ts of Object.values(tracks)) {
          this.tracks.push(...ts);
        }
        const uris = this.tracks.map(t => t.uri);
        this.$mopidy.library.getImages([uris]).then(images => {
          for (const [uri, image] of Object.entries(images)) {
            this.trackImageUris[uri] = image;
          }
          this.trackActions = true;
          this.loading = false;
        });
      });
    },
    onPlayClick (trackUri) {
      this.$emit('play-now', trackUri);
      this.$refs.dialog.hide();
    },
  },
};
</script>
