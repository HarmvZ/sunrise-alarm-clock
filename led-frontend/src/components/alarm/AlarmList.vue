<template>
  <div>
    <alarm-detail
      v-for="alarm in alarms"
      :key="alarm.pk"
      v-bind="alarm"
      :updateAlarm="updateAlarm"
      :removeAlarm="removeAlarm"
    />
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-btn
        fab
        @click="addAlarm()"
        color="primary"
        icon="alarm_add"
      />
    </q-page-sticky>
  </div>
</template>

<script>
import AlarmDetail from 'components/alarm/AlarmDetail';

export default {
  name: 'AlarmList',
  components: { AlarmDetail },
  data () {
    return {
      alarms: [],
    };
  },
  methods: {
    async syncAlarms () {
      const url = '/api/alarms/';
      const response = await this.request({
        method: 'GET',
        url,
        responseType: 'json',
      });
      this.alarms = response;
    },
    async removeAlarm (pk) {
      const url = `/api/alarms/${pk}/`;
      await this.request({
        method: 'DELETE',
        url,
        responseType: 'json',
      });
      this.alarms = this.alarms.filter(alarm => alarm.pk !== pk);
    },
    async updateAlarm (pk, changes) {
      const url = `/api/alarms/${pk}/`;
      const data = changes;
      await this.request({
        method: 'PATCH',
        url,
        data,
        responseType: 'json',
      });
      this.syncAlarms();
    },
    async addAlarm () {
      const url = '/api/alarms/';
      const data = {
        enabled: false,
        minute: '00',
        hour: '08',
        day_of_week: '0,1,2,3,4,5,6',
      };
      await this.request({
        method: 'POST',
        url,
        data,
        responseType: 'json',
      });
      this.syncAlarms();
    },
    refresh (done) {
      this.syncAlarms().then(() => done());
    },
  },
  mounted () {
    this.syncAlarms();
  },
};
</script>
