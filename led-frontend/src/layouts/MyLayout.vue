<template>
  <q-layout
    view="lHh Lpr lFf"
    class="text-grey-4"
    style="background: #1f1f1f"
  >
    <q-header
      elevated
      class="bg-grey-9"
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

        <q-toolbar-title>
          {{ $appName }}
        </q-toolbar-title>

        <connection-status class="q-mr-sm" />
        <mopidy-connection-status />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawerOpen"
      show-if-above

      :mini="miniState"
      mini-to-overlay
      :width="300"
      :breakpoint="500"

      content-class="bg-grey-10"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
    >
      <q-list
        dark
        style="height: calc(100% - 150px); margin-top: 150px;"
      >
        <q-item
          v-for="(menuItem, id) in menuList"
          :key="id"
          v-ripple
          clickable
          :to="menuItem.route"
          exact
        >
          <q-item-section avatar>
            <q-icon :name="menuItem.icon" />
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
import ConnectionStatus from 'components/ConnectionStatus';
import MopidyConnectionStatus from 'components/MopidyConnectionStatus';

const menuList = [
  {
    icon: 'home',
    label: 'Home',
    route: '/',
  },
  {
    icon: 'alarm',
    label: 'Alarms',
    route: '/alarms',
  },
  {
    icon: 'color_lens',
    label: 'Color',
    route: '/colors',
  },
  {
    icon: 'movie_filter',
    label: 'Animations',
    route: '/animations',
  },
  {
    icon: 'audiotrack',
    label: 'Music',
    route: '/music',
  },
];

export default {
  name: 'MyLayout',
  components: { MopidyConnectionStatus, ConnectionStatus },
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
