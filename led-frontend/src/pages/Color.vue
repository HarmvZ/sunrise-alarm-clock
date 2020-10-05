<template>
  <q-page class="row flex flex-center q-px-md">
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white text-h6">
        <div class="text-h6">
          Preset colors
        </div>
      </q-card-section>
      <set-color
        :transition="transition"
        :timestep="timestep"
        :steps="steps"
      />
    </q-card>
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">Custom color</div>
      </q-card-section>
      <div class="row items-center">
        <ChangeColor
          :transition="transition"
          :timestep="timestep"
          :steps="steps"
          class="col-12"
        />
      </div>
    </q-card>
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white text-h6">
        <div class="text-h6">
          Advanced options
        </div>
      </q-card-section>
      <q-card-section>
        <q-toggle
            v-model="transition"
            label="Transition"
            dark
        />
        <div class="column">
            <div class="column items-center">
            <div class="">Steps:</div>
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
            <div class="">Time per step(ms):</div>
            <q-slider
                v-model="timestep"
                :min="1"
                :max="500"
                :step="1"
                label
                class=""
            />
            </div>
            <div class="text-center">Total duration: {{ steps * timestep / 1000 }} seconds </div>
        </div>
      </q-card-section>
    </q-card>
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
