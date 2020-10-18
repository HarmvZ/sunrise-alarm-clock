<template>
  <card>
    <q-parallax
      :src="playlistImageUri"
      :height="150"
      class="opacity-parallax"
    >
      <div class="text-h5 text-white">
        {{ `Alarm ${alarmSetting.pk}` }}
      </div>
      <div class="text-white">
        {{ `Endpoint: /api/start_alarm/${alarmSetting.pk}/` }}
      </div>
    </q-parallax>
    <q-card-section>
      <div class="row">
        <div
          v-for="(c, index) in alarmSetting.colors"
          :key="`${arrayToRgb(c)}_${index}`"
          :style="{height: '3em', backgroundColor: arrayToRgb(c)}"
          class="col"
        />
      </div>
      This alarm will run for <span class="text-weight-bold">{{ durationMinutes }} minutes</span>, progressing through the colors above.
      <template v-if="playlistUri !== ''">
        It will play the playlist <span class="text-weight-bold">{{ playlistObj.name }}</span> with the volume progressing from {{ alarmSetting.volumes[0][1] }}% to {{ alarmSetting.volumes[alarmSetting.volumes.length - 1][1] }}%.
      </template>
    </q-card-section>
    <q-card-section>
      <q-expansion-item
        expand-separator
        dark
        icon="settings"
        label="Settings"
        header-class="bg-grey-9"
      >
        <alarm-config
          v-bind="alarmSetting"
          :update="update"
          :remove="remove"
        />
      </q-expansion-item>
      <q-card-actions align="right">
        <q-btn
          dark
          label="Start alarm"
          color="primary"
          class="full-width q-mb-sm"
        />
        <q-btn
          dark
          label="Remove"
          color="negative"
          class="full-width"
          @click="confirmDelete = true"
        />
      </q-card-actions>
      <q-dialog
        v-model="confirmDelete"
        dark
      >
        <q-card class="bg-grey-9 text-white">
          <q-card-section class="row items-center">
            <q-avatar
              icon="warning"
              color="negative"
              text-color="white"
            />
            <span class="q-ml-sm">Are you sure you want to remove this alarm?</span>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn
              v-close-popup
              flat
              label="Cancel"
              color="white"
            />
            <q-btn
              v-close-popup
              flat
              label="Ok"
              color="negative"
              @click="remove(alarmSetting.pk)"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-card-section>
  </card>
</template>

<style>
</style>

<script>
import AlarmConfig from 'components/alarm/AlarmConfig';
import { arrayToRgb } from 'src/utils/colors';

export default {
  name: 'AlarmConfigDetail',
  components: { AlarmConfig },
  props: {
    alarmSetting: {
      type: Object,
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
      confirmDelete: false,
      playlistObj: {},
      mopidy: window.mopidy,
    };
  },
  computed: {
    playlistUri () {
      return this.alarmSetting.playlist;
    },
    img () {
      const randomInt = Math.floor(Math.random() * 6) + 1;
      return `statics/alarm/${randomInt}.jpg`;
    },
    playlistImageUri () {
      if ('imageUri' in this.playlistObj && this.playlistObj.imageUri !== '') {
        return this.playlistObj.imageUri;
      } else {
        return this.img;
      }
    },
    durationMinutes () {
      return Number.parseInt(this.alarmSetting.duration / 60);
    },
  },
  watch: {
    playlistUri: {
      immediate: true,
      handler: function (val) {
        if (val !== '') {
          this.mopidy.playlists.lookup([val]).then(pl => {
            this.mopidy.library.getImages([[val]]).then(r => {
              if (val in r && r[val].length > 0) {
                pl['imageUri'] = r[val][0].uri;
              }
              this.playlistObj = pl;
            });
          });
        } else {
          this.playlistObj = {
            name: 'None',
            imageUri: '',
          };
        }
      },
    },
  },
  methods: {
    arrayToRgb,
    timeChanged (value) {
      this.timeDialog = false;
      const [hour, minute] = value.split(':');
      this.updateAlarm(this.pk, { hour, minute });
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