

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**Em 28 de maio de 2014, a página dos desenvolvedores do TrueCrypt passou a informar que o desenvolvimento do programa estava, a partir daquele momento, descontinuado. As circunstâncias por trás de tal situação ainda não são claras. A página dos desenvolvedores passou a oferecer uma nova versão do TrueCrypt, a 7.2, com algumas funcionalidades removidas. Apesar da nova versão, recomendamos que você continue a usar a anterior, a 7.1a (veja as instruções sobre como baixá-la), até que saibamos mais sobre o que aconteceu e quais são os planos para o desenvolvimento futuro do software. Para alternativas ao TrueCrypt, veja a seção "GNU Linux, Mac OS e outros programas compatíveis para Windows", abaixo.**

**Site**

**www.truecrypt.org**

**Esta ferramenta requer**

- Windows 2000/XP/2003/Vista/7
- São necessários privilégios administrativos para a instalação ou criação de volumes, mas não para acessar volumes existentes

**Versão usada para este guia**

- 7.1a

**Última revisão deste capítulo**

- Maio de 2014

**Licença de uso**

- Software livre e de código aberto (FOSS)

**Versão portátil**

- [**Guia prático para o TrueCrypt - Versão portátil**](https://securityinabox.org/pt/truecrypt_portable)

**Leitura requerida**

- Capítulo [**4. Como proteger os arquivos sensíveis do seu computador**](/pt/chapter-4), do **Guia de Referência**.

**O que você pode fazer com o programa**:

- Proteger de forma efetiva seus arquivos de acesso não autorizado ou de intrusos
- Guardar cópias de arquivos importantes de forma fácil e segura


**GNU Linux, Mac OS e outros programas compatíveis para Windows:**

**Observação**: O **TrueCrypt** também está disponível para **GNU Linux** e **Mac OS**. 

Várias distribuições **GNU Linux**, como o [**Debian**](https://www.debian.org/) ou o [**Ubuntu**](http://www.ubuntu.com/), têm suporte à criptografia/descriptografia imediata de todo o disco como uma função padrão. É possível usá-la ao instalar o sistema. Além disso, recomendamos habilitar a criptografia do diretório home durante a instalação. Também é possível adicionar a funcionalidade de criptografia a seu sistema **Linux** usando uma integração entre o [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) e o [**cryptsetup com LUKS**](http://code.google.com/p/cryptsetup/). Outra abordagem seria usar o [**ScramDisk para Linux SD4L**](http://sd4l.sourceforge.net/), um programa livre e de código aberto (FOSS) para criptografia-descriptografia imediata.

Para **Mac OS**, é possível usar o **FileVault**, que faz parte do sistema operacional, para fazer uso de criptografia e descriptografia imediata do conteúdo integral do disco e/ou de sua pasta home, com todas as suas subpastas.

Como programas alternativos no **Microsoft Windows**, recomendamos:

* O [**DiskCryptor**](https://diskcryptor.net/wiki/Main_Page) é uma solução livre e de código aberto (FOSS) que permite a criptografia de todas as partições do disco, incluindo a partição do sistema.
* O [**AxCrypt**](http://www.axantum.com/AxCrypt/) é um programa livre e de código aberto (FOSS) que pode criptografar arquivos isolados.

No MS Windows 7, versões Ultimate ou Enterprise, ou no MS Windows 8, versões Pro e Enterprise, há o [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) para criptografar o disco inteiro. Note que o BitLocker é um programa proprietário e de código fechado da Microsoft, que não é auditado de forma independente para que o nível efetivo de proteção e privacidade oferecido por ele para suas informações possa ser estabelecido.


## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##

O **TrueCrypt** protegerá o acesso às suas informações trancando-as com uma senha criada por você. Caso esqueça essa senha, perderá o acesso a tais dados! O **TrueCrypt** usa um processo chamado criptografia para proteger seus arquivos. Tenha em mente que o uso de criptografia é ilegal em alguns países. Em vez de criptografar arquivos específicos, o progama cria uma área protegida no seu computador, chamada de *volume criptografado*, onde é possível guardar os arquivos de forma segura.

O **TrueCrypt** oferece a possibilidade de criar um volume criptografado padrão ou um volume escondido. Ambos manterão os arquivos protegidos, mas um volume oculto possibilita esconder as informações mais importantes atrás de dados menos sensíveis de forma a protegê-las, mesmo caso te obriguem a revelar o seu volume **TrueCrypt**. Este guia fala sobre ambos os tipos de volume em detalhes.

