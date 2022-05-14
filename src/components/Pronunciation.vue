<template>
  <v-card class="overflow-hidden">
    <v-app-bar app elevate-on-scroll scroll-target="#scrolling-techniques-7" elevation="12" color="#d71e28" class="hdr">
      <v-toolbar-title class="flex wht">NAME PRONUNCIATION TOOL</v-toolbar-title>
    </v-app-bar>
    <v-sheet id="scrolling-techniques-7" class="overflow-y-auto" max-height="60" height="60">

    </v-sheet>
  </v-card>
  <v-card>
    <v-form ref="frmMain">
      <v-container>
        <v-row>
          <v-col cols="12" sm="12" md="6">
            <v-text-field solo label="Employee ID" v-model="currUser.id" hint="Employee ID">
            </v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="6">
            <v-btn color="primary" @click="retrieveUser">
              Lookup
            </v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="12" md="4">
            <v-select label="Locale" single-line  v-model="currLocale" :items="locales">
            </v-select>
          </v-col>
          <v-col cols="12" sm="12" md="4">
            <v-select :items="genders" v-model="currGender">
            </v-select>
          </v-col>
          <v-col cols="12" sm="12" md="4">
            <v-select :items="filteredVoices" v-model="currName">
            </v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="12" md="6">
            <v-text-field solo label="First Name" v-model="currUser.firstName" :rules="nameRules" hint="Enter a First Name to Speak" append-icon="mdi-play-circle" @click:append="speakFirstName">
            </v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="6">
            <v-text-field solo label="Last Name" v-model="currUser.lastName" :rules="nameRules" hint="Enter a Last Name to Speak" append-icon="mdi-play-circle" @click:append="speakLastName">
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="12" md="6">
            <v-text-field solo label="Preferred First Name" v-model="currUser.preferredFirstName" :rules="nameRules" hint="Enter a First Name to Speak" append-icon="mdi-play-circle" @click:append="speakPreferredFirstName">
            </v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="6">
            <v-text-field solo label="Preferred Last Name" v-model="currUser.preferredLastName" :rules="nameRules" hint="Enter a Last Name to Speak" append-icon="mdi-play-circle" @click:append="speakPreferredLastName">
            </v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="2" md="1">
            <v-btn color="primary" @click="onSaveClick">
              Save
            </v-btn>
          </v-col>
          <v-col v-if="!newUser" cols="12" sm="2" md="1">
            <v-btn color="primary" @click="deleteUser">
              Forget Me
            </v-btn>
          </v-col>
        </v-row>
        <v-row v-if="!newUser">
          <v-col>
            <p>Click "Forget Me" to not participate in pronuncation program.</p>
          </v-col>
        </v-row>
        <v-row v-if="newUser">
          <v-col>
            <p>Click "Save" to participate in the pronuciation program.</p>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>

</template>

<script lang='ts'>
import { Vue } from "vue-class-component";
import { Watch} from "vue-property-decorator"

import axios from "axios";

export default class Pronunciation extends Vue {
  public txtName = "";
  public frmMain: any;
  public currLocale: string = "";
  public currGender: string = "";
  public currName: string = "";

  public voices: any[] = [];
  public filteredVoices: any[] = [];
  public genders: string[] = ["Male", "Female"];
  public locales: string[] = [];

  public newUser: boolean = true;

  public defaultUser: any = {
        "uid": null,
        "firstName": null,
        "lastName": null,
        "preferredFirstName": null,
        "preferredLastName": null,
        "email": null,
        "userPronunciation": null,
        "systemPronunciation": null,
        "id": null,
        "voiceId": 107,
    }

  public currUser: any = {
        "uid": null,
        "firstName": "",
        "lastName": "",
        "preferredFirstName": null,
        "preferredLastName": null,
        "email": null,
        "userPronunciation": null,
        "systemPronunciation": null,
        "id": null,
        "voiceId": 107,
  }

  public get nameRules() {
    return  [
        (v: string) => !!v || 'Name is required',
        (v: string) => /^[a-zA-Z ]+$/i.test(v) || 'Name must be valid'
      ]
  }


  public speakFirstName() {
    console.log(`Should speak ${this.currUser.firstName}`)
    var audio: HTMLAudioElement = new Audio(`https://name-pronunciation-tool-twh.azurewebsites.net/api/pronounceNameWithVoice/${this.currUser.voiceId}/${this.currUser.firstName}`);
    audio.play();

  }

  public speakLastName() {
    console.log(`Should speak ${this.currUser.firstName}`)
    var audio: HTMLAudioElement = new Audio(`https://name-pronunciation-tool-twh.azurewebsites.net/api/pronounceNameWithVoice/${this.currUser.voiceId}/${this.currUser.lastName}`);
    audio.play();

  }

