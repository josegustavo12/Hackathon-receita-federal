<template>
  <main>
    <div id="navbar" class="py-3">
      <div class="container d-flex justify-content-between align-items-center">
        <router-link to="/">
          <img alt="logo do site" src="../assets/logo.png" style="width: 120px;">
        </router-link>

        <div class="d-inline align-items-center">
          <router-link to="/tutorial" class="text-decoration-none fonte">
            <i class="fa-solid fa-book"></i>
            Comece Aqui
          </router-link>
          <button class="ms-3 btn botao" @click="showLogin = true">Entrar</button>
        </div>
      </div>
    </div>

    <!-- Login Modal -->
    <div v-if="showLogin" class="modal-overlay" @click.self="closeLogin">
      <div class="login-modal text-start">
        <div class="modal-header-custom d-flex justify-content-center align-items-center mb-4">
          <img src="../assets/logo.png" alt="Logo" class="modal-logo" />
        </div>

        <h5 class="fw-bold mb-4">Identifique-se no gov.br com:</h5>

        <div class="d-flex align-items-center mb-2">
          <i class="fa-solid fa-id-card me-2 text-primary"></i>
          <span class="fw-semibold">Número do CPF</span>
        </div>

        <p class="text-muted small mb-3">
          Digite seu CPF para <strong>criar</strong> ou <strong>acessar</strong> sua conta gov.br
        </p>

        <!-- Campo CPF -->
        <div class="mb-3">
          <label for="cpf" class="form-label fw-semibold">CPF</label>
          <input
            id="cpf"
            name="accountId"
            type="tel"
            class="form-control"
            placeholder="Digite seu CPF"
            maxlength="11"
            inputmode="numeric"
            autocomplete="off"
          />
        </div>

        <!-- Botão continuar -->
        <div class="d-flex justify-content-end mb-4">
          <button type="button" class="btn btn-primary continuar-btn">Continuar</button>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const showLogin = ref(false)

function closeLogin() {
  showLogin.value = false
}
</script>

<style scoped>
  #navbar {
    background-color: var(--sec-color);
    height: 75px;
    border-bottom: 1px solid black;
  }

  .navbar {
    font-size: clamp(1.125rem, 3vw + 0.5rem, 1.75rem);
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
    background-color: #155bcb;
    font-weight: bold;
    border-radius: 999px;
    padding: 8px 24px;
    font-size: 1rem;
    border: none;
  }

  .continuar-btn:hover {
    background-color: #0f4cad;
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
</style>