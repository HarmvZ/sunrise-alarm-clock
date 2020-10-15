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
import Mopidy from 'mopidy';
import { openURL } from 'quasar';
import Audio from 'components/Audio';
import Volume from 'components/Volume';

export default {
  name: 'Music',
  components: { Audio, Volume },
  data () {
    return {
      status: 0, // 0: pending, 1: connected, 2: connection failure
      mopidy: null,
      hostname: process.env.HOSTNAME,
    };
  },
  mounted () {
    this.mopidy = new Mopidy({
      webSocketUrl: 'ws://raspberrypi:6680/mopidy/ws', // TODO fix hostname?
    });
    this.mopidy.on('state:online', () => {
      this.status = 1;
    });
    this.mopidy.on('state:offline', () => {
      this.status = 2;
      this.$q.notify({
        message: 'Can\'t connect to MPD server',
        position: 'top',
        color: 'negative',
        icon: 'report_problem',
      });
    });
  },
  methods: {
    openURL,
  },
};
</script>
