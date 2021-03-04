<template>
  <div>
    <AlarmConfigDetail
      v-for="alarmSetting in alarmSettings"
      :key="alarmSetting.pk"
      :alarm-setting="alarmSetting"
      :update="updateAlarmSetting"
      :remove="removeAlarmSetting"
    />
    <q-page-sticky
      position="bottom-right"
      :offset="[18, 18]"
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
import AlarmConfigDetail from 'components/alarm/AlarmConfigDetail';

export default {
  name: 'AlarmList',
  components: { AlarmConfigDetail },
  data () {
    return {
      alarms: [],
      alarmSettings: [],
    };
  },
  mounted () {
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
      this.syncAlarmSettings();
    },

    refresh (done) {
      this.syncAlarmSettings().then(() => this.done());
    },

    // Other methods
    getRandomAlarmImg () {
      const randomInt = Math.floor(Math.random() * 6) + 1;
      return `statics/alarm/${randomInt}.jpg`;
    },
  },
};
</script>
