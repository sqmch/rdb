<template>
  <div id="app" class="md-layout">
    <div class="page-container md-layout-item">
    <md-app md-mode="fixed">
      <md-app-toolbar class="md-primary">
        <div class="md-toolbar-row ">
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
        <!-- TABS-->
        <div class="md-layout-item">
          <md-tabs md-sync-route class="md-primary ">
            <md-tab  id="tab-home" md-label="Home" to="/">
              <div class="md-layout-item">
                <router-view/>
              </div>
            </md-tab>
            <md-tab id="tab-misc" md-label="Misc" to="/misc">
              <div class="md-layout-item">
                <router-view/>
              </div>
            </md-tab>
          </md-tabs>
        </div>
        <!-- /TABS-->
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
import Misc from './components/Misc.vue'
import Home from './components/Home.vue'

export default {
  name: 'App',
  data: () => ({
    menuVisible: false,
    selected: {}
  }),
  components: {
    Misc,
    Home
  }
}

</script>

<style lang="scss">
#app {
	height: 100vh;
	font-family: Roboto, sans-serif;
	//font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 0px;
}
</style>
<style scoped>
.md-app {
	max-height: 400px;
	border: 1px solid rgba(#000, 0.12);
}

// Demo purposes only
.md-drawer {
	width: 230px;
	max-width: calc(100vw - 125px);
}
</style>
