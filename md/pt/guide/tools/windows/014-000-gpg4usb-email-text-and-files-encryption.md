

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Site**

- [**http://www.gpg4usb.org/**](http://www.gpg4usb.org/)

**Esta ferramenta requer**

- Qualquer versão de Windows

**Versão usada para este guia**

- 0.3.3

**Última revisão desse capítulo**

- Julho de 2014

**Licença de uso**

- Software livre e de código aberto (FOSS)

**Leitura requerida**

- Capítulo [**7. Como manter sua comunicação por internet segura**](/pt/chapter-7), do Guia de Referência.

- capítulo **2.4 Criptologia - Criptografia de chave pública (página 38)** do livro [**Segurança Digital e Privacidade para Defensores dos Direitos Humanos**](https://www.frontlinedefenders.org/esecman) (em inglês e espanhol).

**O que você pode fazer com o programa**:

- Criptografar arquivos e textos de onde você estiver (por exemplo, em um Internet Café ou no trabalho)
- Criptografar mensagens/e-mails quando o acesso à internet não estiver disponível, para enviá-las depois, de um computador conectado à internet.


## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##

O **gpg4usb** é um programa simples, leve e portátil que permite criptografar e descriptografar mensagens de texto e arquivos. O software é baseado em uma chave de criptografia pública, método segundo o qual cada pessoa deve gerar seu **par de chaves** pessoal.

A primeira dessas chaves é conhecida como **chave privada** - protegida por uma senha, deve ser armazenada e *nunca* compartilhada com ninguém. A segunda é conhecida como **chave pública** - tal chave pode ser compartilhada com quaisquer pessoas com quem você se corresponda, assim como elas podem compartilhar suas respectivas chaves públicas com você.

Com a chave pública de alguém, é possível enviar e-mails criptografados de forma que somente aquele alguém seja capaz de decodificá-los para ler seu conteúdo (uma vez que apenas ele tem acesso à chave privada correspondente). Similarmente, se você enviar uma cópia de sua chave pública aos seus contatos de e-mail e mantiver sua chave privada protegida, só você será capaz de ler os e-mails criptografados por estes contatos.

Também é possível anexar assinaturas digitais às mensagens. Uma pessoa que receba uma mensagem sua e tenha uma cópia autêntica de sua chave pública será capaz de verificar que o e-mail veio de você e que o conteúdo não foi modificado no caminho. De forma semelhante, se você tem a chave pública de uma pessoa com quem deseja se corresponder, pode verificar a assinatura digital das mensagens daquela pessoa.

O **gpg4usb** permite criar um par de chaves de criptografia, exportar a chave pública para ser compartilhada, escrever mensagens de texto e criptografá-las. Também é possível copiar e colar uma chave pública e/ou uma mensagem criptografada direto do **gpg4usb** para um corpo de e-mail, ou salvá-la como arquivo de texto para ser enviado depois. Documentos e arquivos também podem ser criptografados. 

**Observação**: Atente que a versão original, decodificada, dos seus documentos e arquivos ainda podem ficar no computador. Assim, tanto você como a pessoa com quem se correspondeu devem lembrar de removê-los quando necessário.

O **gpg4usb** permite trocar chaves e criptografar mensagens com outros programas similares, como o **GPG** ou o **PGP**.

