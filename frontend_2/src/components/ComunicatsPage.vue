<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="15">
        <v-card-title><h1>Ogłoszenia</h1></v-card-title>
        <v-list>
          <template v-for="(item,index) in new_items">
            <v-list-item :key="index">
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
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
        title: 'NewName',
        autor: 'asdasd',
        description1: 'asdasd',
      },
      {
        title: 'NewName',
        autor: 'asdasd',
        description1: 'asdasd',
      },
      {
        title: 'NewName',
        autor: 'asdasd',
        description1: 'asdasd',

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
