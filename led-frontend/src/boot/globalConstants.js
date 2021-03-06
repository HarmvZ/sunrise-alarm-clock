import axios from 'axios';
import Mopidy from 'mopidy';

const socket = new WebSocket(process.env.WLED_WS);
const mopidy = new Mopidy({
  webSocketUrl: process.env.MOPIDY_WS,
  autoConnect: false,
});

export default async ({ Vue }) => {
  Vue.prototype.$axios = axios;
  Vue.prototype.$wledSocket = socket;
  Vue.prototype.$mopidy = mopidy;
};
