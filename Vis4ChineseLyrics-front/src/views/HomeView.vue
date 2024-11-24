<template>
  <div class="fullscreen-container">
    <WordCloud :data="wordCloudData" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import WordCloud from '@/components/WordCloud.vue'

// 定义响应式数据
const wordCloudData = ref<Array<[string, number]>>([])

onMounted(async () => {
  try {
    const response = await fetch('/word_freq.json')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    // 解析 JSON 数据并加载前 200 项
    const json = await response.json()
    wordCloudData.value = json
      .filter((item: any) => Array.isArray(item) && item.length === 2)
      .slice(0, 200)
      .map((item: [string, number]) => [String(item[0]), Number(item[1])] as [string, number])
  } catch (error) {
    console.error('Failed to load word_freq.json:', error)
  }
})
</script>

<style scoped>
/* 全屏容器样式 */
.fullscreen-container {
  width: 100vw; /* 占满屏幕宽度 */
  height: 100vh; /* 占满屏幕高度 */
  display: flex; /* 居中对齐支持 */
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 防止溢出滚动 */
}

/* WordCloud 组件内部样式可以单独定义 */
</style>
