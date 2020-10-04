<template>
  <div class="column">
    <div class="q-mt-md">Speed</div>
    <q-slider
      v-model="waitMs"
      :min="1"
      :max="500"
      :step="1"
      label
      class=""
    />
    <q-btn
      v-for="option in options"
      :key="option.value"
      :label="option.label"
      @click="showAnimation(option.value)"
      color="primary"
      size="md"
      class="col-12 q-mb-md q-mx-md"
    />
  </div>
</template>

<style>
</style>

<script>

export default {
  name: 'ShowAnimation',
  data () {
    return {
      waitMs: 20,
      animation: 'theaterChaseRainbow',
      options: [
        {
          label: 'Rainbow',
          value: 'rainbow',
        },
        {
          label: 'Rainbow Cycle',
          value: 'rainbowCycle',
        },
        {
          label: 'Theater Chase Rainbow',
          value: 'theaterChaseRainbow',
        },
      ],
    };
  },
  methods: {
    showAnimation (animation) {
      const data = {
        'animation': animation,
        'wait_ms': this.waitMs,
      };
      let url = '/api/show_animation/';
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
