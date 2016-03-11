

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Thunderbird

---

Seções nesta página:

- [**2.0 Como instalar o Thunderbird**](#2.0)
- [**2.1 Como desabilitar o indexador e a opção de busca global no Thunderbird**](#2.1)
- [**2.2 Como registrar uma conta de e-mail no Thunderbird**](#2.2)
- [**2.3 Como registrar blogs, feed de notícias e contas de grupos de notícias no Thunderbird**](#2.3)


<a name="2.0"></a>
## 2.0 Como instalar o Thunderbird ##

Para começar a instalação do **Thunderbird**, execute os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/thunderbird-pt/01.png); a janela de diálogo *Abrir arquivo - aviso de segurança* deve aparecer. Se isso acontecer, **clique** em ![](/sbox/screen/thunderbird-pt/02.png) para ativar a janela a seguir:

![](/sbox/screen/thunderbird-pt/03.png)

*Figura 1: A barra de progresso de extração de arquivo*

Após a completa extração do arquivo do **Thunderbird**, a janela *Bem-vindo ao assistente de instalação do Mozilla Thunderbird* deve aparecer.

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a janela *Mozilla Thunderbird - Setup Type*. 

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) na janela *Choose setup options*. A configuração padrão é *Standard* 

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para aceitar as configurações padrão e ativar a tela a seguir:

![](/sbox/screen/thunderbird-pt/05.png)

*Figura 2: A tela de resumo do Mozilla Thunderbird*

**Passo 5**. **Clique** em ![](/sbox/screen/thunderbird-pt/06.png) para iniciar o processo de instalação. A tela de status do progresso **Mozilla Thunderbird - Installing** aparecerá. Após completar o processo de instalação, deve aparecer a janela a seguir:

![](/sbox/screen/thunderbird-pt/07.png)

*Figura 3: Tela de Concluindo o assistente de instalação do Mozilla Thunderbird*

**Passo 6**. **Clique** em ![](/sbox/screen/thunderbird-pt/08.png) para completar o processo de instalação.

**Dica**: O **Thunderbird** abrirá automaticamente se a caixa de opção *Iniciar o Mozilla Thunderbird agora* estiver habilitada, como demonstrado na *Figura 3*, acima. Para abrir o programa no futuro, você pode **clicar duas vezes** no ícone do **Thunderbird** na Área de trabalho ou **selecionar: Programas > Mozilla Thunderbird > Mozilla Thunderbird**.


<a name="2.1"></a>
## 2.1 Como desabilitar o indexador e a opção de busca global no Thunderbird ##

**Atenção**: O recurso *Global Search and Indexer* (*Pesquisa global e indexação*) no **Thunderbird** *deve* ser desligado para otimizar sua performance. Dependendo da quantidade e tamanho dos seus e-mails, esta funcionalidade pode reduzir a velocidade do sistema, ao sobrescrever informações de forma contínua e desnecessária no disco rígido. Como seu disco rígido ficará cada vez mais cheio, deixará mais lentas diversas operações de sistema não relacionadas ao programa.

Para desligar a opção *Global Search and Indexer* (*Busca global e Indexador*), execute os passos a seguir: 

**Passo 1**. **Selecione: Ferramentas > Opções** no console do **Thunderbird** para ativar a janela de *Opções*.

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/09.png) para ativar as abas associadas, como a seguir:

![](/sbox/screen/thunderbird-pt/10.png)

*Figura 4: A janela de Opções exibindo a aba Avançado*

**Passo 3**. **Desmarque** a opção *Ativar pesquisa global e indexão*, na seção de *Configuração avançada* para *desabilitá-la*, como demonstrado abaixo:

![](/sbox/screen/thunderbird-pt/11.png)

*Figura 5: A seção de Configuração avançada*

Agora que a opção está desabilitada, já é possível registrar uma conta de e-mail no **Thunderbird**.


<a name="2.2"></a>
## 2.2 Como registrar uma conta de e-mail no Thunderbird ## 

A janela *Integração de sistema* aparecerá no primeiro login. Esta janela pode ser configurada para *utilizar o Thunderbird como cliente padrão para: e-mail*. Alternativamente, você pode escolher *Pular integração*.

**Passo 1**. Na janela *Bem-vindo ao Thunderbird*, **clique** na opção *ignorar e usar meu e-mail existente*. Isso exibirá uma janela semelhante à seguinte:
 
![](/sbox/screen/thunderbird-pt/12.png)

*Figura 6: Tela Bem-vindo ao Thunderbird*

**Passo 2**. **Digite** seu nome, endereço de correio eletrônico e senha nos campos de texto correspondentes; **desabilite** a opção *lembrar minha senha* para que sua tela seja semelhante à *Figura 7*, abaixo.

![](/sbox/screen/thunderbird-pt/13.png)

*Figura 7: A janela Configurar conta de e-mail*

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/14.png) para ativar a janela seguinte:

