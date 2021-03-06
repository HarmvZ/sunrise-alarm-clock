<template>
  <q-page class="items-center q-px-md">
    <card title="WLED control">
      <wled-control class="q-pa-sm" />
    </card>
  </q-page>
</template>

<style>
</style>

<script>
import WledControl from 'components/WledControl';

export default {
  name: 'PageIndex',
  components: { WledControl },
};
</script>
