<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="5" @click="firstClick()" >
        <div>
          <h2>Zgłaszanie problemów</h2>
        </div>
      </v-card>
      <v-card elevation="10" @click="secondClick()">
        <h2>Petycje</h2>
      </v-card>
    </v-row>
    <v-row justify="center">
      <v-card elevation="15" @click="thirdClick()">
        <h2>Ogłoszenia</h2>
      </v-card>
      <v-card elevation="20" @click="fourthClick()">
        <h2>Kontakt</h2>
      </v-card>
    </v-row>
    <v-row justify="center">
      <v-card elevation="24" @click="fifthClick()">
        <h2>Pomoc</h2>
      </v-card>
      <v-card elevation="24" @click="sixthClick()">
        <h2>Przydatne Informacje</h2>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default{
  name: "AboutView",
  methods: {
    firstClick() {this.$router.push({path: "/needed"})},
    secondClick(){this.$router.push({path: "/petition"})},
    thirdClick(){this.$router.push({path: "/comunicats"})},
    fourthClick(){this.$router.push({path: "/contacts"})},
    fifthClick(){this.$router.push({path: "/help"})},
    sixthClick(){this.$router.push({path: "/map"})},
  }
}

</script>

<style>
.v-card{
  padding-top: 10px;
  padding: 5px;
  height: 200px;
  width: 250px;
  margin: 10px;
  text-align: center;
  justify-content: center;
  justify-items: center;
}
</style>
