export default {
  methods: {
    async request (options) {
      this.$q.loadingBar.start();
      try {
        const response = await this.$axios({
          baseURL: process.env.API_BASE_URL,
          ...options,
        });
        this.$q.loadingBar.stop();
        return response.data;
      } catch (error) {
        this.$q.notify({
          message: error.toString(),
          position: 'top',
          color: 'negative',
          icon: 'report_problem',
          actions: [{
            label: 'Retry',
            handler: () => this.request(options),
          }],
        });
      }
    },
  },
};
