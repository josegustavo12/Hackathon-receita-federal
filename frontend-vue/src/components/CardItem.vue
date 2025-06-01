<template>
  <main
    class="card botao text-white p-3 d-flex flex-column justify-content-between mb-4"
    @click="handleClick"
    style="cursor: pointer; width: 100%; height: 300px;"
  >
    <div v-if="quantidade >= 1" class="d-flex flex-column h-100" style="height: 20%">
      <!-- Topo: Imagem -->
      <div class="placeholder-img mb-3">
        <img src="../assets/logo.png" alt="imagem da logo de exemplo"/>
      </div>

      <!-- Conteúdo: título e subtítulo -->
      <div class="flex-grow-1">
        <h5 class="m-0">{{ title }}</h5>
        <sub class="m-0">{{ description }}</sub>
      </div>

      <!-- Rodapé: quantidade -->
      <footer class="text-start pt-5 pb-0">
        <h6 class="m-0">Quantidade: {{ quantidade }}</h6>
      </footer>
    </div>

    <div v-else class="d-flex flex-column h-100">
      <!-- Topo: Imagem -->
      <div class="placeholder-img mb-3" style="height: 40%">
        <img src="../assets/logo.png" alt="imagem da logo de exemplo" />
      </div>

      <!-- Conteúdo: título e subtítulo -->
      <div class="flex-grow-1"> 
        <h5 class="m-0">{{ title }}</h5>
        <sub class="m-0">{{ resumo }}</sub>
      </div>

      <!-- Rodapé: quantidade -->
      <footer class="text-start pt-5 pb-0">
        <h6 class="m-0">{{ author }}</h6>
      </footer>
    </div>
  </main>
</template>

<script setup>
const props = defineProps({
  title: String,
  description: String,
  author: String,
  date: String,
  quantidade: Number,
  resumo: String,
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
  .placeholder-img {
  background-color: #ccc;
  height: 120px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.placeholder-img img {
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}
</style>