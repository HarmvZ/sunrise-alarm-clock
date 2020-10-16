<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
import Vue from 'vue';
import request from 'src/mixins/request';
import Mopidy from 'mopidy';

Vue.prototype.$appName = 'Sunrise Alarm Clock';

Vue.mixin(request);

export default {
  name: 'App',
  mounted () {
    window.mopidyStatus = 0;
    const mopidy = new Mopidy({
      webSocketUrl: 'ws://raspberrypi:6680/mopidy/ws', // TODO fix hostname?
    });
    mopidy.on('state:offline', () => {
      window.mopidyStatus = 2;
    });
    mopidy.on('state:online', () => {
      window.mopidyStatus = 1;
    });
    window.mopidy = mopidy;
  },
};
</script>

<style>
</style>
