<template>
  <q-page class="q-px-md">
    <div
      v-if="connected"
      class="col-12"
    >
      <Audio :mopidy="mopidy" />
      <Volume :mopidy="mopidy" />
    </div>
    <q-spinner
      v-else
      color="primary"
      size="6em"
      :thickness="2"
      class="q-ma-xl"
    />

  </q-page>

</template>

<style>
</style>

<script>
import Mopidy from 'mopidy';
import Audio from 'components/Audio';

export default {
  name: 'Music',
  components: { Audio },
  data () {
    return {
      connected: false,
      mopidy: null,
    };
  },
  mounted () {
    this.mopidy = new Mopidy({
      webSocketUrl: 'ws://raspberrypi:6680/mopidy/ws',
    });
    this.mopidy.on('state:online', () => {
      this.connected = true;
    });
  },
};
</script>
