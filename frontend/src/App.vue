<template>
  <div id="app" class="md-layout">
    <div class="page-container md-layout-item">
      <md-app md-mode="fixed">
        <md-app-toolbar class="md-primary md-dense">
          <div class="md-toolbar-row">
            <!-- MENU ICON ROW-->
            <div class="md-toolbar-section-start">
              <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
                <md-icon>menu</md-icon>
              </md-button>

              <span class="md-title">rdb</span>
            </div>
            <!-- /MENU ICON ROW-->
            <!-- THREE-BUTTON ICON ON THE RIGHT-->
            <div class="md-toolbar-section-end">
              <md-button class="md-icon-button">
                <md-icon>more_vert</md-icon>
              </md-button>
            </div>
            <!-- /THREE-BUTTON ICON ON THE RIGHT-->
          </div>

          <!-- TABS ----------------------------- -->
          <div class="md-layout-item">
            <md-tabs md-sync-route class="md-primary">
              <!-- HOME-->
              <md-tab id="tab-home" md-label="Home" to="/">
                <div class="md-layout-item">
                  <router-view/>
                </div>
              </md-tab>

              <!-- MISC-->
              <md-tab id="tab-histstats" md-label="Stats" to="/stats">
                <div class="md-layout-item">
                  <router-view/>
                </div>
              </md-tab>
            </md-tabs>
          </div>
          <!-- /TABS ---------------------------- -->
        </md-app-toolbar>
        <!-- SLIDING MENU-->
        <md-app-drawer :md-active.sync="menuVisible">
          <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

          <md-list>
            <md-list-item>
              <md-icon>move_to_inbox</md-icon>
              <span class="md-list-item-text">Sign in</span>
            </md-list-item>

            <md-list-item>
              <md-icon>send</md-icon>
              <span class="md-list-item-text">About</span>
            </md-list-item>
          </md-list>
        </md-app-drawer>
        <!-- /SLIDING MENU-->
      </md-app>
    </div>
  </div>
</template>

<script>
import Misc from './components/Misc.vue';
import Home from './components/Home.vue';
import Histstats from './components/Histstats.vue';

export default {
  name: 'App',
  data: () => ({
    menuVisible: false
  }),
  components: {
    Misc,
    Home,
    Histstats
  }
}
</script>

<style lang="scss">
@import "~vue-material/dist/theme/engine";

@include md-register-theme(
  "default",
  (
    primary: md-get-palette-color(blue, A100),
    // The primary color of your application
      accent: md-get-palette-color(red, A100),
    // The accent or secondary color
      theme: dark// This can be dark or light
  )
);

@import "~vue-material/dist/theme/all";
#app {
  height: 100vh;
  font-family: Roboto, sans-serif;
  //font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 0px;
}
</style>
