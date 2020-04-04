<template>
  <vx-card title>
    <br />

    <vs-table search  :data="countries" >
      <template slot="thead">
        <vs-th sort-key="country_name">{{$t('Countries')}}</vs-th>
        <vs-th sort-key="confirmed">{{$t('TotalInfected')}}</vs-th>
        <vs-th>{{$t('Deaths')}}</vs-th>
        <vs-th>{{$t('Recovered')}}</vs-th>
      </template>

      <template slot-scope="{data}">
        <vs-tr :key="indextr" v-for="(tr, indextr) in data">
          <vs-td :data="data[indextr].country_name">{{data[indextr].country_name}}</vs-td>
          <vs-td :data="data[indextr].confirmed">{{data[indextr].confirmed}}</vs-td>
          <vs-td :data="data[indextr].death">{{data[indextr].death}}</vs-td>
          <vs-td :data="data[indextr].cured">{{data[indextr].cured}}</vs-td>
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
  created() {
    axios.get("https://api.covidstatus.com/cases", {}).then(response => {
      this.countries = response.data;
    });
  }
};
</script>
