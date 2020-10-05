<template>
  <q-page class="items-center q-px-md">
    <router-link to="/alarms">
      <UpcomingAlarm />
    </router-link>
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">Color</div>
      </q-card-section>
      <div class="row items-center">
        <ChangeColor
          :transition="true"
          :timestep="20"
          :steps="100"
          class="col-12"
        />
      </div>
    </q-card>
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white text-h6">
        <div class="text-h6">
          Animations
        </div>
      </q-card-section>
      <show-animation />
    </q-card>
    <q-card class="col-12 bg-grey-9 text-center q-mt-md">
      <q-card-section class="bg-primary text-white text-h6">
        <div class="text-h6">
          Clock
        </div>
      </q-card-section>
      <show-clock />
    </q-card>
  </q-page>
</template>

<style>
</style>

<script>
// import DarkCard from 'components/DarkCard';
import UpcomingAlarm from 'components/UpcomingAlarm';
import ChangeColor from 'components/ChangeColor';
import ShowClock from 'components/ShowClock';
import ShowAnimation from 'components/ShowAnimation';

export default {
  name: 'PageIndex',
  components: { UpcomingAlarm, ChangeColor, ShowClock, ShowAnimation }, //, DarkCard },
  data () {
    return {
      alarm: false,
    };
  },
};
</script>
