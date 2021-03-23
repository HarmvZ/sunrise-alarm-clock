<template>
  <q-avatar
    ref="avatar"
    :icon="icons[status]"
    :color="colors[status]"
    text-color="white"
    size="24px"
    :class="status === 0 ? 'spin' : ''"
    rounded
  />
</template>

<style>
</style>

<script>

export default {
  name: 'ConnectionStatus',
  props: {
    status: {
      type: Number,
      required: true,
    },
    icons: {
      type: Object,
      default: () => ({
        0: 'import_export',
        1: 'wb_sunny',
        2: 'error',
      }),
    },
  },
  data () {
    return {
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
