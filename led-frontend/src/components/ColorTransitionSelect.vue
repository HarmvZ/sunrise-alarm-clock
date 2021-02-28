<template>
  <div class="q-py-md row justify-evenly text-grey-6">
    <ChooseColorPopup
      :value="arrayToRgb(colors[0])"
      icon="colorize"
      @input="changeColor(0, $event)"
    />
    <template
      v-for="(c, n) in colors.slice(1, colors.length -1)"
    >
      <q-icon
        :key="'arrow-' + n"
        name="arrow_downward"
        style="font-size: 2em"
      />
      <ChooseColorPopup
        :key="`${arrayToRgb(c)}_${n}`"
        :value="arrayToRgb(c)"
        :removable="true"
        icon="colorize"
        color="grey-9"
        @remove="removeColor(n)"
        @input="changeColor(n + 1, $event)"
      />
    </template>
    <q-icon
      name="arrow_downward"
      style="font-size: 2em"
    />
    <q-btn
      icon="add"
      label=""
      color="grey-9"
      class="full-width"
      @click="addColor()"
    />
    <q-icon
      name="arrow_downward"
      style="font-size: 2em"
    />
    <ChooseColorPopup
      :value="arrayToRgb(colors[colors.length - 1])"
      icon="colorize"
      @input="changeColor(colors.length - 1, $event)"
    />
  </div>
</template>
<script>
import ChooseColorPopup from 'src/components/ChooseColorPopup';
import { arrayToRgb, rgbToArray } from 'src/utils/colors';

export default {
  components: { ChooseColorPopup },
  props: {
    colors: {
      type: Array,
      required: true,
    },
  },
  methods: {
    arrayToRgb,
    rgbToArray,
    removeColor (n) {
      const newColors = [
        ...this.colors.slice(0, n + 1),
        ...this.colors.slice(n + 2),
      ];
      this.$emit('update', { colors: newColors });
    },
    changeColor (index, c) {
      const newColors = this.colors.slice();
      newColors[index] = this.rgbToArray(c);
      this.$emit('update', { colors: newColors });
    },
    addColor () {
      const cLen = this.colors.length;
      const newColors = [
        ...this.colors.slice(0, cLen - 1),
        [255, 255, 255],
        this.colors[cLen - 1],
      ];
      this.$emit('update', { colors: newColors });
    },
  },
};
</script>
