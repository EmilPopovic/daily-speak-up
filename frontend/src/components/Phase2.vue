<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '../api'

const emit = defineEmits<{(e:'done'): void}>()
type Interest = { slug: string; label: string }

const catalog = ref<Interest[]>([])
const picked = ref<string[]>([])

onMounted(async () => {
  try {
    catalog.value = await api('/interests', { method: 'GET' })
  } catch {
    catalog.value = [
      { slug: 'javascript', label: 'JavaScript' },
      { slug: 'react', label: 'React' },
      { slug: 'ai-ml', label: 'AI/ML' },
      { slug: 'devops', label: 'DevOps' },
    ]
  }
})

function toggle(slug: string) {
  picked.value = picked.value.includes(slug)
    ? picked.value.filter(s => s !== slug)
    : [...picked.value, slug]
}

async function save() {
  await api('/onboarding/interests', {
    method: 'PATCH',
    body: JSON.stringify({ interests: picked.value })
  })
  emit('done')
}
</script>

<template>
  <div>
    <div class="grid grid-cols-2 gap-3">
      <button
        v-for="i in catalog"
        :key="i.slug"
        @click="toggle(i.slug)"
        class="border rounded px-3 py-2 text-left"
        :class="picked.includes(i.slug) ? 'bg-black text-white' : ''"
      >
        {{ i.label }}
      </button>
    </div>
    <button :disabled="picked.length === 0" @click="save" class="mt-4 rounded border px-4 py-2">
      Završetak
    </button>
  </div>
</template>
