<template>
  <q-page class="items-center q-px-md">
    <card title="Test alarm">
      <div class="column items-center">
        <q-btn
          label="Test alarm"
          color="primary"
          size="lg"
          class="col-12 q-ma-md"
          @click="startAlarm()"
        />
      </div>
    </card>
    <router-link to="/alarms">
      <UpcomingAlarm />
    </router-link>
    <card title="Color">
      <div class="row items-center">
        <ChangeColor
          :transition="true"
          :timestep="20"
          :steps="100"
          class="col-12"
        />
      </div>
    </card>
    <card title="Animations">
      <show-animation />
    </card>
    <card title="Clock">
      <show-clock />
    </card>
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
  methods: {
    startAlarm () {
      const data = { steps: 100, timestep: 20 };
      const url = '/api/start_alarm/';
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
