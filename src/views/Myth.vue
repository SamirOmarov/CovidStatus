<template>
  <div>
    <h2 class="title mb-4">{{ $t("myth")}}</h2>
    <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('antibiotics')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/myth/antibiotic-resistant.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("antibioticsRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("steroidsRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/2019-novel-coronavirus-myth-versus-fact"
                    >{{ $t("source") }}</a>
                  </td>
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("sprayAlcoholRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("ibuprofenRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.nytimes.com/2020/03/17/health/coronavirus-ibuprofen.html"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("StayinTouch") }}</td>
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("hotBathRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("pneumoniaVaccinesRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("eatGarlicRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("waterNoseRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("vaccineComingRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/2019-novel-coronavirus-myth-versus-fact"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("coldWeatherRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("hotWeatherRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("petSpreadRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/animals.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fprepare%2Fanimals.html"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("chloroquinePreventRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://wellcome.ac.uk/news/can-chloroquine-prevent-coronavirus-disease-only-research-will-give-us-answer?utm_source=twitter&utm_medium=o-wellcome"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("holdBreathRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.snopes.com/fact-check/taiwan-experts-self-check/?collection-id=241238"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>-->
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
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4">
              <table>
                <tr>
                  <td class="data">{{ $t("infectionAgainRes") }}</td>
                </tr>
                <tr>
                  <td class="sources">
                    <a
                      href="https://www.snopes.com/fact-check/covid-19-reinfection/?collection-id=241238"
                    >{{ $t("source") }}</a>
                  </td>
                </tr>
                <!-- <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>-->
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

.sources {
  font-family: "Roboto", sans-serif;
  font-size: 15px;
}
</style>