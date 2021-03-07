<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
import Vue from 'vue';
import request from 'src/mixins/request';
import { mapMutations } from 'vuex';

Vue.prototype.$appName = 'Sunrise Alarm Clock';

Vue.mixin(request);

export default {
  name: 'App',
  created () {
    this.$mopidy.connect();
    this.$mopidy.on('state:offline', () => {
      this.setMopidyStatus(2);
    });
    this.$mopidy.on('state:online', () => {
      this.setMopidyStatus(1);
    });

    // Setup WLED socket connection
    this.$wledSocket.addEventListener('open', (event) => {
      this.setWledStatus(1);
    });
    this.$wledSocket.addEventListener('close', (event) => {
      this.setWledStatus(2);
    });
    this.$wledSocket.addEventListener('error', (event) => {
      this.setWledStatus(2);
    });
    this.$wledSocket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if ('state' in data) {
        this.setWledState(data.state);
      }
    });
    this.$axios.get(process.env.WLED_API).then(r => {
      if (r.status === 200) {
        this.setWledPalettes(r.data.palettes);
        this.setWledEffects(r.data.effects);
      }
    });
  },
  destroyed () {
    this.$mopidy.close();
    this.$mopidy.off();

    this.$wledSocket.close();
  },
  methods: {
    ...mapMutations({
      setWledStatus: 'setWledStatus',
      setWledState: 'setWledState',
      setWledEffects: 'setWledEffects',
      setWledPalettes: 'setWledPalettes',
      setMopidyStatus: 'setMopidyStatus',
    }),
  },
};
</script>

<style>
</style>
