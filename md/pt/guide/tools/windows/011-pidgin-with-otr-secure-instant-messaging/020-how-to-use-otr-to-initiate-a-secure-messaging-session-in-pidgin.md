

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Seções nessa página:

- [**3.0 Sobre o Pidgin e o OTR**](#3.0) 
- [**3.1 Como configurar o plugin Pidgin-OTR**](#3.1) 
- [**3.2 Primeiro passo - Como gerar uma chave privada e exibir sua impressão digital**](#3.2) 
- [**3.3 Segundo passo - Como autenticar uma sessão de mensagens**](#3.3)
- [**3.4 Terceiro passo - Como autenticar a identidade de seu correspondente**](#3.4)


<a name="3.0"> </a> 
## 3.0 Sobre o Pidgin e o OTR ## 

Tanto você como o seu correspondente devem configurar o plug-in **OTR** antes de serem capazes de realizar sessões privadas e seguras de troca de mensagens instantâneas (**MI**). O plugin **OTR** detecta automaticamente quando ambas as partes o possuem instalado e configurado corretamente.

**Observação**: Se você requisitar uma conversa privada com alguém que não possui o **OTR** instalado ou configurado, o plugin enviará automaticamente uma mensagem explicando como obtê-lo. 


<a name="3.1"> </a> 
## 3.1 Como configurar o plugin Pidgin-OTR ## 

Para ativar o plugin **OTR**, execute os seguintes passos: 

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/pidgin-pt/14.png) ou **selecione Iniciar > Todos os Programas > Pidgin** para iniciar o **Pidgin**. Ative a janela *Lista de Amigos* (*Figura 1*). 

**Passo 2**. **Abra** o menu *Ferramentas* e *selecione* o item *Plugins* da seguinte forma: 

![](/sbox/screen/pidgin-pt/39.png) 

*Figura 1: A janela de Lista de amigos, com o item Plugins do menu de Ferramentas selecionado* 

Isso ativará a janela de *Plugins* da seguinte forma: 

**Passo 3**. **Role as opções** até o item *Off-the-Record Messaging* e **marque** a caixa de seleção para habilitá-lo. 

![](/sbox/screen/pidgin-pt/40.png)

*Figura 2: A janela de Plugins do Pidgin, com o Off-the-Record selecionado* 

**Passo 4**. **Clique** em ![](/sbox/screen/pidgin-pt/41.png) para acessar as telas de configuração do *Off-the-Record*. 

Basicamente, são três as etapas envolvidas na configuração do **OTR** para habilitar sessões de bate-papo privadas e seguras, conforme a explicação abaixo:

- **Primeiro passo**: Envolve gerar uma chave privada única, associada à sua conta, e exibir sua impressão digital. 

Os dois passos seguintes estão relacionados à segurança da sessão da troca de mensagens e à autenticação das pessoas com quem você conversa. 

- **Segundo passo**: Um dos correspondentes solicita iniciar uma sessão de mensagens privadas e seguras com outra pessoa online. 

- **Terceiro passo**: Envolve *autenticar*, ou verificar a identidade de seu correspondente do **Pidgin**. (**Importante**: no **Pidgin**, um correspondente é alguém com quem você quer estabelecer sessões de troca de mensagens instantâneas ou bate-papo). O processo de verificar a identidade de um correpondente no **Pidgin** é conhecido como *Autenticação* e significa estabelecer que seu correspondente é *exatamente* a pessoa que afirma ser. 


<a name="3.2"> </a> 
## 3.2 Primeiro passo - Como gerar uma chave privada e exibir sua impressão digital ## 

Sessões de bate-papo seguras no **Pidgin** são ativadas por meio da geração de uma *chave privada* para a conta em questão. A janela de configuração do *Off-the-Record* é dividida nas abas *Config* e *Impressões digitais conhecidas*.

A aba *Config* é usada para gerar uma *chave* para cada uma de suas contas e para estabelecer as opções específicas do **OTR**. Já a aba *Impressões digitais conhecidas* contém uma lista com as impressões digitais das chaves de seus contatos. Você deve possuir uma chave para todos correspondentes com quem você gostaria de bater papo de forma privada. 

![](/sbox/screen/pidgin-pt/42.png) 

*Figura 3: A tela do Off-the-Record exibindo a aba de configuração* 

**Passo 1**. Para otimizar a sua privacidade, **habilite** as opções *Permitir mensagens privadas*, *Iniciar automaticamente mensagens privadas* e *Não anotar conversações OTR* na aba de Configuração, como mostrado na *Figura 3*, acima. 

**Passo 2 **. **Clique** em ![](/sbox/screen/pidgin-pt/43.png) para gerar a sua chave de segurança. A tela informando que a chave privada está sendo gerada se assemelha à seguinte:

![](/sbox/screen/pidgin-pt/44.png) 

*Figura 4: A caixa de confirmação de geração da chave privada* 

**Importante**: Seu correspondente deve executar os mesmos passos para sua respectiva conta. 

**Passo 3**. **Clique** em ![](/sbox/screen/pidgin-pt/46.png) após gerar a chave privada, que se assemelha à seguinte: 

![](/sbox/screen/pidgin-pt/45.png)

*Figura 5: Exemplo de uma impressão digital da chave gerada pelo OTR* 

**Importante**: Você criou agora uma chave privada para a sua conta no seu computador atual. Ela será usada para criptografar suas conversas de forma que ninguém possa lê-las, mesmo caso alguém consiga monitorar suas sessões de bate-papo. A impressão digital é uma longa sequência de letras e números usada ​​para identificar a chave de uma determinada conta, como mostrado na *Figura 5*, acima. 

O **Pidgin** salva automaticamente as impressões digitais suas e de seus amigos no computador que você estiver usando, para que não tenha de se lembrar delas. Porém, se você reinstalar o **Pidgin** ou mudar para outra máquina, terá de gerar uma nova chave e reautenticar todos os seus correspondentes ou mover a sua chave e as impressões digitais de seus contatos para aquele novo computador. Para fazer isso, é preciso copiar o conteúdo da pasta %APPDATA%\\.purple (~/.purple no Linux ou Mac) para a pasta correspondente, no novo computador. 


<a name="3.3"> </a> 
## Segundo passo - Como autenticar uma sessão de mensagens ## 

**Passo 1**. **Clique duas vezes** na conta de um correspondente online para iniciar uma nova conversa. Se ambos têm o plugin **OTR** instalado e configurado corretamente, você notará o aparecimento de um novo botão do **OTR** no canto inferior direito da janela do bate-papo. 

![](/sbox/screen/pidgin-pt/47.png)

*Figura 6: A janela de mensagens Pidgin exibindo o ícone OTR* 

**Passo 2**. **Clique** em ![](/sbox/screen/pidgin-pt/48.png) para ativar o menu, e em seguida, selecione a opção *Start private conversation (Iniciar conversa privada)* da seguinte maneira: 

![](/sbox/screen/pidgin-pt/49.png)

*Figura 7: O menu com o item Start private conversation (Iniciar conversa privada) selecionado* 

Sua **janela de mensagem do Pidgin**, então, se assemelhará à seguinte tela:

![](/sbox/screen/pidgin-pt/50.png)

*Figura 8: A janela de mensagem do Pidgin exibindo o botão Unverified (Não verificado)* 

**Importante**: O **Pidgin** começará a conversar e gerar mensagens automaticamente com o programa de bate-papo do seu correspondente sempre que você habilitar uma sessão de bate-papo privada e segura. Como resultado, o ![](/sbox/screen/pidgin-pt/48.png) **botão OTR** mudará para ![](/sbox/screen/pidgin-pt/51a.png), indicando que você habilitou uma conversa criptografada com seu contato. 

**Aviso**! Embora a conversa já seja segura, a identidade de seu correspondente ainda não foi *verificada*. Tenha cuidado, pois a pessoa com quem você está conversando pode ser alguém *fingindo* ser quem você acreditava seu correspondente.


<a name="3.4"> </a> 
## 3.4 Terceiro passo - Como autenticar a identidade de seu correspondente ## 

Existem três métodos possíveis de identificação para autenticar o seu correspondente no **Pidgin**. Você pode usar (1) uma frase pré-estabelecida, um código secreto ou uma palavra; (2) fazer uma pergunta, cuja resposta só é conhecida por você e por seu correspondente; ou (3) verificar manualmente as impressões digitais de suas chaves usando um meio diferente para esta comunicação de confirmação específica. 


### O uso de uma frase, código secreto ou palavra ### 

Você pode combinar com antecedência com seu correspondente uma frase ou palavra de código, seja em um momento em que vocês se encontrem pessoalmente, seja por um meio alternativo de comunicação (como uma conversa por telefone, via bate-papo pelo [**Jitsi**](/pt/jitsi) ou trocando mensagens de texto pelo celular). Uma vez que ambos digitem a mesma frase, código ou palavra no **Pidgin**, a sessão será autenticada. 

**Importante**: A função de reconhecimento de palavras ou código secreto do **OTR** é sensível a caixa alta e baixa, ou seja, considera as diferenças entre letras maiúsculas (A, B, C) e letras minúsculas (a, b, c). Tenha isso em mente ao inventar uma frase, palavra ou código secreto! 

**Passo 1**. Clique no botão *OTR* na janela de bate-papo e, em seguida, **selecione** o item *Authenticate Buddy (Autenticação de correspondente)* da seguinte forma: 

![](/sbox/screen/pidgin-pt/52.png)

*Figura 9: O menu Unverified (Não confirmado) com o item Authenticate buddy (Autenticar correspondente) selecionado* 

Isso ativará a janela *Authenticate buddy (Autenticar correspondente)*, que pede que você selecione um método de Autenticação. 

**Passo 2**. **Clique** em ![](/sbox/screen/pidgin-pt/53.png) e **selecione** *Shared Secret (Compartilhar segredo)* da seguinte forma: 

![](/sbox/screen/pidgin-pt/54.png)

*Figura 10: A visualização da lista da tela Authenticate buddy (autenticar correspondente)* 

**Passo 3**. **Digite** a palavra, código secreto ou frase da seguinte forma: 

![](/sbox/screen/pidgin-pt/55.png)

*Figura 11: A tela Shared Secret (Segredo compartilhado)* 

**Passo 4**. **Clique** em ![](/sbox/screen/pidgin-pt/56.png) para ativar a tela a seguir: 

![](/sbox/screen/pidgin-pt/58.png)

*Figura 12: A janela Authenticate Buddy (Autenticar correspondente), com um correspondente fictício* 

**Observação**: Neste momento, seu correspondente verá a janela mostrada na *Figura 13* e terá de digitar a mesma palavra, código ou frase. Se forem iguais, a sessão será autenticada.

![](/sbox/screen/pidgin-pt/57.png)

*Figura 13: A janela Authenticate Buddy (Autenticar correspondente), com um correspondente fictício* 

Assim que a sessão for autenticada, o *botão OTR* mudará para ![](/sbox/screen/pidgin-pt/51.png). A sessão agora está segura e você pode ter certeza de que está realmente falando com seu correspondente. 


### Método de Perguntas e Respostas ### 

Outro método de autenticação é através de pergunta e resposta. Crie uma pergunta e uma resposta para seu correspondente. Depois de ler sua pergunta, seu contato deve digitar a resposta *exata*. Se esta corresponder à sua, a identidade de seu correspondente será autenticada automaticamente. 

**Passo 1**. **Clique** no menu *OTR* na janela de mensagens ativa para ativar o menu pop-up correspondente. Em seguida, **selecione** o item *Authenticate Buddy (Autenticar correspondente)*, como indicado na *Figura 9*.

![](/sbox/screen/pidgin-pt/50.png)

*Figura 14: A janela de bate-papo do Pidgin exibindo o ícone OTR* 

Uma janela de *Authenticate Buddy (Autenticar correspondente)* solicitando a escolha do método de Autenticação. 

**Passo 2**. **Clique** no menu e **selecione** o item *Pergunta e resposta* da seguinte maneira: 

![](/sbox/screen/pidgin-pt/60.png)

*Figura 15: A tela de autenticação do correspondente* 

**Passo 3**. **Digite** uma pergunta e uma resposta. A pergunta será enviada para o seu correspondente. 

![](/sbox/screen/pidgin-pt/61.png)

*Figura 16: A tela de Pergunta e Resposta* 

Se a resposta do seu contato corresponder à sua, isso significa que suas identidades foram autenticadas ou verificadas mutuamente, e que ambas as partes são quem dizem ser! 

Assim que a sessão for autenticada, o *botão OTR* mudará para ![](/sbox/screen/pidgin-pt/51.png). A sessão agora está segura e você pode ter certeza de que está realmente falando com seu correspondente. 


### Verificação manual da impressão digital ### 

O terceiro método de autenticar o correspondente é a verificação de impressões digitais. Por este método, é preciso conferir as impressões digitais que são exibidas tanto para você como para seu contato usando outro canal de comunicação (como um e-mail seguro ou chamada de voz). Se as impressões digitais trocadas forem as mesmas, você poderá autenticar a sessão.

![](/sbox/screen/pidgin-pt/79.png)

*Figura 17: A tela de verificação da impressão digital.*

Observe que quando você **Selecionar > Lista de Amigos > Ferramentas > Plugins > Off The Record Messaging > Configurar Plugin**, a aba de impressões digitais *Conhecidas* exibe a conta do seu correspondente junto a uma mensagem informando que a identidade foi verificada. 

![](/sbox/screen/pidgin-pt/62.png)

*Figura 18: A tela Off the-Record Messaging exibindo a aba de impressões digitais conhecidas* 

Parabéns! Você agora pode fazer sessões de bate-papo privadas. Das próximas vezes que você e seu correspondente usarem os mesmos computadores, poderão pular o primeiro e o terceiro passos acima. Basta apenas que uma das pessoas solicite uma conexão segura e a outra aceite.

