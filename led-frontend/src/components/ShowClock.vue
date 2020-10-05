<template>
  <div class="col-12 column q-pa-md">
    <q-dialog v-model="fgDialog">
      <q-color
        dark
        v-model="fg_color"
        format-model="rgb"
        inline
        no-header
      />
    </q-dialog>
    <q-dialog v-model="bgDialog">
      <q-color
        dark
        v-model="bg_color"
        format-model="rgb"
        inline
        no-header
      />
    </q-dialog>
    <div class="row q-mb-md">
      <div class="col-2" :style="'background: ' + fg_color + ';'"></div>
      <q-btn
        color="secondary"
        label="Set time color"
        @click="fgDialog = true"
        class="col-10"
      />
    </div>
    <div class="row q-mb-md">
      <div class="col-2" :style="'background: ' + bg_color + ';'"></div>
      <q-btn
        color="secondary"
        label="Set background color"
        @click="bgDialog = true"
        class="col-10"
      />
    </div>
    <q-btn
      color="primary"
      label="Show Clock"
      icon="query_builder"
      class="col-12"
      @click="showClock()"
    />
  </div>
</template>

<style>
</style>

<script>
import getRGBColorObject from 'src/utils/getRGBColorObject';

export default {
  name: 'ShowClock',
  data () {
    return {
      fgDialog: false,
      bgDialog: false,
      fg_color: 'rgb(255, 0, 0)',
      bg_color: 'rgb(0, 0, 0)',
    };
  },
  methods: {
    showClock () {
      const data = {};
      if (this.fg_color) {
        data['fg'] = getRGBColorObject(this.fg_color);
      }
      if (this.bg_color) {
        data['bg'] = getRGBColorObject(this.bg_color);
      }
      let url = '/api/show_clock/';
      this.request({
        method: 'POST',
        url,
        data,
        responseType: 'json',
      });
    },
  },
};
</script>
