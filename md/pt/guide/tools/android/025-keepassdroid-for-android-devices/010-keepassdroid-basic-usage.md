

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: android
weight: 1
depth: 3
title: KeePassDroid - Basic Usage

---

## 2. Como usar o KeePassDroid ##

- [**2.0 Como instalar o KeePassDroid**](#2.0)
- [**2.1 Como criar um novo banco de dados de senhas**](#2.1)
- [**2.2 Como criar novas entradas no seu banco de dados**](#2.2) 
    - [**2.2.1 Como adicionar grupos**](#2.2.1)
    - [**2.2.2 Como adicionar senhas**](#2.2.2)
- [**2.3 Como copiar uma senha do KeePassDroid**](#2.3)


-------

<a name="2.0"></a>
## 2.0 Como instalar o KeePassDroid ##

**Passo 1**. **Baixe** e **instale** o aplicativo da loja [**Google Play**](https://play.google.com/store/apps/details?id=com.android.keepass) em seu dispositivo Android, clicando em ![](/sbox/screen/keepassdroid-pt/002.png)

![](/sbox/screen/keepassdroid-pt/001.png)

*Figura 1: A página do KeePassDroid na Google Play 

**Passo 2**. Antes que o processo de instalação se inicie, os tipos de acesso que o aplicativo terá sobre seu aparelho celular serão exibidos na tela. Revise cuidadosamente essas informações. Quando estiver contente com as permissões que serão dadas, clique em ![](/sbox/screen/keepassdroid-pt/003.png) e a instalação será concluída; caso não concorde com as permissões requeridas, aperte o botão de voltar e a instalação será cancelada.

![](/sbox/screen/keepassdroid-pt/004.png)

*Figura 2: As permissões necessárias ao KeePassDroid*

**Observação**: O **KeePassDroid** também pode ser baixado [diretamente dos desenvolvedores](https://code.google.com/p/keepassdroid/downloads/list?can=1&q=) ou de outras Loja de Aplicativos como a [F-Droid](https://f-droid.org/repository/browse/?fdfilter=keepass&fdid=com.android.keepass). 


<a name="2.1"></a>
## 2.1 Como criar um novo banco de dados de senhas ##

Nas seções a seguir, você aprenderá a criar uma senha mestre; salvar o seu banco de dados recém criado; gerar uma senha aleatória para um programa específico; e criar uma cópia de reserva (*backup*) do seu banco de dados.

**Passo 1**. Para abrir o **KeePassDroid**, **toque** no ícone do aplicativo.

![](/sbox/screen/keepassdroid-pt/keepass.png)

**Passo 2**. Para criar um novo banco de dados de senhas, **toque** em *criar*.

*Figura 3: A tela de abrir/criar banco de dados.*

Isso ativará a tela de *Entre com a senha do banco de dados*, como demonstrado abaixo.

![](/sbox/screen/keepassdroid-pt/006.png)

*Figura 4: A tela de Entre com a senha do banco de dados.*

**Passo 3**. Para este passo, você criará uma senha mestre forte e única, a qual você **deverá se lembrar**, pois é ela que que será usada para bloquear ou desbloquear o seu banco de dados de senhas.

**Digite** a senha mestre que você inventou no campo de *senha* e no campo de *confirmação de senha*, conforme a figura a seguir:

![](/sbox/screen/keepassdroid-pt/007.png)

*Figura 5: Insira a senha mestre.*

**Dica**: Veja o capítulo [**3. Como criar e manter senhas seguras**](/pt/chapter_3_1), do **Guia de Referência**, para mais informações sobre como criar e manter uma senha mestre forte.

**Passo 4**. **Toque** em **OK** para criar e abrir o seu banco de dados do KeePass.

![](/sbox/screen/keepassdroid-pt/008.png)

*Figura 6: A tela inicial do KeePassDroid*

Parabéns! Você criou seu banco de dados seguro de senhas com sucesso. Agora, poderá usá-lo para guardar todas as suas senhas atuais e futuras de forma segura.

**Observação**: Se você utiliza o **KeePass** em outro computador ou dispositivo móvel, é possível copiar o banco de dados existente e abri-lo com **KeePassDroid** ou **KeePass**.


<a name="2.2"></a>
## 2.2. Como criar novas entradas no seu banco de dados ##

<a name="2.2.1"></a>
### 2.2.1 Como adicionar grupos
Para deixar suas informações organizadas, o **KeePassDroid** armazena as senhas em grupos. Os grupos padrão são **Email** e **Internet**, mas é possível criar o seu próprio ao **tocar** em ![](/sbox/screen/keepassdroid-pt/009.png), digitar o nome do grupo e depois **tocar** em ![](/sbox/screen/keepassdroid-pt/010.png).

![](/sbox/screen/keepassdroid-pt/011.png) ![](/sbox/screen/keepassdroid-pt/012.png)

*Figuras 7 e 8: Adicionando um novo grupo*

**Toque** no grupo recém criado para abri-lo e começar a adicionar suas senhas.


<a name="2.2.2"></a>
### 2.2.2 Como adicionar senhas
A tela **Adicionar Entrada** permite adicionar as informações da conta, senhas e outros detalhes importantes em seu banco de dados recém-criado.

**Passo 1**. **Toque** em ![](/sbox/screen/keepassdroid-pt/013.png) para ativar a tela de *Adicionar Entrada*, como se vê abaixo.

![](/sbox/screen/keepassdroid-pt/014.png)

*Figura 9: Adicionando uma nova entrada de senha.*

**Observação**: A tela de *Adicionar Entrada* apresenta uma série de campos para serem preenchidos, dos quais nenhum é obrigatório. As informações adicionadas aqui servem principalmente para sua própria conveniência. Preenchê-las pode ser útil em situações nas quais você está procurando uma entrada específica.

Segue abaixo uma breve explicação sobre os diferentes campos existentes:

  - **Nome**: Um nome para a entrada da senha. Por exemplo: Conta do *Twitter*.

  - **Nome de Usuário**: O login associado à entrada de senha. Por exemplo, *TherobotONO*

  - **URL**: A página da internet associada à entrada de senha. Por exemplo, *https://twitter.com*

  - **Senha**: A senha para sua conta. Este campo também permite que você [*gere uma senha aleatória*](#2.4), caso não queira ter de pensar em uma.

  - **Confimar senha**: A confirmação da senha.

  - **Comentários**: Aqui, você pode inserir a descrição ou informações gerais sobre a conta ou página da internet a que se referem estas informações. Por exemplo: Configurações de Servidor de Email: *POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*

**Observação**: Criar ou modificar as entradas de senha no **KeePassDroid** não atualiza a senha da sua conta! Pense no **KeePassDroid** como um caderninho seguro para anotar suas senhas. Ele apenas guarda o que você escrever nele, nada mais.

**Passo 2**. **Toque** em **salvar** para guardar as alterações.

Sua nova entrada agora aparece no grupo.

![](/sbox/screen/keepassdroid-pt/015.png)

*Figura 11: A nova entrada sendo exibida no grupo recém criado.*


<a name="2.3"></a>
## 2.3 Como copiar uma senha do KeePassDroid
Uma vez que senhas seguras não são facilmente memorizáveis, o **KeePassDroid** copiá-las do banco de dados e colá-las em qualquer conta ou página de login.

**Passo 1**. Abra a entrada de senha que você deseja utilizar e **toque** no ícone de menu (![](/sbox/screen/keepassdroid-pt/016.png)):

![](/sbox/screen/keepassdroid-pt/017.png)

*Figura 12: As opções de Senha*

**Passo 2**. **Toque** em ![](/sbox/screen/keepassdroid-pt/018.png)

**Passo 3**. **Abra** a conta ou página relacionada à entrada e **cole** a senha **tocando e mantendo o toque** no campo apropriado e selecionando *Colar*:

![](/sbox/screen/keepassdroid-pt/019.png)

*Figura 13: As opções de edição de texto*

