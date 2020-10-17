<template>
  <q-item
    v-ripple
    clickable
    dark
    @click="$emit('click')"
  >
    <q-item-section
      avatar
    >
      <q-avatar>
        <img :src="imageUri">
      </q-avatar>
    </q-item-section>

    <q-item-section no-wrap>
      <q-item-label>{{ item.name }}</q-item-label>
      <q-item-label
        v-if="'artists' in item"
        caption
      >
        {{ artists }}
      </q-item-label>
      <q-item-label
        v-if="'album' in item"
        overline
      >
        {{ item.album.name }}
      </q-item-label>
    </q-item-section>
    <q-item-section>
      <slot />
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
    imageUri: {
      type: String,
      required: true,
    },
  },
  computed: {
    artists () {
      if ('artists' in this.item) {
        return this.item.artists.map(a => a.name).join(', ');
      }
      return '';
    },
  },
};
</script>
