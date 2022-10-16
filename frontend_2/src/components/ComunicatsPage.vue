<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="15">
        <v-card-title><h1>Ogłoszenia</h1></v-card-title>
        <v-list two-line>
          <template v-for="(item,index) in new_items">
            <v-list-item :key="index">
              <v-list-item-content>
                <h3><b>
                  <v-list-item-title v-text="item.title"></v-list-item-title>
                </b></h3>
                <span><span class="text--secondary">{{ item.autor }}</span> &mdash; {{item.description1}}</span>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-row>
  </v-container>
</template>


<script>
export default {
  name: "ComunicatsPage",
  data: () => ({
    new_items: [
      {
        title: 'Pobór krwi',
        autor: 'Lokalny ośrodek zdrowia',
        description1: 'Zapraszamy wszystkie osoby pełnoletnie aby oddały krew w najbliższą środe w ośrodku zdrowia',
      },
      {
        title: 'Sprzątanie parku',
        autor: 'Spółdzielnia mieszkaniowa "Cichy raj"',
        description1: 'Spółdzielnia mieszkaniowa "Cichy raj" organizuje szprzątanie parku przy ulicy miłej w piątek o 14',
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
