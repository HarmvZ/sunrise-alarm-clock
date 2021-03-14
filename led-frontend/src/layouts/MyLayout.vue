<template>
  <q-layout
    view="lHh Lpr lFf"
    style="background: #000811"
  >
    <q-header
      elevated
      class="bg-secondary"
    >
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          aria-label="Menu"
          icon="menu"
          @click="drawerOpen = !drawerOpen"
        />

        <q-toolbar-title />

        <api-connection-status class="q-mr-sm" />
        <mopidy-connection-status class="q-mr-sm" />
        <WledConnectionStatus />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawerOpen"
      show-if-above

      :mini="miniState"
      mini-to-overlay
      :width="300"
      :breakpoint="500"

      content-class="bg-secondary"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
    >
      <q-list
        dark
        style="height: calc(100% - 150px); margin-top: 150px;"
        class="text-grey-5"
      >
        <q-item
          v-for="(menuItem, id) in menuList"
          :key="id"
          v-ripple
          clickable
          :to="menuItem.route"
          exact
          active-class="text-white text-weight-bold"
        >
          <q-item-section
            avatar
            top
          >
            <q-avatar
              :icon="menuItem.icon"
              rounded
            />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ menuItem.label }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <q-img
        class="absolute-top"
        :src="img"
        style="height: 150px"
      >
        <div class="absolute-bottom bg-transparent" />
      </q-img>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { openURL } from 'quasar';
import ApiConnectionStatus from 'components/ApiConnectionStatus';
import MopidyConnectionStatus from 'components/MopidyConnectionStatus';
import WledConnectionStatus from 'components/WledConnectionStatus';

const menuList = [
  {
    icon: 'lightbulb',
    label: 'Light',
    route: '/',
  },
  {
    icon: 'alarm',
    label: 'Alarms',
    route: '/alarms',
  },
  {
    icon: 'audiotrack',
    label: 'Music',
    route: '/music',
  },
];

export default {
  name: 'MyLayout',
  components: { MopidyConnectionStatus, ApiConnectionStatus, WledConnectionStatus },
  data () {
    return {
      drawerOpen: false,
      showPreview: false,
      miniState: true,
      menuList,
      hostname: process.env.HOSTNAME,
    };
  }, //, LEDPreview },
  computed: {
    img () {
      const randomInt = Math.floor(Math.random() * 6) + 1;
      return `statics/alarm/${randomInt}.jpg`;
    },
  },
  methods: {
    openURL,
  },
};
</script>

<style>
</style>
