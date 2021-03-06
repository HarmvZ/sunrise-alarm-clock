<template>
  <q-avatar
    ref="avatar"
    :icon="icons[wledStatus]"
    :color="colors[wledStatus]"
    text-color="white"
    size="24px"
    :class="wledStatus === 0 ? 'spin' : ''"
    rounded
    @click="onClick()"
  />
</template>

<style>
</style>

<script>
import { mapState } from 'vuex';

export default {
  name: 'MopidyConnectionStatus',
  data () {
    return {
      icons: {
        0: 'loop',
        1: 'lightbulb',
        2: 'error',
      },
      colors: {
        0: 'yellow',
        1: 'green',
        2: 'red',
      },
    };
  },
  computed: {
    ...mapState({
      wledStatus: 'wledStatus',
      wledState: 'wledState',
    }),
  },
  watch: {
    wledStatus: {
      immediate: true,
      handler: function (s) {
        console.log(' status', s);
      },
    },
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
