

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Sites**

- [**http://www.mozilla.org/pt-BR/thunderbird/**](http://www.mozilla.org/pt-BR/thunderbird/)
- [**www.enigmail.net**](http://enigmail.net/)
- [**www.gnupg.org**](http://www.gnupg.org/)
- [**trac.torproject.org/projects/tor/wiki/torbirdy**](https://trac.torproject.org/projects/tor/wiki/torbirdy)

**Esta ferramenta requer**

- Qualquer versão do Windows

**Versões usadas neste guia**

- Thunderbird 31.0 
- Enigmail 1.7
- GNU Privacy Guard (GnuPG) 1.4.18
- TorBirdy 0.1.2

**Última revisão deste capítulo**

- Setembro de 2014

**Licença**

- Software livre e de código aberto (FOSS)

**Leitura requerida**

- Capítulo [**7. Como manter sua comunicação por internet segura**](chapter-7), do Guia de Referência.

**O que você pode fazer com o programa**: 

- Gerenciar diferentes contas de e-mails por meio de um único programa
- Ler e compor mensagens após se desconectar da internet
- Utilizar criptografia de chave pública para manter a privacidade do seu e-mail

**GNU Linux, Mac OS e outros programas compatíveis para Windows**:

O cliente de e-mail **Mozilla Thunderbird** está disponível para **GNU Linux**, **Mac OS**, **Microsoft Windows** e outros sistemas operacionais. Gerenciar multiplas contas de e-mail é uma tarefa complexa do ponto de vista da segurança digital. Portanto, *recomendamos fortemente* que você utilize o **Mozilla Thunderbird** para este fim. As vantagens de segurança disponíveis no **Thunderbird**, além da plataforma do programa ser *livre e de código aberto* (FOSS), são ainda mais importantes quando comparadas aos equivalentes comerciais como **Microsoft Outlook**.

No entanto, caso você prefira usar um programa que não o **Mozilla Thunderbird**, recomendamos as alternativas livres e de código aberto a seguir:

* [**Claws Mail**](http://www.claws-mail.org/), disponível para **GNU Linux** e **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/), disponível para **GNU Linux**, **Mac OS** e **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/), disponível **GNU Linux**, **Mac OS** e **Microsoft Windows**.

**Observação**: Embora recomendemos o uso do **Enigmail/GnuPG** por serem fáceis de usar com o Thunderbird, você ainda pode utilizar ferramentas independentes de criptografia como o **gpg4usb** conjuntamente com o Thunderbird. Veja o Guia Prático do [gpg4usb - Criptografia de textos de e-mail e arquivos](/pt/gpg4usb_portable) para ver outra forma de criptografar suas mensagens eletrônicas com o método de criptografia de chave pública.


### 1.1 O que você precisa saber sobre a ferramenta antes de começar ###

O **Mozilla Thunderbird** é um cliente de e-mail multiplataforma livre e de código aberto (FOSS) para receber, enviar e armazenar correspondências eletrônicas. Um cliente de e-mail é um aplicativo de computador que permite baixar e gerenciar suas mensagens sem precisar de um navegador de internet. Também é possível gerenciar múltiplas contas com um único programa.

Antes de usar o **Thunderbird**, é preciso ter uma conta de correio eletrônico. Você também pode criar uma conta de e-mails no [**RiseUp**](/pt/riseup_createaccount) se desejar.

O **Enigmail** é um complemento desenvolvido para o **Thunderbird**. Ele permite que as pessoas acessem os recursos de autenticação e criptografia fornecidos pelo **GNU Privacy Guard** (**GnuPG**).

O **GnuPG** é um programa de criptografia de chave pública utilizado para criar e administrar o par de chaves que será usado para criptografar e descriptografar mensagens, de modo a manter sua comunicação segura e privada. O **GnuPG** deve ser instalado para que o **Enigmail** funcione, como será descrito adiante neste capítulo.

