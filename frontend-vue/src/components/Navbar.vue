<template>
  <main>
    <div id="navbar" class="py-3">
      <div class="container d-flex justify-content-between align-items-center">
        <router-link to="/">
          <img alt="logo do site" src="../assets/logo.png" style="width: 120px;" />
        </router-link>

        <div class="d-inline align-items-center">
          <router-link to="/cards" class="text-decoration-none fonte me-3">
            <i class="fa-solid fa-search"></i>
            Pesquisa
          </router-link>
          <router-link to="/tutorial" class="text-decoration-none fonte me-3">
            <i class="fa-solid fa-book"></i>
            Comece Aqui
          </router-link>

          <!-- Se não estiver logado, exibe “Entrar” -->
          <button
            v-if="!isLoggedIn"
            class="btn botao"
            @click="openModal('login')"
          >
            Entrar
          </button>

          <!-- Se estiver logado, exibe o dropdown “Gerenciar Conta” -->
          <div v-else class="dropdown">
            <button
              class="btn botao dropdown-toggle"
              type="button"
              id="dropdownGerenciarConta"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Gerenciar Conta
            </button>
            <ul
              class="dropdown-menu dropdown-menu-end"
              aria-labelledby="dropdownGerenciarConta"
            >
              <!-- Item que abre o modal de Adicionar Projeto -->
              <li>
                <button class="dropdown-item" @click="openProjectModal">
                  <i class="fa-solid fa-plus me-2"></i>
                  Adicionar Projeto
                </button>
              </li>
              <li><hr class="dropdown-divider"></li>
              <li style="border-top: 1px solid gray">
                <button class="dropdown-item" @click="fazerLogout" style="color: red">
                  <i class="fa-solid fa-sign-out"></i>
                  Sair
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal (Login ou Cadastro) -->
    <div
      v-if="showModal && !isLoggedIn"
      class="modal-overlay"
      @click.self="closeModal"
    >
      <div class="login-modal text-start">
        <div
          class="modal-header-custom d-flex justify-content-center align-items-center mb-3"
        >
          <img src="../assets/logo.png" alt="Logo" class="modal-logo" />
        </div>

        <!-- Frase com link para alternar entre Login e Cadastro -->
        <div class="text-center mb-4">
          <span v-if="!isRegisterMode">
            Não tem uma conta?
            <a href="#" @click.prevent="isRegisterMode = true; limparErros()">
              Crie aqui
            </a>
          </span>
          <span v-else>
            Já tem conta?
            <a href="#" @click.prevent="isRegisterMode = false; limparErros()">
              Faça login aqui
            </a>
          </span>
        </div>

        <!-- ========== FORMULÁRIO DE LOGIN ========== -->
        <div v-if="!isRegisterMode">
          <h5 class="fw-bold mb-4">Identifique‐se no gov.br com:</h5>

          <div class="d-flex align-items-center mb-2">
            <i class="fa-solid fa-id-card me-2" style="color: var(--main-color)"></i>
            <span class="fw-semibold">Número do CPF</span>
          </div>
          <p class="text-muted small mb-3">
            Digite seu CPF e sua senha para acessar sua conta
          </p>

          <!-- Campo CPF -->
          <div class="mb-3">
            <label for="cpf-login" class="form-label fw-semibold">CPF</label>
            <input
              id="cpf-login"
              v-model="cpf"
              type="tel"
              class="form-control"
              placeholder="Digite seu CPF"
              maxlength="11"
              inputmode="numeric"
              autocomplete="off"
            />
          </div>

          <!-- Campo Senha -->
          <div class="mb-4">
            <label for="senha-login" class="form-label fw-semibold">Senha</label>
            <input
              id="senha-login"
              v-model="senha"
              type="password"
              class="form-control"
              placeholder="Digite sua senha"
              autocomplete="off"
            />
          </div>

          <!-- Botão Continuar (Login) -->
          <div class="d-flex justify-content-end mb-3">
            <button
              type="button"
              class="btn botao continuar-btn"
              @click="fazerLogin"
              :disabled="loadingLogin"
            >
              <span v-if="!loadingLogin">Continuar</span>
              <span v-else>Carregando...</span>
            </button>
          </div>

          <!-- Mensagem de erro (Login) -->
          <div v-if="erroLogin" class="alert alert-danger py-2 px-3">
            {{ erroLogin }}
          </div>
        </div>

        <!-- ========== FORMULÁRIO DE CADASTRO ========== -->
        <div v-else>
          <h5 class="fw-bold mb-4">Crie sua conta gov.br:</h5>
          <p class="text-muted small mb-3">
            Preencha os campos abaixo para criar um novo usuário
          </p>

          <!-- CPF -->
          <div class="mb-3">
            <label for="cpf-cadastro" class="form-label fw-semibold">CPF</label>
            <input
              id="cpf-cadastro"
              v-model="cpfCadastro"
              type="tel"
              class="form-control"
              placeholder="Digite seu CPF"
              maxlength="11"
              inputmode="numeric"
              autocomplete="off"
            />
          </div>

          <!-- Email -->
          <div class="mb-3">
            <label for="email-cadastro" class="form-label fw-semibold">Email</label>
            <input
              id="email-cadastro"
              v-model="emailCadastro"
              type="email"
              class="form-control"
              placeholder="Digite seu email"
              autocomplete="off"
            />
          </div>

          <!-- Senha -->
          <div class="mb-4">
            <label for="senha-cadastro" class="form-label fw-semibold">Senha</label>
            <input
              id="senha-cadastro"
              v-model="senhaCadastro"
              type="password"
              class="form-control"
              placeholder="Crie uma senha"
              autocomplete="off"
            />
          </div>

          <!-- Botão Cadastrar -->
          <div class="d-flex justify-content-end mb-3">
            <button
              type="button"
              class="btn botao continuar-btn"
              @click="fazerCadastro"
              :disabled="loadingCadastro"
            >
              <span v-if="!loadingCadastro">Cadastrar</span>
              <span v-else>Carregando...</span>
            </button>
          </div>

          <!-- Mensagem de erro (Cadastro) -->
          <div v-if="erroCadastro" class="alert alert-danger py-2 px-3">
            {{ erroCadastro }}
          </div>
          <!-- Mensagem de sucesso -->
          <div v-if="sucessoCadastro" class="alert alert-success py-2 px-3">
            {{ sucessoCadastro }}
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Adicionar Projeto -->
    <div
      v-if="showProjectModal"
      class="modal-overlay"
      @click.self="closeProjectModal"
    >
      <div class="project-modal text-start">
        <div
          class="modal-header-custom d-flex justify-content-center align-items-center mb-3"
        >
          <h5 class="text-white mb-0">Adicionar Projeto</h5>
        </div>

        <p class="text-muted small mb-3">
          Preencha as informações abaixo para criar um novo projeto
        </p>

        <!-- Campos do formulário de projeto -->
        <div class="mb-3">
          <label for="nome-projeto" class="form-label fw-semibold">Nome</label>
          <input
            id="nome-projeto"
            v-model="nomeProjeto"
            type="text"
            class="form-control"
            placeholder="Nome do projeto"
            autocomplete="off"
          />
        </div>

        <div class="mb-3">
          <label for="resumo-projeto" class="form-label fw-semibold">Resumo</label>
          <textarea
            id="resumo-projeto"
            v-model="resumoProjeto"
            class="form-control"
            rows="2"
            placeholder="Resumo breve"
          ></textarea>
        </div>

        <div class="mb-3">
          <label for="componentes-projeto" class="form-label fw-semibold">Componentes Necessários</label>
          <textarea
            id="componentes-projeto"
            v-model="componentesProjeto"
            class="form-control"
            rows="2"
            placeholder="Liste os componentes"
          ></textarea>
        </div>

        <div class="mb-3">
          <label for="nivel-projeto" class="form-label fw-semibold">Nível de Escolaridade</label>
          <input
            id="nivel-projeto"
            v-model="nivelProjeto"
            type="text"
            class="form-control"
            placeholder="Ex: Ensino Médio, Fundamental..."
            autocomplete="off"
          />
        </div>

        <div class="mb-3">
          <label for="manual-projeto" class="form-label fw-semibold">Manual (URL ou texto)</label>
          <textarea
            id="manual-projeto"
            v-model="manualProjeto"
            class="form-control"
            rows="2"
            placeholder="Link ou instruções"
          ></textarea>
        </div>

        <div class="mb-4">
          <label for="autor-projeto" class="form-label fw-semibold">Autor</label>
          <input
            id="autor-projeto"
            v-model="autorProjeto"
            type="text"
            class="form-control"
            placeholder="Nome do autor"
            autocomplete="off"
          />
        </div>

        <!-- Botão Salvar Projeto -->
        <div class="d-flex justify-content-end mb-3">
          <button
            type="button"
            class="btn botao continuar-btn"
            @click="fazerProjeto"
            :disabled="loadingProjeto"
          >
            <span v-if="!loadingProjeto">Salvar Projeto</span>
            <span v-else>Enviando...</span>
          </button>
        </div>

        <!-- Mensagem de erro (Projeto) -->
        <div v-if="erroProjeto" class="alert alert-danger py-2 px-3">
          {{ erroProjeto }}
        </div>
        <!-- Mensagem de sucesso (Projeto) -->
        <div v-if="sucessoProjeto" class="alert alert-success py-2 px-3">
          {{ sucessoProjeto }}
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

