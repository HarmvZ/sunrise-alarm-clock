<template>
  <q-card
    class="col-12 bg-grey-9 text-center q-mt-md"
  >
    <q-card-section class="bg-primary text-white">
      <div class="text-h5">Music</div>
    </q-card-section>
    <q-parallax
      :src="imageURL"
      :height="250"
      class="opacity-parallax"
    >
    </q-parallax>
    <q-card-section class="column items-center">
      <div class="text-h3 text-white">{{ trackName }}</div>
      <div class="text-h4 text-white">{{ artists }}</div>
      <div class="text-h5 text-gray-8">{{ albumName }}</div>
    </q-card-section>

    <q-card-section class="column items-center">
      <div class="items-center q-mb-md">
        <div v-if="timePosition">
          {{ state }} at {{ timePosition / 1000 }}s
        </div>
        <div v-else>
          {{ state }}
        </div>
      </div>
    </q-card-section>
    <q-card-section class="column items-center">

      <q-btn-group>
        <q-btn
          color="primary"
          icon="skip_previous"
          @click="mopidy.playback.previous()"
        />
        <q-btn
          v-if="state === 'playing'"
          color="primary"
          icon="pause"
          @click="mopidy.playback.pause()"
        />
        <q-btn
          v-if="state === 'paused' || state === 'stopped'"
          color="primary"
          icon="play_arrow"
          @click="mopidy.playback.play()"
        />
        <q-btn
          color="primary"
          icon="skip_next"
          @click="mopidy.playback.next()"
        />
      </q-btn-group>
    </q-card-section>
    <q-card-section class="column items-center">
      <q-btn-group>
        <q-btn
          :color="repeat ? 'primary' : ''"
          icon="repeat"
          @click="mopidy.tracklist.setRepeat([!repeat])"
        />
        <q-btn
          :color="single ? 'primary' : ''"
          icon="repeat_one"
          @click="mopidy.tracklist.setSingle([!single])"
        />
        <q-btn
          :color="random ? 'primary' : ''"
          icon="shuffle"
          @click="mopidy.tracklist.setRandom([!random])"
        />
      </q-btn-group>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'Audio',
  props: {
    mopidy: {
      type: Object,
      required: true,
    },
  },
  data () {
    return {
      connected: false,
      state: null,
      timePosition: 0,
      track: null,
      trackName: null,
      artists: null,
      albumName: null,
      imageURL: null,
      imageWidth: 0,
      imageHeight: 0,
      repeat: false,
      single: false,
      random: false,
    };
  },
  mounted () {
    this.mopidy.playback.getState().then((state, timePosition) => this.updatePlaybackState(state, timePosition));
    this.mopidy.playback.getCurrentTrack().then((track) => this.updateCurrentTrack(track));
    this.mopidy.on('event:playbackStateChanged', eObj => {
      this.updatePlaybackState(eObj.new_state, eObj.time_position);
    });

    this.mopidy.on('event:trackPlaybackStarted', eObj => {
      this.updateCurrentTrack(eObj.tl_track.track);
    });

    this.mopidy.on('event:trackPlaybackStopped', () => {
      this.updatePlaybackState('stopped');
    });

    this.mopidy.on('event:trackPlaybackPaused', eObj => {
      this.updatePlaybackState('paused', eObj.time_position);
    });

    this.mopidy.on('event:trackPlaybackResumed', () => {});
    this.mopidy.on('event:optionsChanged', () => {
      this.updateOptions();
    });
    this.updateOptions();
  },
  methods: {
    updatePlaybackState (state, timePosition) {
      this.state = state;
      this.timePosition = timePosition;
    },
    updateCurrentTrack (track) {
      this.track = track;
      if (track === null) {
        return;
      }
      this.trackName = track.name;
      this.artists = track.artists.map((a) => a.name).join(', ');
      this.albumName = track.album.name;
      if (track.album.date) {
        this.albumName = `${this.albumName} (${track.album.date})`;
      }

      this.mopidy.library
        .getImages([[track.uri]])
        .then((result) => this.updateCover(track.uri, result));
    },
    updateCover (trackUri, images) {
      const [image] = images[trackUri];
      this.imageURL = image.uri;
      this.imageWidth = image.width;
      this.imageHeight = image.height;
    },
    updateOptions () {
      this.mopidy.tracklist.getRepeat().then(repeat => { this.repeat = repeat; });
      this.mopidy.tracklist.getSingle().then(single => { this.single = single; });
      this.mopidy.tracklist.getRandom().then(random => { this.random = random; });
    },
  },
};
</script>
