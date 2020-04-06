<!-- =========================================================================================
  File Name: DashboardAnalytics.vue
  Description: Dashboard Analytics
========================================================================================== -->

<template>
  <div>
    <div class="">
      <!-- <h5 class="mb-2">Theme Mode</h5> -->
      <!-- <br /> -->
    </div>


<!--    <a class="Kofi" href='https://ko-fi.com/A0A21J5UF' target='_blank'><img height='36' style='border:0px;height:36px;'-->
<!--                                                                            src='https://az743702.vo.msecnd.net/cdn/kofi5.png?v=2'-->
<!--                                                                            border='0'-->
<!--                                                                            alt='Buy Me a Coffee at ko-fi.com'/></a>-->
    <h2 class="mb-5 title">{{ $t('YourCountry')}} {{ ip.name}}</h2>

    <div class="vx-row">
      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="UsersIcon"
          :statistic="info.confirmed"
          :statisticTitle="$t('TotalInfected')"
        />
      </div>

      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="SmileIcon"
          :statisticTitle="$t('Recovered')"
          :statistic="info.cured"
          color="success"
        />
      </div>


      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="UserXIcon"
          :statistic="info.death"
          :statisticTitle="$t('Deaths')"
          color="danger"
        />
      </div>

      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="UserPlusIcon"
          :statistic="info.new_confirmed"
          :statisticTitle="$t('NewCases')"
        />
      </div>

      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="UserMinusIcon"
          :statistic="info.new_death"
          :statisticTitle="$t('NewDeath')"
          color="danger"
        />
      </div>


      <!--      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">-->
      <!--        <statistics-card-line-->
      <!--          hideChart-->
      <!--          class="mb-base"-->
      <!--          icon="EyeIcon"-->
      <!--          :statistic="(info.confirmed - info.cured - info.death) ? (info.confirmed - info.cured - info.death) : ''"-->
      <!--          :statisticTitle="$t('Active')"-->
      <!--        />-->
      <!--      </div>-->




      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="PercentIcon"
          :statistic="(info.death/info.confirmed*100).toFixed(2)"
          :statisticTitle="$t('Lethality')"
          color="danger"
        />
      </div>



      <!--      <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">-->
      <!--        <statistics-card-line-->
      <!--          hideChart-->
      <!--          class="mb-base"-->
      <!--          icon="AlertCircleIcon"-->
      <!--          :statistic="info.serious"-->
      <!--          :statisticTitle="$t('Serious')"-->
      <!--          color="#"-->
      <!--        />-->
      <!--      </div>-->
    </div>
    <WorldData/>

    <!-- <div class="vx-col w-full mb-base">
      <vx-card :title="$t('LineChart')">
        <vue-apex-charts
          type="area"
          height="350"
          :options="apexChatData.lineAreaChartSpline.chartOptions"
          :series="apexChatData.lineAreaChartSpline.series"
        ></vue-apex-charts>
      </vx-card>
    </div> -->
  </div>
</template>

<script>
  import StatisticsCardLine from "@/components/statistics-cards/StatisticsCardLine.vue";
  import VueApexCharts from "vue-apexcharts";
  import apexChatData from "./apexChartData.js";
  import WorldData from "@/components/WorldData.vue";

  import axios from "axios";


  export default {
    data() {
      return {
        apexChatData: apexChatData,
        ip: [],
        info: {
          confirmed: 0,
          cured: 0,
          death: 0,
          serious: 0
        }
      };
    },
    components: {
      StatisticsCardLine,
      VueApexCharts,
      WorldData
    },
    async beforeMount() {
      await this.getData();
      // console.log(this.ip);
      // console.log(this.ip.country_code);

      let url = "https://api.covidstatus.com/cases/" + this.ip.code;
      // console.log(url);
      axios.get(url, {}).then(response => (this.info = response.data));
    },

    methods: {
      async getData() {
        const getIpResponse = await axios.get("https://api.covidstatus.com/info_about_country");
        this.ip = getIpResponse.data;
        // console.log(this.ip);
      }
    }
  };
</script>

<style scoped>
  .Kofi {
    float: right;
  }
</style>
