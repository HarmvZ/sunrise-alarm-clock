<template>
  <div>
    <q-color
      dark
      format-model="rgb"
      inline
      no-header
      default-view="palette"
      style="max-width:20em"
      class="q-mx-auto q-my-sm"
      @change="changeColor"
    />
  </div>
</template>

<style>
</style>

<script>
import getRGBColorObject from 'src/utils/getRGBColorObject';

export default {
  name: 'ChangeColor',
  props: {
    transition: {
      type: Boolean,
      required: true,
    },
    steps: {
      type: Number,
      required: true,
    },
    timestep: {
      type: Number,
      required: true,
    },
  },
  methods: {
    changeColor (value) {
      const data = getRGBColorObject(value);
      let url = '/api/set_color/';
      if (this.transition) {
        url = '/api/transition_color/';
      }
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
