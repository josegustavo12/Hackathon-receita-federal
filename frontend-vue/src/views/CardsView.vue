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
            @click="selectTab('componente')"
          >
            Componentes
          </button>
          <button
            class="tab-button flex-fill"
            :class="{ active: selectedTab === 'solucao' }"
            @click="selectTab('solucao')"
          >
            Soluções
          </button>
        </div>
      </div>
    </div>

    <!-- Cards -->
    <div>
      <!-- Se a aba for "solução" e não houver nenhum item, exibimos mensagem -->
      <template v-if="selectedTab === 'solucao' && solucoes.length === 0">
        <p class="text-center text-muted">Nenhuma solução encontrada.</p>
      </template>

      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4">
        <div
          class="col d-flex justify-content-center"
          v-for="(item, index) in filteredCards"
          :key="item.Id || index"
        >
          <CardItem
            :type="item.Tipo"
            :title="item.Nome"
            :description="`${item.Marca} ${item.Modelo}`"
            :resumo="item.Resumo"
            :author="item.Autor"
            :quantidade="item.Quantidade"
            @open="openModal(item)"
          />
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal && selectedTab === 'componente'" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content p-4 text-white">
        <h4>{{ modalData.Nome }}</h4>
        <p class="mb-2" style="font-size: 1.1rem">
          <b>• Marca:</b> {{ modalData.Marca }}<br />
          <b>• Modelo:</b> {{ modalData.Modelo }}<br />
          <b>• Quantidade:</b> {{ modalData.Quantidade }}
        </p>
        <button class="btn btn-light mt-3" @click="closeModal">
          Fechar
        </button>
      </div>
    </div>

    <div v-else-if="showModal && selectedTab === 'solucao'" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content p-4 text-white">
        <h4>{{ modalData.Nome }}</h4>
        <p class="mb-2" style="font-size: 1.1rem">
          <b>• Nível de escolaridade:</b> {{ modalData.NivelEscolaridade }}<br />
          <b>• Componentes necessários:</b> {{ modalData.ComponentesNecessarios }}<br />
          <b>• Data:</b> {{ modalData.Data }}<br />
          <b>• Manual:</b> {{ modalData.Manual }}
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

// Duas listas separadas, preenchidas por GETs distintos
const componentes = ref([])
const solucoes = ref([])

// Função para buscar “componentes” (GET /api/inventario/)
async function fetchComponentes() {
  try {
    console.log('[fetchComponentes] GET /api/inventario/')
    const response = await axios.get('/api/inventario/')
    console.log('[fetchComponentes] resposta componentes:', response.data)
    componentes.value = response.data
  } catch (err) {
    console.error('[fetchComponentes] erro ao buscar componentes:', err)
  }
}

// Função para buscar “soluções” (GET /api/projetos/)
async function fetchSolucoes() {
  try {
    console.log('[fetchSolucoes] GET /api/projetos/')
    const response = await axios.get('/api/projetos/')
    console.log('[fetchSolucoes] resposta soluções:', response.data)
    solucoes.value = response.data
  } catch (err) {
    console.error('[fetchSolucoes] erro ao buscar soluções:', err)
  }
}

// No mounted, chamamos ambas as funções e logo depois mostramos no console
onMounted(async () => {
  await fetchComponentes()
  await fetchSolucoes()
  console.log('[onMounted] lista de componentes:', componentes.value)
  console.log('[onMounted] lista de soluções:', solucoes.value)
})

// Retorna os cards a exibir, filtrando pelo searchTerm
const filteredCards = computed(() => {
  // Escolhe a lista conforme a aba selecionada
  const listaBase = selectedTab.value === 'componente' ? componentes.value : solucoes.value

  console.log(`[filteredCards] aba=${selectedTab.value}, base antes do filtro:`, listaBase)

  return listaBase.filter((card) =>
    (card.Nome || '').toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})

function openModal(data) {
  modalData.value = data
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

function selectTab(tipo) {
  console.log('[selectTab] aba selecionada:', tipo)
  selectedTab.value = tipo
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
