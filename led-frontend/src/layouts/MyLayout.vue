<template>
  <q-layout view="lHh Lpr lFf" class="text-grey-4" style="background: #1f1f1f">
    <q-header elevated class="bg-grey-9">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="drawerOpen = !drawerOpen"
          aria-label="Menu"
          icon="menu"
          />

        <q-toolbar-title>
          {{ $appName }}
        </q-toolbar-title>

        <connection-status />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawerOpen"
      show-if-above

      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      mini-to-overlay

      :width="300"
      :breakpoint="500"
      content-class="bg-grey-10"
    >
      <q-list dark style="height: calc(100% - 150px); margin-top: 150px;">
        <q-item
          v-for="(menuItem, id) in menuList"
          :key="id"
          clickable
          v-ripple
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

      <q-img class="absolute-top" :src="img" style="height: 150px">
        <div class="absolute-bottom bg-transparent">
        </div>
      </q-img>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- <q-footer elevated class="bg-grey-9 flex column items-center">
      <div class="col">
        <q-btn
          flat
          round
          color="white"
          :icon="showPreview ? 'expand_more' : 'expand_less'"
          @click="showPreview = !showPreview"
          label=""
        />
      </div>
      <div class="col">
        <l-e-d-preview v-if="showPreview" class="q-pb-md"/>
      </div>
    </q-footer> -->
  </q-layout>
</template>

<script>
import { openURL } from 'quasar';
import ConnectionStatus from 'components/ConnectionStatus';
// import LEDPreview from '../components/LEDPreview.vue';

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
];

export default {
  name: 'MyLayout',
  data () {
    return {
      drawerOpen: false,
      showPreview: false,
      miniState: true,
      menuList,
    };
  },
  methods: {
    openURL,
  },
  components: { ConnectionStatus }, //, LEDPreview },
  computed: {
    img () {
      const randomInt = Math.floor(Math.random() * 6) + 1;
      return `statics/alarm/${randomInt}.jpg`;
    },
  },
};
</script>

<style>
</style>
