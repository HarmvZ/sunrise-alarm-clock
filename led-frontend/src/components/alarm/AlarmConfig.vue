<template>
  <card title="Alarm settings">
    <q-expansion-item
      dark
      expand-separator
      icon="palette"
      label="Colors"
      caption="Set transition colors"
    >
      <div class="q-my-md">
        <q-btn
          label="Starting color"
          icon="colorize"
          color="grey-9"
          class="full-width"
        >
          <q-popup-proxy class="full-width">
            <q-color
              v-model="startingColor"
              dark
              format-model="rgb"
              inline
              no-header
              default-view="palette"
              @change="triggerChange"
            />
          </q-popup-proxy>
        </q-btn>
      </div>
      <div class="q-my-md">
        <q-btn
          v-for="n in nTransitionColors"
          :key="n"
          :label="`Transition color ${n}`"
          icon="colorize"
          color="grey-9"
          class="full-width"
        >
          <q-popup-proxy class="full-width">
            <q-color
              v-model="transitionColors[n-1]"
              dark
              format-model="rgb"
              inline
              no-header
              default-view="palette"
              @change="triggerChange"
            />
          </q-popup-proxy>
        </q-btn>
        <q-btn
          v-if="isColorAddable"
          icon="add"
          label="Add transition color"
          color="grey-9"
          class="full-width"
          @click="nTransitionColors += 1"
        />
      </div>
      <div class="q-my-md">
        <q-btn
          label="Finish color"
          icon="colorize"
          color="grey-9"
          class="full-width"
        >
          <q-popup-proxy class="full-width">
            <q-color
              v-model="finishColor"
              dark
              format-model="rgb"
              no-header
              default-view="palette"
              @change="triggerChange"
            />
          </q-popup-proxy>
        </q-btn>
      </div>
      <div class="q-py-md row justify-evenly">
        <template
          v-for="(c, idx) in colors"
        >
          <div
            :key="idx"
            class="display-inline"
            :style="{
              width: '3em',
              height: '3em',
              backgroundColor: c,
            }"
          />
          <q-icon
            v-if="idx + 1 < colors.length"
            :key="`${idx}-arrow`"
            name="forward"
            style="font-size: 3em"
            color="grey-9"
          />
        </template>
      </div>
    </q-expansion-item>
    <q-expansion-item
      expand-separator
      dark
      icon="equalizer"
      label="Music"
      caption="Set music or sounds to play"
    >
      <div>
        TODO
      </div>
    </q-expansion-item>
    <q-expansion-item
      expand-separator
      dark
      icon="volume_up"
      label="Volume"
      caption="Set volume progress"
    >
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
    </q-expansion-item>
  </card>
</template>

<style>
</style>

<script>
import getRGBColorObject from 'src/utils/getRGBColorObject';
import VolumeSlider from 'src/components/VolumeSlider';

export default {
  name: 'AlarmConfig',
  components: { VolumeSlider },
  props: {
  },
  data () {
    return {
      nTransitionColors: 0,
      startingColor: 'rgb(0, 0, 0)',
      finishColor: 'rgb(255, 255, 255)',
      transitionColors: [],
      startingVolume: [0, 0],
      finishVolume: [100, 100],
      nTransitionVolumes: 0,
      transitionVolumes: [],
    };
  },
  computed: {
    colors () {
      return [
        this.startingColor,
        ...this.transitionColors,
        this.finishColor,
      ];
    },
    colorsObj () {
      return this.colors.map(c => getRGBColorObject(c));
    },
    isColorAddable () {
      return (
        this.transitionColors.filter(v => typeof (v) === 'undefined').length === 0 &&
        this.nTransitionColors === this.transitionColors.length
      );
    },
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
    triggerChange () {
      // TODO
    },
  },
};
</script>
<style>
.q-parallax.opacity-parallax .q-parallax__media {
  background:#000;
}
.q-parallax.opacity-parallax .q-parallax__media img {
  opacity: .2;
}
</style>
