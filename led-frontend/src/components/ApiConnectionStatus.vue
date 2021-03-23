<template>
  <ConnectionStatus
    :status="status"
    :icons="icons"
  />
</template>

<style>
</style>

<script>
import ConnectionStatus from 'components/ConnectionStatus';

export default {
  name: 'ApiConnectionStatus',
  components: { ConnectionStatus },
  data () {
    return {
      status: 0, // 0: checking, 1: connected, 2: error
      icons: {
        0: 'import_export',
        1: 'api',
        2: 'api',
      },
      timer: null,
    };
  },
  async mounted () {
    this.status = await this.checkStatus();
    this.timer = setInterval(async () => {
      this.status = await this.checkStatus();
    }, 15000);
  },
  beforeDestroy () {
    clearInterval(this.timer);
  },
  methods: {
    async checkStatus () {
      const url = '/api/status/';
      try {
        await this.$axios({
          method: 'GET',
          baseURL: process.env.API_BASE_URL,
          url,
        });
      } catch (err) {
        return 2;
      }
      return 1;
    },
  },
};
</script>
