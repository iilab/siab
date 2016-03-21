

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

Seções nesta página:

- [**3.0 Sobre as opções de segurança do Thunderbird**](#3.0)
- [**3.1 Como desabilitar o painel de pré-visualização no Thunderbird**](#3.1)
- [**3.2 Como desabilitar o recurso HTML no Thunderbird**](#3.2)
- [**3.3 Como configurar as opções de segurança**](#3.3)
- [**3.4 Como habilitar o filtro de spam nas configurações de conta**](#3.4)


<a name="3.0"></a>
## 3.0 Sobre as opções de segurança no Thunderbird ##

No contexto do **Mozilla Thunderbird**, a segurança geralmente refere-se a proteger seu computador de mensagens de e-mails prejudiciais ou maliciosas. Algumas podem ser apenas spam; outras podem conter vírus e spyware, os chamados programas espiões. Existem várias opções que devem ser configuradas, desabilitadas ou ativadas no **Mozilla Thunderbird** para fortalecer a habilidade de proteger seu sistema de ataques originados de e-mails. É também *absolutamente crucial* que você tenha instalados um software antimalware e um firewall.

Para mais informações sobre como evitar a contaminação por programas  prejudiciais e maliciosos, veja o Capítulo [**1. Como proteger seu computador de programas maliciosos e hackers**](/pt/chapter-1), do **Guia de Referência**, para mais informações sobre ferramentas como o [**Avast - Antivírus**](/pt/avast_main), [**Comodo Firewall**](/pt/comodofirewall_main) e [**Spybot - Antispyware**](/pt/spybot_main).


<a name="3.1"></a>
## 3.1 Como desativar o painel de pré-visualização no Thunderbird ##

A janela principal do **Thunderbird** é dividida em três áreas. A barra lateral exibe as pastas para sua conta de e-mail; o lado direito mostra a lista de mensagens; e o painel de baixo exibe uma *pré-visualização* do e-mail selecionado. A visualização é ativada automaticamente quando uma mensagem é selecionada. 

**Observação**: Caso um e-mail contenha qualquer código malicioso, o painel de *pré-visualização* de mensagens pode ativá-lo. Portanto, é uma boa ideia desabilitar esta opção. 

![](/sbox/screen/thunderbird-pt/23.png)

*Figura 1: A interface principal do Thunderbird*

Para desabilitar o painel de pré-visualização, execute os passos a seguir: 

**Passo 1**. **Clique** em ![](/sbox/screen/thunderbird-pt/24a.png) para exibir o *Menu do Thunderbird*. Então, **selecione: Options > Layout > Painel de Mensagens F8** para desabilitar o painel de pré-visualização, como a seguir: 

![](/sbox/screen/thunderbird-pt/24.png)

*Figura 2: O menu de Opções exibindo o sub-menu Layout, com a opção Painel de mensagens desselecionada*

O *painel de mensagens* desaparecerá e você terá de **clicar duas vezes** em um e-mail para ler seu conteúdo. Se uma mensagem parecer suspeita (talvez por ter um título de assunto inesperado ou irrelevante, ou ter vindo de um remetente desconhecido), você agora pode escolher apagá-la sem haver pré-visualizado seu conteúdo.


<a name="3.2"></a>
## 3.2 Como desabilitar o recurso HTML no Thunderbird ##

O **Thunderbird** permite utilizar o **HyperText Markup Language** (**HTML**)  para compor e ler mensagens. Isso permite receber e enviar mensagens que incluem cores, fontes, imagens e outros recursos de formatação. No entanto, o **HTML** é a mesma linguagem usada nas páginas da internet. Ver mensagens com formatação **HTML**, pode te expor a e-mails maliciosos, que representam alguns dos mesmos tipos de ameaças colocados por páginas da web. 
 
Para desabilitar o recurso de formatação **HTML**, execute os seguintes passos: 

**Passo 1**. **Clique** em ![](/sbox/screen/thunderbird-pt/24a.png) para exibir o *Menu do Thunderbird* e **selecione: Opções > Exibir > Formatação da mensagem como > Sem Formatação**, como a seguir: 

![](/sbox/screen/thunderbird-pt/25.png)

*Figura 3: O Menu de visualização exibindo o sub-menu Formatação da mensagem, com a opção Sem formatação selecionada*


<a name="3.3"></a>
### 3.3 Como configurar as opções de segurança ###

O **Thunderbird** possui dois filtros de spam que podem te ajudar a determinar quais de suas mensagens recebidas são spam. Por padrão, tais filtros estão desabilitados. Mesmo após terem sido habilitados, você continuará a receber mensagens indesejadas, mas o **Thunderbird** as classificará e encaminhará automaticamente  para a pasta *Spam*. 

Trapaças via e-mail - conhecidas como e-mails *phishing* - geralmente tentam fazer com que você clique em um link incorporado à mensagem. Frequentemente, estes links direcionam seu navegador de internet para uma página da internet que tentará infectar seu computador com vírus. Em outros casos, o link te levará a um site que parece ser legítimo, mas que tentará te induzir a inserir um login e senha válidos, que podem ser utilizados ou vendidos para propósitos comerciais ou maliciosos. 

O **Thunderbird** pode te ajudar a identificar e alertar sobre e-mails como estes. Adicionalmente, ferramentas que podem te ajudar na prevenção de infecções por sites maliciosos são descritas na seção [**Outras extensões úteis ao Firefox**](/pt/firefox_others), do Guia Prático do [**Firefox - Navegador seguro de internet**](/pt/firefox_main).

O primeiro conjunto controles de segurança e opções de spam são acessados por meio da janela *Opções - Segurança*, na qual a maioria dessas opções de segurança é configurada. Para acessá-la, execute os passos adiante:

**Passo 1**. **Selecione: Menu > Opções** para ativar a janela *Opções*.

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/26.png) para exibir a tela a seguir:

![](/sbox/screen/thunderbird-pt/27.png)

*Figura 4: A janela de Segurança exibindo as abas associadas*

### Aba Antispam  ###

**Passo 1**. **Selecione** a opção relevante na aba *Antispam*, como demonstrado na *Figura 4*, acima, para permitir que o **Thunderbird** exclua as mensagens que você determinou como sendo lixo eletrônico. Configurações adicionais de spam são descritas mais adiante nesta seção.

### Aba Antifraude ###

**Passo 1**. **Selecione** a opção *Alertar se a mensagem exibida for um possível golpe*, para permitir que o **Thunderbird** analise as mensagem procurando por fraudes nos e-mails, como a seguir: 

![](/sbox/screen/thunderbird-pt/28.png)

*Figura 5: A aba Antifraude* 

### Aba Antivírus  ###

**Passo 1**. **Clique** na aba *Antivírus* para ativar a janela seguinte: 

![](/sbox/screen/thunderbird-pt/29.png)

*Figura 6: A aba Antivírus*

Esta opção permite que o seu software antivírus escaneie e isole mensagens individuais ao chegarem. Sem esta opção habilitada, é possivel que sua caixa *Entrada* inteira possa ser colocada em 'quarentena' caso receba uma mensagem infectada.

**Observação**: Usá-la pressupõe que você tenha um programa antivírus instalado e funcionando. Leia o Guia Prático do [**Avast - Antivírus**](/pt/avast_main) para mais informações sobre como instalar e configurar um software antivírus.

### Aba Senhas ###

**Passo 2**. **Clique** na aba *Senhas* para ativar a janela a seguir: 

![](/sbox/screen/thunderbird-pt/30.png)

*Figura 7: A aba Senhas*

**Importante:** Recomendamos fortemente que você mantenha suas senhas seguras e privadas usando um software desenvolvido precisamente para este fim. Veja o Guia Prático do [**KeePass - Armazenamento seguro de senhas**](/pt/keepass_main) para mais informações sobre isso. 

**Observação**: As opções na aba *Senha* só funcionarão se você selecionou a opção *Memorizar senha*, na primeira tela da *Configuração de conta de e-mail* ao registrar sua conta de e-mail no **Thunderbird**. 

**Passo 1**. **Clique** em ![](/sbox/screen/thunderbird-pt/31.png) para ativar a seguinte tela:

![](/sbox/screen/thunderbird-pt/32.png)

*Figura 8: A janela Senhas memorizadas*

A janela *Senhas memorizadas* permite remover ou exibir todas as senhas correspondentes a cada uma de suas contas. No entanto, para aumentar sua privacidade e segurança, é possível definir uma *senha mestra* para proteger o acesso às suas contas de e-mail e tornar todas as senhas inacessíveis a qualquer pessoa que tenha familiaridade com as opções de senha do **Thunderbird**.

**Passo 3**. **Selecione** a opção *Usar uma senha mestra*, como exibido na *Figura 7*, para habilitar o botão *Modificar senha mestra...*.

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/33.png) para ativar a tela a seguir:

![](/sbox/screen/thunderbird-pt/34.png)

*Figura 9: A janela Modificar senha mestra*

**Passo 5**. **Digite** uma senha apropriadamente forte que apenas você se lembrará e **clique** em ![](/sbox/screen/thunderbird-pt/35.png) para confirmá-la como sua *senha mestra*. 

### Conteúdo da Web ###

Um cookie é um pequeno pedaço de texto que seu navegador utiliza para autenticar ou identificar um determinado site da internet. A opção *Web content* permite especificar qual blog, feed de notícias ou grupo de notícias são confiáveis e seguros.  

**Passo 1**. **Clique** em ![](/sbox/screen/thunderbird-pt/36.png) para exibir as opções *Web content*, como a seguir:

![](/sbox/screen/thunderbird-pt/37.png)

*Figura 10: A aba Privacidade*

**Passo 2**. Como segurança adicional, na opção *Keep until:*, **selecione** o item *I close Thunderbird*, para apagar esses cookies ao fechar o **Thunderbird**.


<a name="3.4"></a>
### 3.4 Como habilitar o filtro de spam nas configurações de conta ###

O segundo tipo de filtro de spam do **Thunderbird** está disponível através da janela *Configurar contas - Antispam*. Por padrão, tais filtros estão desabilitados, devendo ser ativados caso deseje usá-los. Sempre que chegarem spams, o **Thunderbird** os classificará automaticamente como tal e os colocará na pasta *Spam* associada à respectiva conta que o recebeu.

**Passo 1**. **Selecione: Ferramentas > Configurar contas** para ativar a janela *Configurar contas*. 

**Passo 2**. **Selecione** a opção *Junk Settings* associada a uma conta especifica do **Gmail** ou do **Riseup**, na barra lateral.

**Passo 3**. **Habilite** a opção *Junk Settings* de modo que sua tela de *Account Settings - Junk Settings* se pareça como a imagem a seguir: 

![](/sbox/screen/thunderbird-pt/38.png)

*Figura 11: A janela Configuração de contas - Junk Settings*

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/35.png) para completar a configuração da janela *Configurar contas*.

**Observação**: As opções *Antispam* devem ser configuradas separadamente para cada conta. Assim, lixos eletrônicos relacionados a uma conta do **Gmail** ou a uma conta **Riseup** serão colocados em uma pasta de *Excluídos* correspondente àquela conta. Alternativamente, é possível designar uma *pasta local* para receber spams de todas as suas contas. 

![](/sbox/screen/thunderbird-pt/39.png)

*Figura 12: Configurações de conta - a janela de Configuração antispam, exibindo as configurações para uma pasta central de lixo eletrônico*

**Passo 1**. **Selecione** a opção *Antispam* diretamente abaixo de *Pastas locais*, na barra lateral.

**Passo 2**. No menu expandido de *Pasta "Spam" conta:*, **selecione** o item *Pastas locais*, como demonstrado na *Figura 13*.

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/35.png) para completar a configuração da janela *Configuração de contas*.

Agora que você configurou com êxito as várias opções de segurança e os parâmetros de lixo eletrônico do **Thunderbird**, dirija-se à próxima seção, [**Como usar Enigmail com GnuPG no Thunderbird**](/pt/thuderbird_encryption). 

