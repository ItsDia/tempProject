<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="navbar bg-body-tertiary fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">智慧城市服务组合平台</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">智慧城市服务组合平台</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item">
              <router-link to="/ViewView" class="nav-link active">查看服务</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/AddView" class="nav-link">添加服务</router-link>
            </li>
            <!-- <li class=" nav-item"> -->
              <!-- <router-link to="#" class="nav-link">服务组合</router-link> -->
            <!-- </li> -->

          </ul>
        </div>
      </div>
    </div>
  </nav>
  <div style="height: 56px"></div>
  <router-view></router-view>


  
</template>

<style scoped>

</style>