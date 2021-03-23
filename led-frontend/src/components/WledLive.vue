<template>
  <div>
    <q-toggle
      :value="showPreview"
      label="Show preview"
      @input="togglePreview"
    />
    <div
      v-if="enabled && showPreview"
      class="row justify-between content-stretch"
      style="height:3em;"
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
      showPreview: true,
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
          if (Object.keys(this.wledState).length === 0) {
            // Send extra message through socket to receive state
            this.sendMessage({ v: true });
            setTimeout(() => {
              this.sendMessage({ lv: true });
            }, 200);
          } else {
            this.sendMessage({ lv: true });
          }
        }
      },
      immediate: true,
    },
  },
  mounted () {
    this.$wledSocket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if ('leds' in data) {
        this.leds = data.leds;
      }
    });
  },
  destroyed () {
    this.sendMessage({ lv: false });
  },
  methods: {
    openURL,
    sendMessage (msg) {
      if (this.wledStatus === 1) {
        this.$wledSocket.send(JSON.stringify(msg));
      }
    },
    togglePreview (value, evt) {
      if (value) {
        this.sendMessage({ lv: true });
      } else {
        this.sendMessage({ lv: false });
      }
      this.showPreview = value;
    },
  },
};
</script>
