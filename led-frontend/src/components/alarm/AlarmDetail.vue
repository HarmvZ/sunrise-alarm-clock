<template>
  <q-card class="col-12 bg-grey-9 text-center q-mt-md">
    <q-parallax
      :src="img"
      :height="150"
      class="opacity-parallax"
    >
      <span class="text-h5 text-white">{{ name }}</span>
      <q-popup-edit v-if="editable" v-model="name">
        <q-input class=" text-h5" v-model="name" dense autofocus />
      </q-popup-edit>
    </q-parallax>
    <q-card-section class="column items-center">
      <div class="row items-center q-mb-md">
        <q-item-label class="text-center">
          <q-toggle
            v-if="editable"
            v-model="alarm_enabled"
            icon="alarm"
            size="xl"
          />
        </q-item-label>
        <q-item-label
          @click="timeDialog = editable"
          lines="1"
          class="text-weight-bold text-primary text-uppercase"
        >
          <span class="cursor-pointer text-h2 text-white">{{ hour }}:{{ minute }}</span>
        </q-item-label>
        <q-item-label class="text-center">
          <q-btn
            v-if="editable"
            @click="confirmDelete = true"
            color="grey-6"
            flat
            size="s"
            icon="delete"
          />
        </q-item-label>
      </div>
      <q-item-label
        caption
        class="q-gutter-xs row items-center"
      >
        <q-btn
          v-for="dow in dow_map"
          :key="dow.value"
          :disabled="!editable"
          @click="toggleDow(dow.value)"
          :flat="!day_of_week.split(',').includes(dow.value)"
          :color="day_of_week.split(',').includes(dow.value) ? 'primary' : 'gray-6'"
          size="md"
          dense
          style="color: #ccc;"
        >
          {{ dow.label }}
        </q-btn>
      </q-item-label>
    </q-card-section>
    <q-dialog v-model="timeDialog">
        <q-time
          v-model="time"
          @input="timeChanged"
          format24h
          dark
        />
    </q-dialog>
    <q-dialog dark v-model="confirmDelete">
      <q-card class="bg-grey-9 text-white">
        <q-card-section class="row items-center">
          <q-avatar icon="warning" color="negative" text-color="white" />
          <span class="q-ml-sm">Are you sure you want to remove "{{ name }}"?</span>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="white" v-close-popup />
          <q-btn flat label="Ok" color="negative" v-close-popup @click="removeAlarm(pk)" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-card>
</template>

<style>
</style>

<script>
// import DarkCard from 'components/DarkCard';

export default {
  name: 'AlarmDetail',
  // components: { DarkCard },
  props: {
    pk: Number,
    name: String,
    hour: String,
    minute: String,
    enabled: Boolean,
    day_of_week: String,
    updateAlarm: Function,
    removeAlarm: Function,
    editable: {
      type: Boolean,
      default: true,
    },
  },
  data () {
    return {
      dow_map: [
        { value: '1', label: 'Mon' },
        { value: '2', label: 'Tue' },
        { value: '3', label: 'Wed' },
        { value: '4', label: 'Thu' },
        { value: '5', label: 'Fri' },
        { value: '6', label: 'Sat' },
        { value: '0', label: 'Sun' },
      ],
      time: this.hour + ':' + this.minute,
      timeDialog: false,
      confirmDelete: false,
    };
  },
  computed: {
    alarm_name: {
      get () {
        return this.name;
      },
      set (name) {
        this.updateAlarm(this.pk, { name });
      },
    },
    alarm_enabled: {
      get () {
        return this.enabled;
      },
      set (enabled) {
        this.updateAlarm(this.pk, { enabled });
      },
    },
    img () {
      const randomInt = Math.floor(Math.random() * 6) + 1;
      return `statics/alarm/${randomInt}.jpg`;
    },
  },
  methods: {
    timeChanged (value) {
      this.timeDialog = false;
      const [hour, minute] = value.split(':');
      this.updateAlarm(this.pk, { hour, minute });
    },
    toggleDow (value) {
      if (!this.editable) {
        return;
      }
      let dow = this.day_of_week.split(',');
      if (dow.includes(value)) {
        dow = dow.filter((dow) => dow !== value);
        this.updateAlarm(this.pk, { day_of_week: dow.join(',') });
      } else {
        dow.push(value);
        this.updateAlarm(this.pk, { day_of_week: dow.join(',') });
      }
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
