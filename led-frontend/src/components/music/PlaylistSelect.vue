<template>
  <div>
    <q-item-section>
      <q-parallax
        :src="playlist.imageUri === '' ? 'statics/audio.jpg' : playlist.imageUri"
        :height="150"
      />
    </q-item-section>
    <q-item-section class="text-h6 text-white">
      {{ playlist.name }}
    </q-item-section>
    <q-card-actions>
      <q-btn
        v-if="playlistUri !== ''"
        label="Edit playlist"
        icon="open_in_new"
        class="full-width q-mb-sm"
        dark
        color="grey-9"
        @click="openURL(editPlaylistUrl)"
      />

      <q-btn
        label="Change playlist"
        icon="queue_music"
        dark
        color="primary"
        class="full-width q-mb-sm"
      >
        <q-popup-proxy
          ref="playlistpopup"
          dark
          class="full-width row justify-center bg-black"
        >
          <Playlists @playlist-click="onPlaylistClick" />
        </q-popup-proxy>
      </q-btn>

      <q-btn
        v-if="playlistUri !== ''"
        label="Clear"
        icon="delete"
        dark
        color="negative"
        class="full-width"
        @click="onRemovePlaylist"
      />
    </q-card-actions>
  </div>
</template>
<script>
import { openURL } from 'quasar';
import Playlists from 'src/components/music/Playlists';
export default {
  components: { Playlists },
  props: {
    playlistUri: {
      type: String,
      required: true,
    },
  },
  data () {
    return {
      hostname: process.env.HOSTNAME,
      playlist: {},
    };
  },
  computed: {
    editPlaylistUrl () {
      if (this.playlistUri !== '') {
        return `http://${this.hostname}:6680/iris/playlist/${encodeURI(this.playlistUri)}`;
      }
      return '';
    },
  },
  watch: {
    playlistUri: {
      immediate: true,
      handler: function (val) {
        if (val !== '') {
          this.$mopidy.playlists.lookup([val]).then(pl => {
            this.$mopidy.library.getImages([[val]]).then(r => {
              if (val in r && r[val].length > 0) {
                pl['imageUri'] = r[val][0].uri;
              }
              this.playlist = pl;
            });
          });
        } else {
          this.playlist = {
            name: 'None',
            imageUri: '',
          };
        }
      },
    },
  },
  methods: {
    onPlaylistClick (playlist) {
      this.$refs.playlistpopup.hide();
      this.$emit('update', { playlist: playlist.uri });
    },
    onRemovePlaylist () {
      this.$emit('update', { playlist: '' });
    },
    openURL,
  },

};
</script>
