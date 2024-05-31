<script setup>

</script>

<template>
    <div class="container">
        <!-- <div class="card" style="width: 20rem;">
            <div class="card-body">
                <router-link to="/ViewView" class="nav-link card-text">查看服务</router-link>
            </div>
        </div> -->
        <div class="card" style="width: 20rem;">
            <div class="card-body">
                <router-link to="/AddView" class="nav-link card-text">添加服务</router-link>
            </div>
        </div>
        <!-- <div class="card" style="width: 20rem;">
            <div class="card-body">
                <router-link to="" class="nav-link card-text">服务组合</router-link>
            </div>
        </div> -->
    </div>
</template>

<style scoped>
.card {
    margin: 10%;
}

.card-body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.card-text {
    text-align: center;
}
</style>