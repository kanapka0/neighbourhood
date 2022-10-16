<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="15">
        <v-card-title><h1>Ogłoszenia</h1></v-card-title>
        <v-list two-line>
          <template v-for="(item,index) in items">
            <v-list-item :key="index">
              <v-list-item-content>
                <v-list-item-title v-text="item.name"></v-list-item-title>
                <span><span class="text--secondary">{{ item.autors }}</span> &mdash; {{item.description}}</span>
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
    items: [
      {
        name: 'NewName',
        autors: 'asdasd',
        description: 'asdasd',
      },
      {
        name: 'NewName',
        autors: 'asdasd',
        description: 'asdasd',
      },
      {
        name: 'NewName',
        autors: 'asdasd',
        description: 'asdasd',

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
