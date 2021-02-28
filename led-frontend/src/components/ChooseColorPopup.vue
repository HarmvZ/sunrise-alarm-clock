<template>
  <q-btn-group class="full-width row">
    <q-btn
      icon="edit"
      :style="{
        backgroundColor: value
      }"
      rounded
      class="col"
    >
      <q-popup-proxy
        dark
        class="full-width row justify-center"
      >
        <q-color
          :value="value"
          dark
          format-model="rgb"
          inline
          no-header
          default-view="palette"
          @change="$emit('input', $event)"
        />
      </q-popup-proxy>
    </q-btn>
    <q-btn
      v-if="removable === true"
      icon="delete"
      color="negative"
      @click="$emit('remove')"
    />
  </q-btn-group>
</template>
<script>
export default {
  props: {
    value: { type: String, required: true },
    label: {
      type: String,
      default: '',
    },
    icon: {
      type: String,
      default: '',
    },
    removable: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
