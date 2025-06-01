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
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

// --- Controle do modal e estado de login/cadastro ---
const showModal = ref(false)
const isRegisterMode = ref(false) // false = login, true = cadastro

// --- Campos de Login ---
const cpf = ref('')
const senha = ref('')
const loadingLogin = ref(false)
const erroLogin = ref(null)

// --- Campos de Cadastro (sem mais o campo "tipo") ---
const cpfCadastro = ref('')
const emailCadastro = ref('')
const senhaCadastro = ref('')
const loadingCadastro = ref(false)
const erroCadastro = ref(null)
const sucessoCadastro = ref(null)

// --- Estado de autenticação ---
const isLoggedIn = ref(false)
const router = useRouter()

// Variável para timer de logout automático (1h)
let logoutTimer = null

// ---------------- FUNÇÕES ---------------- //

// Abre o modal em modo “login” ou “cadastro”
function openModal(mode) {
  isRegisterMode.value = (mode === 'cadastro')
  showModal.value = true
  limparErros()
}

// Fecha o modal e limpa campos/erros
function closeModal() {
  showModal.value = false
  limparErros()
  cpf.value = ''
  senha.value = ''
  cpfCadastro.value = ''
  emailCadastro.value = ''
  senhaCadastro.value = ''
}

// Limpa mensagens de erro e sucesso de ambos formulários
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
  }, 3_600_000) // 3.600.000 ms = 1h
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

  .login-modal {
    background-color: #fff;
    border-radius: 10px;
    padding: 2rem;
    width: 100%;
    max-width: 420px;
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
    height: 75px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    margin: -2rem -2rem 1rem -2rem; /* compensa o padding do modal */
    padding: 0 1rem;
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
