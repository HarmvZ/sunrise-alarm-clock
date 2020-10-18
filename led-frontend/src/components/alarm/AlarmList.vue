<template>
  <div>
    <alarm-detail
      v-for="alarm in alarms"
      :key="alarm.pk"
      v-bind="alarm"
      :day-of-week="alarm.day_of_week"
      :update-alarm="updateAlarm"
      :remove-alarm="removeAlarm"
    />
    <q-expansion-item
      v-for="alarmSetting in alarmSettings"
      :key="alarmSetting.pk"
      expand-separator
      dark
      icon="alarm"
      :label="`Alarm ${alarmSetting.pk} settings`"
      :caption="`Start with /api/start_alarm/${alarmSetting.pk}/`"
    >
      <alarm-config
        v-bind="alarmSetting"
        :update="updateAlarmSetting"
        :remove="removeAlarmSetting"
      />
    </q-expansion-item>
    <q-page-sticky
      position="bottom-right"
      :offset="[18, 18]"
    >
      <q-btn
        fab
        color="primary"
        icon="alarm_off"
        @click="addAlarm()"
      />
    </q-page-sticky>
    <q-page-sticky
      position="bottom-right"
      :offset="[90, 18]"
    >
      <q-btn
        fab
        color="primary"
        icon="alarm"
        @click="addAlarmSetting()"
      />
    </q-page-sticky>
  </div>
</template>

<script>
import AlarmConfig from 'components/alarm/AlarmConfig';
import AlarmDetail from 'components/alarm/AlarmDetail';

export default {
  name: 'AlarmList',
  components: { AlarmDetail, AlarmConfig },
  data () {
    return {
      alarms: [],
      alarmSettings: [],
    };
  },
  mounted () {
    this.syncAlarms();
    this.syncAlarmSettings();
  },
  methods: {
    // Core API methods
    async syncModels (modelName) {
      const url = `/api/${modelName}/`;
      return this.request({
        method: 'GET',
        url,
        responseType: 'json',
      });
    },
    async removeModel (modelName, pk) {
      const url = `/api/${modelName}/${pk}/`;
      await this.request({
        method: 'DELETE',
        url,
        responseType: 'json',
      });
    },
    async updateModel (modelName, pk, changes) {
      const url = `/api/${modelName}/${pk}/`;
      const data = changes;
      await this.request({
        method: 'PATCH',
        url,
        data,
        responseType: 'json',
      });
    },
    async addModel (modelName, data) {
      const url = `/api/${modelName}/`;
      await this.request({
        method: 'POST',
        url,
        data,
        responseType: 'json',
      });
    },
    // Alarm API methods
    async syncAlarms () {
      this.alarms = await this.syncModels('alarms');
    },
    async addAlarm () {
      const data = {
        enabled: false,
        minute: '00',
        hour: '08',
        day_of_week: '0,1,2,3,4,5,6',
      };
      await this.addModel('alarms', data);
      this.syncAlarms();
    },
    async removeAlarm (pk) {
      await this.removeModel('alarms', pk);
      this.alarms = this.alarms.filter(alarm => alarm.pk !== pk);
      this.syncAlarms();
    },
    async updateAlarm (pk, changes) {
      await this.updateModel('alarms', pk, changes);
      this.syncAlarms();
    },

    // AlarmSettings API methods
    async syncAlarmSettings () {
      this.alarmSettings = await this.syncModels('alarm-settings');
    },
    async addAlarmSetting () {
      const data = {
        colors: [[0, 0, 0], [255, 255, 255]],
        playlist: '',
        volumes: [[0, 0], [100, 100]],
        duration: 1800,
      };
      await this.addModel('alarm-settings', data);
      this.syncAlarmSettings();
    },
    async removeAlarmSetting (pk) {
      await this.removeModel('alarm-settings', pk);
      this.alarmSettings = this.alarmSettings.filter(alarmSetting => alarmSetting.pk !== pk);
      this.syncAlarmSettings();
    },
    async updateAlarmSetting (pk, changes) {
      await this.updateModel('alarm-settings', pk, changes);
      this.syncAlarms();
    },

    refresh (done) {
      this.syncAlarms().then(() => this.syncAlarmSettings().then(() => this.done()));
    },
  },
};
</script>
