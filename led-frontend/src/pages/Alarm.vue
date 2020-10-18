<template>
  <q-page class="q-px-md">
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
