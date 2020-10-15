<template>
  <q-page class="flex flex-center row">
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
import ShowClock from 'components/ShowClock';
import ShowAnimation from 'components/ShowAnimation';

export default {
  name: 'Animation',
  components: { ShowClock, ShowAnimation },
};
</script>
