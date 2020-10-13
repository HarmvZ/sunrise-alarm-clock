<template functional>
  <q-card
    class="col-12 bg-grey-10 text-center q-mt-md"
    dark
  >
    <q-card-section
      v-if="props.title !== ''"
      class="bg-grey-9 text-grey-4"
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
