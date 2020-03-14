<template>
  <div>
    <h2 class="title mt-5 mb-10">COVID-19 STATUS</h2>
    <div class="vx-row">
      <div class="vx-col md:w-1/2 w-full mb-base">
        <vx-card title="Seriousness of symptoms">
          <symptoms />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 w-full mb-base">
        <vx-card title="Worldwide percentage status">
          <percentage />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 w-full mb-base">
        <vx-card title="Risk groups by age">
          <risk />
        </vx-card>
      </div>

      <div class="vx-col md:w-1/2 w-full mb-base">
        <vx-card title="Preconditions">
          <illness />
        </vx-card>
      </div>
    </div>
  </div>
</template>

<script>
import symptoms from "@/components/SymptomsContainer.vue";
import percentage from "@/components/PercentageContainer.vue";
import illness from "@/components/PercentageContainer.vue";
import risk from "@/components/PercentageContainer.vue";

export default {
  components: {
    symptoms,
    percentage,
    illness,
    risk
  }
};
</script>