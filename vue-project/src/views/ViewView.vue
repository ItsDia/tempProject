<script setup>
import axios from 'axios';
import * as echarts from "echarts";
import { ref, onMounted } from 'vue';

let showData = ref(null);
let _data = ref([]);
let _link = ref([]);
function init() {
    axios.get("/test.json").then(res => {
        if (res.data && Array.isArray(res.data)) {
            _data.value = res.data.map(item => item.service);
            _link.value = res.data.map(item => item.links);
        }
        // 列出服务
        const chartDom = showData.value;
        if (!chartDom) {
            console.error('未找到 showData DOM 元素');
            return;
        }

        const myChart = echarts.init(chartDom);

        const option = {
            title: {
                text: "",
            },
            tooltip: {},
            animationDurationUpdate: 1500,
            animationEasingUpdate: "quinticInOut",
            series: [
                {
                    type: "graph",
                    layout: "none",
                    symbolSize: 50,
                    roam: true,
                    label: {
                        show: true,
                    },
                    edgeSymbol: ["circle", "arrow"],
                    edgeSymbolSize: [4, 10],
                    edgeLabel: {
                        fontSize: 20,
                    },
                    data: _data.value,
                    links: _link.value,
                    lineStyle: {
                        opacity: 0.9,
                        width: 2,
                        curveness: 0,
                    },
                },
            ],
        };
        option && myChart.setOption(option);
    }).catch(err => {
        console.log('axios获取数据时出错:', err);
    });

}

onMounted(async () => {
    init();
});
</script>

<template>
    <div ref="showData" class="echarts"></div>
</template>

<style scoped>


.echarts {
    width: 100vw;
    height: 100vh;
    /* border: black 1px solid; */
}
</style>
