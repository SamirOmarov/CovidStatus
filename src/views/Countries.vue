<template>
  <vx-card title>
    <br />

    <vs-table  pagination :max-items="20" search :data="countries" >
      <template slot="thead">
        <vs-th sort-key="country_name">{{$t('Countries')}}</vs-th>
        <vs-th sort-key="confirmed">{{$t('TotalInfected')}}</vs-th>
        <vs-th sort-key="death">{{$t('Deaths')}}</vs-th>
        <vs-th sort-key="cured">{{$t('Recovered')}}</vs-th>
        <vs-th >{{$t('Lethality')}}</vs-th>

      </template>

      <template slot-scope="{data}">
        <vs-tr :key="indextr" v-for="(tr, indextr) in data">
          <vs-td :data="data[indextr].country_name">{{data[indextr].country_name}}</vs-td>
          <vs-td :data="data[indextr].confirmed">{{data[indextr].confirmed}}</vs-td>
          <vs-td :data="data[indextr].death">{{data[indextr].death}}</vs-td>
          <vs-td :data="data[indextr].cured">{{data[indextr].cured}}</vs-td>
          <vs-td :data="(data[indextr].death/data[indextr].confirmed*100).toFixed(2)">{{(data[indextr].death/data[indextr].confirmed*100).toFixed(2) + ' %'}}</vs-td>
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
    axios.get("http://api.covidstatus.com/cases", {}).then(response => {
      this.countries = response.data;
      this.countries.sort((b,a) => (a.confirmed > b.confirmed) ? 1 : ((b.confirmed > a.confirmed) ? -1 : 0)); 

    });
  }
};
</script>
