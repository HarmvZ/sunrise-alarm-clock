<template>
  <q-page class="q-px-md">
    <alarm-config />
    <alarm-list dark />
  </q-page>
</template>

<style>
</style>

<script>
import AlarmList from 'components/alarm/AlarmList';
import AlarmConfig from 'components/alarm/AlarmConfig';

export default {
  name: 'PageIndex',
  components: { AlarmConfig, AlarmList },
};
</script>
