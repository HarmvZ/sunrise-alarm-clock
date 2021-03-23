<template>
  <ConnectionStatus
    :status="wledStatus"
    :icons="icons"
    @click="onClick()"
  />
</template>

<style>
</style>

<script>
import { mapState } from 'vuex';
import ConnectionStatus from 'components/ConnectionStatus';

export default {
  name: 'WledConnectionStatus',
  components: { ConnectionStatus },
  data () {
    return {
      icons: {
        0: 'loop',
        1: 'wb_sunny',
        2: 'api',
      },
    };
  },
  computed: {
    ...mapState({
      wledStatus: 'wledStatus',
      wledState: 'wledState',
    }),
  },
  methods: {
    onClick () {
      if (this.wledStatus === 1) {
        if (this.wledState.on) {
          this.$wledSocket.send(JSON.stringify({ 'on': false }));
        } else {
          this.$wledSocket.send(JSON.stringify({ 'on': true }));
        }
      }
    },
  },
};
</script>
