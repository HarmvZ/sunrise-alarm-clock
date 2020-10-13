<template>
  <q-btn
    dense
    :style="btnStyle()"
    label=" "
    @click="changeColor()"
  />
</template>

<style>
</style>

<script>
export default {
  name: 'SetColorBtn',
  props: {
    red: {
      type: Number,
      required: true,
    },
    green: {
      type: Number,
      required: true,
    },
    blue: {
      type: Number,
      required: true,
    },
    transition: {
      type: Boolean,
      default: false,
    },
    steps: {
      type: Number,
      default: 100,
    },
    timestep: {
      type: Number,
      default: 20,
    },
  },
  methods: {
    changeColor () {
      const data = { r: this.red, g: this.green, b: this.blue };
      const url = !this.transition ? '/api/set_color/' : '/api/transition_color/';
      if (this.transition) {
        data['steps'] = this.steps;
        data['timestep'] = this.timestep;
      }
      this.request({
        method: 'POST',
        url,
        data,
        responseType: 'json',
      });
    },
    btnStyle () {
      return `background-color: rgb(${this.red},${this.green},${this.blue});`;
    },
  },
};
</script>
