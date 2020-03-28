<!-- =========================================================================================
  File Name: TheNavbar.vue
  Description: Navbar component
  Component Name: TheNavbar
============================= -->


<template>
  <div class="relative">
    <div class="vx-navbar-wrapper" :class="classObj">
      <vs-navbar
        class="vx-navbar navbar-custom navbar-skelton"
        :color="navbarColorLocal"
        :class="textColor"
      >
        <!-- SM - OPEN SIDEBAR BUTTON -->
        <feather-icon
          class="sm:inline-flex xl:hidden cursor-pointer p-2"
          icon="MenuIcon"
          @click.stop="showSidebar"
        />

        <!-- <bookmarks :navbarColor="navbarColor" v-if="windowWidth >= 992" /> -->
        <img class="logoid sm:inline-flex xl:hidden cursor-pointer p-2" src="@/assets/images/logo/logoCovid.png" alt="ru" />

        <vs-spacer />
        <i18n />

        <div>
          <vs-radio
            v-model="themeMode"
            vs-value="light"
            class="mr-4 ml-4 mt-2"
            vs-name="theme-mode-light"
          >
            <featherIcon icon="SunIcon" />
          </vs-radio>
          <vs-radio v-model="themeMode" vs-value="dark" class="mt-2 mr-4" vs-name="theme-mode-dark">
            <featherIcon icon="MoonIcon" />
          </vs-radio>
        </div>
      </vs-navbar>
    </div>
  </div>
</template>


<script>
// import Bookmarks            from "./components/Bookmarks.vue"
// import SearchBar            from "./components/SearchBar.vue"
// import NotificationDropDown from "./components/NotificationDropDown.vue"
// import ProfileDropDown      from "./components/ProfileDropDown.vue"
import I18n from "./components/I18n.vue";
import featherIcon from "@/components/FeatherIcon.vue";

export default {
  name: "the-navbar-vertical",
  props: {
    navbarColor: {
      type: String,
      default: "#fff"
    }
  },
  components: {
    // Bookmarks,
    // SearchBar,
    // NotificationDropDown,
    // ProfileDropDown,
    I18n,
    featherIcon
  },
  computed: {
    themeMode: {
      get() {
        return this.$store.state.theme;
      },
      set(val) {
        this.$store.dispatch("updateTheme", val);
      }
    },
    navbarColorLocal() {
      return this.$store.state.theme === "dark" && this.navbarColor === "#fff"
        ? "#10163a"
        : this.navbarColor;
    },
    verticalNavMenuWidth() {
      return this.$store.state.verticalNavMenuWidth;
    },
    textColor() {
      return {
        "text-white":
          (this.navbarColor != "#10163a" &&
            this.$store.state.theme === "dark") ||
          (this.navbarColor != "#fff" && this.$store.state.theme !== "dark")
      };
    },
    windowWidth() {
      return this.$store.state.windowWidth;
    },

    // NAVBAR STYLE
    classObj() {
      if (this.verticalNavMenuWidth == "default") return "navbar-default";
      else if (this.verticalNavMenuWidth == "reduced") return "navbar-reduced";
      else if (this.verticalNavMenuWidth) return "navbar-full";
    }
  },
  methods: {
    showSidebar() {
      this.$store.commit("TOGGLE_IS_VERTICAL_NAV_MENU_ACTIVE", true);
    }
  }
};
</script>

<style scoped>
.logoid{
  max-width: 55px;
}
</style>