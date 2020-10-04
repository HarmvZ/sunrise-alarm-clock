<template>
  <q-avatar
    :icon="icons[status]"
    :color="colors[status]"
    text-color="white"
    size="24px"
    ref="avatar"
  />
</template>

<style>
</style>

<script>

export default {
  name: 'ConnectionStatus',
  data () {
    return {
      status: 0, // 0: checking, 1: connected, 2: error
      icons: {
        0: 'import_export',
        1: 'import_export',
        2: 'error',
      },
      colors: {
        0: 'yellow',
        1: 'green',
        2: 'red',
      },
      text: {
        0: 'Checking...',
        1: 'Connected',
        2: 'Failed',
      },
      timer: null,
    };
  },
  methods: {
    async checkStatus () {
      this.$refs.avatar.$el.classList.add('spin');
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
      await new Promise(resolve => setTimeout(resolve, 2000));
      this.$refs.avatar.$el.classList.remove('spin');
      return 1;
    },
  },
  async mounted () {
    this.status = await this.checkStatus();
    this.timer = setInterval(async () => {
      this.status = await this.checkStatus();
    }, 5000);
  },
  beforeDestroy () {
    clearInterval(this.timer);
  },
};
</script>

<style scoped>
.spin{
  animation-name: spin;
  animation-duration: 500ms;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}

@keyframes spin {
    from {
        transform:rotate(0deg);
    }
    to {
        transform:rotate(360deg);
    }
}
</style>
