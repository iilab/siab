

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

Seções nessa página:

- [**3.1 Como exportar sua chave pública com o gpg4usb**](#3.1)
- [**3.2 Como importar a chave pública de alguém com o gpg4usb**](#3.2)
- [**3.3 Como verificar uma chave pública com o gpg4usb**](#3.3)


<a name="3.1"></a>
## 3.1 Como exportar sua chave pública com o gpg4usb ##

Antes que alguém possa enviar uma mensagem criptografada para você, é preciso enviar sua chave pública para aquela pessoa.

Para exportar sua chave pública usando o **gpg4usb**, siga os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/02.png) para abrir a pasta **gpg4usb**.

**Passo 2**. **Clique duas vezes** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o programa **gpg4usb**. 

**Passo3**. **Clique** em ![](/sbox/screen/gpg4usb-pt/13a.png) para abrir a janela a seguir:

![](/sbox/screen/gpg4usb-pt/13.png)

*Figura 1: A janela do gerenciador de chaves exibindo todos os pares de chaves*

**Passo 3**. **Selecione** sua chave, como demonstrado na *Figura 1* acima.

**Passo 4**. No menu **Chave**, **selecione** o item *Exportar para arquivo*, como demonstrado abaixo:

![](/sbox/screen/gpg4usb-pt/14.png)

*Figura 2: A janela do gerenciador de chaves com o item 'exportar para arquivo' selecionado*

Isso ativará a seguinte janela:

![](/sbox/screen/gpg4usb-pt/15.png)

*Figura 3: A janela de navegação 'exportar para arquivo'*

**Passo 5**. **Clique** em ![](/sbox/screen/gpg4usb-pt/16.png) para salvar seu par de chaves na pasta do programa **gpg4usb**.

**Passo 6**: **Envie** como anexo o arquivo exportado com sua chave pública para a pessoa com quem você irá se corresponder.


<a name="3.2"></a>
## 3.2 Como importar a chave pública de alguém com o gpg4usb ##

Antes de poder criptografar informações para enviá-las a alguém, é preciso receber e importar a chave pública daquela pessoa. Para isso, siga os seguintes passos:

**Passo 1**. Dê um **duplo clique** em ![](/sbox/screen/gpg4usb-pt/03.png) para abrir o programa **gpg4usb**.

**Passo 2**. **Clique** em ![](/sbox/screen/gpg4usb-pt/17a.png) para ativar a seguinte janela:

![](/sbox/screen/gpg4usb-pt/17.png)

*Figura 4: A caixa de diálogo de Importar Chave*

**Passo 3**. **Selecione** a chave que deseja importar.

![](/sbox/screen/gpg4usb-pt/18.png)

*Figura 5: Abrir chave*

**Passo 4**. **Clique** em *Abrir* para ativar a janela a seguir.

![](/sbox/screen/gpg4usb-pt/19.png)

*Figura 6: Detalhes da importação da chave*

**Passo 5**. **Clique** em OK para fechar a janela acima e retornar para a tela principal do **gpg4usb**. A chave recém importada será exibida como mostra a tela abaixo.

![](/sbox/screen/gpg4usb-pt/20.png)

*Figura 7: O console do gpg4usb mostrando a nova chave importada, associada à conta correspondente*

Agora que você conseguiu importar corretamente a chave pública da pessoa com quem irá se relaciomar, é preciso verificar e assinar a chave importada.


<a name="3.3"></a>
## 3.3 Como verificar uma chave pública com o gpg4usb ##

Você deve verificar se a chave importada realmente pertence à pessoa que supostamente a enviou, para então considerá-la como autêntica. Este é um passo importante, que você e seus contatos de e-mail devem seguir para cada chave pública recebida. 

Para verificar um par de chaves, execute os passos a seguir:

**Passo 1**. **Contate** a pessoa dona da chave por algum meio de comunicação que não seja e-mail.

**Observação**: Você pode usar o telefone, mensagens de texto, programas de **voz sobre IP (VoIP)** ou qualquer outro método, desde que tenha certeza de estar se comunicando com a pessoa correta. Ligações telefônicas e encontros presenciais proporcionam maior garantia quanto à autenticidade da identidade de alguém, quando é possível fazê-los com segurança. 

**Passo 2**. Você e a pessoa com quem irá se corresponder devem verificar se as 'impressões digitais' (*fingerprints*) das chaves públicas recebidas são as mesmas das enviadas.

**Observação**: Uma impressão digital ou *fingerprint* é uma série única de números e letras que identifica cada chave. A impressão digital em si não é um segredo, podendo ser guardada e usada quando necessária para verificações futuras.

Para ver a impressão digital do par de chaves que você criou, ou das chaves que você importou, execute os passos a seguir:

**Passo 1**. **Selecione** uma chave. **Clique sobre ela com o botão direito do mouse** para ativar o menu relacionado àquela chave.

**Passo 2**. **Selecione** o item *Exibir detalhes da chave*, como demonstrado abaixo na *Figura 8*. 

![](/sbox/screen/gpg4usb-pt/21.png)

*Figura 8: O menu pop-up da chave de um contato*

A tela a seguir será exibida:

![](/sbox/screen/gpg4usb-pt/22.png)

*Figura 9: A janela de 'Detalhes da chave' com a assinatura/impressão digital na parte inferior*

**Passo 3**. **Compare** a impressão digital desta tela com a que a outra pessoa vê em seu **gpg4usb**.

Tal pessoa deve repetir estes passos para a sua chave pública. É preciso confirmar que as impressões digitais das chaves que vocês receberam coincidem com as originais enviadas. Se não coincidirem, troquem as chaves novamente (talvez por um endereço de e-mail ou meio de comunicação diferente). Repitam o processo de verificação.

Se as impressões digitais coincidem *exatamente*, poderão enviar e receber mensagens e arquivos criptografados de forma segura.

