<template>
  <card>
    <q-card-section
      v-if="wledStatus === 1"
      class="q-pa-none"
    >
      <q-parallax
        src="statics/light/3.jpg"
        :height="150"
        :speed=".5"
      >
        <div class="text-h5 text-white">
          {{ `LED dashboard` }}
        </div>
        <q-toggle
          :value="wledState.on"
          :disabled="!enabled"
          size="xl"
          icon="power_settings_new"
          color="accent"
          @input="sendMessage({ on: !wledState.on })"
        />
      </q-parallax>
      <WledLive />

      <q-item>
        <q-item-section side>
          <q-icon
            name="brightness_medium"
            color="primary"
          />
        </q-item-section>
        <q-item-section>
          <q-slider
            :value="wledState.bri"
            :min="0"
            :max="255"
            color="primary"
            @input="sendMessage({ on: true, bri: $event })"
          />
        </q-item-section>
      </q-item>
      <q-select
        filled
        dark
        :value="selectedPalette"
        :options="wledPalettes"
        label="Palette"
        class="q-mb-sm"
        @input="sendMessage({ on: true, seg: [{pal: wledPalettes.indexOf($event)}] })"
      />
      <q-btn-group
        v-if="mainSegment"
        spread
        class="q-mb-sm"
      >
        <q-btn
          v-for="n in 3"
          :key="n"
          icon="edit"
          :style="{
            backgroundColor: colorsRgb[n - 1]
          }"
        >
          <q-popup-proxy
            dark
            class="full-width row justify-center"
          >
            <q-color
              :value="colorsRgb[n - 1]"
              dark
              format-model="rgb"
              inline
              no-header
              default-view="palette"
              @change="changeColor($event, n - 1)"
            />
          </q-popup-proxy>
        </q-btn>
      </q-btn-group>
      <q-select
        filled
        dark
        :value="selectedEffect"
        :options="wledEffects"
        label="Effect"
        @input="sendMessage({ on: true, seg: [{fx: wledEffects.indexOf($event)}] })"
      />
      <q-item>
        <q-item-section side>
          <q-icon
            name="speed"
            color="primary"
          />
        </q-item-section>
        <q-item-section>
          <q-slider
            :value="mainSegment.sx"
            :min="0"
            :max="255"
            color="primary"
            @input="sendMessage({ on: true, seg: [{sx: $event}] })"
          />
        </q-item-section>
      </q-item>
      <q-btn
        color="primary"
        class="q-mb-md"
        @click="openURL(wledUrl)"
      >
        Open WLED UI&nbsp;
        <q-icon name="open_in_new" />
      </q-btn>
    </q-card-section>
    <q-card-section
      v-if="wledStatus === 2"
      class=""
    >
      <div class="">
        WLED connection failure
      </div>
    </q-card-section>
    <q-inner-loading :showing="wledStatus === 0">
      <q-spinner
        size="50px"
        color="primary"
      />
    </q-inner-loading>
  </card>
</template>

<style>
</style>

<script>
import { mapState } from 'vuex';
import { openURL } from 'quasar';
import WledLive from 'components/WledLive';

export default {
  name: 'WledControl',
  components: { WledLive },
  data () {
    return {
      wledUrl: process.env.WLED_UI,
    };
  },
  computed: {
    enabled () {
      return this.wledStatus === 1;
    },
    mainSegment () {
      try {
        return this.wledState.seg[this.wledState.mainseg];
      } catch (e) {
        return false;
      }
    },
    selectedPalette () {
      return this.wledPalettes[this.mainSegment.pal];
    },
    selectedEffect () {
      return this.wledEffects[this.mainSegment.fx];
    },
    colorsRgb () {
      return this.mainSegment.col.map(c => `rgb(${c.join(',')})`);
    },
    ...mapState({
      wledStatus: 'wledStatus',
      wledState: 'wledState',
      wledPalettes: 'wledPalettes',
      wledEffects: 'wledEffects',
    }),
  },
  methods: {
    openURL,
    sendMessage (msg) {
      if (this.wledStatus === 1) {
        this.$wledSocket.send(JSON.stringify(msg));
      }
    },
    changeColor (colorStr, index) {
      const colors = this.mainSegment.col.slice();
      colors[index] = colorStr.replace(/(rgb\()|\)/g, '').split(',');
      this.sendMessage({ on: true, seg: [{ col: colors }] });
    },
  },
};
</script>
