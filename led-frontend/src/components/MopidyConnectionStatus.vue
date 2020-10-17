<template>
  <q-avatar
    ref="avatar"
    :icon="icons[mopidyStatus]"
    :color="colors[mopidyStatus]"
    text-color="white"
    size="24px"
    :class="mopidyStatus === 0 ? 'spin' : ''"
    rounded
  />
</template>

<style>
</style>

<script>

export default {
  name: 'MopidyConnectionStatus',
  data () {
    return {
      mopidyStatus: window.mopidyStatus,
      icons: {
        0: 'loop',
        1: 'audiotrack',
        2: 'error',
      },
      colors: {
        0: 'yellow',
        1: 'green',
        2: 'red',
      },
    };
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
