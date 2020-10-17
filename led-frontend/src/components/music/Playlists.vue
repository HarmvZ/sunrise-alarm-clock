<template>
  <q-list
    bordered
    dark
    separator
    class="text-left full-width bg-grey-10"
  >
    <q-item-label
      header
      class="text-weight-bold"
    >
      Playlists
    </q-item-label>
    <q-separator dark />
    <q-item
      v-for="item in playlists"
      :key="item.uri"
      v-ripple
      dark
      clickable
      @click="onPlaylistClick(item)"
    >
      <q-item-section
        top
        avatar
      >
        <q-avatar rounded>
          <img :src="getImageUri(item.uri)">
        </q-avatar>
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ item.name }}</q-item-label>
      </q-item-section>
    </q-item>
  </q-list>
</template>

<script>

export default {
  data () {
    return {
      mopidy: window.mopidy,
      mopidyStatus: window.mopidyStatus,
      playlists: [],
      imageUris: {},
    };
  },
  watch: {
    playlists: function (val) {
      const uris = val.map(pl => pl.uri);
      window.mopidy.library.getImages([uris]).then(r => { this.imageUris = r; });
    },
  },
  mounted () {
    if (this.mopidyStatus !== 1) {
      return;
    }
    this.mopidy.playlists.asList().then(pl => {
      this.playlists = pl;
    });
  },
  methods: {
    getImageUri (uri) {
      return uri in this.imageUris && this.imageUris[uri].length > 0 ? this.imageUris[uri][0].uri : 'statics/audio.jpg'; // TODO default image
    },
    onPlaylistClick (playlist) {
      playlist['imageUri'] = this.getImageUri(playlist.uri);
      this.$emit('playlist-click', playlist);
    },
  },
};
</script>
