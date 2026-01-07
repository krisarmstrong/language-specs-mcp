# Vue.js Patterns & Best Practices (Vue 3 Composition API)

## Component Structure

### Script Setup (Recommended)

```vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import type { User } from '@/types'

// Props with TypeScript
const props = defineProps<{
  userId: string
  showDetails?: boolean
}>()

// Emits with TypeScript
const emit = defineEmits<{
  select: [id: string]
  update: [user: User]
}>()

// Reactive state
const user = ref<User | null>(null)
const loading = ref(false)

// Computed
const displayName = computed(() =>
  user.value ? `${user.value.firstName} ${user.value.lastName}` : ''
)

// Methods
async function loadUser() {
  loading.value = true
  try {
    user.value = await fetchUser(props.userId)
  } finally {
    loading.value = false
  }
}

// Lifecycle
onMounted(() => {
  loadUser()
})
</script>

<template>
  <div class="user-card">
    <span v-if="loading">Loading...</span>
    <template v-else-if="user">
      <h3>{{ displayName }}</h3>
      <button @click="emit('select', user.id)">Select</button>
    </template>
  </div>
</template>
```

## Composables (Reusable Logic)

### Creating Composables

```typescript
// composables/useUser.ts
import { ref, computed, watch } from 'vue'
import type { Ref } from 'vue'

export function useUser(userId: Ref<string>) {
  const user = ref<User | null>(null)
  const loading = ref(false)
  const error = ref<Error | null>(null)

  const fullName = computed(() =>
    user.value ? `${user.value.firstName} ${user.value.lastName}` : ''
  )

  async function fetchUser() {
    loading.value = true
    error.value = null
    try {
      user.value = await api.getUser(userId.value)
    } catch (e) {
      error.value = e as Error
    } finally {
      loading.value = false
    }
  }

  // Auto-fetch when userId changes
  watch(userId, fetchUser, { immediate: true })

  return {
    user,
    fullName,
    loading,
    error,
    refresh: fetchUser,
  }
}

// Usage in component
const userId = ref('123')
const { user, fullName, loading } = useUser(userId)
```

### Composable for Local Storage

```typescript
// composables/useLocalStorage.ts
import { ref, watch } from 'vue'

export function useLocalStorage<T>(key: string, defaultValue: T) {
  const stored = localStorage.getItem(key)
  const data = ref<T>(stored ? JSON.parse(stored) : defaultValue)

  watch(
    data,
    (newValue) => {
      localStorage.setItem(key, JSON.stringify(newValue))
    },
    { deep: true }
  )

  return data
}

// Usage
const theme = useLocalStorage('theme', 'light')
theme.value = 'dark' // Automatically persists
```

## State Management (Pinia)

### Store Definition

```typescript
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // State
  const user = ref<User | null>(null)
  const token = ref<string | null>(null)

  // Getters
  const isAuthenticated = computed(() => !!token.value)
  const displayName = computed(() => user.value?.name ?? 'Guest')

  // Actions
  async function login(credentials: Credentials) {
    const response = await api.login(credentials)
    token.value = response.token
    user.value = response.user
  }

  function logout() {
    token.value = null
    user.value = null
  }

  return {
    user,
    token,
    isAuthenticated,
    displayName,
    login,
    logout,
  }
})

// Usage in component
const userStore = useUserStore()
await userStore.login({ email, password })
```

## Props and Events

### Props Validation

```vue
<script setup lang="ts">
// With defaults
const props = withDefaults(
  defineProps<{
    title: string
    count?: number
    items?: string[]
  }>(),
  {
    count: 0,
    items: () => [],
  }
)
</script>
```

### Custom v-model

```vue
<script setup lang="ts">
const props = defineProps<{
  modelValue: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

// Computed for two-way binding
const value = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val),
})
</script>

<template>
  <input v-model="value" />
</template>
```

## Template Best Practices

### Conditional Rendering

```vue
<template>
  <!-- Use v-if for conditional blocks -->
  <div v-if="status === 'loading'">Loading...</div>
  <div v-else-if="status === 'error'">Error: {{ error.message }}</div>
  <div v-else>{{ data }}</div>

  <!-- Use v-show for frequent toggles -->
  <div v-show="isVisible">Toggled content</div>

  <!-- Use template for grouping without wrapper -->
  <template v-if="showDetails">
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </template>
</template>
```

### List Rendering

```vue
<template>
  <!-- Always use :key with v-for -->
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </ul>

  <!-- Avoid v-if with v-for on same element -->
  <!-- BAD -->
  <li v-for="item in items" v-if="item.active" :key="item.id">
    {{ item.name }}
  </li>

  <!-- GOOD - Filter in computed -->
  <li v-for="item in activeItems" :key="item.id">
    {{ item.name }}
  </li>
</template>

<script setup>
const activeItems = computed(() => items.value.filter((i) => i.active))
</script>
```

## Anti-Patterns to Avoid

### Don't Mutate Props

```vue
<script setup>
// BAD - Mutating prop directly
props.items.push(newItem)

// GOOD - Emit event to parent
emit('add-item', newItem)
</script>
```

### Don't Use Reactive for Primitives

```typescript
// BAD - reactive doesn't work with primitives
const count = reactive(0)

// GOOD - use ref for primitives
const count = ref(0)
```

### Don't Forget to Unsubscribe

```typescript
// BAD - Event listener leaks
onMounted(() => {
  window.addEventListener('resize', handleResize)
})

// GOOD - Clean up in onUnmounted
onMounted(() => {
  window.addEventListener('resize', handleResize)
})
onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// BETTER - Use VueUse composable
import { useEventListener } from '@vueuse/core'
useEventListener(window, 'resize', handleResize) // Auto cleanup
```

### Don't Use Arrow Functions for Methods with `this`

```typescript
// In Options API - BAD
export default {
  methods: {
    handleClick: () => {
      this.count++ // 'this' is undefined!
    },
  },
}

// In Options API - GOOD
export default {
  methods: {
    handleClick() {
      this.count++ // 'this' works correctly
    },
  },
}

// In Composition API - Arrow functions are fine (no 'this')
const handleClick = () => {
  count.value++
}
```
