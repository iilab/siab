

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

Seções nessa página:

- [**2.1 Como instalar o Jitsi**](#2.1)
- [**2.2 Como adicionar contas no Jitsi**](#2.2)
- [**2.2.1 Como adicionar uma conta do Google/Gmail**](#2.2.1)
- [**2.2.2 Como criar uma nova conta Jabber/XMPP ou SIP e adicioná-la ao Jitsi**](#2.2.2)
- [**2.2.3 Como adicionar uma conta do Facebook**](#2.2.3)
- [**2.3 Como alterar senhas de contas usando o Jitsi**](#2.3)
- [**2.4 Como configurar o Jitsi para aumentar a segurança do programa**](#2.4)
- [**2.4.1 Como desabilitar e remover o histórico de chamadas e das conversas de bate papo**](#2.4.1)
- [**2.4.2 Como requerer que a troca de mensagens em conversas por texto seja privada**](#2.4.2)
- [**2.4.3 Proteja as senhas de suas contas com uma senha mestre**](#2.4.3)

<a name="2.1"></a>
## 2.1 Como instalar o Jitsi ##

Para instalar o **Jitsi**, siga os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/jitsi-pt/02.png). Um alerta com o *Aviso de Segurança* pode aparecer; caso apareça, **clique** em ![](/sbox/screen/jitsi-pt/03.png) para abrir a janela do *Instalador para Windows*, que será seguida pela janela de *Boas Vindas ao Assistente de Configuração do Jitsi*.

**Passo 2**. **Clique** em ![](/sbox/screen/jitsi-pt/04.png) para seguir para a janela do *Termo de Licença do Usuário*. Marque a opção *Eu aceito os termos de Licença do Usuário* para ativar o botão *Próximo*, e **clique** em ![](/sbox/screen/jitsi-pt/04.png) para seguir para a janela de *Pasta de Destino*.

**Passo 3**. **Clique** em ![](/sbox/screen/jitsi-pt/04.png) para ativar a janela de tarefas adicionais e aceitar as configurações padrão apresentadas.

**Observação**: Ativar a opção de *Inicialização automática quando o computador é ligado ou reiniciado* pode reduzir a velocidade de inicialização do seu computador, especialmente se você já possui outros aplicativos configurados para serem iniciados quando a máquina é ligada.

**Passo 4**. **Clique** em ![](/sbox/screen/jitsi-pt/04.png) para ativar a janela de *Jitsi Pronto para Instalar* e depois **clique** em ![](/sbox/screen/jitsi-pt/05.png) para ativar a janela de *Instalando Jitsi*, que mostra uma barra com o progresso da instalação.

**Passo 5**. **Clique** em ![](/sbox/screen/jitsi-pt/06.png) para completar o processo de instalação e iniciar automaticamente a janela de configuração de contas do **Jitsi**, como a seguir:

![](/sbox/screen/jitsi-pt/07.png)

*Figura 1: A janela de Configuração de Contas do Jitsi*

**Observação**: Em alguns casos, instalar e abrir o **Jitsi** pela primeira vez pode ativar um *Alerta de Segurança do Windows* (*Figura 2*, abaixo). Este é um alerta padrão do sistema operacional **MS Windows**, e é seguro continuar utilizando o programa. Mesmo se você não clicar em nenhum dos botões e só fechar a janela, o **Jitsi** ainda poderá se comunicar a servidores públicos como **Jabber/XMPP** ou **SIP**, **Google Chat/Hangouts** e **Facebook Chat**, ou **Yahoo Messenger**. Entretanto, clicar no botão *Permitir Acesso* libera uma opção avançada do **Jitsi** chamada *Registrarless SIP Accounts*. Para mais informações sobre estas contas especiais, veja a página do [**Registrarless SIP Accounts**](https://jitsi.org/Documentation/RegistrarlessSIPAccount).

![](/sbox/screen/jitsi-pt/08.png)

*Figura 2: O Alerta de Segurança do Windows*

**Passo 6**. **Selecione** as caixas de opção tanto para redes **Privadas** quanto **Públicas** e depois **clique** em **Permitir Acesso** para seguir para a janela de configuração de contas do **Jitsi** (como na *Figura 1*, acima) ou para a janela principal (*Figura 4*, abaixo).


<a name="2.2"></a>
##2.2 Como adicionar contas no Jitsi ##

O **Jitsi** suporta vários tipos diferentes de contas e esta seção descreve como adicioná-las ou configurá-las no programa. As que utilizaremos abaixo são baseadas nos protocolos de comunicação **Jabber/XMPP** e **SIP**.

Dentre outros serviços, o **Jitsi** também permite que você use contas do **Gmail** ou **Facebook** para se comunicar. Como estes são dois dos serviços mais utilizados na internet, mostraremos abaixo como adicioná-los ao programa e como melhorar a segurança de conversas que os utilizem. Isso é possível devido à camada de criptografia independente do **Jitsi** que recai sobre a proteção oferecida pelos provedores dos serviços.

Entretanto, note que mesmo com a criptografia do aplicativo, provedores de serviços como **Google** ou **Facebook** (assim como outros) monitoram o simples fato de você estar se comunicando (e talvez com quem você esteja se comunicando), e podem compartilhar esta informação com terceiros, como empresas ou governos. Portanto, talvez seja melhor evitar usar estas contas em comunicações sensíveis, mesmo com a criptografia do **Jitsi**. Também mostraremos nesta seção como criar contas mais seguras (Jabber/XMPP ou SIP) e adicioná-las ao Jitsi, e recomendamos que você passe a utilizá-las.


<a name="2.2.1"></a>
### 2.2.1 Como adicionar uma conta do Google/Gmail ###

**Observação**: O exemplo a seguir é baseado em uma conta do **Google Talk/Hangouts**. O processo de configuração é similar para os outros protocolos listados na *Figura 1*, acima. Pode não ser possível estabelecer comunicação ou usar outras funcionalidades (como a criptografia independente para mensagens de texto e voz - **OTR** e **ZRTP**) entre pessoas usando dois ou mais provedores de serviços diferentes (como Facebook, Gmail, Yahoo etc.). Entretanto, isso deve funcionar quando as comunicaçṍes forem feitas entre duas contas do mesmo provedor de serviço.

**Passo 1**. **Selecione Iniciar > Jitsi** ou **Clique duas vezes** no ícone do **Jitsi** na Área de Trabalho para abrir o programa.

**Passo 2** Na janela de configuração de contas, **digite** o login e a senha da conta do **Gmail** que você pretende utilizar para o bate papo (chat), como na figura abaixo:

![](/sbox/screen/jitsi-pt/09.png)

*Figura 3: A janela de "Entrar" (reduzida)*

**Observação**: Você pode adicionar várias contas de diferentes protocolos ao mesmo tempo.

**Passo 3**. **Clique** em ![](/sbox/screen/jitsi-pt/09s.png) para ativar sua conta e seguir para a janela principal, como se vê a seguir:

![](/sbox/screen/jitsi-pt/10.png)

*Figura 4: Um exemplo da janela principal do Jitsi após adicionada a conta Gmail*

**Observação**: Se você fechou a janela de *Configuração de Contas*, ou quer adicionar outra conta, pode fazê-lo em **Ficheiro > Nova Conta**, no menu. Na nova janela, escolha *Google Talk* em **Rede** e **digite** o login e senha da conta do Gmail, como na imagem abaixo:

![](/sbox/screen/jitsi-pt/11.png)

*Figura 5: A janela de "Adicionar contas"*

Para verificar que sua conta do **Gmail** está registrada no **Jitsi**, siga os seguintes passos:

**Passo 1**. **Selecione *Ferramentas* > *Preferências*** do menu para abrir a seguinte janela:

![](/sbox/screen/jitsi-pt/12.png)

*Figura 6: A janela de Preferências mostrando a nova conta Gmail registrada (reduzida)*

**Observação**: Se você usa a [verificação em duas etapas](https://support.google.com/accounts/answer/180744?hl=pt) para proteger os acessos da sua conta do Gmail, quando tentar entrar usando o **Jitsi** e sua senha normal, uma mensagem como a abaixo pode ser exibida. Para acessar a conta pelo **Jitsi**, você precisa gerar uma "senha específica para o aplicativo". Veja as [instruções do Google de como fazer isto](https://support.google.com/accounts/answer/185833?hl=pt). 

![](/sbox/screen/jitsi-pt/13.png)

*Figura 7: Exemplo de falha na autenticação de entrada do Google Talk/Hangouts*


<a name="2.2.2"></a>
### 2.2.2 Como criar uma nova conta Jabber/XMPP ou SIP e adicioná-la ao Jitsi ###

**Jabber/XMPP** e **SIP** são padrões livres de comunicação de texto e de voz. Existem [muitos servidores](https://xmpp.net/directory.php) que oferecem contas gratuitas que podem ser utilizadas com Jitsi. Abaixo, recomendamos alguns que você pode usar para comunicações sensíveis.

Note que também existe a possibilidade de baixar o [programa de servidor Jabber/XMPP](http://xmpp.org/xmpp-software/servers/) (como [ejabbered](http://www.process-one.net/en/ejabberd/) ou [Prosody IM](http://prosody.im/)), instalar o seu próprio servidor e configurá-lo para comunicações seguras e privadas entre pessoas do seu grupo, comunidade ou organização.

  * A conta Jabber/XMPP do **Riseup.net** 

Se você possui uma conta no [serviço de e-mail seguro Riseup.net](/pt/riseup_main) (localizado nos Estados Unidos), também pode [usá-la para comunicar através da Rede Jabber/XMPP](https://www.riseup.net/en/chat) adicionando-a ao Jitsi - veja abaixo como.

  * **Jit.si** e outras contas Jabber/XMPP

Você pode registrar uma conta no servidor Jabber.ccc.de (localizado na Alemanha) seguindo os seguintes passos:

**Passo 1**. No menu do **Jitsi**, **selecione *Ficheiro* > *Nova Conta***. Na nova janela, **selecione** **XMPP** em *Rede* e **marque** a opção de **Criar uma nova conta**. Em *Servidor*, **digite** 'jabber.ccc.de', **digite** o login que você deseja criar no campo de 'username', e **preencha** os campos de *Senha* e *Confirmação de Senha* como na imagem abaixo:

![](/sbox/screen/jitsi-pt/14.png)

*Figura 8: Exemplo da janela de "Nova Conta" com a opção de "Criar uma nova conta XMPP" selecionada*

**Passo 2**. **Clique *Adicionar***. Depois de completar o registro, uma janela similar à *Figura 4*, acima, será exibida.

Se o login que você escolheu já estiver sendo utilizado por alguém, o processo de registro falhará e exibirá a seguinte mensagem: *Falha na criação de conta devido ao seguinte erro: Não foi possível confirmar os dados.* Você pode tentar novamente escolhendo um login diferente e repetindo o processo.

**Note** que se você não utilizar sua conta jabber.ccc.de em um período de 12 meses, ela será apagada do servidor automaticamente e o login ficará disponível para uso por outras pessoas.

Outro servidor Jabber/XMPP que vale a pena ser mencionado é o **jit.si**, mantido pelos desenvolvedores do programa **Jitsi**. Você pode criar uma conta no servidor [**jit.si**](https://jit.si) e em vários outros servidores públicos Jabber/XMPP da mesma forma descrita na seção anterior. O IM Observatory (Observatório de Mensagens Instantâneas) mantém [uma lista e um ranking dos servidores públicos Jabber/XMPP](https://xmpp.net/directory.php) e também permite que você [teste a segurança de qualquer servidor Jabber/XMPP](https://xmpp.net/index.php).

* **ostel.co** SIP

Contas **SIP** não podem ser registradas de dentro do programa **Jitsi**. O servidor **ostel.co** (localizado no Estados Unidos) permite o registro [em sua página](https://ostel.co/users/sign_up). **Escolha** um login e senha, **informe** um endereço de e-mail existente e **clique** no botão **Sign up** da página.

Após completar o registro, volte para o programa **Jitsi**. No menu, **selecione *Ficheiro* > *Nova conta*** e depois **selecione a Rede: SIP**, **digite** o login (ex. terence.the.tester@ostel.co) e a senha criados durante o registro online e **clique em *Adicionar***. Veja a imagem para referência:

![](/sbox/screen/jitsi-pt/15.png)

*Figura 9: Exemplo de janela de "Nova conta" para contas SIP*

  * **Como adicionar ao Jitsi uma conta Jabber/XMPP ou SIP já existente**

Se você já possui uma conta Jabber/XMPP ou SIP, pode adicioná-la ao **Jitsi**. **Selecione *Ficheiro* > *Nova conta*** no menu do programa e escolha a **Rede** apropriada (XMPP ou SIP, dependendo do tipo de conta).


<a name="2.2.3"></a>
### 2.2.3 Como adicionar uma conta do Facebook ###

O **Facebook** tem duas configurações que talvez você tenha que mudar para que o **Jitsi** consiga se conectar com o Facebook Chat.

  * **Facebook username** 

O **Facebook** pede um *username* (ou nome de usuária/o) para que o **Jitsi** consiga se conectar ao chat do Facebook. Normalmente, quem tem um perfil no **Facebook** já possui esse *username*. Para verificá-lo, **acesse** sua conta do **Facebook** e entre na sua Página ou Linha do Tempo: o *username* é o que aparece na barra de endereços do navegador depois do *https://www.facebook.com/*. O *username* também aparece no e-mail do **Facebook** relacionado à sua conta pessoal (ex: username@facebook.com).

Você pode ver, mudar ou criar um *username* (ou nome de usuária/o) na seção *Configurações de Conta > Configurações Gerais* ou acessando o endereço [https://www.facebook.com/username](https://www.facebook.com/username). Para configurá-lo, o **Facebook** pode requerer uma verificação de conta - durante o processo de validação, será preciso fornecer ao **Facebook** um número de telefone celular, ao qual será enviada uma mensagem de texto SMS. Para mais detalhes veja [a explicação do Facebook sobre este assunto](https://www.facebook.com/help/329992603752372/).

  * **Configurações de Aplicativos**

A "plataforma de aplicativos" do **Facebook** deve estar ativada para que o **Jitsi** consiga se contectar ao chat do serviço. Na sua página do **Facebook**, entre em *Configurações de Conta > Aplicativos* e verifique se a opção para *Aplicativos em Uso* está ligada (*On*). Ela ativa a "plataforma de aplicativos" relacionados à sua conta.

**Note** que ativar a "plataforma de aplicativos" abre muitos dos seus dados no **Facebook** a desenvolvedores externos de programas. Tais dados ficam disponíveis não só para os aplicativos que você utiliza; também ficam expostos a programas usados por quaisquer pessoas com quem você se relacione. 

Depois de ativada a "plataforma de aplicativos" do **Facebook**, não se esqueça de verificar as configurações em *Aplicativos usados por outros*. Elas permitem esconder algumas informações pessoais suas de programas usados por alguém em sua rede de contatos. Infelizmente, o **Facebook** não permite esconder todos os seus dados pessoais. Alguns tipos de informação como sua lista de pessoas conhecidas, gênero ou coisas que você tornou públicas ficarão disponíveis enquanto a "plataforma de aplicativos" estiver ligada. Cabe a você decidir se compensa abrir essas informações como troca para usar o serviço de bate papo integrado ao **Jitsi**.

Agora é possível adicionar a sua conta do **Facebook** no **Jitsi**. Para isso, siga os passos abaixo:

**Passo 1**. No menu princial, **selecione *Ficheiro > Nova conta***.

**Passo 2**. Na janela de Nova conta, **selecione** *Facebook* no campo *Rede*, **insira** seu *username* e *senha* e **clique** em **Adicionar**.

![](/sbox/screen/jitsi-pt/16.png)

*Figura 10: Exemplo de janela de "Nova conta" para contas do Facebook*


<a name="2.3"></a>
## 2.3 Como alterar senhas de contas usando o Jitsi ##

Saber como alterar a senha de cada uma das contas que você possui é um fator de segurança importante. Muitos dos serviços que podem ser usados com o **Jitsi** permitem modificar a senha de acesso em suas configurações, acessíveis através de uma página na internet.

Entretanto, algumas contas Jabber/XMPP e SIP não são gerenciadas por páginas na internet. É possível alterar suas senhas usando o Jitsi, de acordo com os passos abaixo:

**Passo 1**. No menu, **vá até *Ferramentas* > *Preferências*** e **selecione** a aba de **Contas**.

![](/sbox/screen/jitsi-pt/17.png)

*Figura 11: Janela de Preferências com uma conta selecionada*

**Passo 2**. **Clique** no botão **Editar**, na parte de baixo da janela, para ativar a seguinte tela:

![](/sbox/screen/jitsi-pt/18.png)

*Figura 12: A janela do Menu de Registro de Contas com o botão de alterar senha na parte de baixo.

**Passo 3**. **Clique** no botão **Alterar Senha** para ativar a janela de *Alteração de Senhas*:

![](/sbox/screen/jitsi-pt/19.png)

*Figura 13: A janela de Alteração de Senhas*

**Passo 4**. **Insira** a nova senha e **repita-a** no campo abaixo. **Clique** no botão **OK** para fechar esta janela.

**Passo 5**. Feche o Menu de Registro de Contas.


<a name="2.4"></a>
## 2.4 Como configurar o Jitsi para aumentar a segurança do programa ##


<a name="2.4.1"></a>
### 2.4.1 Como desabilitar e remover o histórico de chamadas e das conversas de bate papo ##

Por padrão, o **Jitsi** armazena informações sobre as chamadas de voz feitas  e recebidas, assim como o histórico das mensagens de texto - todas as mensagens que você escreveu e recebeu. Você pode acessar as chamadas de voz ou de vídeo **clicando** no ícone do relógio, na janela principal do programa:

![](/sbox/screen/jitsi-pt/20.png)

*Figura 14: Parte de cima da janela principal do Jitsi, com o botão do histórico de chamadas em destaque*

Você pode ver o histórico das conversas **clicando** no ícone da ampulheta dentro da janela de chat, enquanto estiver conversando com alguém:

![](/sbox/screen/jitsi-pt/21.png)

*Figura 15: A janela de chat com o botão de histórico em destaque*

Estas informações são coletadas e armazenadas no seu computador. **Mesmo que você criptografe as conversas de bate papo com OTR, todas as mensagens enviadas e recebidas serão salvas no seu computador em formato de texto aberto.** O mesmo acontece nos computadores das pessoas com quem você se comunicar.

Para prevenir que o Jitsi salve esse tipo de informação e para remover as já armazenadas, **você e seus contatos devem realizar os seguintes passos**.

#### Para desabilitar o armazenamento de dados pelo Jitsi: ####

**Passo 1**. No menu, **vá** em ***Ferramentas* > *Preferências*** e **selecione** a aba de **Configurações Gerais**.

![](/sbox/screen/jitsi-pt/22.png)

*Figura 16: Janela de *Preferências*, aba de "Configurações Gerais": a opção "Registrar histórico de conversas" ('Log chat history') desabilitada*

**Passo 2**. Na janela de *Preferências*, **vá até** a aba **Configurações Avançadas**, **selecione** a seção *Logs* e **desmarque** a opção *Habilitar registro de pacotes*, como na imagem abaixo:

![](/sbox/screen/jitsi-pt/23.png)

*Figura 17: Janela "Preferências", aba "Configurações Avançadas": a seção de "Logs" com a opção "Habilitar guarda de pacotes" desativada.*

Suas alterações entrarão em vigor após **reiniciar o Jitsi**.


#### Para remover as informações já armazenadas sobre suas chamadas e mensagens de texto: ####

**Passo 1**. **Feche** o Jitsi. 

**Passo 2**. Dentro da pasta de *perfil do usuária/o* do **Jitsi**, apague a pasta inteira de histórico de registros *history_ver1.0*. Caso queira remover apenas parte dos históricos, elimine a subpasta correspondente dentro de *history_ver1.0*. A localização das pastas de *perfil do usuária/o* e *histórico de registros* dependem do sistema operacional:

  * No Windows XP e versões mais antigas, estão localizadas em *C:\Documents and Settings\&lt;Windows login/user name&gt;\Application Data\Jitsi\history_ver1.0*
  * No Windows Vista, Windows 7 e Windows 8, estão em *C:\Users\&lt;Windows login/user name&gt;\AppData\Roaming\Jitsi\history_ver1.0* (**Note** que a pasta "AppData" pode estar oculta. Veja [como exibir arquivos ocultos](http://windows.microsoft.com/en-us/windows/show-hidden-files)).
  * No Mac OS X, no seguinte endereço, a partir da sua pasta home: *~/Library/Application Support/Jitsi/history_ver1.0*
  * No Linux, no seguinte endereço, a partir da sua pasta home: *~/.jitsi/history_ver1.0* (**Note** que a pasta ".jitsi" pode estar oculta. Veja como [exibir arquivos ocultos no Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/)).

Veja o Capítulo [**6. Como destruir informações sensíveis**](chapter-6), do **Guia de Referência**, para mais informações sobre eliminação segura de informações.


<a name="2.4.2"></a>
### 2.4.2 Como requerer que a troca de mensagens em conversas por texto seja privada ###

É recomendado que você configure o **Jitsi** para solicitar que mensagens de texto sejam privadas e [criptografadas](/pt/glossary#encryption) com [*OTR*](/pt/glossary#OTR) sempre que possível. Para fazer isto, **vá até** o menu **Ferramentas**, **selecione** a aba **Segurança**, **selecione** a sub-aba **Conversar** e **marque** as opções para **Solicitar Mensagens Privadas** na parte de baixo da tela, como demonstrado abaixo:

![](/sbox/screen/jitsi-pt/24.png)

*Figura 18: Janela "Preferências", aba "Segurança", sub-aba "Conversar" com a opção "Solicitar Mensagens Privadas" em destaque*



<a name="2.4.3"></a>
### 2.4.3 Proteja as senhas de suas contas com uma senha mestre ###

É melhor não permitir que o **Jitsi** armazene senhas, pois isso permitirá a qualquer pessoa com acesso a seu computador acessar suas contas simplesmente iniciando o programa ou ver suas senhas ao entrar na janela de *Preferências*.

Portanto, é **altamente recomendado** proteger suas senhas com uma **senha mestre** forte. Uma vez configurada, a senha mestre será solicitada sempre que o programa for iniciado.

**Passo 1**. **Abra** a janela de *Preferências* indo até o menu e **selecionando *Ferramentas* > *Preferências***, **vá até** a aba **Segurança** e a sub-aba ***Palavra-passe***, e **marque *Utilizar senha mestre*** (*Use a master password*) para ativar a janela de ***senha mestre***.

**Passo 2**. Na nova janela, **digite sua senha** como indicado na figura abaixo. Para mais informações sobre como criar uma senha segura, veja o Capítulo [**3: Como criar e manter senhas seguras**](/pt/chapter-3), do **Guia de Referência**.

![](/sbox/screen/jitsi-pt/25.png)

*Figura 19: A janela de "senha mestre"*

**Passo 3**. **Clique** em **OK** para confirmar a senha e ativar a nova janela, que deve dizer ***senha mestre configurada com sucesso***. **Clique** em **OK** para fechá-la e voltar para a janela de *Preferências*, que deve aparecer como na imagem abaixo:

![](/sbox/screen/jitsi-pt/26.png)

*Figura 20: Janela "Preferências", aba "Segurança", sub-aba "Palavra-passe" com a opção "Utilizar senha mestre" indicada*

**Observação**: O botão de ***Alterar senha mestre*** permite que você altere a senha mestre; o botão ***Senhas Salvas*** permite que você acesse a lista de senhas salvas pelo Jitsi e as remova quando necessário.

