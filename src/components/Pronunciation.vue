<template>
  <v-card class="overflow-hidden" >
    <v-app-bar app  elevate-on-scroll scroll-target="#scrolling-techniques-7" elevation="12" color="#d71e28" class="hdr">
      <v-toolbar-title class="flex wht">Name Pronunciation Tool</v-toolbar-title>
    </v-app-bar>
    <v-sheet id="scrolling-techniques-7" class="overflow-y-auto" max-height="60" height="60">
      
    </v-sheet>
  </v-card>
  <v-card>
    <v-form>
      <v-container>
        <v-row>
          <v-col cols="12" sm="6" md="4">
            <v-text-field solo label="Name" v-model="txtName">
            </v-text-field>
            <v-btn color="primary" @click="requestSpokenName">
              <v-icon left>
                mdi-play-circle
              </v-icon>
              Listen
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>

</template>

<script lang='ts'>
import { Vue } from "vue-class-component";

export default class Pronunciation extends Vue {
  public txtName = "";

  public requestSpokenName() {
    console.log(`Your name is ${this.txtName}`);
    // validation if name is empty
    var audio: any = new Audio("/static/service-bell_daniel_simion.mp3");
    audio.play();
  }
}
</script>

<style>
.hdr {
  background-color: #d71e28;
  border-bottom: 4px solid #ffcd41;
}

.wht {
   color: #ffffff;
}
</style>