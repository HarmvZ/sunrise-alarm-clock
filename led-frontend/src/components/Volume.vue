<template>
  <q-item>
    <q-item-section side>
      <q-btn
        color="primary"
        :flat="!mute"
        :outline="mute"
        :icon="mute ? 'volume_off' : 'volume_up'"
        @click="$mopidy.mixer.setMute([!mute])"
      />
    </q-item-section>
    <q-item-section>
      <q-slider
        v-model="volume"
        :min="0"
        :max="100"
        label
        @change="changeVolume"
      />
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'Volume',
  data () {
    return {
      volume: 100,
      mute: false,
    };
  },
  mounted () {
    this.$mopidy.on('event:volumeChanged', eObj => {
      this.volume = eObj.volume;
    });

    this.$mopidy.on('event:muteChanged', eObj => {
      this.mute = eObj.mute;
    });
    this.$mopidy.mixer.getMute().then(mute => { this.mute = mute; });
    this.$mopidy.mixer.getVolume().then(volume => { this.volume = volume; });
  },
  methods: {
    incrementVolume (inc) {
      const v = Math.max(0, Math.min(100, this.volume + inc));
      this.$mopidy.mixer.setVolume([v]);
    },
    changeVolume (v) {
      this.$mopidy.mixer.setVolume([v]);
    },
  },
};
</script>