// --- Controle do modal de Login/Cadastro ---
const showModal = ref(false)
const isRegisterMode = ref(false) // false = login, true = cadastro

// Campos de Login
const cpf = ref('')
const senha = ref('')
const loadingLogin = ref(false)
const erroLogin = ref(null)

// Campos de Cadastro
const cpfCadastro = ref('')
const emailCadastro = ref('')
const senhaCadastro = ref('')
const loadingCadastro = ref(false)
const erroCadastro = ref(null)
const sucessoCadastro = ref(null)

// --- Estado de autenticação ---
const isLoggedIn = ref(false)
const router = useRouter()

// --- Controle do modal de “Adicionar Projeto” ---
const showProjectModal = ref(false)
const nomeProjeto = ref('')
const resumoProjeto = ref('')
const componentesProjeto = ref('')
const nivelProjeto = ref('')
const manualProjeto = ref('')
const autorProjeto = ref('')
const loadingProjeto = ref(false)
const erroProjeto = ref(null)
const sucessoProjeto = ref(null)

// Variável para timer de logout automático (1h)
let logoutTimer = null

// ---------------- FUNÇÕES ---------------- //

// Abre o modal em modo “login” ou “cadastro”
function openModal(mode) {
  isRegisterMode.value = (mode === 'cadastro')
  showModal.value = true
  limparErros()
}

