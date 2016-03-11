

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Site**
			
[**https://www.torproject.org**](https://www.torproject.org/)
			
**Esta ferramenta requer**

- Qualquer versão do **Windows** (XP ou mais recente)
- Uma conexão de internet		

**Versão usada para este guia**

- Navegador Tor: 3.6.2

**Última revisão deste capítulo**

- Março de 2014

**Licença de uso** 

- Software livre e de código aberto ([Licença BSD](https://en.wikipedia.org/wiki/BSD_license))

**Leitura requerida**

- Capítulo [**8: Como se manter anônimo e contornar a censura na internet**](/pt/chapter-8), do **Guia de Referência**.


**O que você pode fazer com o programa**:

- Esconder sua identidade digital dos sites que visita
- Esconder seus destinos online do seu **Provedor de Internet** e outros mecanismos de vigilância
- Contornar a censura na internet e regras de bloqueio

**GNU Linux, Mac OS e outros programas compatíveis para Windows:**

O **Navegador Tor** está disponível para os sistemas operacionais **GNU Linux**, **Mac OS**, **Microsoft Windows** e **Android**. O **Tor** é a ferramenta mais recomendada e rigorosamente testada para manter o anonimato das suas atividades online. Mas gostaríamos de listar aqui outras soluções recomendadas:

* [**Riseup VPN**](https://help.riseup.net/en/riseup-vpn/) é uma **Virtual Private Network** (**VPN**, ou rede privada virtual), um servidor proxy para **Linux**, **MAC**, **Android** e **Microsoft Windows**.
* [**Psiphon3**](http://www.psiphon3.com/) é uma solução livre comercial de **Virtual Private Network** (**VPN**, ou rede privada virtual) para **Microsoft Windows** e **Android OS**.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) é uma ferramenta livre de proxy para **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) é uma ferramenta comercial de proxy que também oferece um serviço grátis (embora lento). Está disponível para **Linux**, **Mac OS** e **Microsoft Windows**.

## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##

O **Navegador Tor** é uma ferramenta desenvolvida para aumentar a privacidade e segurança das suas atividades e hábitos na Internet. Ele mascara sua identidade e sua navegação online de diversas formas de vigilância na Internet. O **Tor** pode também ser útil como um meio seguro para contornar restrições eletrônicas, assim você pode publicar ou acessar o seu blog e as suas notícias.

O **Tor** protege seu *anonimato* ao rotear sua comunicação através de uma rede distribuída de servidores, gerida por voluntários do mundo todo. Ao usar o **Tor**, você esconde os sites que visita de potenciais observadores e oculta sua localização/identidade desses sites. O programa é desenvolvido também para garantir que os servidores da rede **Tor** **não saibam** a sua localização assim como os sites que você está visitando.

O **Tor** também toma medidas para criptografar a comunicação para e pela sua rede. **Porém** tais medidas não podem se extender por todo o caminho até um site que esteja enviando e recebendo conteúdo, caso este utilize canais não criptografados (por exemplo, sem prover acesso https). Ainda assim, a vantagem de usar o **Tor** ao acessar tais sites é que o programa torna sua comunicação segura até o momento entre o último servidor **Tor** e o site não-seguro, o que limita a chance de ter o conteúdo interceptado a apenas aquela última etapa.

O **Navegador Tor** consiste no programa **Tor** e uma versão modificada do navegador web **Firefox**, o qual é desenvolvido para fornecer uma proteção extra ao usá-lo. O navegador inclui ainda os complementos [**NoScript**](/pt/firefox_noscript) e [**HTTPS-Everywhere**](/pt/firefox_others#5.1). 

**Observação**: Existe um balanço entre anonimato e velocidade. Como o Tor facilita a navegação anônima passando seu tráfego através de computadores de voluntários e servidores em várias partes do mundo, isso será definitivamente mais lento que usar outro navegador de internet no seu computador.

**Definições**:

- **Ponte**: Uma Ponte ou "Bridge Relay", é um servidor **Tor** que não é publicamente anunciado. Se escolher usar uma ponte, o servidor poderá prover acesso à rede **Tor** mesmo se o **Tor** for bloqueado em seu país.

- **Porta:** Neste capítulo, a porta é um ponto de acesso pelo qual o programa se comunica com o serviço executado em outros computadores da rede. Se uma URL, como **www.google.com**, fosse o 'endereço da rua' de um serviço, então, a porta seria a entrada que você usaria ao chegar no destino correto. Ao navegar na Rede, você geralmente usa a porta 80 para sites não seguros (**http://mail.google.com**) e a porta 443 para os seguros (**https://mail.google.com**).

- **Proxy:** Um proxy é um programa intermediário que roda no seu computador, na sua rede local ou em algum outro lugar na Internet, e que ajuda a transmitir sua comunicação até o seu destino final.

- **Rota:** Uma rota é o caminho de comunicação na Internet entre o seu computador e o servidor de destino.

