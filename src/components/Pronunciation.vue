<template>
  <v-container>
    <v-card class="mt-6 pa-6">
      <h4 class="text-center hdr">
        Name Pronunciation Tool 
      </h4>
      <p class="font-italic">
        Everyone has a name. We'll help you pronounce them.
      </p>
      <v-form>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="3">
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
  </v-container>
</template>

<script lang='ts'>
import { Vue } from "vue-class-component";

export default class Pronunciation extends Vue {
  public txtName = "";
  
  public requestSpokenName() {
    console.log(`Your name is ${this.txtName}`);
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
</style>