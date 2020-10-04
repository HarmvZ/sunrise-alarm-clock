<template>
  <q-page class="flex flex-center row">
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
import ShowClock from 'components/ShowClock';
import ShowAnimation from 'components/ShowAnimation';

export default {
  name: 'Animation',
  components: { ShowClock, ShowAnimation },
};
</script>