// Fecha o modal de Login/Cadastro
function closeModal() {
  showModal.value = false
  limparErros()
  cpf.value = ''
  senha.value = ''
  cpfCadastro.value = ''
  emailCadastro.value = ''
  senhaCadastro.value = ''
}

// Limpa mensagens de erro e sucesso de Login/Cadastro
function limparErros() {
  erroLogin.value = null
  erroCadastro.value = null
  sucessoCadastro.value = null
}

// Inicia timer para logout automático em 1h
function iniciarTimerLogout() {
  clearTimeout(logoutTimer)
  logoutTimer = setTimeout(() => {
    fazerLogout()
  }, 3_600_000) // 1 hora
}

// Logout: limpa token, estado e redireciona
function fazerLogout() {
  clearTimeout(logoutTimer)
  localStorage.removeItem('access_token')
  isLoggedIn.value = false
  router.push('/')
}

// onMounted: checa se já existe token salvo
onMounted(() => {
  const token = localStorage.getItem('access_token')
  if (token) {
    isLoggedIn.value = true
    iniciarTimerLogout()
  }
})

// Antes de destruir, limpa timer
onBeforeUnmount(() => {
  clearTimeout(logoutTimer)
})

// ========== LOGIN ========== //
async function fazerLogin() {
  if (!cpf.value || !senha.value) {
    erroLogin.value = 'Preencha CPF e senha antes de continuar.'
    return
  }

  loadingLogin.value = true
  erroLogin.value = null

  try {
    const form = new URLSearchParams()
    form.append('username', cpf.value)
    form.append('password', senha.value)

    const response = await axios.post(
      '/api/usuario/login',
      form,
      { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    )

    const { access_token } = response.data

    localStorage.setItem('access_token', access_token)
    isLoggedIn.value = true

    iniciarTimerLogout()
    closeModal()
    await router.push('/cards')
  }
  catch (err) {
    if (err.response) {
      if (err.response.status === 404) {
        erroLogin.value = 'Usuário não encontrado.'
      }
      else if (err.response.status === 401) {
        erroLogin.value = 'Senha incorreta.'
      }
      else {
        erroLogin.value = 'Falha ao autenticar. Tente novamente mais tarde.'
      }
    }
    else {
      console.error("Detalhes do erro:", err.message, err.config, err.code)
      erroLogin.value = 'Erro de rede. Verifique sua conexão.'

    }
  }
  finally {
    loadingLogin.value = false
  }
}

// ========== CADASTRO ========== //
async function fazerCadastro() {
  // Validação simples de campo vazio
  if (!cpfCadastro.value || !emailCadastro.value || !senhaCadastro.value) {
    erroCadastro.value = 'Preencha todos os campos antes de continuar.'
    return
  }

  loadingCadastro.value = true
  erroCadastro.value = null
  sucessoCadastro.value = null

  try {
    // Monta objeto conforme UsuarioRequest: { CPF, email, senha }
    const novoUsuario = {
      CPF: cpfCadastro.value,
      email: emailCadastro.value,
      senha: senhaCadastro.value
    }

    await axios.post(
      '/api/usuario/newuser',
      novoUsuario,
      { headers: { 'Content-Type': 'application/json' } }
    )

    sucessoCadastro.value = 'Usuário criado com sucesso! Agora efetue login.'
    // Após 1,5s, volta para o modo login automaticamente
    setTimeout(() => {
      isRegisterMode.value = false
      limparErros()
    }, 1500)
  }
  catch (err) {
    if (err.response) {
      // Caso o backend retorne HTTPException com detail
      erroCadastro.value = err.response.data.detail || 'Falha ao criar usuário.'
    }
    else {
      erroCadastro.value = 'Erro de rede. Verifique sua conexão.'
    }
  }
  finally {
    loadingCadastro.value = false
  }
}

// ========== ABRIR / FECHAR MODAL DE PROJETO ========== //
function openProjectModal() {
  showProjectModal.value = true
  limparErrosProjeto()
}

function closeProjectModal() {
  showProjectModal.value = false
  limparErrosProjeto()
  nomeProjeto.value = ''
  resumoProjeto.value = ''
  componentesProjeto.value = ''
  nivelProjeto.value = ''
  manualProjeto.value = ''
  autorProjeto.value = ''
}

function limparErrosProjeto() {
  erroProjeto.value = null
  sucessoProjeto.value = null
}

function gerarUUIDv4() {
  // gera um uuid no formato xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = (Math.random() * 16) | 0
    const v = c === 'x' ? r : (r & 0x3) | 0x8
    return v.toString(16)
  })
}


