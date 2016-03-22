

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 012
title: Jitsi - Secure Audio, Video and Instant Text Messaging 

---

**Site**

- [**https://jitsi.org/**](https://jitsi.org/)

**Esta ferramenta requer**

- Qualquer versão do Windows, Mac OS X ou Linux 

**Versão usada para este guia**

- 2.4

**Última revisão deste capítulo**

- Janeiro de 2014

**Licença de uso**

- Software livre e de código aberto (FOSS)

**O que você pode fazer com o programa**:

- Usar um sistema integrado de comunicação privada e segura, o que inclui chamadas de vídeo.
- Criptografar suas conversas, independentemente do provedor do serviço de comunicação.
- Criar e utilizar simultaneamente contas de diferentes serviços, como **Facebook**, **Google Talk/Hangouts**, **Yahoo! Messenger**.

**GNU Linux, Mac OS e outros programas compatíveis para Windows:**

O **Jitsi** está disponível para **GNU Linux**, **Mac OS** e também para **MS Windows**. Em breve, estará também para **Android OS**. Outros programas com os quais o Jitsi consegue se comunicar usando as criptografias independentes **OTR** e **ZRTP** são recomendados abaixo:

- Para **conversas de texto**: [**Pidgin**](/pt/pidgin_main) (**MS Windows** e **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**) e [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) (**Android OS** e **iOS**, antes chamado [**Gibberbot**](/pt/Gibberbot_main)) .

- Para **chamadas de voz**: **CSipSimple** (**Android OS**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android OS**, **iOS** e outros).


## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##

O **Jitsi** suporta vários tipos de contas e diferentes protocolos de comunicação, podendo, com isso, se comunicar com interlocutores que utilizem programas distintos.

Alguns desses programas, como os mencionados na seção anterior, podem oferecer funcionalidades similares de melhoria à segurança da comunicação, com suporte a criptografia independente de texto e voz (**OTR** e **ZRTP**). Outros, especialmente os proprietários (como o **Facebook Chat** ou o **Google Talk/Hangouts**), não possuem essas funcionalidades extras de segurança. Com o **Jitsi**, você ainda poderá se comunicar normalmente com contatos que utilizem programas proprietários; a diferença é que os recursos extras de proteção não estarão disponíveis.

Independentemente de a comunicação ser por texto, fala ou vídeo, os provedores de serviços como o **Facebook Chat**, **Google Talk/Hangouts**, **Yahoo! Messenger**, **Skype** ou **Viber** têm acesso às suas sessões de conversa e podem oferecer este acesso a terceiros, como corporações e governos. O **Jitsi** permite que você se comunique de maneira privada e segura utilizando suas contas já existentes cobertas por uma nova camada de criptografia. Isso torna o conteúdo de sua comunicação inacessível aos provedores dos serviços e outros terceiros potenciais. Para proteger sessões de conversação, o **Jitsi** usa sistemas de criptografia como o **Off-the-Record** ([**OTR**](/pt/glossary#OTR)) em mensagens de texto, e **ZRTP/SRTP** para chamadas por voz.

Outra diferença notável entre o **Jitsi** e programas como o **Skype** é que o **Jitsi** permite às pessoas usar contas já existentes, de provedores de serviços diferentes e independentes dos desenvolvedores do programa. Isso também significa que antes de poder utilizar o **Jitsi** é preciso criar uma conta.

**Observação**: o **Jitsi** utiliza a linguagem de programação **Java**, portanto, é necessário ter o aplicativo Java instalado no computador para que funcione corretamente. O **Oracle Java** é conhecido por conter inúmeras vulnerabilidades de segurança, que podem permitir a alguém assumir remotamente o controle de um computador e instalar spyware (programas espiões) para acessar ou monitorar informações e comunicações. É **altamente recomendado** que você reduza o número de programas capazes de utilizar Java em seu computador. Veja a seção [**Como desabilitar ou desinstalar complementos da Mozilla**](/pt/firefox_addons#3.2) e siga o [**passo a passo para desativar o Java de todos os navegadores do seu computador**](https://www.java.com/en/download/help/disable_browser.xml) (em inglês). Entretanto, como você verá mais para frente neste capítulo, apesar da ulitização do **Java** existem inúmeros benefícios de segurança em usar o **Jitsi**.

