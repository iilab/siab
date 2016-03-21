

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

Seções nessa página:

- [**4.0 Como criptografar mensagens de texto com o gpg4usb**](#4.0)
- [**4.1 Como descriptografar mensagens de texto com o gpg4usb**](#4.1)
- [**4.2 Como criptografar arquivos com o gpg4usb**](#4.2)
- [**4.3 Como descriptografar arquivos com o gpg4usb**](#4.3)

<a name="4.0"></a>
## 4.0 Como criptografar mensagens de texto com o gpg4usb ##

No exemplo a seguir, Terence vai criptografar um e-mail para sua amiga Salima. Para fazer como ela, siga os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o console do **gpg4usb**.

**Passo 2**. **Escreva** sua mensagem como demonstrado no exemplo abaixo:

![](/sbox/screen/gpg4usb-pt/23.png)

*Figura 1: O console do gpg4usb mostrando um exemplo de mensagem*

**Passo 3**. **Selecione** a caixa ao lado do e-mail de destino, como a seguir:

![](/sbox/screen/gpg4usb-pt/24.png)

*Figura 2: O console gpg4usb mostrando o e-mail de destino*

**Observação:** É possível criptografar a mensagem para mais de uma pessoa; basta selecionar as caixas ao lado de seus respectivos endereços no painel *Encriptar para*. Além disso, não esqueça de selecionar a caixa ao lado de seu próprio e-mail. Dessa forma, poderá ler depois o que enviou, se quiser.

**Passo 4**. **Clique** em ![](/sbox/screen/gpg4usb-pt/25a.png) ou **selecione** a opção **Encriptar** do menu **Encriptar** para criptografar sua mensagem, como a seguir:

![](/sbox/screen/gpg4usb-pt/25.png)

*Figura 3: O console gpg4usb mostrando um exemplo de mensagem criptografada*

**Passo 5**. **Clique** em ![](/sbox/screen/gpg4usb-pt/26a.png) para selecionar toda a mensagem codificada e então **clique** em ![](/sbox/screen/gpg4usb-pt/26.png) para copiá-la para a área de transferência. 

**Observação**: Alternativamente, é possível usar atalhos de teclado associados a cada item do menu. Neste caso, **Ctrl + E** vai criptografar a mensagem; **Ctrl + A** selecionará todo o conteúdo da área de texto; e **Ctrl + C** o copiará para a área de transferência.

**Passo 6**. **Abra** sua conta de e-mail. Em seguida, **crie** uma nova mensagem e **cole** o texto codificado no corpo do e-mail. O resultado deve ficar assim:

![](/sbox/screen/gpg4usb-pt/27.png)

*Figura 4: Um exemplo de mensagem criptografada no gpg4usb e colada em uma conta de e-mail do Gmail*

**Observação**: O formato **Rich Text** (**RTF**) pode corromper o modo como a mensagem criptografada é enviada, ao inserir estilos de visualização no texto - principalmente espaçamento maior entre as linhas. Portanto, em geral é melhor compor suas mensagens em um aplicativo de texto sem formatação. Para converter do formato **RTF** para texto simples no **Gmail**, basta **clicar** em *Mais opções* no painel ao rodapé da mensagem como demonstrado abaixo (veja a imagem abaixo) e **selecionar** *Modo de texto simples*.

 ![](/sbox/screen/gpg4usb-pt/28.png)

*Figura 5: Opções de formatação do Gmail*


<a name="4.1"></a>
## 4.1 Como descriptografar mensagens de texto com o gpg4usb ##

Para descriptografar um e-mail recebido, execute os passos a seguir:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o programa **gpg4usb**.

**Passo 2**. **Abra** sua conta de e-mail. Então, **abra** a mensagem criptografada recebida.

**Passo 3**. **Selecione** todo o texto em código, **copie-o** (**Ctrl + C**) e **cole-o** (**Ctrl + V**) na aba *Semtitulo1.txt* do console do **gpg4usb**, como demonstrado a seguir:

![](/sbox/screen/gpg4usb-pt/29.png)

*Figura 6: O console do gpg4usb mostrando uma mensagem para decodificar*

**Observação**: Se o texto criptografado aparecer com espaçamento duplo entre as linhas, como mostrado na *Figura 7* abaixo, o **gpg4usb** pode não ser capaz de decodificá-lo automaticamente. Para remover essa quebra de linha dupla, **clique** em ![](/sbox/screen/gpg4usb-pt/29a.png) (ou **selecione** *Remover espaçamento* no menu **Editar**) para continuar o processo de descriptografia no **Passo 4**.

![](/sbox/screen/gpg4usb-pt/30.png)

*Figura 7: O console do gpg4usb mostrando uma mensagem para decodificar com espaçamento duplo entre as linhas*
 
**Passo 4**. **Clique** em ![](/sbox/screen/gpg4usb-pt/31a.png) e insira a senha que você atribuiu quando gerou seu par de chaves, como demonstrado na janela a seguir: 

![](/sbox/screen/gpg4usb-pt/31.png)

*Figura 8: A janela para inserção de senha*

**Passo 5**. **Clique** em *OK* para ativar o console **gpg4usb**, como na *Figura 2* acima.


<a name="4.2"></a>
## 4.2 Como criptografar arquivos com o gpg4usb ##

O processo para criptografar um arquivo é similar ao de cifrar e-mails. No exemplo a seguir, Salima vai criptografar um arquivo para Terence, usando os passos a seguir:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o programa **gpg4usb**.

**Passo 2**. **Clique** em ![](/sbox/screen/gpg4usb-pt/32a.png) e *Encriptar arquivo* para ativar a tela a seguir:

![](/sbox/screen/gpg4usb-pt/32.png)

*Figura 9: A janela de encriptar arquivo*

A janela *Encriptar arquivo* possui uma lista de rolagem que permite escolher as contas de e-mail e respectivas chaves a serem utilizadas para criptografar a mensagem.

**Passo 3**. **Clique** em ![](/sbox/screen/gpg4usb-pt/33.png) ao lado do item *Entrada* para ativar a janela a seguir:

![](/sbox/screen/gpg4usb-pt/34.png)

*Figura 10: A janela de navegação Abrir arquivo*

**Passo 4**. **Clique** em ![](/sbox/screen/gpg4usb-pt/35.png) para anexar o arquivo que será criptografado e retorne para a janela *Encriptar arquivo*, como a seguir:

![](/sbox/screen/gpg4usb-pt/36.png)

*Figura 11: A janela Encriptar arquivo mostrando arquivo designado para ser criptografado*

**Passo 5**. **Clique** em *OK* para ativar a janela a seguir:

![](/sbox/screen/gpg4usb-pt/37.png)

*Figura 12: A caixa de diálogo de processo concluído/Done*

A caixa de diálogo de processo *Concluído/Done* mostra onde a cópia criptografada do arquivo foi salva. Arquivos criptografados também podem ser identificados pela extensão *.asc*. Por exemplo, *Anotações da Reunião.docx.asc*. 

**Passo 6**. **Clique** em *OK* para completar o processo de criptografia.

**Observação**: Você pode criptografar separadamente uma mensagem de texto, que pode ser enviada junto com o arquivo cifrado.

**Passo 7**. Usando sua conta de e-mail, **navegue** para a pasta onde está a cópia criptografada do arquivo (*Figura 12*) e então anexe-o normalmente, como faria com qualquer outro arquivo.

**IMPORTANTE**: Observe que o nome do arquivo **não é criptografado**. Certifique-se que este nome não revele nenhuma informação importante! E não se esqueça que ele é uma cópia - uma versão decodificada do arquivo (a original) continua no seu computador.


<a name="4.3"></a>
## 4.3 Como descriptografar arquivos com o gpg4usb ##

No exemplo a seguir, Terence irá decodificar o arquivo que Salima o enviou, usando os passos a seguir:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o programa **gpg4usb**.

**Passo 2**. **Abra** sua conta de e-mail, **abra** a mensagem que contém o arquivo criptografado e **baixe-o** para o computador.

**Observação**: Se alguém te enviou uma mensagem de texto acompanhando o arquivo criptografado, decodifique-a usando o método descrito na seção [**4.1 Como descriptografar mensagens de texto com o gpg4usb**](/pt/gpg4usb-encryptdecrypt#4.1)

**Passo 3**. No console do **gpg4usb** (como na *Figura 1*, acima), **clique** em ![](/sbox/screen/gpg4usb-pt/32a.png) para abrir a janela **Decriptar Arquivo** (como na *Figura 13*, abaixo). 

**Passo 4**. **Clique** em ![](/sbox/screen/gpg4usb-pt/33.png) ao lado do item *Entrada* para escolher o local no computador onde o arquivo criptografado foi salvo, como a seguir:

![](/sbox/screen/gpg4usb-pt/38.png) 

*Figura 13: A janela Decriptar arquivo, mostrando o caminho para o arquivo criptografado*

**Passo 5**. **Clique** em *OK* para ativar a janela a seguir:

![](/sbox/screen/gpg4usb-pt/39.png)

*Figura 14: A caixa de diálogo de confirmação, mostrando a localização do arquivo decodificado*

**Importante**: Se você está trabalhando em uma LAN House, Internet Café ou em estações de trabalho nas quais outras pessoas podem ter acesso à versão decodificada do arquivo, é melhor copiar o arquivo original *.asc* para seu pen drive ou HD externo e levá-lo para que possa ser descriptografado com mais privacidade em sua casa.



