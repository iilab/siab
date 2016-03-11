

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 Usando o Navegador Tor**](#4.0)
- [**4.1 Verificação extra: o Navegador Tor está funcionando?**](#4.1)
- [**4.2 Como criar uma nova identidade**](#4.2)
- [**4.3 Como ativar o complemento NoScript**](#4.3)
- [**4.3 Atualizações do Navegador Tor**](#4.3)


<a name="4.0"></a>
## 4.0 Usando o Navegador Tor ##

O **Navegador Tor** foi desenvolvido para ser muito fácil de usar. Na verdade, se você conhece qualquer navegador de internet, será capaz de usá-lo, pois é uma versão do **Firefox** modificada para prover mais privacidade e segurança.

**Observação**: como o **Navegador Tor** é desenvolvido com a privacidade em mente, é configurado para não salvar nenhuma informação no seu computador ou pen drive. Isso significa que quando você sai do programa, todo seu histórico de navegação é esquecido.


<a name="4.1"></a>
## 4.1 Verificação extra: o Navegador Tor está funcionando? ##

Assim como qualquer programa de contorno à censura, é recomendado fazer alguns testes simples para garantir que o **Navegador Tor** está funcionando. Isso pode ser feito acessando qualquer página que tente identificar onde você está fisicamente com base no endereço IP usado para visitá-la.

Há vários sites gratuitos que fazem isso, como: [check.torproject.org](https://check.torproject.org), [iplocation.net](http://www.iplocation.net/), [ip2location.com](http://www.ip2location.com/), [whatismyipaddress.com](http://whatismyipaddress.com/) etc. Se você acessar qualquer um desses sites diretamente, sem usar o **Navegador Tor** ou outra ferramenta de contornar bloqueios, deverão mostrar o seu endereço IP real e indicar, de forma mais ou menos exata, sua localização física. No entanto, acessar os mesmos sites com o **Navegador Tor** ou outro programa circunvenção, a localização e o endereço IP exibidos deverão ser diferentes.

![](/sbox/screen/tor-pt/031.png)

*Figura 1: Firefox (acima) & o Navegador Tor (abaixo) no mesmo computador mostrando a diferença entre o status do Tor e o endereço IP*


<a name="4.2"></a>
## 4.2 Como criar uma nova identidade ##

Você pode criar uma *nova identidade* para seu navegador. Isso significa que uma série aleatória de servidores proxy do **Tor** será selecionada para você usar e fará que você pareça estar em uma localização nova para os servidores de rede. Para fazer isso, clique em ![](/sbox/screen/tor-pt/022.png) e selecione *Nova Identidade* do menu. O *Navegador Tor* fechará momentaneamente, apagando seu *histórico de navegação* e os *cookies*, e reiniciará. Uma vez reiniciado, você pode checar sua nova localização como descrito acima, na seção 4.1.

![](/sbox/screen/tor-pt/032.png)

*Figura 2: Selecionando a Nova Identidade pelo menu TorButton*


<a name="4.3"></a>
## 4.3 Como ativar o complemento NoScript ##

O **Navegador Tor** vem com o complemento **NoScript** pré-instalado. O **NoScript** pode ser uma proteção a mais contra sites maliciosos e impedir sua identidade real de vazar devido à execução de scripts pelo **Navegador Tor**. Entretanto, o **NoScript** vem desativado por padrão, de modo que essa proteção adicional não está prontamente disponível.

Se quiser habilitar a proteção extra proporcionada pelo **NoScript**, ative-o abrindo o menu **NoScript** e clicando em *Forbid Scripts Globally* ('Proibir scripts globalmente'). Configure as várias *opções* oferecidas.

Recomendamos que você leia mais sobre o [**complemento NoScript** no capítulo do **FireFox**](/pt/firefox_noscript). 

![](/sbox/screen/tor-pt/033.png)

*Figura 3: Habilitando o NoScript ao selecionar a opção *Proibir scripts globalmente (recomendado)*


<a name="4.4"></a>
## 4.4 Atualizações do Navegador Tor ##

No capítulo do **[1.4 do Guia de Referência](/pt/chapter_1_4)**, explicamos quão importante é manter seus programas atualizados. O **Navegador Tor** não é exceção.

Sempre que há uma atualização disponível, o **Navegador Tor** exibirá, ao ser iniciado, uma tela de aviso de que o navegador está desatualizado (*Figura 4*) e o caminho para o botão onde é possível **Baixar a atualização do Navegador Tor**. O clique leva para a página do **Projeto Tor**, onde é possível baixar a última atualização. Uma vez baixada, siga esse mesmo guia para instalá-la.

![](/sbox/screen/tor-pt/034.png)

*Figura 4: O Navegador Tor mostrando que há uma atualização disponível*


