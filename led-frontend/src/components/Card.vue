<template functional>
  <q-card
    class="col-12 bg-secondary text-center q-mb-md"
    dark
  >
    <q-card-section
      v-if="props.title !== ''"
      class="bg-dark text-white"
    >
      <div class="text-h5">
        {{ props.title }}
      </div>
    </q-card-section>
    <slot />
  </q-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '',
    },
  },
};
</script>
