<template>
  <q-popup-proxy
    ref="popup"
    class="full-width"
  >
    <q-list class="full-width bg-grey-9 text-white">
      <q-item
        v-if="timeChangeable"
        class="row justify-center"
      >
        <q-input
          dark
          :value="time"
          type="number"
          filled
          style="max-width: 200px"
          @input="changeTime"
        >
          <template v-slot:append>
            <q-icon name="access_time" />
          </template>
        </q-input>
      </q-item>
      <q-item>
        <q-item-section side>
          <q-icon name="volume_down" />
        </q-item-section>
        <q-item-section>
          <q-slider
            dark
            :value="volume"
            :min="0"
            :max="100"
            :step="1"
            label
            @change="changeVolume"
          />
        </q-item-section>
        <q-item-section side>
          <q-icon name="volume_up" />
        </q-item-section>
      </q-item>
    </q-list>
  </q-popup-proxy>
</template>

<script>
export default {
  props: {
    volume: {
      type: Number,
      required: true,
    },
    time: {
      type: Number,
      required: true,
    },
    timeChangeable: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    changeVolume (volume) {
      this.$emit('change-volume', volume);
    },
    changeTime (time) {
      this.$emit('change-time', Number.parseInt(time));
    },
  },
};
</script>
