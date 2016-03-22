

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: android
weight: 2
depth: 3
title: Orbot and Orfox - Usage

---

### 3. Como usar o Orbot ###

- [**3.0 Uso Básico**](#3.0)
    - [**3.0.1 Iniciando e desligando o Orbot**](#3.0.1)
    - [**3.0.2 Navegando pela internet de forma anônima**](#3.0.2)

- [**3.1 Uso Avançado**](#3.1)
    - [**3.1.1 Uma nova identidade**](#3.1.1)
    - [**3.1.2 Utilizando pontes**](#3.1.2)
    - [**3.1.3 Iniciando o Orbot de forma automática**](#3.1.3)

---

<a name="3.0"></a>
## 3.0 Uso Básico ##

<a name="3.0.1"></a>
## 3.0.1 Iniciando e desligando o Orbot ##
**Passo 1:** **Pressione e segure** o ícone cinza do **Orbot** no centro da tela até que se torne amarelo e apareça a mensagem *Orbot is starting* (*Iniciando o Orbot*).

![](/sbox/screen/orbot-pt/014.png) ![](/sbox/screen/orbot-pt/015.png) 

*Figuras 1 e 2: Ativando o Orbot*

**Passo 2:** A primeira vez que o **Orbot** for iniciado, aparecerá uma notificação para confirmar que você se conectou à **Rede Tor** com sucesso. **Toque** em ![](/sbox/screen/orbot-pt/016.png) para ver o indicador do **Orbot** em verde, significando que o programa está funcionando.

![](/sbox/screen/orbot-pt/017.png) ![](/sbox/screen/orbot-pt/018.png) 

*Figuras 3 e 4: O Orbot ao completar a conexão*

**Observação:** A janela de notificação (*Fig. 3*) aparece apenas na primeira vez que o **Orbot** é iniciado, após a instalação.

**Passo 3** Para desconectar o **Orbot**, **toque e segure** o ícone verde do programa até que fique cinza. Ou, se quiser desconectar e sair do **Orbot**, **toque** no ícone do menu (![](/sbox/screen/orbot-pt/019.png)), no canto superior direito e selecione ![](/sbox/screen/orbot-pt/020.png) .

![](/sbox/screen/orbot-pt/021.png)

*Figura 5: Saindo do Orbot*


<a name="3.0.2"></a>
## 3.0.2 Navegando pela internet de forma anônima ##
Para navegar ou conversar na internet de forma anônima, é preciso instalar um aplicativo (navegador ou chat) que permita redirecionar sua conexão através de uma série de proxies com o **Orbot**. Veja os *Guias Práticos* relacionados a como utilizar o [**Orweb**](/pt/Orweb_main) e o [**Gibberbot**](/pt/gibberbot_main) junto com o **Orbot**.


<a name="3.1"></a>
## 3.1 Uso Avançado ##

<a name="3.1.1"></a>
## 3.1.1 Uma nova identidade ##
Se em algum momento você quiser alterar o local de origem de sua conexão, é possível gerar uma Nova Identidade **deslizando** o dedo para a *direita* ou *esquerda* no ícone verde do **Orbot**. O ícone irá rodar rapidamente e exibir o aviso *You've switched to a new Tor Identity* (*Você alterou a sua identidade do Tor*).

![](/sbox/screen/orbot-pt/022.png)

*Figure 6: Gerando uma Nova Identidade do Tor*

<a name="3.1.2"></a>
## 3.1.2 Utilizando pontes ##
Se o seu acesso à **Rede Tor** é restrito ou você quer disfarçar que está usando o **Tor**, pode configurar o **Orbot** para utilizar **pontes** (*bridges*).

**Passo 1:** **Toque** no ícone ![](/sbox/screen/orbot-pt/023.png), na parte de cima da tela, para acessar a área de configurações.

**Passo 2:** Encontre a seção **pontes** e marque a opção *Use Bridges* (*Utilizar Pontes*).

![](/sbox/screen/orbot-pt/024.png)

*Figura 7: Ativando a conexão via pontes*

**Passo 3:** **Toque** na seção *Pontes*, abaixo de *Utilizar Pontes*, para acessar a janela de configuração do *endereço de IP* da **ponte** que você está querendo acessar. Uma vez configurado corretamente, **toque** em ![](/sbox/screen/orbot-pt/025.png). Reinicie o **Orbot** para começar uma conexão através da *ponte*.

![](/sbox/screen/orbot-pt/026.png)

*Figura 8: Configurando a ponte*

**Observação:** para saber mais sobre conexões e endereços de ponte, visite a Seção [3.3 Como obter endereços de ponte](/pt/tor_anonymitynetwork#3.3), do Guia Prático do Tor.

<a name="3.1.3"></a>
## 3.1.3 Iniciando o Orbot de forma automática ##
Para assegurar que você não vai esquecer de usar o **Orbot**, o programa pode ser configurado para ser iniciado assim que o seu dispositivo Android seja ligado.

**Passo 1:** **Toque** no ícone ![](/sbox/screen/orbot-pt/023.png), na parte de cima da tela, para acessar as área de configurações.

**Passo 2:** **Marque** a opção *Start Orbot on boot* (*Iniciar Orbot na Inicialização*), no topo da janela de configurações.

![](/sbox/screen/orbot-pt/027.png)

*Figura 9: Iniciando o Orbot de forma automática*

