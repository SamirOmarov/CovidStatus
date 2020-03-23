<template>
  <div>
    <h2 class="title mb-4">How to Protect Yourself and Others</h2>
    <div class="vx-row">
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('Spreads')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4 " id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/Spreads.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("Transmission") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("Transmission2") }}</td>
                </tr>
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('CleanHands')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/clean.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("Wash") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("Sanitizer") }}</td>
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
        <vx-card :title="$t('Avoid')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/StayHome.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("ProtectYourself1") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("ProtectYourself2") }}</td>
                </tr>
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('Stay')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/RestHome.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("StayHome") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("StayinTouch") }}</td>
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
        <vx-card :title="$t('ProtectOthers')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/Cover.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("Cover") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("Cover2") }}</td>
                </tr>
              </table>
            </div>
            <!-- /Information - Col 1 -->
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full xl:w-1/2">
        <vx-card :title="$t('MaskTitle')" class="mb-base">
          <!-- Avatar -->
          <div class="vx-row">
            <!-- Avatar Col -->
            <div class="vx-col sm:w-2/5 md:w-1/4 lg:w-1/4 xl:w-1/4" id="avatar-col">
              <div class="img-container mb-4">
                <img src="@/assets/images/protection/Facemask.png" class="rounded wRound" />
              </div>
            </div>

            <!-- Information - Col 1 -->
            <div class="vx-col sm:w-3/5 md:w-3/4 lg:w-3/4 xl:w-3/4 ">
              <table>
                <tr>
                  <td class="data">⚫ {{ $t("Mask") }}</td>
                </tr>
                <tr>
                  <td class="data">⚫ {{ $t("Mask2") }}</td>
                </tr>
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

    <h2 class="title mb-4">Symptoms</h2>

    <div class="flex flex-wrap mb-10">
      <div class="w-1/4 ml-auto">
        <div class="img-container mb-4">
          <img src="@/assets/images/protection/symptoms-cough.png" class="rounded symptom" />
        </div>
      </div>

      <div class="w-1/4 ml-auto">
        <div class="img-container mb-4">
          <img src="@/assets/images/protection/symptoms-fever.png" class="rounded symptom" />
        </div>
      </div>

      <div class="w-1/4 ml-auto">
        <div class="img-container mb-4">
          <img
            src="@/assets/images/protection/symptoms-shortnessOfBreath.png"
            class="rounded symptom"
          />
        </div>
      </div>
    </div>

    <div class="vx-col w-full">
      <vx-card>
        <p class="dataTitle">{{$t("emergency") }}</p>
        <table>
          <tr>
            <td class="data">● {{ $t("breath") }}</td>
          </tr>
          <tr>
            <td class="data">● {{ $t("chest") }}</td>
          </tr>
          <tr>
            <td class="data">● {{ $t("confusion") }}</td>
          </tr>
          <tr>
            <td class="data">● {{ $t("lips") }}</td>
          </tr>
        </table>
      </vx-card>
    </div>
  </div>
</template>


<style scoped>
.wRound {
  width: 60%;
}
.symptom {
  width: 50%;
}
</style>