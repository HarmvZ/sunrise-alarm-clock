<template>
  <q-page class="row flex flex-center q-px-md">
    <card title="Preset colors">
      <set-color
        :transition="transition"
        :timestep="timestep"
        :steps="steps"
      />
    </card>
    <card title="Custom color">
      <div class="row items-center">
        <ChangeColor
          :transition="transition"
          :timestep="timestep"
          :steps="steps"
          class="col-12"
        />
      </div>
    </card>
    <card title="Advanced options">
      <q-card-section>
        <q-toggle
          v-model="transition"
          label="Transition"
          dark
        />
        <div class="column">
          <div class="column items-center">
            <div class="">
              Steps:
            </div>
            <q-slider
              v-model="steps"
              :min="1"
              :max="500"
              :step="1"
              label
              class=""
            />
          </div>
          <div class="column items-center">
            <div class="">
              Time per step(ms):
            </div>
            <q-slider
              v-model="timestep"
              :min="1"
              :max="500"
              :step="1"
              label
              class=""
            />
          </div>
          <div class="text-center">
            Total duration: {{ steps * timestep / 1000 }} seconds
          </div>
        </div>
      </q-card-section>
    </card>
  </q-page>
</template>

<style>
</style>

<script>
import ChangeColor from 'components/ChangeColor';
import SetColor from 'components/SetColor';
// import DarkCard from 'components/DarkCard';

export default {
  name: 'Color',
  components: { ChangeColor, SetColor }, //, DarkCard },
  data () {
    return {
      transition: true,
      steps: 100,
      timestep: 20,
    };
  },
};
</script>
