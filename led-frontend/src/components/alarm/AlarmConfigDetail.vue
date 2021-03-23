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
        {{ apiUrl }}
      </div>
    </q-parallax>
    <div class="row">
      <div
        v-for="n in (alarmSetting.colors.length - 1)"
        :key="`${arrayToRgb(alarmSetting.colors[n - 1])}_to_${arrayToRgb(alarmSetting.colors[n])}_${n}`"
        :style="{
          height: '3em',
          background: `linear-gradient(to right, ${arrayToRgb(alarmSetting.colors[n - 1])}, ${arrayToRgb(alarmSetting.colors[n])})`
        }"
        class="col"
      />
    </div>
    <q-card-section
      class="text-grey-5"
      v-html="alarmDescriptionHtml"
    />
    <q-card-actions
      class="row"
    >
      <q-btn-group
        spread
        class="col"
      >
        <q-btn
          dark
          icon="play_arrow"
          color="accent"
          @click="startAlarm()"
        />
        <q-btn
          dark
          icon="stop"
          color="grey-10"
          @click="stopAlarm()"
        />
        <q-btn
          dark
          color="negative"
          icon="delete"
          @click="confirmDelete = true"
        />
      </q-btn-group>
    </q-card-actions>
    <q-expansion-item
      expand-separator
      dark
      icon="settings"
      label="Settings"
      header-class="bg-grey-10"
    >
      <alarm-config
        v-bind="alarmSetting"
        :update="update"
        :remove="remove"
      />
    </q-expansion-item>
    <q-dialog
      v-model="confirmDelete"
      dark
    >
      <q-card class="bg-grey-10 text-white">
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
    apiUrl () {
      return `${process.env.API_BASE_URL}/api/start_alarm/${this.alarmSetting.pk}/`;
    },
    alarmDescriptionHtml () {
      const highlightText = text => `<span class="highlight">${text}</span>`;
      let text = 'This alarm will transition through the colors above in ';
      text += highlightText(`${this.durationMinutes} minutes`);
      if (this.playlistUri !== '') {
        text += `, while playing the ${highlightText(this.playlistObj.name)} playlist`;
        if (this.alarmSetting.shuffle) {
          text += ' on shuffle';
        }
        text += ' with volume progressing from';
        text += ` ${highlightText(`${this.alarmSetting.volumes[0][1]}%`)} to`;
        text += ` ${highlightText(`${this.alarmSetting.volumes[this.alarmSetting.volumes.length - 1][1]}%`)}`;
      }
      text += '.';
      return text;
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
    startAlarm () {
      const url = `/api/start_alarm/${this.alarmSetting.pk}/`;
      this.request({
        method: 'POST',
        url,
        responseType: 'json',
      });
    },
    stopAlarm () {
      const url = `/api/stop_alarm/`;
      this.request({
        method: 'POST',
        url,
        responseType: 'json',
      });
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
span.highlight {
  font-weight: bold;
  color: white;
}
</style>
