<template>
  <main>
    <div class="bloco">
      <div class="container">
        <div class="row">
          <div class="col-8 ms-auto">
            <h1><b>Da apreensão ao reaproveitamento</b></h1>
            <h1><b>— tudo em um só sistema</b></h1>
            <p class="fs-5">Gerencie, catalogue e transforme eletrônicos apreendidos em recursos para educação e inovação</p>
            <router-link to="/tutorial">
              <button class="btn botao">Venha colaborar conosco!</button>
            </router-link>
          </div>
          </div>
        </div>
      </div>
    <div class="sobre">
      <h2>Sobre</h2>
      <p class="fs-4">O RECAP é um sistema voltado para o registro e reaproveitamento de eletrônicos apreendidos. Ele organiza os componentes e orienta seu uso em projetos educacionais, como aulas de robótica e programação, promovendo a reutilização de forma didática e sustentável.</p>
      <br>
      <br>
      <p class="fs-4">Mais do que apenas armazenar dados, o sistema promove o uso consciente e sustentável desses materiais, incentivando sua aplicação em projetos educacionais e sociais. As peças reaproveitadas ganham nova vida em aulas práticas de robótica, programação, eletrônica e inovação tecnológica, contribuindo para a formação de estudantes e o fortalecimento de iniciativas pedagógicas.</p>
    </div>
    <div class="estat">
      <section class="container">
        <div class="features row">
          <div class="col-12 col-md-6 col-lg-4 mb-4 d-flex justify-content-center">
            <div class="feature">
              <div class="icon">🗑️</div>
              <p>O lixo eletrônico é atualmente o tipo de resíduo mais frequentemente apreendido globalmente, representando 1 em cada 6 apreensões de resíduos</p>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4 mb-4 d-flex justify-content-center">
            <div class="feature">
              <div class="icon">♻️</div>
              <p>Aproximadamente 75% da população não sabe que todos os eletroeletrônicos podem ser reciclados se descartados corretamente</p>
            </div>
          </div>
          <div class="col-12 col-md-6 col-lg-4 mb-4 d-flex justify-content-center">
            <div class="feature">
              <div class="icon">📦</div>
              <p>Em 2024, foram apreendidos mais de 650 mil celulares contrabandeados, avaliados em cerca de R$ 550 milhões</p>
            </div>
          </div>
        </div>
      </section>

        <img src="@/assets/passo-a-passo.png" alt="passo a passo" class="imagem-apos-feature"  />
    </div>
    <div class="galeria">
      GALERIAAAAAAAAAAAAAAAAA
    </div>
    <div class="conclu">
       <h2 class="mb-4">RECAP: Reutilize, Eduque, Inove</h2>
       <p class="fs-4 mb-5" style="text-align: justify;">Cada componente reaproveitado é uma chance a mais de transformar vidas por meio da educação e da inovação. Contribuir com o nosso banco de soluções significa apoiar um futuro mais sustentável, criativo e inclusivo.
Participe, compartilhe suas ideias e faça parte dessa rede que transforma eletrônicos descartados em oportunidades reais de aprendizado e desenvolvimento. Com o RECAP, seu engajamento ajuda a construir um mundo onde tecnologia e educação caminham juntas para um amanhã melhor.</p>
      <router-link to="/cards">
        <button class="btn botao">Faça sua primeira pesquisa!</button>
      </router-link>
    </div>
    <footer>© 2025 Recap</footer>
  </main>
</template>

<script>
  export default {
    name: 'HomeView',
  }
</script>


<style>
  .bloco {
    background-image: url('@/assets/landing-page-bg.png');
    background-size: cover;          
    background-position: center;    
    background-repeat: no-repeat; 
    background-color: #00205B;
    font-family: Arial, Helvetica, sans-serif;
    min-height: 90vh; 
    color: white;
    display: flex;
    align-items: center;
    text-align: right;
    justify-content: flex-end;
    padding: 50px;
    box-sizing: border-box;
  }

.bloco p{
  color: #00205b;
}

.sobre {
  background-color: #00205b;
  color: #fff;
  padding: 80px 20px;
  text-align: justify;
  min-height: 100vh;
  justify-content: center;
}

.sobre h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  position: relative;
  text-align: center;
}

.sobre h2::after {
  content: "";
  display: block;
  width: 60px;
  height: 4px;
  background-color: #64A70B;
  margin: 10px auto 0;
  border-radius: 2px;
}


.sobre p {
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.2rem;
  line-height: 1.8;
  font-weight: 300;
}


.estat{
  background-color: #f9fafb;
  color: black;
  min-height: 100vh;
}

.galeria{
  background-color: #00205b;
  min-height: 100vh;
  color: white;
}

.conclu{
  background-color: white;
  color: black;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  margin-top: 90px;
}

.conclu h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  position: relative;
  text-align: center;
  color: #00205B;
}

.conclu h2::after {
  content: "";
  display: block;
  width: 600px;
  height: 4px;
  background-color: #64A70B;
  margin: 10px auto 0;
  border-radius: 2px;
}

.conclu p,
.conclu h4{
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.0rem;
  line-height: 1.8;
  font-weight: 300;
}

.conclu .botao {
  margin: 0 auto;
  display: block;
  font-size: 1.1rem;
  padding: 16px 32px;
}

footer{
  min-height: 10vh;
  background-color: #00205B;
  text-align: center;   
  font-size: 14px;      
  padding: 16px 0; 
  color: white
}

.botao {
    background-color: #64A70B;
    color:#fff;
    border: 1px solid #00205b;
    padding: 20px 40px;
    transition: background-color 0.3s ease;
    border-radius: 10px;

}

.botao:hover {
    background-color: #64A70B;
    border: 1px solid rgba(0, 32,91,0.8);

}

.features {
  margin: 0 auto;
  max-width: 1200px;
  padding: 30px 15px;
}

.feature {
  background: white;
  border-radius: 8px;
  padding: 30px 20px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  height: 100%;
}

.icon {
  font-size: 2rem;
  margin-bottom: 15px;
}

.imagem-apos-feature {
  display: block;
  margin: 40px auto;
  max-width: 100%;
  width: 90%;
  height: auto;
}

</style>