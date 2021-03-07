<template>
  <q-page class="items-center q-px-md">
    <card

      title="WLED control"
    >
      <wled-control
        v-if="wledStatus === 1"
        class="q-pa-sm"
      />
      <q-card-section
        v-if="wledStatus === 2"
        class=""
      >
        <div class="">
          WLED connection failure
        </div>
      </q-card-section>
      <q-inner-loading :showing="wledStatus === 0">
        <q-spinner-gears
          size="50px"
          color="primary"
        />
      </q-inner-loading>
    </card>
  </q-page>
</template>

<style>
</style>

<script>
import WledControl from 'components/WledControl';
import { mapState } from 'vuex';

export default {
  name: 'PageIndex',
  components: { WledControl },
  computed: {
    ...mapState({
      wledStatus: 'wledStatus',
    }),
  },
};
</script>
