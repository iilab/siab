

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Seções nessa página:

- [**2.0 Como instalar o gpg4usb**](#2.0)
- [**2.1 Como gerar um par de chaves com o gpg4usb**](#2.1)

<a name="2.0"></a>
## 2.0 Como instalar o gpg4usb ##

O **gpg4usb** é uma ferramenta portátil, que não precisa ser instalada em seu computador. Ele é distribuído como arquivo zip e deve ser extraído diretamente para um pen drive ou para uma pasta do computador. Siga o seguinte passo para começar: 

**Passo 1**. **Localize** o arquivo zipado do **gpg4usb**. **Extraia** todos os arquivos para um pen drive ou para uma pasta do computador: 

![](/sbox/screen/gpg4usb-pt/01.png)

*Figura 1: Local de destino do programa gpg4usb*

<a name="2.1"></a>
## 2.1 Como gerar um par de chaves com o gpg4usb ##

Antes de começar a criptografar e descriptografar e-mails, mensagens de texto, documentos e arquivos, é preciso tomar três medidas preparatórias.

A primeira é gerar ou importar para o programa seu par de chaves pessoais de criptografia; a segunda é enviar sua chave pública para seus contatos; e a terceira é receber as chaves públicas respectivas àqueles contatos e importá-las para seu chaveiro. Descreveremos como compartilhar chaves públicas na próxima seção.

O **gpg4usb** te ajudará a gerar um par de chaves assim que for iniciado. Note que sempre é possível voltar à janela do *Auxiliar de primeiro uso* em *Ajuda* -> *Abrir o Auxiliar*, no menu.

**Passo 1**. Para executar o programa **gpg4usb** pela primeira vez, **localize e clique duas vezes** na pasta ![](/sbox/screen/gpg4usb-pt/02.png) para abri-la. A seguir, **clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png). Isso ativará o *Auxiliar de primeiro uso*. Escolha o idioma *português do Brasil (pt_BR)* e clique em *Avançar*.

![](/sbox/screen/gpg4usb-pt/04.png)

*Figura 2: O Auxiliar de primeiro uso*

![](/sbox/screen/gpg4usb-pt/05.png)

*Figura 3: Escolha seu idioma*

**Passo 2**. Na tela *Selecione sua ação*, clique em *criar um novo par de chaves*

![](/sbox/screen/gpg4usb-pt/06.png)

*Figura 4: Selecione sua ação*

Observe as outras opções disponíveis para importar chaves existentes na tela inicial do auxiliar. Se estiver usando uma versão mais atual, em substituição a uma versão anterior do **gpg4usb**, pode escolher *importar as configurações e/ou chaves do gpg4usb*. Se estiver usando o [Thunderbird com Enigmail](/pt/thunderbird_main), pode escolher a opção *importar as chaves do GnuPG*. Também é possível importar as chaves em uma fase posterior, executando o auxiliar novamente a partir do menu *Ajuda* -> *Abrir o auxiliar*.

**Passo 3**. Em *Criar um par de chaves*, **clique** em *Criar nova chave*

![](/sbox/screen/gpg4usb-pt/07.png)

*Figura 5: Criar nova chave* 

**Passo 4**. **Preencha** os campos de texto com as informações solicitadas. Sua janela deve ficar parecida com esta:

![](/sbox/screen/gpg4usb-pt/08.png)

*Figura 6: Exemplo de um formulário para gerar chave preenchido*

**Importante:** 

  * Defina uma senha segura para proteger sua chave privada (veja o capítulo [**3. Como criar e manter senhas seguras**](/pt/chapter-3), do Guia de Referência).
  * Aconselhamos você a usar uma data de expiração menor do que 5 anos.
  * É altamente recomendável gerar chaves com pelo menos 2048 bits de tamanho. Chaves maiores são mais seguras, mas também levam mais tempo para serem geradas, assim como para criptografar e descriptografar textos.

**Observação**: Não é preciso usar nomes e endereços de e-mail reais quando gerar sua chave. No entanto, usar o  e-mail da conta que você for usar para se comunicar torna mais fácil para seus contatos associar sua chave a esta conta. 

**Passo 6**. **Clique** em *OK* para gerar o par de chaves.

![](/sbox/screen/gpg4usb-pt/09.png)

*Figura 7: Gerando as chaves...*

![](/sbox/screen/gpg4usb-pt/10.png)

*Figura 8: Nova chave criada*

**Passo 7**. **Clique** em *OK* para voltar à janela do *Auxiliar de primeiro uso* do **gpg4usb**.

![](/sbox/screen/gpg4usb-pt/11.png)

*Figura 9: Divirta-se com o gpg4usb*

Depois clique em **Terminar** para exibir a tela inicial do **gpg4usb**. Com as chaves criadas, você verá uma tela semelhante à seguinte:

![](/sbox/screen/gpg4usb-pt/12.png)

*Figura 10: A janela do gpg4usb, exibindo o novo par de chaves* 

Agora que você criou com êxito um par de chaves, precisa aprender como exportar sua chave pública para ser compartilhada e como importar chaves públicas das pessoas com quem irá se corresponder.

