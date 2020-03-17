<template>
  <div>
    <h2 class="title mt-5 mb-10">COVID-19 STATUS</h2>
    <div class="vx-row">
      <div class="vx-col md:w-1/2 xl:w-1/4 w-full mb-base">
        <vx-card :title="$t('Symptoms')">
          <symptoms />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 xl:w-1/4 w-full mb-base">
        <vx-card :title="$t('WorldWidePercentage')">
          <percentage />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 xl:w-1/4 w-full mb-base">
        <vx-card :title="$t('Preconditions')">
          <risk />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 xl:w-1/4 w-full mb-base">
        <vx-card :title="$t('RiskGroup')">
          <illness />
        </vx-card>
      </div>
    </div>
  </div>
</template>

<script>
import symptoms from "@/components/SymptomsContainer.vue";
import percentage from "@/components/PercentageContainer.vue";
import illness from "@/components/RiskDataContainer.vue";
import risk from "@/components/IlnessDataContainer.vue";




export default {
  components: {
    symptoms,
    percentage,
    illness,
    risk
  }
};
</script>