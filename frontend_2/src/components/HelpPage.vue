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
        Imie:
        Nazwisko:
        Tytuł:
        Opis:

      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelpPage",

  data: () => ({
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
</style>
