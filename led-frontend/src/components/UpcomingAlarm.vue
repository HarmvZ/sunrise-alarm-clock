<template>
  <card title="Upcoming alarm">
    <AlarmDetail
      v-if="alarm !== false"
      v-bind="alarm"
      :editable="false"
      style="margin-top: 0;"
    />
    <div
      v-else
      class="justify-center q-pa-md"
    >
      No upcoming alarms found!
    </div>
  </card>
</template>

<style>
</style>

<script>
import AlarmDetail from 'components/alarm/AlarmDetail';

export default {
  name: 'UpcommingAlarm',
  components: { AlarmDetail },
  data () {
    return {
      alarm: false,
    };
  },
  mounted () {
    this.getUpcomingAlarm().then(data => {
      if (Object.keys(data).length !== 0) {
        this.alarm = data;
      }
    });
  },
  methods: {
    async getUpcomingAlarm () {
      const url = '/api/alarms/first_upcoming_alarm';
      const response = await this.request({
        method: 'GET',
        url,
        responseType: 'json',
      });
      return response;
    },
  },
};
</script>
