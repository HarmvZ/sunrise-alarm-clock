<template>
  <div>
    <q-input
      v-model="musicSearch"
      label="Search"
      debounce="500"
      dark
    >
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
    <SearchResultList
      :search-results="searchResults"
      :image-uris="imageUris"
      class="text-left"
      @track-clicked="$emit('track-clicked', $event)"
    />
  </div>
</template>

<script>
import SearchResultList from 'components/music/SearchResultList';

export default {
  components: { SearchResultList },
  data () {
    return {
      musicSearch: '',
      searchResults: {},
      imageUris: {},
    };
  },
  watch: {
    musicSearch: function (val) {
      if (val !== '') {
        window.mopidy.library.search({ query: { artist: [val] } }).then(r => {
          this.searchResults = r[0];
          const uris = [];
          for (const tType of ['albums', 'artists', 'tracks']) {
            if (tType in this.searchResults) {
              uris.push(...this.searchResults[tType].map(a => a.uri));
            }
          }
          window.mopidy.library.getImages([uris]).then(r => {
            for (const [uri, image] of Object.entries(r)) {
              this.$set(this.imageUris, uri, image);
            }
          });
        });
      }
    },
  },
};
</script>