  public speakPreferredFirstName() {
    console.log(`Should speak ${this.currUser.firstName}`)
    var audio: HTMLAudioElement = new Audio(`https://name-pronunciation-tool-twh.azurewebsites.net/api/pronounceNameWithVoice/${this.currUser.voiceId}/${this.currUser.preferredFirstName}`);
    audio.play();

  }

  public speakPreferredLastName() {
    console.log(`Should speak ${this.currUser.firstName}`)
    var audio: HTMLAudioElement = new Audio(`https://name-pronunciation-tool-twh.azurewebsites.net/api/pronounceNameWithVoice/${this.currUser.voiceId}/${this.currUser.preferredLastName}`);
    audio.play();

  }

  public onSaveClick() {
    if (this.newUser) {
      this.addUser();
    } else {
      this.updateUser();
    }
  }
  public addUser() {
    this.currUser.uid = this.currUser.id;
    axios.post(`https://name-pronunciation-tool-twh.azurewebsites.net/api/users`, this.currUser).then((response: any) => {
      this.newUser = false;
    }).catch((response: any) => {

    });
  }

  public updateUser() {
    this.voices.forEach( element  => {
      if (element.name == this.currName) {
        this.currUser.voiceId = element.id;
      }
    })

    axios.put(`https://name-pronunciation-tool-twh.azurewebsites.net/api/users/${this.currUser.id}`, this.currUser).then((response: any) => {
    }).catch((response: any) => {

    });

  }

  public deleteUser() {
    axios.delete(`https://name-pronunciation-tool-twh.azurewebsites.net/api/users/${this.currUser.id}`).then((response: any) => {
      this.newUser = true;
    })
    .catch((response: any) => {});
  }

  public retrieveUser() {
    console.log(`Retrieving user: ${this.currUser.id}`)
    axios.get(`https://name-pronunciation-tool-twh.azurewebsites.net/api/users/${this.currUser.id}`).then((response: any) => {
      this.currUser = response.data;
      this.voices.forEach(element => {
        if (this.currUser.voiceId == element.id) {
          this.currLocale = element.locale;
          this.currGender = element.gender;
          this.currName = element.name;
        }
      })
      this.newUser = false;
    }).catch((respons: any) => {
      let tmp = this.currUser.id;
      Object.assign(this.currUser,this.defaultUser);
      this.currUser.id = tmp;
      this.voices.forEach(element => {
        if (this.currUser.voiceId == element.id) {
          this.currLocale = element.locale;
          this.currGender = element.gender;
          this.currName = element.name;
        }
      })
      this.newUser = true;
    });
  }

  private filterDownVoices() {
      this.voices.forEach(element => {
        if (element.locale == this.currLocale) {
          if (element.gender == this.currGender) {
            this.filteredVoices.push(element.name);
          }
        }
      });

      this.filteredVoices.sort();
  }

  @Watch('currLocale')
  public onLocaleChg(value: string, oldValue: string) {
    console.log("Locale changed")
    this.filteredVoices = [];
    if (this.currGender && this.currLocale) {
      this.filterDownVoices();
    }
  }

  @Watch('currGender')
  public onGenderChg(value: string, oldValue: string) {
    this.filteredVoices = [];
    if (this.currGender && this.currLocale) {
      this.filterDownVoices();
    }
  }

  @Watch('currName')
  public onVoiceChange(value: string, oldValue: string) {
    this.voices.forEach( element  => {
      if (element.name == this.currName) {
        this.currUser.voiceId = element.id;
      }
    })
  }

  public mounted() {
    axios.get("https://name-pronunciation-tool-twh.azurewebsites.net/api/voice/list/all").then((response: any) => {
      this.voices = response.data;
      this.locales = [];
      this.voices.forEach(element => {
        let i = this.locales.indexOf(element.locale);
        if (i == -1) {
          this.locales.push(element.locale);
        }
      });
      this.locales.sort();
    })
    .catch((error: any) => {
      this.voices = [];
    })
  }
}

// import { defineComponent } from 'vue';

// export default defineComponent({
//   data() {
//     return {
//       nameRules: [
//         (v) => !!v || 'Name is required',
//         (v) => /^[a-zA-Z ]+$/i.test(v) || 'Name must be valid'
//       ]
//     }
//   },

//   methods: {
//     requestSpokenName() {
//       console.log(`Your name is ${this.txtName}`);
//       this.$refs.form.validate().then(function (result) {
//         if (result.valid) {
//           var audio: any = new Audio("/static/service-bell_daniel_simion.mp3");
//           audio.play();
//         }
//         else {
//           return;
//         }
//       });
//     }
//   },

// });
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