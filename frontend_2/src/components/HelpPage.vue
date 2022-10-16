<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="24" pa="2">
        <v-card-title><h2>Lista</h2></v-card-title>

        <v-list two-line>
          <template v-for="(item,index) in items">
            <v-list-item :key="index">
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
                <span><span class="text--secondary">{{ item.zglaszajacy }}</span> &mdash; {{item.description}}</span>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
      <v-card>
        <v-card-title><h2>Zgłoszenie</h2></v-card-title>
        <v-form v-model="valid">
          <v-row>
            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="new_title"
                  label="Title"
                  required
              ></v-text-field>
            </v-col>
            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="new_imie"
                  label="First name"
                  required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="new_nazwisko"
                  label="Last name"
                  required
              ></v-text-field>
            </v-col>
            <v-col
                cols="12"
                md="12"
            >
              <v-text-field
                  v-model="new_description"
                  label="Description"
                  required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelpPage",

  data: () => ({
    new_title: '',
    valid: false,
    new_imie: '',
    new_nazwisko: '',
    new_description: '',

    items: [
      {
        title: "Problem z kotem",
        description: "dassad",
        zglaszajacy: "Bacia Gienia"
      },
      {
        title: "Problem z kotem2",
        description: "dassad",
        zglaszajacy: "Bacia Gienia"
      },
      {
        title: "Problem z kotem3",
        description: "dassadasdsad",
        zglaszajacy: "Bacia Gienia"
      },
    ]
  }),
}
</script>

<style scoped>
.v-card{
  width: 49%;
  padding-top: 1%;
  margin: 1px;
}
.send_button{
  width: 100%;
}
</style>
