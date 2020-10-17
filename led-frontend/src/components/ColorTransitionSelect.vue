<template>
  <div>
    <ChooseColorPopup
      v-model="startingColor"
      label="Starting color"
      icon="colorize"
      class="q-my-md"
    />

    <div class="q-my-md">
      <ChooseColorPopup
        v-for="n in nTransitionColors"
        :key="n"
        v-model="transitionColors[n-1]"
        :label="`Transition color ${n}`"
        icon="colorize"
        color="grey-9"
        class="full-width"
      />
      <q-btn
        v-if="isColorAddable"
        icon="add"
        label="Add transition color"
        color="grey-9"
        class="full-width"
        @click="nTransitionColors += 1"
      />
    </div>
    <ChooseColorPopup
      v-model="finishColor"
      label="Finish color"
      icon="colorize"
      class="q-my-md"
    />
    <div class="q-py-md row justify-evenly">
      <template
        v-for="(c, idx) in colors"
      >
        <div
          :key="idx"
          class="display-inline"
          :style="{
            width: '3em',
            height: '3em',
            backgroundColor: c,
          }"
        />
        <q-icon
          v-if="idx + 1 < colors.length"
          :key="`${idx}-arrow`"
          name="forward"
          style="font-size: 3em"
          color="grey-9"
        />
      </template>
    </div>
  </div>
</template>
<script>
import ChooseColorPopup from 'src/components/ChooseColorPopup';
import getRGBColorObject from 'src/utils/getRGBColorObject';

export default {
  components: { ChooseColorPopup },
  data () {
    return {
      nTransitionColors: 0,
      startingColor: 'rgb(0, 0, 0)',
      finishColor: 'rgb(255, 255, 255)',
      transitionColors: [],
    };
  },
  computed: {
    colors () {
      return [
        this.startingColor,
        ...this.transitionColors,
        this.finishColor,
      ];
    },
    colorsObj () {
      return this.colors.map(c => getRGBColorObject(c));
    },
    isColorAddable () {
      return (
        this.transitionColors.filter(v => typeof (v) === 'undefined').length === 0 &&
        this.nTransitionColors === this.transitionColors.length
      );
    },
  },
};
</script>
