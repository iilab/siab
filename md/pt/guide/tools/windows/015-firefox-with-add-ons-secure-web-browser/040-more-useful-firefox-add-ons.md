

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: More Useful Firefox Add-Ons

---

Seções nessa página:

- [**5.0 Sobre as Extensões**](#5.0)
- [**5.1 Como usar HTTPS Everywhere**](#5.1)
- [**5.2 Como usar Adblock Plus**](#5.2)
- [**5.3 Como usar o Beef Taco (Opção de rejeitar cookies de propaganda dirigida)**](#5.3)
- [**5.4 Como usar o Better Privacy**](#5.4) 
- [**5.5 Outros Complementos úteis**](#5.5)

-------

<a name="5.0"></a>
## 5.0 Sobre as Extensões ##

As **Extensões do Mozilla Firefox** que são mostradas dessa seção foram feitas para aumentar e proteger o anonimato, a privacidade e a segurança durante a navegação na internet. Para baixá-las, consulte a seção principal [**Baixando o Firefox**](/pt/firefox_main).


<a name="5.1"></a>
## 5.1 Como usar o HTTPS Everywhere##

![](/sbox/screen/firefox-pt/httpseverywherelogo.png)

O **HTTPS Everywhere** é uma extensão do **Mozilla Firefox** que assegura que você se comunirá com uma lista específica de sites por meio de de uma conexão criptografada (*https*). Embora muitos sites ofereçam criptografia, tendem a configurar o endereço padrão para um http não criptografado.

A Extensão **HTTPS Everywhere** conserta esses problemas reescrevendo todos os requerimentos para tais sites no protocolo **HTTPS**. Ela roda silenciosamnete no fundo, assegurando que a conexão aos sites escolhidos sejam seguras. Porém, isso funcionará *somente* quando aqueles sites usam o protocolo **HTTPS**.

Após instalar a Extensão **HTTPS Everywhere**, a seguinte tela aparecerá:

![](/sbox/screen/firefox-pt/75.png)

*Figura 1: A tela inicial de O HTTPS Everywhere deve usar o Observatório SSL?* 

**Passo 1**. **Clique** em ![](/sbox/screen/firefox-pt/76.png) para ativar as seguintes telas: 

![](/sbox/screen/firefox-pt/77.png)

*Figura 2: As opções do Observatório SSL*

**Observação**: Se existe uma instalação anterior do **HTTPS Everywhere** no seu navegador **Firefox**, **selecione Ferramentas > Complementos > Extensões > HTTPS Everywhere > Opções > SSL Observatory** e verifique se as opções *Usar esse Observatório?* e *Quando você vir um novo certificado, diga ao Observatórios a qual ISP você está conectado* estão habilitadas. Se você não estiver usando o **Tor**, **habilite** a opção *Checar os certificados mesmo se o Tor não estiver disponível*.


<a name="5.2"></a>
## 5.2 Como usar o Adblock Plus ##

![](/sbox/screen/firefox-pt/adblockpluslogo.png)

O **Adblock Plus** é um complemento de filtro de conteúdo feito para limitar ou restringir as publicidades exibidas na tela.

Após instalar o **Adblock Plus**, as seguintes páginas serão abertas: 
[**chrome://adblockplus/content/ui/firstRun.html**](chrome://adblockplus/content/ui/firstRun.html)
 
![](/sbox/screen/firefox-pt/60.png)

*Figura 3: Página inicial do Adblock Plus*

**Passo 1**. **Clique** em ![](/sbox/screen/firefox-pt/61.png) para habilitar as mudanças, ligando ![](/sbox/screen/firefox-pt/62.png) para as opções de *Bloqueio de Malware*, *Remover Botões de Redes Sociais* e *Desativar o Rastreamento* (como ilustrado na *Figura 1*, acima).

**Passo 2**. **Selecione Ferramentas > Complementos > Adblock Plus > Opções de filtros...** para ativar a seguinte janela:

![](/sbox/screen/firefox-pt/63.png)

*Figura 4: As Opções de Filtro do Add Adblock Plus indicando as inscrições de filtros disponíveis*

**Passo 2**. **Clique** em cada caixa de opção para habilitar a inscrição no filtro (como ilustrado na *Figura 2*, acima), e **desabilite** a opção ![](/sbox/screen/firefox-pt/64.png), para prevenir *todas* publicidades descritas ou listadas nesses filtros de aparecerem. 

**Passo 3**. Se você trabalha em plataformas de múltiplas línguas **clique** em ![](/sbox/screen/firefox-pt/65.png) para visualizar diferentes inscrições, então **clique** em ![](/sbox/screen/firefox-pt/66.png) para ativar o menu expandido dos diferentes filtros. **Selecione** os filtros apropriados e **clique** em ![](/sbox/screen/firefox-pt/67.png).

**Passo 4**. Para atualizar as inscrições de filtros, **clique** em ![](/sbox/screen/firefox-pt/68.png), e então **selecione** o item *Atualizar filtros* no menu.


<a name="5.3"></a>
## 5.3 Como usar o Beef Taco (Opção de rejeitar cookies de propaganda dirigida) ##

![](/sbox/screen/firefox-en/beeftacologo.png)

O **Beef Taco** é um complemento do **Mozilla Firefox** para gerenciar os cookies associados a publicidades de diferentes empresas, entre as quais **Google**, **Microsoft** e **Yahoo**. O complemento pode ser configurado para apagar automaticamente **cookies de propaganda dirigida**. Contudo, também permite a pessoas de conhecimento de nível **Experiente** ou **Avançado** especificar com mais detalhes de qual forma os cookies poderão entrar no sistema, e como serão eliminados.


<a name="5.4"></a>
## 5.4 Como usar o Better Privacy ##

![](/sbox/screen/firefox-pt/betterprivacylogo.png)

O **Better Privacy** é um complemento do **Mozilla Firefox** que ajuda na proteção de cookies especiais referenciados como **LSO** (**Local Shared Objects**, ou objetos compartilhados localmente) os quais podem ser inseridos no seu computador por scripts de **Flash**. Esses cookies não são removidos pelo procedimento de limpeza padrão do **Firefox**.


<a name="5.5"></a>
## 5.5 Outros Complementos úteis ##
Esta seção descreve uma série de complementos e extensões úteis que são gratuitos, de código aberto (ou em processo de se tornar), e que podem aumentar ou extender sua capacidade de navegar na internet de forma privada e segura.


### 5.5.1 Cryptocat ###

[![](/sbox/screen/firefox-pt/cryptocatlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/cryptocat/)

O **Cryptocat** é um complemento de código aberto de conversas privadas e criptografadas, e que funciona no próprio navegador. Portanto, em certas situações pode ser mais fácil usar do que outros programas similares de conversação (chat) online. 

O **Cryptocat** permite a criação de uma sala virtual na qual você pode conversar com várias pessoas ou discutir assuntos reservadamente, com participantes individuais. Todas as mensagens são criptografadas e decodificadas nos navegadores de cada um antes de serem enviadas e após serem recebidas. O **Cryptocat** está disponível também como uma extensão do **Mozilla Firefox**, **Google Chrome** e **Apple Safari**, assim como aplicativo para o **Mac OS X**. [**Leia mais...**](https://crypto.cat/)


### 5.5.2 Disconnect ###

[![](/sbox/screen/firefox-pt/disconnectmelogo.png)](https://addons.mozilla.org/en-us/firefox/user/disconnect/)

O **Disconnect** foi feito para manter seus dados seguros de rastreadores de terceiros e também para analisar dados rastreados, classificando-os em diferentes grupos. Por exemplo: publicitários, dados de análise de tráfico e de mídias sociais. [**Leia mais...**](https://www.disconnect.me/)


### 5.5.3 DuckDuckGo ### 

[![](/sbox/screen/firefox-pt/duckduckgologo.png)](https://addons.mozilla.org/en-US/firefox/addon/duckduckgo-ssl/)

O **DuckDuckGo** foi pensado para oferecer uma alternativa privada e segura para sistemas de buscas na internet como **Google** ou **Bing**. O **DuckDuckGo** não grava nem compartilha os seus dados, e quem o utiliza tem acesso à mesma informação. Você pode ir diretamente para o site [**DuckDuckGo**](https://duckduckgo.com/) ou **clicar** no ícone do programa para instalá-lo como sistema padrão de buscas.


### 5.5.4 vtzilla ###

[![](/sbox/screen/firefox-pt/vtzillalogo.png)](https://addons.mozilla.org/en-us/firefox/addon/vtzilla/)

O **vtzilla** é uma extensão do navegador **Mozilla Firefox** feita para buscar malware e vírus em sites e downloads. Depois de instalada, a barra de ferramentas do complemento (que pode ser ligada ou desligada) aparecerá abaixo da barra de navegação do **Firefox**. Basta copiar e colar, ou digitar o endereço do site na caixa de busca do **vtzilla**, e seu pedido será redirecionado o **Virus Total**, um site que direciona mais de 40 varredores de vírus e malware para o link ou site especificado. O **vtzilla** reduz o risco de infecções ao adicionar mais um nível de proteção ao programa antivírus existente (por exemplo, o [**avast!**](https://securityinabox.org/en/avast_main)), fazendo uma varredura nos arquivos baixados na internet. [**Leia mais...**](https://www.virustotal.com/en/documentation/browser-extensions/).


### 5.5.5 ShareMeNot ###

[![](/sbox/screen/firefox-pt/sharemenotlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/sharemenot/)

O **ShareMeNot** foi feito para prevenir que botões de terceiros incorporados em diversos sites na internet (como o "Curtir", do Facebook, ou o "tweet", do Twitter) rastreem suas ações até que você eventualmente clique neles. [**Leia mais...**](http://sharemenot.cs.washington.edu/.)


### 5.5.6 ClickClean ###

[![](/sbox/screen/firefox-pt/clickcleanlogo.png)](https://addons.mozilla.org/en-US/firefox/addon/Cliqueclean/) 

O **Click&Clean** foi feito para apagar automaticamente dados privados ao fechamento do navegador **Firefox**. Isso inclui limpar registros do seu histórico de download, apagar o histórico de navegação e remover cookies, incluindo os **Flash Local Shared Objects** (**LSO**, ou objetos compartilhados localmente). Ele também apaga arquivos temporários e esvazia o cache local. 

 **Observação**: Como alternativa, é possível considerar usar aplicações externas como o [**CCleaner**](https://securityinabox.org/pt/ccleaner_main), o **Wise Disk Cleaner** ou outros no sistema operacional **Windows**, ou **Janitor** e **BleachBit** no **Linux**.


