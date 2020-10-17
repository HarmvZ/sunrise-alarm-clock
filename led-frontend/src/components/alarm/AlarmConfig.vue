<template>
  <div>
    <card
      title="Color progression"
      caption="Set transition colors"
      icon="palette"
    >
      <ColorTransitionSelect />
    </card>
    <card
      title="Music"
      caption="Set music"
      icon="audio_track"
    >
      <q-expansion-item
        default-opened
        expand-separator
        dark
        icon="equalizer"
        label="Music"
        caption="Set music or sounds to play"
      >
        <div class="q-pa-md">
          <q-expansion-item
            expand-separator
            dark
            label="Playlist"
          >
            <div class="q-py-md">
              <q-list
                v-if="playlists.length > 0"
                bordered
                dark
                separator
              >
                <q-item-label header>
                  Playlists
                </q-item-label>
                <q-separator />
                <q-item
                  v-for="item in playlists.slice(0,10)"
                  :key="item.uri"
                  dark
                >
                  <q-item-section
                    top
                    avatar
                  >
                    <q-avatar rounded>
                      <img :src="playlistImageURIs[item.uri][0].uri">
                    </q-avatar>
                  </q-item-section>

                  <q-item-section>
                    <q-item-label>{{ item.name }}</q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </div>
          </q-expansion-item>
        </div>
        <MusicSelectAction
          class="q-pa-md"
          @play-now="playTrackNow($event)"
          @add-to-playlist="addTrackToPlaylistFirst($event)"
        >
          <template v-slot:default="slotProps">
            <q-btn
              label="Add"
              icon="library_add"
              @click="addTrackToList(slotProps.track.uri)"
            />
          </template>
        </MusicSelectAction>
      </q-expansion-item>
    </card>
    <card
      title="Volume progression"
      caption="Set volume progression"
      icon="volume_up"
    >
      <q-expansion-item
        default-opened
        expand-separator
        dark
        icon="volume_up"
        label="Volume"
        caption="Set volume progress"
      >
        <VolumeTransitionSelect />
      </q-expansion-item>
    </card>
  </div>
</template>

<style>
</style>

<script>
import VolumeTransitionSelect from 'src/components/VolumeTransitionSelect';
import ColorTransitionSelect from 'src/components/ColorTransitionSelect';

export default {
  name: 'AlarmConfig',
  components: { VolumeTransitionSelect, ColorTransitionSelect },
  props: {
  },
  data () {
    return {

      mopidy: window.mopidy,
      mopidyStatus: window.mopidyStatus,
      playlists: [],
      playlistImageURIs: {},
      tracks: [],

    };
  },
  computed: {

  },
  watch: {
    playlists: function (val) {
      const uris = val.map(pl => pl.uri);
      window.mopidy.library.getImages([uris]).then(r => { this.playlistImageURIs = r; });
    },
  },
  mounted () {
    if (this.mopidyStatus !== 1) {
      return;
    }
    this.mopidy.playlists.asList().then(pl => {
      this.playlists = pl;
    });
  },
  methods: {
    addTrackToList (track) {
      this.tracks.push(track.uri);
    },
    triggerChange () {
      // TODO
    },
  },
};
</script>
<style>
.q-parallax.opacity-parallax .q-parallax__media {
  background:#000;
}
.q-parallax.opacity-parallax .q-parallax__media img {
  opacity: .2;
}
</style>
