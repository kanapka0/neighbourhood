<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="5">
        1. Zgłaszanie problemów
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="firstClick()"
        >Click ME</v-btn>
      </v-card>
      <v-card elevation="10">
        2. Petycje
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="secondClick()"
        >Click ME</v-btn>
      </v-card>
    </v-row>
    <v-row justify="center">
      <v-card elevation="15">
        3. Ogłoszenia
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="thirdClick()"
        >Click ME</v-btn>
      </v-card>
      <v-card elevation="20">
        4. Kontakt
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="fourthClick()"
        >Click ME</v-btn>
      </v-card>
    </v-row>
    <v-row justify="center">
      <v-card elevation="24">
        5. Pomoc
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="fifthClick()"
        >Click ME</v-btn>
      </v-card>
      <v-card elevation="24">
        6. Przydatne Informacje
        <br><br>
        <v-btn
            color="primary"
            elevation="2"
            large
            small
            @click="sixthClick()"
        >Click ME</v-btn>
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
  height: 200px;
  width: 250px;
  margin: 10px;
  padding: 5px;
  text-align: center;
  justify-content: center;
  justify-items: center;
}
</style>
