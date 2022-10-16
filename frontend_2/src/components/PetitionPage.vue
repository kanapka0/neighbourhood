<template>
  <v-container>
    <v-row justify="center">
      <v-card elevation="10">
        <v-card-title>Lista Petycji</v-card-title>
        <v-list two-line>
          <template v-for="(item,index) in items">
            <v-list-item :key="index">
              <v-list-item-content>
                <b><v-list-item-title v-text="item.title"></v-list-item-title></b>
                <span><span class="text--secondary">{{ item.zglaszajacy }}</span> &mdash; {{item.description}}</span>
                <v-divider></v-divider>
                Popularność: <b>{{item.rating}}</b>
                <v-divider></v-divider>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
      <v-spacer></v-spacer>
      <v-card elevation="10">
        <v-card-title>Petycja</v-card-title>
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
        <v-divider></v-divider>
        <v-btn class="send_button">SEND</v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "PetitionPage",
  data: () => ({
    new_title: '',
    valid: false,
    new_imie: '',
    new_nazwisko: '',
    new_description: '',

    items: [
      {
        title: "Nowa Ławka",
        description: "Prosimy o zamontowanie nowej ławki na skwerku wagnera, ponieważ stara już jest zniszczona",
        zglaszajacy: "Agata Kowalska",
        rating: 10
      },
      {
        title: "Petycja o posadzenie",
        description: "Wnosimy o posadzenie nowych drzew w naszym parku, ponieważ z powodu suszy większość po usychała",
        zglaszajacy: "Adam Nowak",
        rating: 20
      },
      {
        title: "Wywoz smieci",
        description: "Zglaszamy sie z prosba o zapenienie dodatkowych wywozow smieci z terenow przy akademickich na naszym osiedlu z powodu nie ustajacych imprez.",
        zglaszajacy: "Rodzina Kamieńskich",
        rating: 30
      },
    ]
  })
}
</script>

<style scoped>
.v-card{
  width: 49%;

}
.send_button{
  width: 100%;
}
</style>
