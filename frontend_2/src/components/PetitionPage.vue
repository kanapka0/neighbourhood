<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="10" pa="2">
        <v-card-title>Lista Petycji</v-card-title>
        <v-list two-line>
          <template v-for="(item,index) in items">
            <v-list-item :key="index">
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
                <span><span class="text--secondary">{{ item.zglaszajacy }}</span> &mdash; {{item.description}}</span>
                {{item.rating}}
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
      <v-card>
        <v-card-title>Petycja</v-card-title>


      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "PetitionPage",
  data: () => ({
    new_title: '',

    items: [
      {
        title: "Problem z kotem",
        description: "dassad",
        zglaszajacy: "Bacia Gienia",
        rating: 10
      },
      {
        title: "Problem z kotem2",
        description: "dassad",
        zglaszajacy: "Bacia Gienia",
        rating: 20
      },
      {
        title: "Problem z kotem3",
        description: "dassadasdsad",
        zglaszajacy: "Bacia Gienia",
        rating: 30
      },
    ]
  })
}
</script>

<style scoped>
.v-card{
  width: 49%;
  padding-top: 1%;
  margin: 1px;
}
</style>
