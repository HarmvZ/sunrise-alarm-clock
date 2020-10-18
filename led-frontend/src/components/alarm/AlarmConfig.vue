<template>
  <div>
    <card
      title="Color progression"
      caption="Set transition colors"
      icon="palette"
    >
      <ColorTransitionSelect class="q-ma-md" />
    </card>
    <card
      title="Music"
      caption="Set music"
      icon="audio_track"
    >
      <q-card
        class="q-pa-md"
        flat
        dark
        bordered
      >
        <q-card-section
          horizontal
          dark
          class="justify-between"
        >
          <q-card-section class="q-pt-xs">
            <div class="text-overline">
              Playlist
            </div>
            <div class="text-h5 q-mt-sm q-mb-xs">
              {{ playlist.name }}
            </div>
          </q-card-section>
          <q-card-section class="col-5 flex flex-center">
            <q-img
              class="rounded-borders"
              :src="playlist.imageUri"
            />
          </q-card-section>
        </q-card-section>

        <q-card-actions>
          <q-btn
            v-if="playlistUri !== ''"
            label="Edit playlist"
            icon="open_in_new"
            class="full-width q-mb-sm"
            dark
            color="grey-9"
            @click="openURL(`http://${hostname}:6680/iris/playlist/${playlistUri}`)"
          />

          <q-btn
            label="Set playlist"
            icon="queue_music"
            dark
            color="grey-9"
            class="full-width"
          >
            <q-popup-proxy
              ref="playlistpopup"
              dark
              class="full-width row justify-center bg-black"
            >
              <Playlists @playlist-click="onPlaylistClick" />
            </q-popup-proxy>
          </q-btn>
        </q-card-actions>
      </q-card>
    </card>
    <card
      title="Volume progression"
      caption="Set volume progression"
      icon="volume_up"
    >
      <VolumeTransitionSelect class="q-ma-md" />
    </card>
  </div>
</template>

<script>
import VolumeTransitionSelect from 'src/components/VolumeTransitionSelect';
import ColorTransitionSelect from 'src/components/ColorTransitionSelect';
import Playlists from 'src/components/music/Playlists';
import { openURL } from 'quasar';

export default {
  name: 'AlarmConfig',
  components: { VolumeTransitionSelect, Playlists, ColorTransitionSelect },
  data () {
    return {
      mopidy: window.mopidy,
      mopidyStatus: window.mopidyStatus,
      playlist: {
        name: 'None',
        imageUrl: '',
      },
      playlistUri: '',
    };
  },
  watch: {
  },
  mounted () {
  },
  methods: {
    onPlaylistClick (playlist) {
      this.playlist = playlist;
      this.playlistUri = playlist.uri;
      this.$refs.playlistpopup.hide();
    },
    triggerChange () {
      // TODO
    },
    openURL,
  },
};
</script>
