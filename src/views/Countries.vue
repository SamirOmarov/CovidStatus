<template>
  <vx-card title>
    <br/>

    <vs-table pagination :max-items="20" search :data="countries">
      <template slot="thead">
        <vs-th sort-key="country_name">{{$t('Countries')}}</vs-th>
        <vs-th sort-key="confirmed">{{$t('TotalInfected')}}</vs-th>
        <vs-th sort-key="new_confirmed">{{$t('NewCases')}}</vs-th>
        <vs-th sort-key="death">{{$t('Deaths')}}</vs-th>
        <vs-th sort-key="new_death">{{$t('NewDeath')}}</vs-th>
        <vs-th sort-key="cured">{{$t('Recovered')}}</vs-th>
        <vs-th sort-key="tests">{{$t('NumberOfTests')}}</vs-th>
        <vs-th sort-key="lethality">{{$t('Lethality')}}</vs-th>
      </template>

      <template slot-scope="{data}">
        <vs-tr :key="indextr" v-for="(row, indextr) in data">
          <vs-td :data="row.country_name">{{row.country_name}}</vs-td>
          <vs-td :data="parseInt(row.confirmed)">{{row.confirmed}}</vs-td>
          <vs-td :data="parseInt(row.new_confirmed)">{{row.new_confirmed}}</vs-td>
          <vs-td :data="parseInt(row.death)">{{row.death}}</vs-td>
          <vs-td :data="parseInt(row.new_death)">{{row.new_death}}</vs-td>
          <vs-td :data="parseInt(row.cured)">{{row.cured}}</vs-td>
          <vs-td :data="parseInt(row.tests)">{{row.tests}}</vs-td>
          <vs-td :data="parseInt(row.lethality)">{{row.lethality}} %</vs-td>
        </vs-tr>
      </template>
    </vs-table>
  </vx-card>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        countries: []
      };
    },
    mounted() {
      axios.get("https://api.covidstatus.com/cases", {}).then(response => {
        this.countries = response.data;
        for (let i = 0; i < this.countries.length; i++) {
          if (this.countries[i]['confirmed'] != 0) {
            this.countries[i]['lethality'] = parseFloat((this.countries[i]['death'] * 100 / this.countries[i]['confirmed']).toFixed(2));
          } else {
            this.countries[i]['lethality'] = 0
          }
        }
        this.countries.sort((b, a) => (a.confirmed > b.confirmed) ? 1 : ((b.confirmed > a.confirmed) ? -1 : 0));

      });
    }
  };
</script>
