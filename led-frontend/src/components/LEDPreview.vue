<template>
  <div>
    <table>
      <tr v-for="(row, id) in rows" :key="id">
        <td v-for="(col, col_id) in cols" :key="`${id}${col_id}`">
          <div class="pixel" :ref="`pixel_${id}_${col_id}`"></div>
        </td>
      </tr>
    </table>
  </div>
</template>

<style>
</style>

<script>

export default {
  name: 'LEDPreview',
  data () {
    return {
      pixels: false,
      interval: false,
    };
  },
  computed: {
    rows () {
      return [1] * 10;
    },
    cols () {
      return [1] * 30;
    },
  },
  watch: {
    pixels (val) {
      for (const [id, pixel] of val.entries()) {
        const row = parseInt(id / 30);
        const col = id % 30;
        const div = this.$refs[`pixel_${row}_${col}`][0];
        div.style.backgroundColor = `rgb(${pixel[0]},${pixel[1]},${pixel[2]})`;
      }
    },
  },
  methods: {
    async getPixels () {
      const url = '/api/get_pixels/';
      const response = await this.request({
        method: 'GET',
        url,
        responseType: 'json',
      });
      return response.pixels;
    },
  },
  mounted () {
    this.getPixels().then(data => {
      this.pixels = data;
      this.interval = setInterval(async () => {
        this.pixels = await this.getPixels();
      }, 500);
    });
  },
  beforeDestroy () {
    clearInterval(this.interval);
  },
};
</script>
<style scoped>
table{
  background: #000;
}
.pixel{
  display: block;
  width: 5px;
  height: 5px;
}
</style>
