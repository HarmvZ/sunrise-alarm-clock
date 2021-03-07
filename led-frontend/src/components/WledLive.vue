<template>
  <div
    v-if="enabled"
    class="row justify-between content-stretch"
    style="height:2em;"
  >
    <div
      v-for="(l, index) in leds"
      :key="index"
      :style="{
        backgroundColor: `#${l}`,
      }"
      class="col"
    />
  </div>
</template>

<style>
</style>

<script>
import { mapState } from 'vuex';
import { openURL } from 'quasar';

export default {
  name: 'WledLive',
  data () {
    return {
      wledUrl: process.env.WLED_UI,
      leds: [],
    };
  },
  computed: {
    enabled () {
      return this.wledStatus === 1;
    },
    ...mapState({
      wledStatus: 'wledStatus',
      wledState: 'wledState',
      wledPalettes: 'wledPalettes',
      wledEffects: 'wledEffects',
    }),
  },
  watch: {
    wledStatus: {
      handler: function (val) {
        if (val === 1) {
          this.sendMessage({ 'lv': true });
        }
      },
      immediate: true,
    },
  },
  mounted () {
    this.sendMessage({ 'lv': true });
    this.$wledSocket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if ('leds' in data) {
        this.leds = data.leds;
      }
    });
  },
  destroyed () {
    this.sendMessage({ 'lv': false });
  },
  methods: {
    openURL,
    sendMessage (msg) {
      if (this.wledStatus === 1) {
        this.$wledSocket.send(JSON.stringify(msg));
      }
    },
  },
};
</script>
