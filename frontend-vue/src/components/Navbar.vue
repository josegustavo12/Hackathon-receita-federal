<template>
  <main>
    <div id="navbar" class="py-3">
      <div class="container d-flex justify-content-between align-items-center">
        <p>logo</p>

        <div class="d-inline align-items-center">
          <router-link to="/tutorial" class="text-decoration-none fonte">
            <i class="fa-solid fa-book"></i>
            Comece Aqui
          </router-link>
          <button class="ms-3 btn botao">Entrar</button>
        </div>
        
      </div>
    </div>
  </main>
</template>

<script>

  export default {
    name: 'Navbar',
  }
</script>

<style scoped>
  #navbar {
    background-color: var(--sec-color);
    height: 75px;
    border: 1px solid black;
  }

  .botao {
    background-color: var(--main-color);
    color:#fff;
    border: 1px solid var(--main-color);
  }

  .botao:hover {
    background-color: var(--main-hover);
    color: #fff;
    border: 1px solid var(--main-hover);
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
</style>