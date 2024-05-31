<script setup>
import { ref, reactive, watch } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import axios from 'axios';
import { useRouter } from 'vue-router';

const serviceOptions = [
    { value: 's1', label: '用户验证服务' },
    { value: 's2', label: '车辆验证服务' },
    { value: 's3', label: '订单派送服务' },
    { value: 's4', label: '路径规划服务' },
    { value: 's5', label: '费用计算服务' },
    { value: 's6', label: '货币兑换服务' },
];

let selectedService = ref('');
let form = reactive({});
let isLast = ref(false);
let router = useRouter();

watch(selectedService, (newService) => {
    if (newService) {
        generateInputs(newService).forEach(input => {
            form[input.name] = '';
        });
    }
});

const generateInputs = (service) => {
    const labels = {
        s1: [{ name: 'userN', label: '用户姓名' }, { name: 'userFV', label: '用户面部视频' }, { name: 'userID', label: '用户ID' }],
        s2: [{ name: 'vehicleCV', label: '车辆视频' }, { name: 'vehicleID', label: '车辆ID' }],
        s3: [{ name: 'userID', label: '用户ID' }, { name: 'vehicleID', label: '车辆ID' }, { name: 'pNname', label: '乘客姓名' }, { name: 'pPhone,', label: '手机号' }, { name: 'origin', label: '出发地' }, { name: 'des', label: '目的地' }],
        s4: [{ name: 'origin', label: '出发地' }, { name: 'des', label: '目的地' }, { name: 'route', label: '路线' }, { name: 'time', label: '预估时间' }],
        s5: [{ name: 'userN', label: '出发地' }, { name: 'des', label: '目的地' }, { name: 'cost', label: '费用' }],
        s6: [{ name: 'cost', label: '费用' }, { name: 'USD', label: '美元' }, { name: 'EUR', label: '欧元' }, { name: 'newCost', label: '转换汇率后的金额' }],
    };
    return labels[service];
};

const handleSubmit = () => {
    try {
        console.log(selectedService.value, JSON.parse(JSON.stringify(form)));
        ElMessage({
            message: '服务已提交',
            type: 'success',
        });
        ElMessageBox.confirm(
            '是否是继续增加服务？',
            '提示',
            {
                confirmButtonText: '是',
                cancelButtonText: '否',
                type: 'warning',
            }
        ).then(() => {
            isLast.value = true;
        }).catch(() => {
            isLast.value = false;
            setTimeout(() => {
                router.push('/ViewView');
            }, 2000);
        });

        axios.post('/submit', form).then(res => {
            console.log(res);
        }).catch(err => {
            console.error('提交服务时出错:', err);
            ElMessage({
                message: '提交服务时出错',
                type: 'error',
            })
        });
        selectedService.value = '';
        for (const key in form) {
            delete form[key];
        }
    }
    catch (err) {
        console.error('提交服务时出错:', err);
        ElMessage({
            message: '提交服务时出错',
            type: 'error',
        });
    }
};

</script>

<template>
    <div class="container"><el-form :model="form" label-width="auto" style="max-width: 600px;">
            <el-form-item label="服务类型">
                <el-select v-model="selectedService" placeholder="请选择服务类型" clearable>
                    <el-option v-for="service in serviceOptions" :key="service.value" :label="service.label"
                        :value="service.value" />
                </el-select>
            </el-form-item>

            <div v-if="selectedService">
                <el-form-item v-for="(input, index) in generateInputs(selectedService)" :key="index"
                    :label="input.label">
                    <el-input v-model="form[input.name]" />
                </el-form-item>
            </div>

            <el-form-item>
                <el-button type="primary" @click="handleSubmit">提交</el-button>
            </el-form-item>
        </el-form></div>
</template>



<style scoped>
.container {
    margin: auto;
}
</style>
