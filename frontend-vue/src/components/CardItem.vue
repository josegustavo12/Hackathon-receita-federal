<template>
  <div
    class="card botao text-white p-3 d-flex flex-column justify-content-between"
    @click="handleClick"
    style="cursor: pointer; width: 100%; max-width: 270px; height: 300px;"
    >

    <div v-if="type === 'componente'">
      <!-- Imagem simulada -->
      <div class="placeholder-img mb-3"></div>

      <!-- Título e quantidade -->
      <div class="d-flex justify-content-between align-items-center">
        <span>{{ title }}</span>
        <small>{{ quantidade || '—' }}</small>
      </div>

      <!-- Descrição centralizada -->
      <p class="text-center mt-3 fs-5">{{ description }}</p>
    </div>

    <div v-else>
      <h5>{{ title }}</h5>
      <p>{{ description }}</p>
      <p>
        <small>{{ author }}<br />{{ date }}</small>
      </p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  description: String,
  author: String,
  date: String,
  quantidade: Number,
  type: {
    type: String,
    default: 'componente',
  },
})

const emit = defineEmits(['open'])

function handleClick() {
  emit('open', { ...props })
}
</script>

<style scoped>
.botao {
  background-color: #00205b;
  color: #fff;
  border: 1px solid #00205b;
  transition: background-color 0.2s ease;
  border-radius: 16px;
}

.botao:hover {
  background-color: rgba(0, 32, 91, 0.8);
  border-color: rgba(0, 32, 91, 0.8);
}

.placeholder-img {
  background-color: #ccc;
  height: 120px;
  border-radius: 8px;
}
</style>