![](/sbox/screen/thunderbird-pt/15.png)

*Figura 8: A janela Configurar conta de e-mail, com a opção **IMAP (pastas remotas)** habilitada*

## IMAP e POP: Descrições e utilização ###

O **Internet Message Access Protocol** (**IMAP**) e o **Post Office Protocol** (**POP**) são dois métodos diferentes utilizados para armazenar e receber e-mails.

- **Internet Message Access Protocol** (**IMAP**): Ao utilizar **IMAP** todas as suas pastas (incluindo *Entrada*, *Rascunhos*, *Templates*, *Enviados*, *Lixeira* e todas as demais) são hospedadas no servidor de e-mails. Com isso, você pode acessá-las a partir de computadores diferentes. Todas as mensagens ficarão no servidor e, inicialmente, apenas o cabeçalho ou a barra de título das mensagens (contendo informações como data e hora, assunto, nome de remetente etc.) são baixados para serem exibidos no seu computador. As mensagens completas só serão baixadas ao abrir o e-mail. O **Thunderbird** também pode ser configurado para armazenar cópias de todas as mensagens ou de algumas pastas em seu computador, de modo que você possa trabalhar com elas quando estiver offline (sem conexão com a internet). No **IMAP**, quando você apaga mensagens ou pastas, o faz *tanto* no seu computador *como* no servidor.

- **Post Office Protocol version 3** (**POP3**): Ao utilizar o **POP3**, apenas a *Entrada* (a pasta onde são entregues as novas mensagens) ficará no servidor; todas as demais pastas são armazenadas apenas no seu computador. Você deve escolher entre manter as mensagens na pasta *Entrada* do servidor após tê-las baixado para o computador ou apagá-las de lá. Se você acessa sua conta de e-mail a partir de computadores diferentes, será capaz de visualizar apenas as mensagens na pasta *Entrada* (novas e velhas mensagens não apagadas). **Observação**: dependendo da configuração do servidor, cópias de e-mails enviados podem ser armazenadas no servidor na pasta *Enviados*. Vale a pena checar isso.

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/16.png) para criar sua conta e ativar o console do **Thunderbird** com sua conta de e-mail exibida na barra lateral à esquerda, como a seguir:

![](/sbox/screen/thunderbird-pt/17.png)

*Figura 9: A interface principal do Mozilla Thunderbird exibindo a nova conta criada, do Riseup*

**Observação**: Para adicionar outra conta de e-mail, **clique** em **Pastas Locais > Contas > Criar nova conta: E-mail** para ativar a *Figura 7* desta seção. Repita do **Passo 2** ao **Passo 4**.

Após haver registrado sua conta de e-mail no **Thunderbird**, a próxima vez que abrir a interface principal, o programa pedirá que você coloque sua senha para cada conta, como a seguir: 

![](/sbox/screen/thunderbird-pt/20.png)

*Figura 10: A janela de Requisição de senha do servidor de e-mails*

**Observação**: Embora os recursos de gravação ou 'lembrança' de senhas geralmente não sejam recomendandos do ponto de vista de privacidade e segurança da internet, o **Thunderbird** suporta o recurso *Master Password* (*Senha Mestra*). Tal recurso permite utilizar uma senha para proteger todas as outras, relacionadas às diferentes contas e informadas durante o processo de instalação. Para mais informações sobre este recurso, leia a Seção [**3.3 Como configurar as abas de segurança no Thunderbird**](/pt/thunderbird_security#3.3) - **Aba de Senha**.


<a name="2.3"></a>
## 2.3 Como registrar blogs, feed de notícias e contas de grupos de notícias no Thunderbird ##

Para criar e registrar uma conta para blogs, feeds de notícias e grupos de notícias, execute os seguintes passos:

**Passo 1**. Selecione sua conta na barra lateral à esquerda e **clique** em **Contas > Feeds** para ativar a janela *Feed Account Wizard* abaixo:

![](/sbox/screen/thunderbird-pt/21.png)

*Figura 11: A janela Feed Account Wizard - Nome da conta*

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a seguinte janela: 

![](/sbox/screen/thunderbird-pt/22.png)

*Figura 12: A janela Feed Account Wizard - Resumo*

**Passo 5**. **Clique** em ![](/sbox/screen/thunderbird-pt/08.png) para completar o processo de configuração da conta e voltar ao console do **Thunderbird**.

Agora que o **Thunderbird** está configurado corretamente, para uma melhor utilização, veja a próxima sessão, [**Como configurar as opções de segurança do Thunderbird**](/pt/thunderbird_security).

