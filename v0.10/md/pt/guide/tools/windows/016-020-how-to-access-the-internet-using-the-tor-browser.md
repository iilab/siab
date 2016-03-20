

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

- [**3.0 Como se conectar à Rede Tor**](#3.0)
- [**3.1.1 - Acesso direto**](#3.1.1)
- [**3.1.2 - Acesso restrito**](#3.1.2)
- [**3.2 Como reconfigurar o acesso à Rede Tor**](#3.2)
- [**3.3 Como obter endereços de ponte**](#3.3)

<a name="3.0"></a>
## 3.0 Como se conectar à Rede Tor ##

Quando você iniciar o **Navegador Tor** pela primeira vez, a opção de como acessar a internet será exibida:

- [Acesso Direto](#3.1.1):  Selecione essa opção se o seu acesso à internet não é restrito e se o uso do **Tor** **não é** bloqueado, banido ou monitorado onde você está.

- [Acesso Restrito](#3.1.2): Selecione essa opção se seu acesso à internet é restrito ou se o uso do **Tor** **é** bloqueado, banido ou monitorado onde você está.

Essas opções podem ser modificadas a qualquer momento a partir do **Navegador Tor** sem precisar reinstalar o programa, o que talvez precise ser feito caso sua localização mude ou se você estiver visitando um país diferente.

Posteriormente quando você iniciar o **Navegador Tor**, ele conectará com a rede **Tor** sem precisar de nenhuma configuração a mais.


<a name="3.1.1"></a>
## 3.1.1 Como se conectar à Rede Tor - Acesso direto ##

Para configurar o **Navegador Tor** para acessar a rede **Tor** diretamente, siga os seguintes passos:

**Passo 1**: **Navegue** até a pasta do *Navegador Tor* e dê **dois cliques** em ![](/sbox/screen/tor-pt/010.png) para ativar a seguinte tela:

![](/sbox/screen/tor-pt/012.png)

*Figura 1: O painel de Configurações da Rede Tor*

**Passo 2**: **Clique** no botão ![](/sbox/screen/tor-pt/013.png) para abrir a janela de **Status do Tor**, que mostrará o progresso da conexão do programa na **Rede Tor**.

![](/sbox/screen/tor-pt/014.png)

*Figura 2: A janela de Status do Tor, mostrando o progresso da conexão*

Um tempo depois, o **Navegador Tor** ativará uma nova janela mostrando a seguinte tela:

![](/sbox/screen/tor-pt/015.png)

*Figura 3: O Navegador Tor conectado com sucesso à rede Tor*

Agora você pode navegar pela web com a proteção da *rede Tor*.

**Observação**: Toda vez que iniciar o **Navegador Tor**, a janela de *Status do Tor* (*Figura 2*) abrirá automaticamente antes de iniciar o navegador (*Figura 3*).


<a name="3.1.2"></a>
## 3.1.2 Como se conectar à Rede Tor - Acesso restrito ##

Se você vive em um local onde é arriscado ou não é possível acessar a rede Tor diretamente, como descrito acima, pode configurar o programa para tentar contornar os obstáculos que estão no caminho.

**Passo 1**: **Navegue** até a pasta do *Tor* e depois dê um **clique duplo** em ![](/sbox/screen/tor-pt/010.png) para ativar a seguinte tela:

![](/sbox/screen/tor-pt/012.png)

*Figura 4: O painel de Configurações da Rede Tor*

**Passo 2**: **Clique** no botão ![](/sbox/screen/tor-pt/016.png) para abrir uma nova janela. Três breves perguntas de configuração serão exibidas para ajudar a acessar a **Rede Tor**.

**Pergunta 1:** *Acesso por proxy.*  Se você precisa acessar a internet por um proxy, selecione **sim** e, então, pressione ![](/sbox/screen/tor-pt/017.png). Se você não usa proxy, então selecione **não** e pressione ![](/sbox/screen/tor-pt/017.png).

Se você selecionou **sim** acima, preencha as suas configurações de proxy na tela seguinte. Se não as souber, verifique no seu próprio navegador de internet. 

![](/sbox/screen/tor-pt/018.png)

*Figura 5: Tela de configurações de Proxy*

**Pergunta 2:** *Portas restritas.* Se você está acessando a internet por um firewall que permite o acesso apenas por meio de certas portas (por exemplo, a *porta 80 ou 443* para navegação na rede), selecione **sim** e pressione ![](/sbox/screen/tor-pt/017.png) para configurá-las. Caso contrário selecione **não** e pressione ![](/sbox/screen/tor-pt/017.png). 

![](/sbox/screen/tor-pt/019.png)

*Figura 6: Tela de configuração das portas restritas*

**Pergunta 3:** *Conexão de internet censurada.* Se você vive em um país que ativamente bloqueia ou monitora o tráfego do **Tor**, pode configurá-lo para usar uma *Ponte* ('Bridge'), o que disfarçará o fato de você estar usando o programa.

Após clicar em ![](/sbox/screen/tor-pt/017.png), depois da *pergunta 2*, será exibida uma tela que permite colar os **endereços de ponte**. Veja a seção [Como obter endereços de ponte](#3.3) para mais instruções.

![](/sbox/screen/tor-pt/020.png)

*Figura 7: Tela de configuração da Ponte do Tor*

Uma vez adicionados os **endereços de ponte**, clique em ![](/sbox/screen/tor-pt/021.png) para terminar a configuração e se conectar à **Rede Tor**.

![](/sbox/screen/tor-pt/014.png)

*Figura 8: A janela de Status do Tor mostrando a conexão em progresso*

Um tempo depois, o **Navegador Tor** ativará uma nova janela do navegador mostrando a seguinte tela:

![](/sbox/screen/tor-pt/015.png)

*Figura 9: O Navegador Tor conectado com sucesso à rede Tor*

Agora você pode navegar na rede com a proteção da *rede Tor*.

**Observação**: Toda vez que você iniciar o **Navegador Tor**, a janela de *Status do Tor* (*Figura 8*) será aberta automaticamente antes de iniciar o navegador (*Figura 9*).


<a name="3.2"></a>
## 3.2 Como reconfigurar o acesso à Rede Tor ##

A qualquer momento, se precisar acessar a **Rede Tor** de um modo diferente (por exemplo, se viajar para um país que bloqueia o Tor), você pode atualizar suas configurações pelo navegador. Clique no ícone ![](/sbox/screen/tor-pt/022.png) e selecione *Abrir as Configurações de Rede*.

![](/sbox/screen/tor-pt/023.png)

*Figura 10: As opções do Navegador Tor*

Será exibida uma nova janela (*Figura 11*, abaixo), que permitirá mudar como o **Navegador Tor** acessa a internet. Selecione as opções que deseja e mude as configurações. Uma vez que você esteja contente com as mudanças, pressione ![](/sbox/screen/tor-pt/024.png) e reinicie o **Navegador Tor**.

![](/sbox/screen/tor-pt/025.png)

*Figura 11: Opções do Navegador Tor*


<a name="3.3"></a>
## 3.3 Como obter endereços de ponte ###

Para configurar o **Navegador Tor** para usar **Pontes** (ou 'bridges') é necessário obter seus endereços. Há duas formas de se fazer isso:

**Por e-mail**:

Para obter as pontes por e-mail, você precisará de uma conta do Gmail ou do Yahoo. Envie um e-mail para bridges@bridges.torproject.org com o assunto *get bridges*. Depois de alguns minutos você receberá um e-mail com 3 pontes listadas e mais alguns detalhes.

![](/sbox/screen/tor-pt/026.png)

*Figura 12: E-mail com as pontes listadas*

**Via site**

Se o seu acesso não estiver completamente restrito, é possível obter os endereços de **ponte** a partir do site do Tor, visitando o endereço [https://bridges.torproject.org/](https://bridges.torproject.org/)

Depois de abrir a página, é preciso executar três passos:

- Clique em ![](/sbox/screen/tor-pt/027.png);

- Clique em ![](/sbox/screen/tor-pt/028.png);

- Preencha o *captcha* e pressione ![](/sbox/screen/tor-pt/029.png).

Uma vez inserido corretamente o *captcha* três endereços de **Ponte** serão exibidos.

![](/sbox/screen/tor-pt/030.png)

*Figura 13: Endereços de Ponte recebidos pelo site do Projeto Tor*

**Observação**: O *Banco de dados de Pontes* foi desenvolvido para evitar que uma única pessoa descubra facilmente todos os endereços. Em um primeiro momento, pode parecer que apenas os mesmos endereços são fornecidos. Porém, de tempos em tempos, o banco eventualmente proverá novos endereços.

Depois de receber os endereços de ponte, copie-os e cole-os no campo da janela, como mostrado na *Figura 7: Tela de configuração da Ponte do Tor* ou na *Figura 11: Opções do Navegador Tor*.

