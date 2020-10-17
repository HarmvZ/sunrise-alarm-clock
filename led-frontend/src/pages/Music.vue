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
      <card
        title="Music search"
      >
        <MusicSelectAction
          class="q-pa-md"
          @play-now="playTrackNow($event)"
          @add-to-playlist="addTrackToPlaylistFirst($event)"
        />
      </card>
      <Volume :mopidy="mopidy" />
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
import MusicSelectAction from 'components/music/MusicSelectAction';

export default {
  name: 'Music',
  components: { Audio, Volume, MusicSelectAction },
  data () {
    return {
      status: window.mopidyStatus,
      mopidy: window.mopidy,
      hostname: process.env.HOSTNAME,
      trackActions: false,
    };
  },
  methods: {
    openURL,
    async playTrackNow (uri) {
      const tlTracks = await this.addTrackToPlaylistFirst(uri);
      await window.mopidy.playback.play({ tl_track: tlTracks[0] });
    },
    async addTrackToPlaylistFirst (uri) {
      const tlIndex = await window.mopidy.tracklist.index();
      const tlTracks = await window.mopidy.tracklist.add({ uris: [uri], at_position: tlIndex + 1 });
      return tlTracks;
    },
  },
};
</script>
