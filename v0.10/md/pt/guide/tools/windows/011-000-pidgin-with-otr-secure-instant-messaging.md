

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Site**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**https://otr.cypherpunks.ca/**](https://otr.cypherpunks.ca/)

**Esta ferramenta requer**:

- Conexão com a internet
- Qualquer versão do Windows

**Versões usadas nesse guia**:

- Pidgin 2.10.9 
- OTR 4.0.0-1 

**Última revisão desse capítulo**:

- Agosto de 2014

**Licença de uso**: 

- Software livre e de código aberto (FOSS)

**Leitura requerida**

Capítulo [**7. Como manter sua comunicação por internet segura**](/pt/chapter-7), do Guia de Referência.

**O que você pode fazer com o programa**:

- Organizar e gerenciar seus serviços de mensagem instântanea em um único programa
- Conversar em bate papos de forma privada e autenticada

**GNU Linux, Mac OS e outros programas compatíveis para Windows:**

**Observação:** Recomendamos o [**Jitsi**](/en/jitsi) como substituto ao **Pidgin**. Além de poder usar o **Jitsi** para conversas privadas de bate papo (inclusive com contatos que usam o Pidgin), é possível usá-lo também para conversas seguras de áudio e vídeo com outras pessoas que usam o programa. O **Jitsi** também está disponível para **Microsoft Windows**, **GNU/Linux**, **Mac OS** e outros.

O **Pidgin** e o **OTR** estão disponíveis para **Microsoft Windows** e para **GNU/Linux**. Um outro programa multiprotocolo **MI** para **Microsoft Windows** e que suporta o **OTR** é o [**Miranda IM**](http://www.miranda-im.org/). Para **Mac OS** você poderá usar o [**Adium**](http://adium.im/), que é um programa multiprotocolo **MI** que suporta o plugin **OTR**.


## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##

Antes de começar a usar o **Pidgin**, é preciso ter pelo menos uma conta de **MI**. Por exemplo, se você tem uma conta no **Google**, poderá usar o serviço de mensagens instantâneas do **GoogleTalk** com o **Pidgin**. Os detalhes de login da sua conta existente de **MI** serão usados para registrá-la e acessá-la através do **Pidgin**. 

**Observação**: Encorajamos as pessoas a buscar obter o maior conhecimento possível das regras de segurança e privacidade relacionadas a seus **provedores de mensagens instântaneas**. 

O **Pidgin** suporta os seguintes serviços de **MI**: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MSN**](http://www.msn.com/), [**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** e qualquer cliente **MI** que use o protocolo de mensagem **XMPP**.

O **Pidgin** não permite conversas entre diferentes serviços de mensagens instantâneas. Por exemplo, se você está usando o **Pidgin** para acessar sua conta no **Google Talk**, não conseguirá conversar com alguém que estiver usando uma conta do **ICQ**. 

Entretanto, o programa pode ser configurado para gerenciar múltiplas contas que sejam baseadas nos protocolos de mensagens instantâneas suportados. Isso quer dizer que você pode usar as contas do **Gmail** e do **ICQ** ao mesmo tempo, conversando com ambos os serviços correspondentes (suportados pelo **Pidgin**). 

O plugin de mensagem **Off-the-Record** (**OTR**) foi desenvolvido especificamente para o **Pidgin**. Ele oferece as características de segurança e privacidade:

- **Autenticação**: Você garante que a pessoa com quem está falando é quem você pensa que ela é.
- **Negação plausível**: após a sessão de bate papo ser encerrada, as mensagens não podem ser identificadas sendo vindas de você ou de seu contato.
- **Criptografia**: Ninguém mais pode acessar ou ler suas mensagens instântaneas.
- **Garantia de segurança futura** (*Perfect forward security*): Se outra pessoa tiver acesso às suas chaves privadas (sua e de seu contato), nenhuma conversa anterior é comprometida.

**Observação**: O **Pidgin** deve ser instalado antes do plugin **OTR**.

