<script setup lang="ts">
import { ref } from 'vue'
import { api } from '../api'

const emit = defineEmits<{(e:'done'): void}>()
const name = ref('')
const handle = ref('')
const avatar = ref<File | null>(null)
const checking = ref(false)
const handleAvailable = ref<boolean | null>(null)

async function checkHandle() {
  if (!handle.value) return
  checking.value = true
  const res = await api(`/handles/check?handle=${encodeURIComponent(handle.value)}`)
  handleAvailable.value = res.available
  checking.value = false
}

async function uploadAvatarIfAny(file?: File) {
  if (!file) return undefined
  const up = await api('/uploads/avatar-url', {
    method: 'POST',
    body: JSON.stringify({ contentType: file.type })
  })
  await fetch(up.uploadUrl, { method: 'PUT', body: file })
  return up.publicUrl as string
}

async function submit() {
  await checkHandle()
  if (handleAvailable.value === false) return alert('Handle zauzet')
  const avatarUrl = await uploadAvatarIfAny(avatar.value || undefined)
  await api('/onboarding/profile', {
    method: 'PATCH',
    body: JSON.stringify({ name: name.value, handle: handle.value, avatarUrl })
  })
  emit('done')
}
</script>

<template>
  <form class="space-y-4" @submit.prevent="submit">
    <label class="block">
      <span>Ime</span>
      <input class="mt-1 w-full border p-2" v-model="name" required />
    </label>
    <label class="block">
      <span>Handle</span>
      <input class="mt-1 w-full border p-2" v-model="handle" required pattern="^[a-z0-9_]{3,20}$" @blur="checkHandle" />
      <small class="text-gray-500">
        <template v-if="checking">Provjera...</template>
        <template v-else-if="handle">@{{ handle }} <span v-if="handleAvailable === false" style="color:#c00">zauzet</span></template>
      </small>
    </label>
    <label class="block">
      <span>Profilna slika</span>
      <input type="file" accept="image/*" @change="(e: { target: HTMLInputElement; }) => avatar = (e.target as HTMLInputElement).files?.[0] || null" />
    </label>
    <button class="mt-4 rounded border px-4 py-2" type="submit">Spremi i nastavi</button>
  </form>
</template>
