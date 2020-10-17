<template>
  <div>
    <div class="q-py-md">
      <q-btn
        label="Starting volume"
        icon="colorize"
        color="grey-9"
        class="full-width"
      >
        <volume-slider
          :volume="startingVolume[1]"
          :time-changeable="false"
          :time="startingVolume[0]"
          @change-volume="$set(startingVolume, 1, $event)"
        />
      </q-btn>
    </div>
    <div class="q-my-md">
      <q-btn
        v-for="n in nTransitionVolumes"
        :key="n"
        :label="`Transition volume ${n}`"
        icon="colorize"
        color="grey-9"
        class="full-width"
      >
        <volume-slider
          :volume="transitionVolumes[n-1][1]"
          :time-changeable="true"
          :time="transitionVolumes[n-1][0]"
          @change-volume="$set(transitionVolumes, n-1, [transitionVolumes[n-1][0], $event])"
          @change-time="$set(transitionVolumes, n-1, [$event, transitionVolumes[n-1][1]])"
        />
      </q-btn>
      <q-btn
        v-if="isVolumeAddable"
        icon="add"
        label="Add volume progress step"
        color="grey-9"
        class="full-width"
        @click="addVolumeTransition()"
      />
    </div>
    <div class="q-my-md">
      <q-btn
        label="Finish volume"
        icon="colorize"
        color="grey-9"
        class="full-width"
      >
        <volume-slider
          :volume="finishVolume[1]"
          :time-changeable="false"
          :time="finishVolume[0]"
          @change-volume="$set(finishVolume, 1, $event)"
        />
      </q-btn>
    </div>
    <div class="q-py-md row justify-evenly">
      <template
        v-for="(v, idx) in volumes"
      >
        <div
          :key="idx"
          class="display-inline q-pa-sm bg-grey-9 row justify-center"
          style="width: 5em"
        >
          <div class="row items-center">
            {{ v[0] }}
            <q-icon
              name="access_time"
              class="q-ml-sm text-grey-5"
            />
          </div>
          <div class="row items-center">
            {{ v[1] }}
            <q-icon
              name="volume_up"
              class="q-ml-sm text-grey-5"
            />
          </div>
        </div>
        <q-icon
          v-if="idx + 1 < volumes.length"
          :key="`${idx}-arrow`"
          name="forward"
          style="font-size: 3em"
          color="grey-9"
        />
      </template>
    </div>
  </div>
</template>
<script>
import VolumeSlider from 'src/components/VolumeSlider';

export default {
  components: { VolumeSlider },
  data () {
    return {
      startingVolume: [0, 0],
      finishVolume: [100, 100],
      nTransitionVolumes: 0,
      transitionVolumes: [],
    };
  },
  computed: {
    volumes () {
      return [
        this.startingVolume,
        ...this.transitionVolumes,
        this.finishVolume,
      ];
    },
    isVolumeAddable () {
      return (
        this.transitionVolumes.filter(v => v.length === 0).length === 0 &&
        this.nTransitionVolumes === this.transitionVolumes.length
      );
    },
  },
  methods: {
    addVolumeTransition () {
      this.nTransitionVolumes += 1;
      this.transitionVolumes.push([50, 50]);
    },
  },
};
</script>
