

---

lang: pt
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

Os capítulos anteriores discutiram diversos hábitos e ferramentas capazes de ajudar na proteção de dados sensíveis. Mas o que fazer quando não é mais necessário guardar determinado tipo de informação? Se você chegar à conclusão, por exemplo, de que as cópias de reserva criptografadas (*backup*) de um arquivo são suficientes e quiser apagar a versão principal, qual a melhor forma de fazê-lo?

Infelizmente, a resposta é mais complicada do que parece. Quando se apaga um arquivo, mesmo após esvaziar a **Lixeira** do computador, o conteúdo daquele arquivo permanece no disco rígido e pode ser recuperado por qualquer pessoa com as ferramentas certas e um pouco de sorte.

Para ter certeza que dados apagados não caiam em mãos erradas, é preciso confiar em programas especiais que os removam de forma segura e permanente - o [*Eraser*](/pt/glossary#Eraser) é uma ferramenta assim e é discutido abaixo. Usá-lo é um pouco como rasgar um documento de papel em pequenos pedaços, em vez de jogá-lo em uma lata de lixo e esperar que ninguém o encontre. E, claro, apagar arquivos é apenas um exemplo de situação na qual você pode querer destruir informações sensíveis.

Considere os detalhes que poderiam ser aprendidos sobre sua organização se alguém, em especial um adversário particularmente poderoso e motivado politicamente, tivesse acesso a determinados arquivos que você considerou estarem apagados. Provavelmente, outros exemplos surgirão. É preciso [*apagar de forma segura*](/pt/glossary#Wiping) cópias de *backup* desatualizadas e discos rígidos antigos, assim como apagar contas de login antigas, limpar históricos de navegação de internet, entre outros.

O [*CCleaner*](/pt/glossary#CCleaner), outro programa descrito neste capítulo, pode ajudar a vencer o desafio de apagar os diversos arquivos temporários gerados pelo sistema operacional e pelos aplicativos, cada vez que são usados.

### Pano de fundo ###

<div class="background" markdown="1">
Elena é uma ativista de causas ambientais em um país de língua russa, onde mantém um site cada vez mais popular sobre a extensão do desmatamento ilegal na região. Ela fez cópias de reserva (*backup*) das informações usadas para criar o site e as mantém em casa, no escritório e em seu novo laptop. Recentemente, também passou a guardar cópias dos registros de visitantes e do banco de dados com as conversas realizadas no fórum do site.

Elena sairá do país em breve para participar de uma grande conferência global de ativistas ambientais e há notícias de participantes que tiveram seus laptops detidos por mais de uma hora em postos de fronteira. Para proteger as informações sensíveis e resguardar a segurança das pessoas mais políticas que participam do fórum, moveu os *backups* de casa e do trabalho para um volume do TrueCrypt e apagou a cópia que estava no laptop. Ao pedir conselho a seu sobrinho Nikolai, ele a advertiu que, caso julgue possível tê-lo apreendido por oficiais de fronteira, é necessário mais do que apenas apagar o *backup* que estava no laptop.
</div>

### O que aprender deste capítulo ###

  * Como remover informações sensíveis de forma permanente do computador
  * Como remover dados armazenados em dispositivos removíveis como CDs e pen drives
  * Como evitar que alguém saiba quais documentos foram acessados anteriormente em um computador
  * Como manter um computador de forma que arquivos apagados não possam ser recuperados no futuro

