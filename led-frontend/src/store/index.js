import Vue from 'vue';
import Vuex from 'vuex';

// import example from './module-example'

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    state: {
      wledStatus: 0,
      wledState: {},
      wledEffects: [],
      wledPalettes: [],
      mopidyStatus: 0,
    },
    mutations: {
      setWledStatus (state, status) {
        state.wledStatus = status;
      },
      setWledState (state, wledState) {
        state.wledState = wledState;
      },
      setWledEffects (state, wledEffects) {
        state.wledEffects = wledEffects;
      },
      setWledPalettes (state, wledPalettes) {
        state.wledPalettes = wledPalettes;
      },
      setMopidyStatus (state, status) {
        state.mopidyStatus = status;
      },
    },

    modules: {
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV,
  });

  return Store;
}
