<template>
  <q-page padding>
    <alarm-list dark />
  </q-page>
</template>

<style>
</style>

<script>
import AlarmList from 'components/alarm/AlarmList';

export default {
  name: 'PageIndex',
  components: { AlarmList },
};
</script>
