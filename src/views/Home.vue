<!-- =========================================================================================
  File Name: DashboardAnalytics.vue
  Description: Dashboard Analytics
========================================================================================== -->

<template>
  <div >
      <WorldData />

    <h2 class="mt-5 mb-5 title">{Country} Status</h2>
    
    <div class="vx-row">
            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
            
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="EyeIcon"
                  statistic="36.9k"
                  statisticTitle="Active" />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="SmileIcon"
                  statisticTitle="Recovered"
                  statistic="12k"
                  color='success' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="XIcon"
                  statistic="978"
                  statisticTitle="Deaths"
                  color='warning' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="PercentIcon"
                  statistic="6.8%"
                  statisticTitle="Lethality"
                  color='danger' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="InfoIcon"
                  statistic="689"
                  statisticTitle="Total Infected"
                  color='warning' />
            </div>

            <div class="vx-col w-1/2 md:w-1/3 xl:w-1/6">
                <statistics-card-line
                  hideChart
                  class="mb-base"
                  icon="AlertCircleIcon"
                  statistic="2"
                  statisticTitle="Serious"
                  color='#'/>
            </div>
        </div>
        
    <div class="vx-col  w-full mb-base">
        <vx-card title="Line Area Chart of Covid-19">
          <vue-apex-charts
            type="area"
            height="350"
            :options="apexChatData.lineAreaChartSpline.chartOptions"
            :series="apexChatData.lineAreaChartSpline.series"
          ></vue-apex-charts>
          
        </vx-card>
      </div>
  </div>
</template>

<script>
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
import VueApexCharts from "vue-apexcharts";
import apexChatData from "./apexChartData.js";
import WorldData from '@/components/WorldData.vue'

export default{
    data() {
    return {
      apexChatData: apexChatData
    };
  },
    components: {
        StatisticsCardLine,
        VueApexCharts,
        WorldData
    },

}

</script>


