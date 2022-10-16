<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="5">
        <v-card-title><h2>Zgłaszanie problemów</h2></v-card-title>
        <v-form v-model="valid">
          <v-row>
            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="title"
                  :counter="15"
                  label="Title"
                  required
              ></v-text-field>
            </v-col>
            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="firstname"
                  :rules="nameRules"
                  :counter="15"
                  label="First name"
                  required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="lastname"
                  :rules="nameRules"
                  :counter="15"
                  label="Last name"
                  required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
              ></v-text-field>
            </v-col>
            <v-col
                cols="12"
                md="12"
            >
              <v-text-field
                  v-model="description"
                  label="Description"
                  required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
        Zdjęcie:
        <v-divider></v-divider>
        <v-btn class="send_button">SEND</v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "NeededPage",
  data: () => ({
    valid: false,
    title: '',
    firstname: '',
    lastname: '',
    description: '',
    picture: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => v.length <= 10 || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
  }),
}
</script>

<style scoped>
.v-card{
  width: 100%;
}
.send_button{
  width: 100%;
}
</style>
