<template>
  <vs-dropdown vs-custom-content vs-trigger-click class="cursor-pointer">
    <span class="cursor-pointer flex items-center i18n-locale">
      <img class="h-4 w-5" :src="i18n_locale_img" :alt="$i18n.locale" />
      <span class="hidden sm:block ml-2">{{ getCurrentLocaleData.lang }}</span>
    </span>
    <vs-dropdown-menu class="w-48 i18n-dropdown vx-navbar-dropdown">
      <vs-dropdown-item @click="updateLocale('en')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/en.png" alt="en" /> &nbsp;English
      </vs-dropdown-item>
      <vs-dropdown-item @click="updateLocale('fr')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/fr.png" alt="fr" /> &nbsp;French
      </vs-dropdown-item>
      <vs-dropdown-item @click="updateLocale('de')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/de.png" alt="de" /> &nbsp;German
      </vs-dropdown-item>
      <vs-dropdown-item @click="updateLocale('ru')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/ru.png" alt="ru" /> &nbsp;Русский 
      </vs-dropdown-item>
      <vs-dropdown-item @click="updateLocale('tr')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/tr.png" alt="tr" /> &nbsp;Türkçe
      </vs-dropdown-item>
      <vs-dropdown-item @click="updateLocale('az')">
        <img class="h-4 w-5 mr-1" src="@/assets/images/flags/az.png" alt="tr" /> &nbsp;Azərbaycanca
      </vs-dropdown-item>
    </vs-dropdown-menu>
  </vs-dropdown>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      ip: []
    };
  },
  computed: {
    i18n_locale_img() {
      return require(`@/assets/images/flags/${this.$i18n.locale}.png`);
    },
    getCurrentLocaleData() {
      const locale = this.$i18n.locale;

      if (locale == "en") return { flag: "us", lang: "English" };
      else if (locale == "ru") return { flag: "ru", lang: "Русский" };
      else if (locale == "fr") return { flag: "fr", lang: "French" };
      else if (locale == "de") return { flag: "de", lang: "German" };
      else if (locale == "tr") return { flag: "tr", lang: "Türkçe" };
      else if (locale == "az") return { flag: "az", lang: "Azərbaycanca" };
    }
  },
  methods: {
    updateLocale(locale) {
      this.$i18n.locale = locale;
    },
    async getData() {
      const getIpResponse = await axios.get("http://api.covidstatus.com/info_about_country");
      this.ip = getIpResponse.data;
      // console.log(this.ip);
    }
  },
  async mounted() {
    await this.getData();
    this.updateLocale(this.ip.code.toLowerCase());
  }
};
</script>
