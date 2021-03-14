<template>
  <div>
    <div
      v-for="resultType in resultTypes"
      :key="resultType"
    >
      <q-list
        v-if="resultType in searchResults && searchResults[resultType].length"
        dark
        dense
      >
        <q-item-label
          no-wrap
          class="text-weight-bold"
          header
        >
          {{ capitalize(resultType) }}
        </q-item-label>
        <Track
          v-for="item in searchResults[resultType].slice(0,5)"
          :key="item.uri"
          :item="item"
          :image-uri="getImageUri(item.uri)"
          @click="$emit('track-clicked', item.uri)"
        />
      </q-list>
    </div>
  </div>
</template>

<script>
import Track from 'components/music/Track';
import { format } from 'quasar';
const { capitalize } = format;

export default {
  components: { Track },
  props: {
    searchResults: {
      type: Object,
      required: true,
    },
    imageUris: {
      type: Object,
      required: true,
    },
  },
  data () {
    return {
      resultTypes: ['tracks', 'albums', 'artists'],
    };
  },
  methods: {
    getImageUri (uri) {
      return uri in this.imageUris && this.imageUris[uri].length > 0 ? this.imageUris[uri][0].uri : 'statics/audio.jpg'; // TODO default image
    },
    capitalize,
  },

};
</script>
