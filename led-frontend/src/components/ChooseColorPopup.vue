<template>
  <q-btn
    :label="label"
    :icon="icon"
    color="grey-9"
    class="full-width"
  >
    <q-popup-proxy
      dark
      class="full-width row justify-center"
    >
      <q-color
        v-model="startingColor"
        dark
        format-model="rgb"
        inline
        no-header
        default-view="palette"
        @change="$emit('input', startingColor)"
      />
    </q-popup-proxy>
  </q-btn>
</template>
<script>
export default {
  props: {
    value: { type: String, required: true },
    label: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      startingColor: this.value,
    };
  },
};
</script>
