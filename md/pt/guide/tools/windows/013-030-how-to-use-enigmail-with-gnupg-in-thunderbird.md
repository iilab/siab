

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Seções nesta página:

- [**4.0 Visão geral do Enigmail, GnuPG e criptografia de chave pública e privada**](#4.0)
- [**4.1 Como instalar o Enigmail e o GnuPG**](#4.1)
- [**4.2 Como gerar um par de chaves e configurar o Enigmail para funcionar com suas contas de e-mails**](#4.2)
- [**4.3 Como trocar chaves públicas**](#4.3)
- [**4.4 Como validar e assinar um par de chaves**](#4.4)
- [**4.5 Como criptografar e descriptografar uma mensagem**](#4.5)


<a name="4.0"></a>
## 4.0 Visão geral do Enigmail, GnuPG e criptografia de chave pública e privada ##

O **Enigmail** permite proteger a privacidade da sua comunicação por e-mails. Ele é um complemento (*addon*) ao **Mozilla Thunderbird** que possibilita ao programa usar o **GnuPG**, um software de criptografia. A interface do **Engimail** é representada como *Enigmail* na barra de ferramentas do console do **Thunderbird**. 

O **Engimail** é baseado em [**criptografia de chave pública**](https://pt.wikipedia.org/wiki/Criptografia_de_chave_p%C3%BAblica). Por este método, cada indivíduo deve gerar seu próprio par de chaves.

A primeira chave é conhecida como a *chave privada*; ela é protegida por uma senha ou frase secreta, que deve ser armazenada e *jamais compartilhada* com *alguém*. 

A segunda chave é conhecida como a *chave pública*. Esta pode ser compartilhada com qualquer pessoa. Uma vez que tenha a *chave pública* da pessoa com quem quer se comunicar, você pode começar a enviar e-mails criptografados a ela. Apenas esta pessoa será capaz de decodificar e ler suas mensagens, pois é a única a ter acesso à *chave privada* correspondente.

De forma similar, se você enviar uma cópia da sua *chave pública* a seus contatos de e-mail e mantiver a *chave privada* correspondente guardada, apenas você poderá ler e decodificar mensagens daqueles contatos.

O **Enigmail** também permite adicionar *assinaturas digitais* aos seus e-mails. Desta forma, apenas quem tiver uma cópia genuína da sua *chave pública* será capaz de verificar que determinada mensagem veio de você e que o conteúdo não foi alterado pelo caminho. Da mesma forma, se você tem a *chave pública* de alguém, pode verificar as assinaturas digitais nas mensagens assinadas por aquela pessoa.


<a name="4.1"></a>
## 4.1 Como instalar o Enigmail e o GnuPG ##

Leia a seção [**Baixando o Thunderbird, o Enigmail e o GnuPG**](/pt/thunderbird_main) para instruções sobre como baixar o **Enigmail** e o **GnuPG**.


### 4.1.1 Como instalar GnuPG ###

A instalação do **GnuPG** é bem simples e parecida com outras instalações de software. Siga os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/thunderbird-pt/40.png) para iniciar o processo de instalação. A janela de diálogo *Aviso de segurança - Executar arquivo* deve aparecer. Caso isso aconteça, **clique** em ![](/sbox/screen/thunderbird-pt/02.png) para ativar a seguinte tela:

![](/sbox/screen/thunderbird-pt/41.png)

*Figura 1: O assistente de configuração do GNU Privacy Guard*

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a janela *GNU Privacy Guard Setup - License Agreement*; após ter lido todo o texto, **clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a janela *GNU Privacy Guard Setup - Choose Components*.

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para aceitar as configurações padrão e ativar a janela *GNU Privacy Guard Setup - Install Options - GnuPG Language Selection*. 

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para aceitar *pt_BR - Português (do Brasil)* como língua padrão e ativar a janela *Choose Install Location*.

**Passo 5**. **Clique** em ![](/sbox/screen/thunderbird-pt/06.png) para aceitar o caminho padrão da instalação e ativar a tela *Choose Start Menu Folder*.

**Passo 6**. **Clique** em ![](/sbox/screen/thunderbird-pt/06.png) e comece a desempacotar e instalar os diversos pacotes do **GnuPG**. Após este processo ser concluído, a tela *Installation Complete* aparecerá.

**Passo 7**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) e depois em ![](/sbox/screen/thunderbird-pt/08.png) para completar a instalação do programa **GnuPG**.


### 4.1.2 Como instalar o complemento Enigmail ###

Após instalar o **GnuPG**, o sistema está pronto para instalar o complemento **Enigmail**. Para iniciar, execute os passos a seguir: 

**Passo 1**. **Abra** o **Thunderbird** e **clique** em ![](/sbox/screen/thunderbird-pt/24a.png) para exibir o *Menu do Thunderbird*. **Selecione Complementos** para ativar a janela *Gerenciador de complementos*.

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/44.png) na coluna à esquerda - se o complemento **Enigmail** ainda não houver sido detectado, você verá a mensagem *Não há nenhum complemento deste tipo instalado*.

**Passo 3**. Se o complemento **Enigmail** aparecer no painel principal *Extensões*, **clique** em ![](/sbox/screen/thunderbird-pt/46.png); se não aparecer, **clique** em ![](/sbox/screen/thunderbird-pt/45a.png) e **selecione** *Instalar de um arquivo*, como se vê abaixo: 

![](/sbox/screen/thunderbird-pt/46a.png)

*Figura 3: O menu de ferramentas para complementos*

**Passo 4**. Navegue até a pasta onde você salvou o complemento **Enigmail** (provavelmente na sua pasta *Downloads*), como exibido na tela a seguir:

![](/sbox/screen/thunderbird-pt/47.png)

*Figura 4: O arquivo do Enigmail selecionado*

**Passo 5**.  **Clique** em ![](/sbox/screen/thunderbird-pt/48.png) para ativar a tela a seguir:

![](/sbox/screen/thunderbird-pt/49.png)

*Figura 5: A janela de instalação de extensões e temas*

**Importante**: Antes de executar o passo 6, certifique-se que todo seu trabalho online esteja salvo!

**Passo 6**. **Clique** em ![](/sbox/screen/thunderbird-pt/50.png) e então **clique** em ![](/sbox/screen/thunderbird-pt/51.png) para completar a instalação do complemento **Enigmail** e reiniciar o **Thunderbird**. 

Ao reiniciar o **Thunderbird** a janela *Assistente de configuração* do **Enigmail** deve aparecer como a seguinte: 

![](/sbox/screen/thunderbird-pt/51a.png)

Para verificar se instalação do complemento **Enigmail** foi bem sucedida, retorne para a interface principal do **Thunderbird**, **clique** em ![](/sbox/screen/thunderbird-pt/24a.png) e verifique se o *Enigmail* aparece como uma das opções, como a seguir: 

![](/sbox/screen/thunderbird-pt/52.png)

*Figura 6: O menu do Thunderbird com o Enigmail em destaque*


### 4.1.3 Como confirmar que o Enigmail e o GnuPG estão funcionando ###

Antes de começar a utilizar o **Enigmail** e o **GnuPG** para se autenticar e criptografar seus e-mails, você deve primeiro garantir que ambos estejam se comunicando.

**Passo 1**. No menu do Thunderbird, **selecione: Enigmail > Preferências** para exibir a tela *Preferências Enigmail*, como a seguir:

![](/sbox/screen/thunderbird-pt/53.png)

*Figura 7: A janela Preferências Enigmail*

Se o **GnuPG** foi instalado corretamente, o caminho ![](/sbox/screen/thunderbird-pt/54.png) estará visível na seção *Arquivos e diretórios*; caso contrário, você receberá um alerta pop-up semelhante ao seguinte:

![](/sbox/screen/thunderbird-pt/55.png)

*Figura 8: Mensagem pop-up de alerta do Enigmail*

**Dica**: Se você recebeu esta mensagem, isto pode indicar que o **GnuPG** não está instalado ou que você o instalou em um local diferente. Se você instalou o **GnuPG** em um local diferente, **selecione** a opção *sustituir com* para habilitar o botão de *Localizar*; então **clique** em ![](/sbox/screen/thunderbird-pt/69.png) para ativar o *Localizar* e navegue para o local do arquivo *gpg.exe* em seu computador. Caso contrário, retorne ao item [4.1 Como instalar o Enigmail e o GnuPG](#4.1).

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/35.png) para retornar ao **Thunderbird**.


<a name="4.2"></a>
## 4.2 Como gerar um par de chaves e configurar o Enigmail para funcionar com suas contas de e-mails ##

Uma vez que tenha confirmado que o **Enigmail** e o **GnuPG** estão funcionando corretamente, você pode configurar uma ou mais contas de e-mail para usar o **Enigmail** e gerar um ou mais pares de chaves pública/privada.

### 4.2.1 Como utilizar o assistente do Enigmail para gerar um par de chaves ###

O **Enigmail** disponibiliza duas formas de gerar um par de chaves pública-privada; o primeiro usa o *Assistente de configuração do Enigmail*; o segundo usa a tela de *Gerenciamento de chaves*. 

Para gerar um par de chaves pela primeira vez com o *Assistente de configuração do Enigmail*, execute os passos a seguir: 

**Passo 1**. Se a janela **Assistente de configuração** ainda não estiver ativada **selecione: Enigmail > Assistente de Configuração** para abrir a tela *Assistente de configuração do Enigmail*, como a seguir: 

![](/sbox/screen/thunderbird-pt/56.png)

*Figura 9: A janela Bem-vindo a assistente de configuração do Enigmail*

**Passo 2**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a seguinte janela. *Observação - esta janela só aparecerá se você tiver configurado um par de chaves para outra conta.*

![](/sbox/screen/thunderbird-pt/59.png)

*Figura 10: A tela Selecionar indentidades*

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a tela a seguir:

![](/sbox/screen/thunderbird-pt/60.png)

*Figura 11: A janela Encryption - criptografe suas mensagens enviadas*

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a seguinte tela: 

![](/sbox/screen/thunderbird-pt/61.png)

*Figura 12: A janela Assinatura - Assinar digitalmente suas mensagens enviadas*

**Passo 5**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a seguinte tela: 

![](/sbox/screen/thunderbird-pt/62.png)

*Figura 13: A janela Preferências - altere suas configurações de mensagens para fazer o Enigmail funcionar melhor*

**Passo 6**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a janela *Gerar chave - Eu desejo criar um novo par de chaves para assinar e criptografar minhas mensagens*. 

**Observação**: A primeira vez que você tentar criar uma chave para uma conta de e-mail, a tela *No OpenPGP Key Found* aparecerá. 

**Passo 7**. **Selecione** *Eu quero criar um novo par de chaves para assinar e criptografar minhas mensagens*

**Passo 8**. **Digite** uma senha forte em ambos os campos de *senha*.

![](/sbox/screen/thunderbird-pt/65.png)

*Figura 15: A janela Gerar chave - gerar uma chave para assinar e criptografar mensagens*

**Passo 9**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para ativar a tela *Sumário*, que exibirá as configurações utilizadas durante a geração do par de chaves.

**Passo 10**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para iniciar a criação do par de chaves, como exibido no janela a seguir:

![](/sbox/screen/thunderbird-pt/67.png)

*Figura 16: A janela Criação de chave - sua chave está sendo gerada*

**Observação**: Qualquer par de chaves gerado via o *Assistente de configuração do Enigmail* tem automaticamente o tamanho de 4096-bit e validade de 5 anos.

**Passo 11**. Após haver gerado a chave, você poderá criar um certificado de revogação. **Clique** em ![](/sbox/screen/thunderbird-pt/76.png) como demonstrado na tela a seguir:

![](/sbox/screen/thunderbird-pt/68.png)

*Figura 17: A tela de confirmação do Enigmail*

**Observação**: Se você sabe que alguém obteve acesso não autorizado à sua chave privada, ou se perdeu o acesso a ela, deve enviar o certificado de revogação a seus contatos para que saibam que não devem usar a chave pública correspondente à chave privada comprometida. Tenha em mente que você terá de fazer isso caso perca seu computador, caso ele seja roubado ou confiscado. Portanto, é extremamente recomendado fazer cópias de reserva (*backups*) e proteger seu certificado de revogação.

**Passo 12**. O programa pedirá que você **digite** a senha associada à nova chave criada. Então, **navegue** para um local onde possa armazenar de forma segura o certificado e **clique** em ![](/sbox/screen/thunderbird-pt/78.png) na janela a seguir:

![](/sbox/screen/thunderbird-pt/70.png)

*Figura 18: Criar e salvar o certificado de revogação*

**Passo 13**. **Clique** em ![](/sbox/screen/thunderbird-pt/04.png) para completar a criação do par de chaves e do seu respectivo certificado de revogação.


### 4.2.2 Como gerar um par de chaves e o certificado de revogação adicional para outra conta de e-mail ###

É uma prática comum ter um par de chaves para cada conta de e-mails. Utilizar o mesmo par de chaves para muitas contas de e-mail é possível, mas pode confundir seus contatos. É possível adicionar mais de uma conta de e-mails a um único par de chaves (não discutiremos isso neste capítulo), o que traz alguns benefícios de usabilidade, mas também associa todas aquelas contas de e-mail a uma única pessoa, o que pode não ser desejado.

Siga os passos abaixo se deseja gerar um par de chaves adicional para outra conta de e-mail.

**Passo 1**. **Selecione: Enigmail > Gerenciamento de Chaves OpenPGP** para ativar a tela a seguir: 

![](/sbox/screen/thunderbird-pt/71.png)

*Figura 19: Menu Gerenciamento de chaves Enigmail, com o item Gerar novo par de chaves selecionado*

**Observação**: **Selecione** a opção *Mostrar todas as chaves por padrão* para ver o par de chaves gerado para sua primeira conta de e-mail via *Assistente de configuração do OpenPGP*, como exibido na *Figura 19*, acima, e na *Figura 23*, abaixo.

**Passo 2**. **Selecione: Gerar > Novo par de chaves** no *Gerenciamento de chaves Enigmail*, como demonstrado na *Figura 19*, acima, para ativar a seguinte janela: 

![](/sbox/screen/thunderbird-pt/72.png)

*Figura 20: A tela Gerar chave OpenPGP*

**Passo 3**. **Selecione** uma conta de e-mail a partir da lista expandida do item *Conta / Identidade de usuário*. **Selecione** a opção *Usar chave gerada para a identidade selecionada*. Crie uma senha longa e segura para proteger sua chave privada.

**Importante**: Sempre crie pares de chaves com senhas. *Nunca* habilite a opção "sem senha".

![](/sbox/screen/thunderbird-pt/73.png)

*Figura 21: A janela Gerar chave OpenPGP, exibindo a aba Expiração de chave*

**Observação**: O período de duração pelo qual um par de chaves é válido depende totalmente das suas necessidades de privacidade e segurança; quanto mais frequentemente você trocá-lo, mais difícil fica de comprometê-lo. No entanto, sempre que você trocar seu par de chaves, será preciso enviar a nova chave pública criada a todas as pessoas com quem você se comunica e verificá-la com cada uma delas.

**Passo 4**. **Digite** o número apropriado e **selecione** a unidade de tempo desejada (*dias*, *meses* ou *anos*) para o qual o par de chaves permanecerá válido. 

**Passo 5**. **Clique** em ![](/sbox/screen/thunderbird-pt/74.png) para ativar a janela de confirmação do Enigmail.

**Passo 6**. O programa pedirá que você gere um certificado de revogação, como demonstrado na *Figura 17*.

**Passo 7**. **Clique** em ![](/sbox/screen/thunderbird-pt/76.png) para ativar a janela *Criar e salvar o certificado de revogação*.

**Observação**: Se você sabe que alguém obteve acesso não autorizado à sua chave privada, ou se perdeu o acesso a ela, deve enviar o certificado de revogação a seus contatos para que saibam que não devem usar a chave pública correspondente à chave privada comprometida. Tenha em mente que você terá de fazer isso caso perca seu computador, caso ele seja roubado ou confiscado. Portanto, é extremamente recomendado fazer cópias de reserva (*backups*) e proteger seu certificado de revogação.

**Passo 8**. Navegue para um local seguro onde possa armazenar o certificado, como demonstrado na figura acima, e **clique** em ![](/sbox/screen/thunderbird-pt/78.png). **Digite** a senha associada à nova chave criada.

![](/sbox/screen/thunderbird-pt/77.png)

*Figura 22: Criar e salvar certificado de revogação*

**Passo 9**. **Clique** em ![](/sbox/screen/thunderbird-pt/35.png) para completar o processo de criação do par de chaves e do certificado de revogação então retorne para a seguinte janela: 

![](/sbox/screen/thunderbird-pt/79.png) 

*Figura 23: A janela Gerenciamento de chaves Enigmail exibindo os pares de chaves*

**Observação**: **Selecione** a opção *Exibir todas as chaves por padrão* para ver todos os pares de chaves e suas contas associadas. Certifique-se de estar em um ambiente seguro ao fazer isso.

Após haver gerado corretamente seu par de chaves e o certificado de revogação correspondente, você já pode trocar sua chave pública com alguém confiável.


### 4.2.3 Como configurar a utilização do Enigmail com sua conta de e-mails ###

Para habilitar a utilização do **Enigmail** com uma conta de e-mail específica, execute os passos a seguir:

**Passo 1**. **Clique** em ![](/sbox/screen/thunderbird-pt/24a.png) para exibir o *Menu Thunderbird* e **selecione: Opções > Configuração de contas**.

**Passo 2**. **Selecione** o item *OpenPGP Security* na barra lateral do menu, como a seguir: 

![](/sbox/screen/thunderbird-pt/80.png)

*Figura 24: A tela Configurar contas - Segurança OpenPGP*

**Passo 3**. **Selecione** a opção *Habilitar suporte OpenPGP* e **selecione** a opção *Utilizar o endereço de e-mail desta identidade para identificar a chave OpenPGP*.

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/35.png) para retornar ao console do **Thunderbird**. 


<a name="4.3"></a>
## 4.3 Como trocar chaves públicas ##

Antes de começar a enviar e-mails criptografados para alguém, você deve trocar com aquelas pessoas suas respectivas chaves públicas. Também é preciso confirmar a validade de cada chave recebida, confirmando se ela realmente pertence a quem supostamente a enviou para você.

### 4.3.1 Como enviar uma chave pública usando o Enigmail ###

Para enviar uma chave pública usando o **Enigmail** os seguintes passos devem ser executados tanto por você como pela pessoa com quem irá se comunicar: 

**Passo 1**. **Abra o Thunderbird** e **clique** em ![](/sbox/screen/thunderbird-pt/81.png) para escrever uma nova mensagem.

**Passo 2**. Selecione a opção no menu **Enigmail > Anexar minha chave pública**.

**Observação**: Por este método, o painel **Anexos** não é exibido imediatamente; ele aparecerá assim que você enviar a mensagem.

Se quiser enviar uma chave pública diferente, **selecione** a opção no menu **Enigmail > Anexar uma chave pública ...** e então **selecione** a chave que gostaria de enviar.

![](/sbox/screen/thunderbird-pt/82.png)

*Figura 25: O painel Escreva a mensagem exibindo no painel Anexos a chave pública anexada*

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/83.png) para enviar o e-mail com a chave pública em anexo.


### 4.3.2 Como importar uma chave pública no Enigmail ###

Ao importar uma chave pública, tanto você como a pessoa com quem deseja se comunicar devem executar os mesmos passos para importar chave pública do outro.

**Passo 1**. **Selecione** e **abra** o e-mail contendo a chave pública recebida. O anexo deve se parecer ao seguinte: ![](/sbox/screen/thunderbird-pt/87.png)

**Passo 2**. **Clique** no arquivo anexado acima ![](/sbox/screen/thunderbird-pt/87a.png). O **Enigmail** detectará que a mensagem contém uma chave pública e proporá importá-la, como a seguir:

![](/sbox/screen/thunderbird-pt/88.png)

*Figura 26: O Enigmail confirmando a importação da chave pública* 

**Passo 3**. **Clique** em ![](/sbox/screen/thunderbird-pt/89.png) para importar a chave pública de seu correspondente.

Se a chave pública foi importada com sucesso, uma mensagem semelhante à seguinte deve ser exibida:

![](/sbox/screen/thunderbird-pt/90.png)

*Figura 27: A tela Alerta do Enigmail exibindo a chave pública do correspondente*

Para confirmar que a chave pública foi importada com sucesso, execute os passos a seguir:

**Passo 1**. **Selecione: Enigmail > Gerenciamento de chaves OpenPGP** para exibir a janela *Gerenciamento de chaves Enigmail*, como a seguir:

![](/sbox/screen/thunderbird-pt/91.png)

*Figura 28: A tela de Gerenciamento de chaves Enigmail exibindo a chave pública recém importada* 

**Observação:** A opção *Exibir todas as chaves por padrão* precisa estar selecionada para que você possa ver as chaves.


<a name="4.4"></a>
## 4.4 Como validar e assinar um par de chaves ##

Finalmente, você deverá verificar se a chave importada realmente pertence à pessoa que a enviou para, então, confirmar sua 'validade'. Este é um passo importante e que tanto você como seu contato devem seguir sempre que receberem uma nova chave.

### 4.4.1 Como validar um par de chaves ###

**Passo 1**. **Contate** seu correspondente através de algum meio de comunicação, que não um e-mail. Você pode usar um telefone, mensagens de texto SMS, **Voz sobre IP** (**VoIP**) ou qualquer outro método. Porém, você **deve** ter certeza absoluta de que está realmente falando com a pessoa certa. Conversas por voz ou vídeo e encontros cara-a-cara funcionam melhor, se caso o encontro seja possível e possa ser organizado de forma segura. 

**Passo 2**. Tanto você como seu contato devem verificar a 'impressão digital' da chave pública recebida. Uma impressão digital é uma série única de números e letras que identificam cada chave. Use a tela do *Gerenciamento de chaves Enigmail* do **Enigmail** para visualizar a impressão digital do par de chaves criado por você e da chave pública recebida.

Para ver a impressão digital de um par de chaves específico, execute os seguintes passos:

**Passo 1**. **Selecione: Enigmail > Gerenciamento de chaves OpenPGP** e **clique com o botão direito** em uma chave particular para ativar o menu pop-up: 

![](/sbox/screen/thunderbird-pt/92.png) 

*Figura 29: O menu do gerenciamento de chaves Enigmail com o item Propriedades da chave selecionado*

**Passo 2**. **Selecione** o item *Propriedades da chave* para ativar a tela a seguir: 

![](/sbox/screen/thunderbird-pt/93.png)

*Figura 30: A tela Propriedades da chave*

Seu correspondente deve repetir os mesmos passos. Para confirmar as impressões digitais, leia para seu contato a sequência de caracteres de sua chave e peça que verifique se esta é a mesma sequência que ele vê na chave pública recebida. Então, inverta os papéis e peça a seu contato que leia a impressão digital da chave dele. Se as impressões digitais não conferirem, troquem as chaves públicas novamente e repitam o processo de validação.

**Observação**: A impressão digital não é um segredo e pode ser gravada para verificação posterior, conforme sua conveniência.


### 4.4.2 Como assinar uma chave pública válida ###

Após haver verificado a chave pública de seu correspondente, você pode *assiná-la* para confirmar que a considera válida. Assinaturas de chaves podem expor uma conexão entre você e seu correspondente quando a chave assinada é enviada para alguém ou exportada para um servidor de chaves. Para evitar que isso aconteça, selecione sempre a opção *Assinatura local (não exportável)*, como se vê abaixo.

Para assinar uma chave pública válida, excecute os passos a seguir:

**Passo 1**. **Selecione: Enigmail > Gerenciador de chaves** para abrir a tela *Gerenciamento de chaves Enigmail*.

**Passo 2**. **Clique com o botão direito** na chave pública de seu correspondente a partir da tela *Gerenciador de chaves* (veja a *Figura 29*, acima) e **selecione** o item *Assinar a chave* no menu, para ativar a tela a seguir:

![](/sbox/screen/thunderbird-pt/94.png)

*Figura 31: A tela Enigmail - assinar a chave*

**Passo 3**. **Selecione** a opção *Verifiquei com bastante cuidado ...*, **selecione** *Assinatura local (não exportável)* e então **clique** em ![](/sbox/screen/thunderbird-pt/35.png) para assinar a chave pública de seu correspondente. Você pode ter de fornecer a senha para sua chave privada para finalizar o processo.


#### 4.4.3 Como gerenciar seu par de chaves ####

A janela *Gerenciador de chaves do Enigmail* é usada para gerar, validar e assinar pares de chaves diferentes. Entretanto, você pode executar outras tarefas relacionadas ao processo de gerenciamento de chaves além dessas (veja a *Figura 29*, acima): 

- **Gerenciar IDs de usuário** permite associar mais de um endereço de e-mail a um único par de chaves.
- **Alterar data de expiração** permite alterar a data de expiração do seu par de chaves.
- **Alterar senha** permite alterar a senha de proteção do seu par de chaves.
- **Gerar & salvar o certificado de revogação** permite gerar um novo certificado de revogação, caso tenha perdido o seu ou esquecido onde onde estava guardado.


<a name="4.5"></a>
## 4.5 Como criptografar e descriptografar uma mensagem de e-mail ##

**Importante**: O cabeçalho das mensagens de e-mail - isto é, o *Assunto* e informações como endereços de destinatários, incluídos nos campos *Para*, *CC* e *BCC* - *não é* criptografado e é enviado como texto aberto. Para garantir a privacidade e segurança da suas trocas de e-mails, o assunto do seu e-mail deve ser mantido como não descritivo para não revelar informações sensíveis. Adicionamente, recomendamos colocar todos os endereços de e-mail no campo *BCC - Cópia oculta* sempre que enviar mensagens destinadas a grupos de pessoas.

Ao criptografar mensagens que contenham anexos, recomendamos fortemente usar a opção **PGP/MIME**, pois ela estenderá a criptografia a todos os arquivos e nomes de arquivos incluídos no e-mail.

Observe que todo e-mail enviado pelo Thunderbird/Enigmail/GnuPG é criptografado automaticamente também para a sua chave, além das chaves das pessoas escolhidas para recebê-los. Isso significa que você pode descriptografar as mensagens contidas na caixa de Enviados.

### 4.5.1 Como criptografar uma mensagem ###

Agora que você e seu correspondente conseguiram importar, validar e assinar as chaves públicas um do outro, estão prontos para começar a enviar mensagens criptografadas e para descriptografar as recebidas.

Para cifrar os conteúdos da sua mensagem de e-mail para seu correspondente, execute os passos adiante:

**Passo 1**. **Abra** o **Thunderbird** e **clique** em ![](/sbox/screen/thunderbird-pt/81.png) para escrever uma mensagem.

**Passo 2**. Para criptografar a mensagem, **clique** em *Enigmail -> A mensagem não será criptografada* e **selecione** *Force encryption* (*'Forçar criptografia'*), como exibido na tela a seguir:

![](/sbox/screen/thunderbird-pt/84.png) 

*Figura 33: A opção Forçar criptografia*

**Passo 3**. Para assinar a mensagem, **clique** em *Enigmail -> Mensagem não será assinada* e **selecione** *Forçar assinatura*.

**Observação**: Para verificar se sua mensagem será criptografada e assinada, verifique se os dois ícones aparecem **detacados** no canto inferior direito do painel de mensagem, como a seguir:

![](/sbox/screen/thunderbird-pt/85.png) 

*Figura 34: Criptografia e assinatura habilitadas*

**Passo 4**. **Clique** em ![](/sbox/screen/thunderbird-pt/83.png) para enviar a mensagem. Você pode ter de inserir a senha para a sua chave privada para assinar a mensagem.

**Passo 5 (Opcional)**. Se estiver anexando qualquer arquivo à sua mensagem, **selecione** a opção *Encrypt and sign the message as a whole and send it using PGP/MIME* ('*Criptografe/assine a mensagem como um todo e envie-a usando PGP/MIME*'). Então, **clique** no botão OK, na janela a seguir: 

![](/sbox/screen/thunderbird-pt/86.png)

*Figura 35: A tela Pergunta do Enigmail*


### 4.5.2 Como descriptografar uma mensagem ###

Ao receber e abrir uma mensagem criptografada, o **Enigmail/OpenPGP** tentará automaticamente descriptografá-la. Caso isso não aconteça, selecione o botão *Descriptografar*, ativando a tela a seguir:

![](/sbox/screen/thunderbird-pt/96.png)

*Figura 36: Pergunta do Enigmail - Digite sua senha OpenPGP ou o PIN do SmartCard*

**Passo 1**. **Digite** sua senha, como demonstrado acima.

Após inserir a senha da sua chave privada, a mensagem será descriptografada como exibido a seguir:

![](/sbox/screen/thunderbird-pt/97.png)

*Figura 37: O Painel de mensagens com a mensagem recém descriptografada.*

Você conseguiu descriptografar a mensagem. Ao repetir os passos descritos na seção **4.5 Como criptografar e descriptografar uma mensagem de e-mail** sempre que trocar mensagens com alguém, você manterá um canal de comunicação privado e autenticado, independentemente de quem esteja monitorando suas trocas de e-mails.


### 4.5.3 Opções extras de segurança ###

Ao utilizar o *Enigmail e o GnuPG* para manter sua privacidade, é muito importante assegurar que **todos** os e-mails que você envia estarão criptografados. Em particular, isso inclui respostas a e-mails que vieram criptografados, rascunhos de mensagens às quais você gostaria de cifrar e citações a e-mails codificados anteriormente. 

**Habilite sempre a opção de mensagem criptografada (como visto na seção *4.5.1 Como criptografar uma mensagem*, acima) antes de começar a escrevê-la**. Assim, você garante que os rascunhos das mensagens serão gravados criptografados no servidor de e-mails.

Também recomendamos fortemente que você **configure o Enigmail para alertar antes de enviar um e-mail descriptografado**. Os passos abaixo mostram como fazer isso:

**Passo 1**. **Clique** no menu *Enigmail > Preferências* e **selecione** a aba *Envio*.

**Passo 2**. **Selecione** a opção *Confirmar antes de enviar* - *se estiver descriptografado ...*  e clique ok.

![](/sbox/screen/thunderbird-pt/99.png)

*Figura 38: As preferências do Enigmail - confirme antes de enviar*

Todo e-mail que você tentar enviar descriptografado emitirá um alerta como o exibido abaixo, dizendo que a mensagem está sendo enviada sem criptografia. Se a ideia era enviá-la cifrada, **clique** em *cancelar* e siga os passos mostrados na seção 4.5.1, acima.
 
![](/sbox/screen/thunderbird-pt/98.png)

*Figura 39: Confirmação do Enigmail*

**Lembre-se mais uma vez que** os campos *Assunto, Para, CC* e *BCC* **nunca** são criptografados.


