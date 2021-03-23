<template>
  <ConnectionStatus
    :status="mopidyStatus"
    :icons="icons"
  />
</template>

<style>
</style>

<script>
import { mapState } from 'vuex';
import ConnectionStatus from 'components/ConnectionStatus';

export default {
  name: 'MopidyConnectionStatus',
  components: { ConnectionStatus },
  data () {
    return {
      icons: {
        0: 'loop',
        1: 'audiotrack',
        2: 'audiotrack',
      },
    };
  },
  computed: {
    ...mapState({
      mopidyStatus: 'mopidyStatus',
    }),
  },
};
</script>
