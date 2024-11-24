<template>
  <div ref="wordCloud" style="width: 100%; height: 500px"></div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'
import 'echarts-wordcloud'

// 定义 props
const props = defineProps({
  data: {
    type: Array as () => Array<[string, number]>,
    required: true,
  },
})

const wordCloud = ref<HTMLDivElement | null>(null)

const initChart = () => {
  if (!wordCloud.value) return

  const chart = echarts.init(wordCloud.value)

  // 使用 props.data
  const formattedData = props.data.map(([name, value]) => ({ name, value }))

  const options = {
    tooltip: {
      show: true,
    },
    series: [
      {
        type: 'wordCloud',
        shape: 'circle',
        sizeRange: [10, 50],
        rotationRange: [-90, 90],
        textStyle: {
          color: () =>
            `rgb(${Math.random() * 160 + 80}, ${Math.random() * 160 + 80}, ${
              Math.random() * 160 + 80
            })`,
        },
        data: formattedData,
      },
    ],
  }

  chart.setOption(options)

  window.addEventListener('resize', () => chart.resize())
}

// 初始化词云
onMounted(initChart)

// 监听 props.data 的变化
watch(() => props.data, initChart, { deep: true })
</script>

<style scoped>
/* 根据需要调整样式 */
</style>
