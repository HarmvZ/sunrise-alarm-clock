<template>
  <div>
    <q-card-section class="row">
      <SetColorBtn
        v-for="(color, id) of colors"
        :key="id"
        :red="color.r"
        :green="color.g"
        :blue="color.b"
        :transition="transition"
        :timestep="timestep"
        :steps="steps"
        class="col-4"
        style="height: 3em;"
      />
    </q-card-section>
  </div>
</template>

<style>
</style>

<script>
import SetColorBtn from 'components/SetColorBtn';

export default {
  name: 'Color',
  components: { SetColorBtn },
  props: {
    transition: Boolean,
    steps: {
      type: Number,
      required: true,
    },
    timestep: {
      type: Number,
      required: true,
    },
  },
  computed: {
    colors () {
      const colors = [];
      const c = [0, 125, 255];
      for (const r of c) {
        for (const g of c) {
          for (const b of c) {
            colors.push({ r, g, b });
          }
        }
      }
      return colors;
    },
  },
};
</script>
