<template>
  <main>
    <div class="tutorial">
      <div class="passo-a-passo-tutorial container py-5">
        <h2 class="text-center mb-4">Como adicionar uma Solução de Reaproveitamento</h2>
        <ol class="lista-passo">
          <li>No menu principal, clique na opção “Entrar”.</li>
          <li>Faça o login ou Cadastrar-se.</li>
          <li>Em seguida, clique em “Adicionar Solução” ou no botão “+ Nova Solução”.</li>
          <li>Dê um título claro e objetivo.</li>
          <li>Escreva o passo a passo de como reaproveitar o componente, com linguagem acessível e didática.</li>
          <li>Liste todos os componentes eletrônicos necessários para realizar a atividade.</li>
          <li>Revise as informações inseridas.</li>
          <li>Clique em “Salvar” para disponibilizar a solução aos usuários do sistema.</li>
          <li>A solução será listada e poderá ser consultada por filtros como nome, nível de escolaridade (dificuldade) ou componentes utilizados.</li>
        </ol>
      </div>
    </div>
    <footer>© 2025 Recap</footer>
  </main>
</template>

<script>
export default {
  name: 'TutorialView',
}
</script>

<style>
.tutorial {
  background-color: white;
  min-height: 100vh;
  padding-top: 40px;
}

/* Estilo do bloco de passo a passo */
.passo-a-passo-tutorial {
  background-color: #f9fafb;
  border-radius: 12px;
  padding: 40px;
  color: #00205B;
  max-width: 900px;
  margin: 0 auto;
  border: 2px solid #00205B
}

/* Estilo da lista numerada */
.lista-passo {
  list-style: decimal;
  padding-left: 20px;
  font-size: 1.1rem;
  line-height: 2;
}

footer {
  min-height: 10vh;
  background-color: #00205B;
  text-align: center;
  font-size: 14px;
  padding: 16px 0;
  color: white;
}
</style>
