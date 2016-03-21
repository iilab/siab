

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Creating a digital backup

---

Dos vários tipos de dados descritos aqui, os 'documentos eletrônicos' são os que as pessoas tendem a se preocupar mais ao elaborar uma política de *backup*. Esse termo é um pouco ambíguo, mas costuma se referir a arquivos que você sabe onde estão e aos quais pode abrir manualmente, seja clicando duas vezes ou ao usar o menu de Arquivo de algum programa específico. O termo engloba arquivos de texto simples, documentos de processadores de texto, apresentações, PDFs e planilhas, entre outros exemplos. Diferentemente de mensagens de e-mail, por exemplo, documentos eletrônicos não costumam estar sincronizados com cópias remotas na internet.

Quando fizer cópias de reserva de seus documentos eletrônicos, lembre-se de incluir os bancos de dados dos aplicativos. Se você usa calendários ou agendas, por exemplo, terá de encontrar o diretório onde tais programas guardam as informações. É comum que as bases de dados estejam no mesmo local dos documentos eletrônicos, pois costumam ficar dentro da pasta de **Meus Documentos** em computadores que usam Windows. Porém, se não estiverem lá, você deve adicioná-las ao fazer o *backup* periódico.

E-mails armazenados por aplicativos como o [*Thunderbird*](/pt/glossary#Thunderbird) são um exemplo especial de banco de dados. Se você usa um programa de e-mails, especialmente se não pode ou não quer deixar cópias de suas mensagens em um servidor, deve ter certeza de que estarão incluídos nos *backups* periódicos. Já arquivos de imagem ou de vídeo podem ser considerados tanto como documentos eletrônicos como itens pertencentes à base de dados de um programa, dependendo de como você os utiliza. Aplicativos como o Windows Media player e o iTunes, por exemplo, funcionam como bancos de dados, pois gerenciam arquivos reais de mídia mas exibem apenas uma referência a eles na interface do software. Se você usa programas como esses, talvez tenha de fazer uma busca no computador para descobrir onde estão os arquivos reais.


### Dispositivos de armazenamento ###

Antes de fazer cópias de reserva (*backup*) dos documentos eletrônicos, avalie o tipo de dispositivo de armazenamento a ser usado.

**Pen drives ou HDs externos** - Pen drives e HDs externos são opções baratas e com bastante espaço de armazenamento. São fáceis de apagar e podem ser reescritos diversas vezes. Possuem um tempo de funcionamento limitado, que depende muito de como e do quanto são usados, mas geralmente estimado em torno de 10 anos.

**Compact Discs (CDs)** - CDs podem guardar cerca de 700 Megabytes (MB) de dados. Para criar cópias de reserva (*backup*) nesta mídia, é preciso um [*gravador de CD*](/pt/glossary#CD_burner) e discos em branco. Se quiser apagar um CD e atualizar os arquivos gravados nele, precisará de um gravador de CD-RW e discos regraváveis. Todos os principais sistemas operacionais, incluindo o Windows XP, vêm com programas já instalados para escrever em CDs e CD-RWs. Tenha em mente que as informações gravadas nesses discos podem começar a deteriorar após 5 ou 10 anos. Se for preciso guardar um *backup* por mais tempo, use novos CDs, compre discos especiais de 'vida longa' ou use um método diferente.

**Digital Video Discs (DVDs)** - DVDs armazenam até 4.7 Gigabytes (GB) de dados. Funcionam de forma bem parecida aos CDs, mas requerem um equipamento levemente mais caro. Será preciso um [*gravador de DVD ou DVD-RW*](/pt/glossary#CD_burner) e as mídias apropriadas. Como um CD, as informações escritas em um DVD normal vão eventualmente desvanecer.

**Servidor remoto** - Um servidor de *backup* em rede bem mantido possui capacidade quase ilimitada, mas a velocidade e a estabilidade de sua conexão de internet determinarão se esta é uma opção realista ou não. Tenha em mente que ter um servidor de *backup* situado dentro do local de trabalho, embora seja mais rápido do que copiar a informação por internet, viola o requisito de que as cópias das informações importantes devem ser mantidas em dois locais físicos diferentes.

Também há serviços gratuitos de armazenamento na internet, mas os riscos de colocar dados online devem ser avaliados com muito cuidado. As cópias de reserva devem ser sempre criptografadas antes de colocadas em servidores de organizações ou pessoas que você não conhece ou confia. Veja alguns exemplos na seção de [***Leitura extra***](/pt/chapter_5_5).


### Programa para *backup* ###

O Cobian Backup é uma ferramenta amigável que pode ser configurada para rodar automaticamente a intervalos regulares de tempo e para incluir apenas arquivos modificados desde a última cópia de reserva. O programa também pode comprimir os *backups* para que ocupem menos espaço.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Cobian Backup*](/en/cobian_main)
</div>

Como sempre, é uma boa ideia criptografar os arquivos de *backup* com uma ferramenta como o [*TrueCrypt*](/pt/glossary#TrueCrypt). Mais informações sobre criptografia de dados podem ser vistas no [***Capítulo 4: Como proteger os arquivos sensíveis do seu computador***](/pt/chapter-4).

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*TrueCrypt - Armazenamento seguro de arquivos*](/pt/truecrypt_main)
</div>
<p>

Quando usar as ferramentas de *backup*, há algumas coisas que você pode fazer para que o sistema de gerar cópias de reserva funcione sem problemas:

  * Organize os arquivos do computador. Tente deixar em um único local todas as pastas onde estão os documentos eletrônicos dos quais serão feitas cópias de reserva. Um exemplo seria dentro do diretório **Meus Documentos**.
  * Se você usa programas que guardam as informações em bancos de dados, ache primeiro onde estão esses bancos. Caso não estejam em locais convenientes, veja se o programa permite usar outra pasta. Se sim, use o mesmo diretório onde estão seus documentos eletrônicos.
  * Monte uma agenda regular para fazer as cópias de reserva (*backup*).
  * Tente estabelecer procedimentos para todas as pessoas da equipe em seu local de trabalho que ainda não têm uma política de *backup* segura ou confiável. Ajude-as a entender a importância do tema.
  * Lembre-se de testar os procedimentos de recuperação dos dados contidos em cópias de reserva. Afinal, quando um problema aparecer, é o procedimento de recuperar as informações que vai importar, e não o de fazer o *backup*!



<div class="background" markdown="1">
Elena: Muito bem, fiz uma cópia de reserva criptografada no trabalho e a gravei em um CD. O Cobian está agendado para atualizar meu backup em alguns dias. Minha mesa do escritório tem uma gaveta com tranca e estou pensando em deixar os CDs ali, para que não se percam ou quebrem.

Nikolai: E se houver um incêndio no escritório e o computador, mesa, CDs de backup e tudo o mais queime? Ou se as pessoas que frequentam o fórum do seu site comecem a planejar manifestações gigantes de protesto e as autoridades entrem em parafuso? As coisas podem sair do controle e sua organização ser invadida. Duvido que a trava da sua mesa segure a polícia de levar os CDs. Que tal deixá-los em casa, ou pedir a um amigo que as guarde para você?
</div>

