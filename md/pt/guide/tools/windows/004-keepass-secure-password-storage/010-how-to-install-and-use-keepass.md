

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Use KeePass

---

Seções nessa página:

- [**2.0 Como instalar o KeePass**](#2.0)
- [**2.1 Como deixar a interface do KeePass em português**](#2.1)
- [**2.2 Como criar um novo banco de dados de senhas**](#2.2)
- [**2.3 Como adicionar uma entrada**](#2.3)
- [**2.4 Como editar uma entrada**](#2.4)
- [**2.5 Como gerar senhas aleatórias**](#2.5)
- [**2.6 Como fechar, minimizar e restaurar o KeePass**](#2.6)
- [**2.7 Como criar um backup do seu banco de dados de senhas**](#2.7)
- [**2.8 Como trocar a senha mestra**](#2.8)


<a name="2.0"></a>
## 2.0 Como instalar o KeePass ##

**Passo 1**. **Dê dois cliques** em ![](/sbox/screen/keepass-pt/01.png); a caixa de diálogo *Abrir Arquivo - Aviso de Segurança* pode aparecer. Nesse caso, **clique** em ![](/sbox/screen/keepass-en/02.png) para ativar a seguinte tela:

![](/sbox/screen/keepass-pt/03.png)

*Figura 1: A tela de Selecionar Idioma do Programa de Instalação*

**Passo 2**. Na caixa *Selecione o idioma a ser utilizado durante a instalação*, escolha o idioma "Português (Brasil)" e então **clique** em ![](/sbox/screen/keepass-pt/04.png) para ativar a tela *KeePass Password Safe - Programa de Instalação – Bem-vindo ao Assistente de Instalação de KeePass Password Safe*.

**Passo 3**. **Clique** em ![](/sbox/screen/keepass-pt/05.png) para ativar a tela *Contrato de Licença de Uso*. Leia o *Contrato de Licença de Uso* antes de continuar com o restante do processo de instalação.

**Passo 4**. **Marque** a opção *Eu aceito os termos do Contrato* para habilitar o botão *Avançar*, e então **clique** em ![](/sbox/screen/keepass-pt/05.png) para ativar a tela *Selecione o Local de Destino*.

**Passo 5**. **Clique** em ![](/sbox/screen/keepass-pt/05.png) para aceitar a pasta padrão de instalação e ativar a seguinte tela.

![](/sbox/screen/keepass-pt/06.png)

*Figura 2: A tela de Selecionar Tarefas Adicionais*

**Passo 6**. **Marque** a opção ![](/sbox/screen/keepass-pt/07.png) como mostrado na *Figura 2*, acima.

**Observação**: Se você habiliar a opção *Criar um ícone na Barra de Inicialização Rápida*, o *KeePass Password Safe - Programa de Instalação* automaticamente criará um ícone do **KeePass** ao lado do menu *Iniciar*.

**Passo 7**. **Clique** em ![](/sbox/screen/keepass-pt/05.png) para abrir a tela de resumo *Pronto para Instalar*, e então **clique** em ![](/sbox/screen/keepass-pt/08.png).

Alguns segundos depois, a tela *Finalizando o Assistente de Instalação de KeePass Password Safe* aparecerá.

**Passo 8**. **Marque** a opção *Executar KeePass* e então **clique** em ![](/sbox/screen/keepass-pt/09.png) para abrir o **KeePass** imediatamente. Se estiver conectado à Internet, página *Plugins and Extensions* do **KeePass** será aberta.


<a name="2.1"></a>
## 2.1 Como deixar a interface do KeePass em português ##

É possível deixar a interface do KeePass em português. Para isso, siga os seguintes passos:

**Passo 1**. Abra o link [www.keepass.info/translations.html](http://www.keepass.info/translations.html).

**Passo 2**. Na listagem, encontre a versão "Portuguese, BR" e baixe o arquivo para versão *[1.27+]*.

**Passo 3**. Extraia o arquivo *Portuguese_BR.lng* para a mesma pasta onde o programa do KeePass foi instalado - no Windows, a pasta padrão é *C:/Arquivos de Programas/KeePass Password Safe/*.

**Passo 4**. **Selecione Iniciar > Programas > KeePass** ou **clique** no ícone ![](/sbox/screen/keepass-pt/36.png) na Área de Trabalho para ativar a tela principal do **KeePass**.

**Passo 5**. **Selecione View > Change Language** para abrir a tela 'Load Language File', como na imagem abaixo.

![](/sbox/screen/keepass-pt/keepass_language.png)

**Passo 6**. **Selecione Portuguese_BR** entre as línguas disponíveis. Clique em ![](/sbox/screen/keepass-pt/43.png) para reiniciar o KeePass, já em português.


<a name="2.2"></a>
## 2.2 Como criar um novo banco de dados de senhas ##

Nas seções seguintes, você aprenderá a criar uma senha mestra, salvar seu banco de dados recém-criado, gerar uma senha aleatória para um determinado programa, criar uma cópia de resevra (*backup*) do seu banco de dados e extrair as senhas do **KeePass** quando necessário.

Para abrir o **KeePass**, **selecione Iniciar > Programas > KeePass** ou **clique** no ícone ![](/sbox/screen/keepass-pt/36.png) na Área de Trabalho para ativar a tela principal, que se parecerá com essa:

![](/sbox/screen/keepass-pt/10.png)

*Figura 3: O console do KeePass*

### 2.2.1 Como criar um novo banco de dados de senhas

Criar um novo banco de dados de senhas consiste em dois passos. Primeiro, é preciso pensar em uma senha mestra, única e forte, que você usará para bloquear e desbloquear seu banco de dados de senhas. Depois, é necessário salvar o banco de dados de senhas.

Para criar um novo banco de dados de senhas, siga os seguintes passos:

**Passo 1**. **Selecione Arquivo > Novo banco...** desta maneira:

![](/sbox/screen/keepass-pt/11.png)

*Figura 4: A tela do KeePass com a opção Arquivo > Novo banco... selecionada*

Isso ativará a tela *Criação de Banco de Dados* desta maneira:

![](/sbox/screen/keepass-pt/12.png)

*Figura 5: A tela Criação de Banco de Dados*

**Passo 2**. **Digite** a senha mestra que você criou no campo *Senha Mestra*.

![](/sbox/screen/keepass-pt/13.png)

*Figura 6: A tela Configurar Chave Mestra Composta do KeePass, com o campo Senha Mestra preenchido.*

Uma barra de progresso laranja e verde abaixo do campo de senha será exibida. Conforme você digita uma senha e o número de caracteres cresce, a proporção de verde na barra aumentará para refletir a melhoria da complexidade e força da sua senha.

**Dica**: Tenha como meta encher pelo menos a metade da barra de verde ao terminar de digitar sua senha.

**Passo 3**. **Clique** em ![](/sbox/screen/keepass-pt/14.png) para ativar a tela *Repita a Senha Mestra* e confirme a senha mestra na tela abaixo:

![](/sbox/screen/keepass-pt/15.png)

*Figura 7: A tela Repita a Senha Mestra do KeePass*

**Passo 4**. **Digite** a mesma senha de antes, e então **clique** em ![](/sbox/screen/keepass-pt/14.png).

**Passo 5**. Se quiser ver a senha como texto, para confirmar se a digitação está correta, **clique** em ![](/sbox/screen/keepass-pt/16.png).

**Aviso**: Jamais use o botão descrito no *Passo 5* se suspeitar que alguém possa estar olhando a tela do seu computador por trás de você.

Assim que houver digitado a senha mestra duas vezes, o console do **KeePass** será ativado da seguinte maneira:

![](/sbox/screen/keepass-pt/17.png)

*Figura 8: A tela do KeePass em modo ativo*

Um banco de dados de senhas acabou de ser criado. Agora, é necessário salvá-lo. Para fazê-lo, siga esses passos:

**Passo 1**. **Selecione Arquivo > Salvar como** desta maneira:

![](/sbox/screen/keepass-pt/18.png)

*Figura 9: A opção de Salvar Como, no menu de Arquivo*

Isso ativará a janela de 'Salvar como' desta maneira:

![](/sbox/screen/keepass-pt/19.png)

*Figura 10: A janela Salvar Como*

**Passo 2**. **Digite** um nome para seu novo arquivo de banco de dados de senhas.

**Passo 3**. **Clique** em ![](/sbox/screen/keepass-pt/20.png) para salvar o banco de dados.

**Dica**: Lembre-se do local e do nome do arquivo do seu banco de dados! Isso vai ser muito útil no momento que for criar uma cópia reserva (*backup*) dele.

Parabéns! Você criou e salvou seu banco de dados seguro de senhas com sucesso. Agora já pode começar a preenchê-lo com todas as suas senhas atuais e futuras.


<a name="2.3"></a>
## 2.3 Como adicionar uma entrada ##

A tela *Adicionar entrada* permite que você adicione informações de contas, senhas e outros detalhes importantes em seu banco de dados recém-criado. No exemplo a seguir, você adicionará entradas para guardar logins e senhas para diferentes sites e contas de e-mail.

**Passo 1**. **Selecione Editar > Adicionar entrada** na tela principal do KeePass para ativar a tela *Adicionar entrada* desta maneira:

![](/sbox/screen/keepass-pt/21.png)

*Figura 11: A tela principal do KeePass com a opção 'Editar > Adicionar entrada' selecionada*

![](/sbox/screen/keepass-pt/22.png)

*Figura 12: A tela Adicionar entrada do KeePass*

**Observação**: A tela *Adicionar entrada* apresenta uma série de campos a serem preenchidos. Nenhum desses campos é obrigatório; as informações passadas aqui servem para a sua própria conveniência. Elas podem ser úteis em situações onde você busca por uma entrada em particular.

Uma breve explicação dessas diferentes caixas de texto é apresentada a seguir:

  * **Categoria**: O **KeePass** permite organizar suas senhas em categorias pré-definidas. Por exemplo: *'Internet'* seria um bom local para guardar senhas relacionadas a contas em sites.
  * **Título**: Um nome para descrever essa entrada de senha em particular. Por exemplo: Senha do Gmail.
  * **Usuário**: O login, ou nome de usuária/o, associado com essa entrada de senha. Por exemplo: securitybox@gmail.com.
  * **Endereço**: O site associado com a entrada de senha. Por exemplo: https://mail.google.com.
  * **Senha**: Essa funcionalidade gera automaticamente uma senha aleatória quando a tela *Adicionar entrada* é ativada. Se você está registrando uma nova conta de e-mail, pode usar a combinação 'padrão' que já aparece nesse campo. Também é possível usar essa funcionalidade se quiser trocar uma senha já existente pela gerada pelo **KeePass**; como o programa sempre a lembrará por você, não é preciso nem vê-la. Uma senha gerada aleatoriamente é considerada forte, ou seja, é uma combinação difícil para que um alguém a adivinhe ou quebre.

Explicaremos como gerar uma combinação aleatória sob demanda na próxima seção. É possível, claro, substituir a senha padrão por outra de sua escolha. Por exemplo, ao criar uma entrada para uma conta que já existe, você vai querer preencher esse campo com a senha correta.

- **Repita**: A confirmação da senha.
- **Qualidade**: Uma barra de progresso que mede a força da senha de acordo com seu tamanho e aleatoriedade. Quanto mais verde houver na escala, mais forte é a senha que você escolheu.

**Observação**: Criar ou modificar as entradas de senha no **KeePass** não muda de fato a sua senha! Pense no **KeePass** como uma agenda eletrônica segura para suas senhas. Ela só guarda o que você escrever nela, nada mais.

Se você selecionar *Internet* da lista expandida *Categoria*, sua entrada de senha pode se parecer com o seguinte:

![](/sbox/screen/keepass-pt/24.png)

*Figura 13: A tela Adicionar entrada do KeePass preenchida*

**Passo 2**. **Clique** em ![](/sbox/screen/keepass-pt/14.png) para salvar suas mudanças da tela *Adicionar entrada*.

Sua entrada de senha agora aparece no grupo *Internet*.

![](/sbox/screen/keepass-pt/25.png)

*Figura 14: A tela do KeePass com uma nova entrada de senha*

**Observação**: O painel inferior dessa janela exibe informações sobre a entrada selecionada. Isso inclui os horários de criação, edição e expiração, assim como as anotações que você pode haver associado a ela, mas não revela a senha.

  * **Expiração**: Marque este item para ativar as caixas de texto nas quais você pode especificar uma data de expiração. Ao fazer isso, é possível criar um lembrete de mudança de senha para um dia específico (por exemplo, a cada 3 meses). Quando a senha expirar, ela aparecerá com uma cruz vermelha ao lado do nome, como se vê no o exemplo abaixo:

![](/sbox/screen/keepass-pt/23.png)

*Figura 15: Exemplo de uma senha expirada na tela NetSecureDb.kdb*


<a name="2.4"></a>
## 2.4 Como editar uma entrada ##

Você pode editar uma entrada existente no **KeePass** a qualquer momento. É possível mudar sua senha ou modificar outros detalhes armazenados nela. Costuma-se considerar uma boa prática de segurança trocar de senha em intervalos de três a seis meses (lembrando de atualizá-la no sistema de e-mail, site etc antes de modificá-la no KeePass).

Para editar uma entrada, siga os seguintes passos:

**Passo 1**. **Selecione** a *Categoria* correta do lado esquerdo para ativar as entradas associadas a ela.

**Passo 2**. **Selecione** a entrada relevante e então **clique com o botão direito do mouse** na entrada selecionada para ativar a seguinte janela:

![](/sbox/screen/keepass-pt/26.png)

*Figura 16: O KeePass exibindo o menu Editar*

**Passo 3**. **Clique** em ![](/sbox/screen/keepass-pt/14.png) para salvar quaisquer mudanças feitas às informações, inclusive a senha.

Para mudar uma senha existente, já criada anteriormente, por uma gerada e sugerida pelo **KeePass**, leia a próxima seção.


<a name="2.5"></a>
## 2.5 Como gerar senhas aleatórias ##

Senhas longas e aleatórias são consideradas fortes no mundo da segurança. A aleatoriedade dessas senhas é baseada em princípios matemáticos e não pode simplesmente ser 'adivinhada' por alguém que tente invadir uma de suas contas. Para ajudar nesse processo de criação, o **KeePass** oferece um *Criador de Senha*. Como você viu antes, uma senha aleatória é automaticamente gerada quando uma nova entrada é adicionada. Esta seção descreverá como gerar uma combinação por conta própria.

**Observação**: O *Criador de Senha* pode ser ativado de dentro das telas *Adicionar entrada* e *Editar/exibir a entrada*. Alternativamente, **selecione: Ferramentas > Criador de Senha**.

**Passo 1**. **Clique** em ![](/sbox/screen/keepass-pt/27.png) de dentro de uma das telas *Adicionar entrada* e *Editar/exibir a entrada* para ativar a tela *Criador de Senha* desta maneira:

![](/sbox/screen/keepass-pt/28.png)

*Figura 17: A tela do Criador de Senha do KeePass*

A tela do *Criador de Senha* apresenta uma série de opções para gerar uma senha. É possível especificar o tamanho da combinação desejada, os tipos de caracteres usadas pra criá-la, dentre outras. Para nossos propósitos, podemos usar as opções apresentadas por padrão. Isso significa que nosso segredo gerado terá o tamanho de 20 caracteres e será constituído por letras maiúsculas e minúsculas e também por números.

**Passo 2**. **Clique** em ![](/sbox/screen/keepass-pt/29.png) para começar o processo. Quando terminar, o **KeePass** apresentará a senha gerada.

![](/sbox/screen/keepass-pt/30.png)

*Figura 18: A seção 'Senha gerada' do KeePass*

**Observação**: É possível ver a senha gerada **clicando** em ![](/sbox/screen/keepass-pt/16.png). No entanto, mostrá-la pode ser um risco de segurança caso outra pessoa também possa ver a tela de seu computador, mesmo que por trás de você. Resumindo, você nunca precisará ver a combinação gerada. Falaremos mais sobre isso na seção [**3.0 Usando as senhas do KeePass**](/pt/keepass_passwords).

**Passo 3**: **Clique** em ![](/sbox/screen/keepass-pt/31.png) para aceitar a senha e voltar à tela *Adicionar entrada* desta maneira:

![](/sbox/screen/keepass-pt/24.png)

*Figura 19: A tela Adicionar entrada do KeePass*

**Passo 4**. **Clique** em ![](/sbox/screen/keepass-pt/14.png) para salvar essa entrada.

**Passo 5**. **Selecione Arquivo > Salvar** para salvar seu banco de dados de senhas atualizado.


<a name="2.6"></a>
## 2.6 Como fechar, minimizar e restaurar o KeePass ##

Você pode minimizar ou fechar o **KeePass** a qualquer momento. Quando abrir ou restaurar o programa novamente, será preciso digitar a *Senha Mestra*.

Ao ser minimizado, o ícone do **KeePass** aparece na *Bandeja do Sistema* (no canto inferior direito da tela) desta maneira: ![](/sbox/screen/keepass-pt/39.png).

Também é possível bloquear o programa. Para fazê-lo, siga os seguintes passos:

**Passo 1**. **Selecione Arquivo > Bloquear o acesso à interface** para ativar a seguinte tela:

![](/sbox/screen/keepass-pt/40.png)

*Figura 20: A tela KeePass - Confirmar*

**Passo 2**. **Clique** em ![](/sbox/screen/keepass-pt/43.png) para salvar suas informações e desabilitar o console do **KeePass**, fazendo com que ele se pareça à *Figura 3*. O seguinte ícone aparecerá na sua *Bandeja do Sistema*: ![](/sbox/screen/keepass-pt/42.png).

Para restaurar o **KeePass**, siga os seguintes passos:

**Passo 1**. **Dê dois cliques** nesse ícone para restaurar o **KeePass** a seu tamanho normal e ativar a seguinte tela:

![](/sbox/screen/keepass-pt/33.png)

*Figura 21: A tela 'Banco de Dados - NetSecureDb.kdb' do KeePass*

**Passo 2**. **Digite** sua *Senha Mestra* para abrir o programa.

Para fechar o **KeePass** completamente, **selecione Arquivo > Fechar**. Se houver mudanças não salvas no banco de dados, o programa pedirá que você as salve.


<a name="2.7"></a>
## 2.7 Como criar um backup do seu banco de dados de senhas ##

O arquivo de banco de dados do **KeePass** no seu computador é reconhecido por sua extensão .kdb. Você pode copiar esse arquivo para um pen drive, pois não é possível abrir o banco de dados sem ter a senha mestra.

Para fazê-lo, **selecione Arquivo > Salvar como**, na tela principal, e salve uma cópia do banco de dados em outro local.

É possível executar o **KeePass** inteiramente a partir de um pen drive. Veja mais informações na seção [**KeePass - Versão portátil**](/pt/keepass_portable).


<a name="2.8"></a>
## 2.8 Como trocar a senha mestra ##

É possível trocar a *Senha Mestra* a qualquer momento que o banco de dados de senhas esteja aberto. Para isso, siga os passos:

**Passo 1**. **Selecione Arquivo > Alterar a senha mestra**

![](/sbox/screen/keepass-pt/34.png)

*Figura 22: A tela 'Alterar a senha mestra' do KeePass*

**Passo 2**. **Digite** a nova *Senha Mestra* duas vezes quando pedido pelo programa.

![](/sbox/screen/keepass-pt/35.png)

*Figura 23: A tela de 'Alteração da Senha Mestra' do KeePass*

