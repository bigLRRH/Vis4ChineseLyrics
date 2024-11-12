<template>
  <div class="chart-container">
    <!-- 第一个饼图：学历分布 -->
    <div ref="educationChart" class="chart" style="height: 400px"></div>

    <!-- 第二个饼图：城市分布 -->
    <div ref="cityChart" class="chart" style="height: 400px"></div>

    <!-- 第三个饼图：职位分布 -->
    <div ref="positionChart" class="chart" style="height: 400px"></div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import * as echarts from 'echarts'

const educationChart = ref<HTMLDivElement | null>(null)
const cityChart = ref<HTMLDivElement | null>(null)
const positionChart = ref<HTMLDivElement | null>(null)

// 加载数据并生成饼图
const loadData = async () => {
  try {
    const response = await fetch('/data1.json') // 假设 data1.json 存放在 public 目录下
    const data = await response.json()

    // 统计学历分布
    const educationCounts = data.reduce((counts: { [key: string]: number }, item: any) => {
      counts[item.edu] = (counts[item.edu] || 0) + 1
      return counts
    }, {})

    // 统计城市分布
    const cityCounts = data.reduce((counts: { [key: string]: number }, item: any) => {
      const city = item.location.split('-')[0] // 提取城市名（假设城市在位置字段的第一个部分）
      counts[city] = (counts[city] || 0) + 1
      return counts
    }, {})

    // 统计职位分布
    const positionCounts = data.reduce((counts: { [key: string]: number }, item: any) => {
      counts[item.name] = (counts[item.name] || 0) + 1
      return counts
    }, {})

    // 生成图表
    generateEducationChart(educationCounts)
    generateCityChart(cityCounts)
    generatePositionChart(positionCounts)
  } catch (error) {
    console.error('加载数据失败:', error)
  }
}

// 根据学历数据生成学历分布饼图
const generateEducationChart = (educationCounts: { [key: string]: number }) => {
  if (educationChart.value) {
    const chart = echarts.init(educationChart.value)
    const option = {
      title: {
        text: '学历分布',
        subtext: '数据来源于职位招聘',
        left: 'center',
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)',
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: Object.keys(educationCounts),
      },
      series: [
        {
          name: '学历层次',
          type: 'pie',
          radius: '50%',
          data: Object.keys(educationCounts).map((key) => ({
            name: key,
            value: educationCounts[key],
          })),
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)',
            },
          },
        },
      ],
    }

    chart.setOption(option)
  }
}

// 根据城市数据生成城市分布饼图
const generateCityChart = (cityCounts: { [key: string]: number }) => {
  if (cityChart.value) {
    const chart = echarts.init(cityChart.value)
    const option = {
      title: {
        text: '城市分布',
        subtext: '数据来源于职位招聘',
        left: 'center',
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)',
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: Object.keys(cityCounts),
      },
      series: [
        {
          name: '城市分布',
          type: 'pie',
          radius: '50%',
          data: Object.keys(cityCounts).map((key) => ({
            name: key,
            value: cityCounts[key],
          })),
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)',
            },
          },
        },
      ],
    }

    chart.setOption(option)
  }
}

// 根据职位数据生成职位分布饼图
const generatePositionChart = (positionCounts: { [key: string]: number }) => {
  if (positionChart.value) {
    const chart = echarts.init(positionChart.value)
    const option = {
      title: {
        text: '职位分布',
        subtext: '数据来源于职位招聘',
        left: 'center',
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)',
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: Object.keys(positionCounts),
      },
      series: [
        {
          name: '职位分布',
          type: 'pie',
          radius: '50%',
          data: Object.keys(positionCounts).map((key) => ({
            name: key,
            value: positionCounts[key],
          })),
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)',
            },
          },
        },
      ],
    }

    chart.setOption(option)
  }
}

onMounted(() => {
  loadData() // 加载数据并生成饼图
})
</script>

<style scoped>
.chart-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 设置两列布局 */
  grid-template-rows: auto auto; /* 设置两行布局 */
  gap: 40px; /* 设置图表之间的间距 */
  position: relative;
  height: 800px; /* 设置容器高度以适应所有图表 */
}

.chart {
  width: 400px;
  height: 400px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影 */
  border-radius: 8px; /* 圆角 */
  background-color: #fff; /* 背景色 */
  padding: 20px; /* 内边距 */
}

/* 特定位置调整 */
#educationChart {
  grid-column: 1 / 2; /* 放置在第一列 */
  grid-row: 1 / 2; /* 放置在第一行 */
}

#cityChart {
  grid-column: 1 / 2; /* 放置在第一列 */
  grid-row: 2 / 3; /* 放置在第二行 */
}

#positionChart {
  grid-column: 2 / 3; /* 放置在第二列 */
  grid-row: 1 / 2; /* 放置在第一行 */
}
</style>
