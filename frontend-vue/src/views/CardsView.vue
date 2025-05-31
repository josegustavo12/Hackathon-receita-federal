<template>
  <div class="container">
    <!-- Filtro e Pesquisa -->
    <div class="my-4">
      <div class="row align-items-center g-2">
        <!-- Campo de pesquisa (8 colunas) -->
        <div class="col-md-8">
          <input
            type="text"
            class="form-control"
            v-model="searchTerm"
            placeholder="Pesquisar por título..."
          />
        </div>

        <!-- Botões (4 colunas) -->
        <div class="col-md-4 d-flex gap-2">
          <button
            class="tab-button flex-fill"
            :class="{ active: selectedTab === 'componente' }"
            @click="selectedTab = 'componente'"
          >
            Componentes
          </button>
          <button
            class="tab-button flex-fill"
            :class="{ active: selectedTab === 'solucao' }"
            @click="selectedTab = 'solucao'"
          >
            Soluções
          </button>
        </div>
      </div>
    </div>

    <!-- Cards -->
    <div>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4">
        <div
          class="col d-flex justify-content-center"
          v-for="(item, index) in filteredCards"
          :key="index"
        >
          <CardItem v-bind="item" @open="openModal" />
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content p-4 text-white">
        <h4>{{ modalData.title }}</h4>
        <p class="mb-2" style="font-size: 1.1rem">{{ modalData.description }}</p>
        <p v-if="modalData.author">
          <strong>{{ modalData.author }}</strong><br />
          <small>{{ modalData.date }}</small>
        </p>
        <button class="btn btn-light mt-3" @click="closeModal">Fechar</button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue'
import CardItem from '../components/CardItem.vue'

const selectedTab = ref('componente')
const searchTerm = ref('')
const showModal = ref(false)
const modalData = ref({})

const cards = [
  {
    type: 'componente',
    title: 'Botão Primário',
    description: 'Um botão com cor padrão e bordas arredondadas.',
    quantidade: 10
  },
  {
    type: 'componente',
    title: 'Input Texto',
    description: 'Campo de texto simples com label flutuante.',
    quantidade: 14
  },
  {
    type: 'solucao',
    title: 'Sistema de Login',
    description: 'Login com autenticação via JWT.',
    author: 'João Silva',
    date: '30/05/2025',
  },
  {
    type: 'solucao',
    title: 'Painel de Admin',
    description: 'Dashboard com gráficos e métricas.',
    author: 'Maria Santos',
    date: '28/05/2025',
  },
]

const filteredCards = computed(() => {
  return cards.filter((card) => {
    const matchesTab = card.type === selectedTab.value
    const matchesSearch = card.title.toLowerCase().includes(searchTerm.value.toLowerCase())
    return matchesTab && matchesSearch
  })
})

function openModal(data) {
  modalData.value = data
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}
</script>


<style scoped>
.tab-button {
  background-color: transparent;
  border: 2px solid #00205b;
  color: #00205b;
  font-weight: bold;
  padding: 6px 16px;
  border-radius: 8px;
  transition: all 0.2s ease-in-out;
}
.tab-button:hover {
  background-color: rgba(0, 32, 91, 0.1);
}
.tab-button.active {
  background-color: #00205b;
  color: #fff;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1050;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: #00205b;
  border-radius: 12px;
  max-width: 400px;
  width: 90%;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}
</style>