<template>
  <div>
    <h2 class="title mb-4">{{ $t("myth")}}</h2>
    <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('antibiotics')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4 " id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/antibiotic-resistant.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("antibioticsRes") }}</td>
                </tr>
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('steroids')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/steroid.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("steroidsRes") }}</td>
                </tr>
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>

    <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('sprayAlcohol')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/spray.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("sprayAlcoholRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("ProtectYourself2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('ibuprofen')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/drug.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("ibuprofenRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("StayinTouch") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>

    <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('hotBath')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/baby-tub.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("hotBathRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('pneumoniaVaccines')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/vaccine (1).png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("pneumoniaVaccinesRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr> -->
                <!-- <tr>
              <td>{{ $t("WorldStatus") }}</td>
                </tr>-->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>

      <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('eatGarlic')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/garlic.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("eatGarlicRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('waterNose')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/nasal-spray.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("waterNoseRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr> -->
                <!-- <tr>
              <td>{{ $t("WorldStatus") }}</td>
                </tr>-->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>

      <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('vaccineComing')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/vaccine.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("vaccineComingRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('coldWeather')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/snow.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("coldWeatherRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr> -->
                <!-- <tr>
              <td>{{ $t("WorldStatus") }}</td>
                </tr>-->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>

      <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('hotWeather')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/hot.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("hotWeatherRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('petSpread')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/cat.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("petSpreadRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr> -->
                <!-- <tr>
              <td>{{ $t("WorldStatus") }}</td>
                </tr>-->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>
      <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('chloroquinePrevent')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/malar.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("chloroquinePreventRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('holdBreath')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/lung.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("holdBreathRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr> -->
                <!-- <tr>
              <td>{{ $t("WorldStatus") }}</td>
                </tr>-->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
    </div>
      <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('infectionAgain')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/sick.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data"> {{ $t("infectionAgainRes") }}</td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr> -->
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      
    </div>

   
  </div>
</template>


<style scoped>
.wRound {
  width: 40%;
}
.symptom {
  width: 50%;
}
</style>