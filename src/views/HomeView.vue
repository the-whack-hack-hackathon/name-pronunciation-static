<template>
  <pronunciation />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Pronunciation from '../components/Pronunciation.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    Pronunciation
  },
});
</script>
