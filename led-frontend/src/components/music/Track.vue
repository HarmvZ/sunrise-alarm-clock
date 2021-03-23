<template>
  <q-item
    :v-ripple="clickable"
    :clickable="clickable"
    dark
    @click="clickable ? $emit('click') : null"
  >
    <q-item-section
      avatar
    >
      <q-avatar rounded>
        <img :src="imageUri">
      </q-avatar>
    </q-item-section>

    <q-item-section
      no-wrap
      class="ellipsis"
    >
      <q-item-label>{{ item.name }}</q-item-label>
      <q-item-label
        v-if="'artists' in item"
        caption
      >
        {{ artists }}
      </q-item-label>
      <q-item-label
        v-if="false && 'album' in item"
        overline
      >
        {{ item.album.name }}
      </q-item-label>
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
    clickable: {
      type: Boolean,
      default: true,
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
