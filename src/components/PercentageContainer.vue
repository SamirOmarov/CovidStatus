<template>
  <div class="container">
    <PercChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import PercChart from "@/components/charts/Percentage.vue";


export default {
  name: 'PercChartContainer',
  components: { PercChart },
  data: () => ({
    loaded: false,
    chartdata: null
  }),
  async mounted () {
    this.loaded = false
    try {
      const { datalist } = await fetch('api/datalist/percentage',
      )
      this.chartdata = datalist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}

</script>