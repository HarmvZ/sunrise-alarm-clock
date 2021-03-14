<template>
  <q-list
    dark
    class="full-width"
    separator
  >
    <q-item class="column">
      <q-item-label
        class="text-subtitle1 text-center q-pb-sm"
      >
        Color progression
      </q-item-label>
      <q-item-label>
        <ColorTransitionSelect
          class="q-ma-md"
          :colors="colors"
          @update="update(pk, $event)"
        />
      </q-item-label>
    </q-item>
    <q-item class="column">
      <q-item-label
        class="text-subtitle1 text-center q-pb-sm"
      >
        Set Playlist
      </q-item-label>
      <q-item-label>
        <PlaylistSelect
          :playlist-uri="playlist"
          @update="update(pk, $event)"
        />
        <q-toggle
          label="Shuffle"
          :value="shuffle"
          @input="toggleShuffle()"
        />
      </q-item-label>
    </q-item>
    <q-item class="column">
      <q-item-label
        class="text-subtitle1 text-center q-pb-sm"
      >
        Volume progression
      </q-item-label>
      <q-item-label>
        <VolumeTransitionSelect
          class="q-ma-md"
          :volumes="volumes"
          @update="update(pk, $event)"
        />
      </q-item-label>
    </q-item>
    <q-item class="column">
      <q-item-label
        class="text-subtitle1 text-center q-pb-sm"
      >
        Duration
      </q-item-label>
      <q-item-label class="q-pt-lg">
        <q-slider
          :value="durationMinutes"
          color="primary"
          :min="0"
          :step="1"
          :max="120"
          label
          label-always
          :label-value="durationMinutes + ' minutes'"
          @change="changeDuration($event)"
        />
      </q-item-label>
    </q-item>
  </q-list>
</template>

<script>
import VolumeTransitionSelect from 'src/components/VolumeTransitionSelect';
import ColorTransitionSelect from 'src/components/ColorTransitionSelect';
import PlaylistSelect from 'src/components/music/PlaylistSelect';

export default {
  name: 'AlarmConfig',
  components: { VolumeTransitionSelect, ColorTransitionSelect, PlaylistSelect },
  props: {
    pk: {
      type: Number,
      required: true,
    },
    playlist: {
      type: String,
      required: true,
    },
    shuffle: {
      type: Boolean,
      required: true,
    },
    duration: {
      type: Number,
      required: true,
    },
    volumes: {
      type: Array,
      required: true,
    },
    colors: {
      type: Array,
      required: true,
    },
    update: {
      type: Function,
      required: true,
    },
    remove: {
      type: Function,
      required: true,
    },
  },
  data () {
    return {
      durationVal: 0,
    };
  },
  computed: {
    durationMinutes () {
      return Number.parseInt(this.duration / 60);
    },
  },
  methods: {
    changeDuration (d) {
      this.update(this.pk, { duration: d * 60 });
    },
    toggleShuffle () {
      this.update(this.pk, { shuffle: !this.shuffle });
    },
  },
};
</script>