// ========== SUBMETER PROJETO ========== //
async function fazerProjeto() {
  // Validação básica: todos os campos obrigatórios
  if (
    !nomeProjeto.value ||
    !resumoProjeto.value ||
    !componentesProjeto.value ||
    !nivelProjeto.value ||
    !manualProjeto.value ||
    !autorProjeto.value
  ) {
    erroProjeto.value = 'Preencha todos os campos antes de continuar.'
    return
  }

  loadingProjeto.value = true
  erroProjeto.value = null
  sucessoProjeto.value = null

  try {
    const token = localStorage.getItem('access_token')
    if (!token) {
      throw new Error('Usuário não autenticado.')
    }

    // Geração de Id e Data
    const novoId = gerarUUIDv4()
    const nowISO = new Date().toISOString()

    const novoProjeto = {
      Id: novoId,
      Data: nowISO,
      Nome: nomeProjeto.value,
      Resumo: resumoProjeto.value,
      ComponentesNecessarios: componentesProjeto.value,
      NivelEscolaridade: nivelProjeto.value,
      Manual: manualProjeto.value,
      Autor: autorProjeto.value
    }

    await axios.post(
      '/api/projetos/',
      novoProjeto,
      {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        }
      }
    )

    sucessoProjeto.value = 'Projeto criado com sucesso!'
    setTimeout(() => {
      closeProjectModal()
    }, 1000)
  }
  catch (err) {
    if (err.response) {
      erroProjeto.value = err.response.data.detail || 'Falha ao criar projeto.'
    }
    else {
      erroProjeto.value = err.message || 'Erro de rede. Verifique sua conexão.'
    }
  }
  finally {
    loadingProjeto.value = false
  }
}
</script>

<style scoped>
  #navbar {
    background-color: var(--sec-color);
    height: 75px;
    border-bottom: 1px solid black;
  }

  .fonte {
    color: black;
  }

  .fonte:hover {
    color: #222;
  }
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 2000;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

/* Aplica tanto para login-modal quanto project-modal */
.login-modal,
.project-modal {
  background-color: #fff;
  border-radius: 10px;
  padding: 2rem;
  width: 100%;
  max-width: 500px;

  /* NOVO: limitar altura e ativar rolagem interna */
  max-height: 90vh;
  overflow-y: auto;

  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  font-family: 'Segoe UI', sans-serif;
}

  .continuar-btn {
    font-weight: bold;
    border-radius: 999px;
    padding: 8px 24px;
    font-size: 1rem;
    border: none;
  }
  
  .modal-header-custom {
    background-color: var(--sec-color); /* mesma cor da navbar */
    padding: 1rem;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }

  .modal-logo {
    height: 60px;
    object-fit: contain;
  }

  .alert {
    font-size: 0.9rem;
    margin-top: -0.5rem;
  }

  /* Para alinhar o dropdown corretamente */
  .dropdown {
    display: inline-block;
  }
  .dropdown-toggle::after {
    margin-left: 0.25rem;
  }

  /* Link dentro do modal */
  .login-modal a {
    color: #0d6efd;
    text-decoration: none;
  }
  .login-modal a:hover {
    text-decoration: underline;
  }
</style>
