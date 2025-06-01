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
          :key="item.Id || index"
        >
          <!-- Passamos todas as props de item para CardItem -->
          <CardItem
            :type="item.Tipo"
            :title="item.Nome"
            :description="`${item.Marca} ${item.Modelo}`"
            :quantidade="item.Quantidade"
            :author="item.Author || ''"
            :date="item.Date || ''"
            @open="openModal(item)"
          />
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content p-4 text-white">
        <h4>{{ modalData.title }}</h4>
        <p class="mb-2" style="font-size: 1.1rem">
          {{ modalData.description }}
        </p>
        <p v-if="modalData.author">
          <strong>{{ modalData.author }}</strong><br />
          <small>{{ modalData.date }}</small>
        </p>
        <button class="btn btn-light mt-3" @click="closeModal">
          Fechar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import CardItem from '../components/CardItem.vue'

const selectedTab = ref('componente')
const searchTerm = ref('')
const showModal = ref(false)
const modalData = ref({})

// Agora `cards` será preenchido via GET axios
const cards = ref([])

async function fetchCards() {
  try {
    // Requisição GET para /inventario/ (baseURL configurada em main.js)
    const response = await axios.get('/inventario/')
    // `response.data` é um array de InventarioRequest
    // Exemplo de InventarioRequest:
    // {
    //   Id: "7025d50ea5254df59821ece43e2b9cdf",
    //   Nome: "Teclado",
    //   Tipo: "Periférico",
    //   Marca: "Logitech",
    //   Modelo: "K120",
    //   Quantidade: 5,
    //   Bateria: "",
    //   Coil: "",
    //   Reservatorio: "",
    //   Sensores: "",
    //   Circuito: "",
    //   Outros: "",
    //   Data: "2025-06-01T14:23:00"
    // }
    cards.value = response.data
  } catch (err) {
    console.error('Erro ao buscar itens do inventário:', err)
  }
}

onMounted(() => {
  fetchCards()
})

const filteredCards = computed(() => {
  // Filtra pelo tipo “componente” ou “solucao” (ajuste conforme seu campo Tipo)
  // e pelo título (campo Nome)
  return cards.value
    .filter((card) => {
      // Se quiser mapear distintos tipos de abas, você pode usar:
      // - Aba “componente” => card.Tipo === "Componente"
      // - Aba “solucao”   => card.Tipo === "Solução"
      // No exemplo original o Tipo vem como “Periférico”, “Outro”, etc.
      // Ajuste essa lógica caso queira uma correspondência exata ou coloque 
      // uma propriedade adicional no backend para designar tipo “componente” 
      // ou “solucao”.
      // Aqui, para continuar o exemplo, vamos assumir que:
      //   Tipo "Componentes" contém a substring "Comp" e 
      //   Tipo "Soluções" contém a substring "Sol".
      const typeNormalized = card.Tipo.toLowerCase()
      const matchesTab =
        (selectedTab.value === 'componente' &&
          typeNormalized.includes('comp')) ||
        (selectedTab.value === 'solucao' &&
          typeNormalized.includes('sol'))
      const matchesSearch = card.Nome.toLowerCase().includes(searchTerm.value.toLowerCase())
      return matchesTab && matchesSearch
    })
    .map((card) => {
      // Mapeia os campos do InventarioRequest para as props que o CardItem espera
      return {
        Id: card.Id,
        type: selectedTab.value,
        title: card.Nome,
        description: `${card.Marca} ${card.Modelo}`,
        quantidade: card.Quantidade,
        author: card.Author || '', // se não existir, deixa string vazia
        date: card.Data || '', // se não existir, deixa string vazia
      }
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
