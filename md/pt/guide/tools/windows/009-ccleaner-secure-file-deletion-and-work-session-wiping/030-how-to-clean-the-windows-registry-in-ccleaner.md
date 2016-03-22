

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Clean the Windows Registry in CCleaner

---

Seções nessa página:

- [**4.0 Antes de começar**](#4.0)
- [**4.1 Como limpar o Registro do Windows usando o CCleaner**](#4.1)
- [**4.2 Como recuperar o arquivo de backup do Registro**](#4.2)


<a name="4.0"></a>
## 4.0 Antes de começar ##

O **CCleaner** também possibilita fazer a limpeza do **Registro do Windows**, um banco de dados que armazena informações de configuração e preferências de hardware e software do seu sistema. Toda vez que você altera informações de configuração do sistema, instala software ou realiza outras tarefas de rotina, essas mudanças são refletidas e armazenadas no **Registro do Windows**.

Com o passar do tempo, porém, o **Registro do Windows** acumula configurações e preferências ultrapassadas, incluindo traços de programas obsoletos. A opção *Registro* do **CCleaner** lhe permite escanear e remover essas informações, melhorando o funcionamento geral e a velocidade do sistema, assim como protegendo sua segurança e privacidade digitais.

**Dica**: Uma *varredura* do **Registro do Windows** deve ser realizada mensalmente.


<a name="4.1"></a>
## 4.1 Como limpar o Registro do Windows usando o CCleaner ##

**Passo 1**. **Clique** em ![](/sbox/screen/ccleaner-pt/30.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/31.png)

*Figura 1: A interface do CCleaner no modo Registro*

A janela *Registro* do **CCleaner** é dividida entre uma lista *Limpador do registro* e um painel, usado para exibir informações sobre quaisquer problemas encontrados.

**Passo 2**. **Marque** todos os itens na lista *Limpador do registro* (como mostra a *Figura 1*), e então **clique** em ![](/sbox/screen/ccleaner-pt/32.png) para começar a procurar por problemas no registro a serem consertados; depois de um tempo, os resultados podem se parecer com estes:

![](/sbox/screen/ccleaner-pt/33.png)

*Figura 2: O painel de resultados exibindo uma lista de problemas a serem consertados*

Como uma medida de precaução, antes de começar a consertá-lo, o programa te obrigará a salvar uma cópia de reserva (*backup*) do **Registro do Windows**. Se um problema ocorrer após a limpeza, é possível restaurá-lo ao estado original com o arquivo de *backup*.

**Passo 3**. **Clique** em ![](/sbox/screen/ccleaner-pt/34.png) para ativar a seguinte caixa de diálogo de confirmação:

![](/sbox/screen/ccleaner-pt/35.png)

*Figura 3: A caixa de diálogo de confirmação*

**Dica**: Se esquecer onde a cópia de reserva (*backup*) do registro ficou armazenada, faça uma busca pela extensão de arquivo *.reg*. 

**Passo 4**. **Clique** em ![](/sbox/screen/ccleaner-pt/36.png) para fazer um *backup* do registro e ative a seguinte tela:

![](/sbox/screen/ccleaner-pt/37.png)

*Figura 4: O navegador de locais Salvar Como*

**Passo 5**. Após escolher um local para o arquivo de *backup*, **clique** em ![](/sbox/screen/ccleaner-pt/38.png) para ativar a seguinte caixa de diálogo:

![](/sbox/screen/ccleaner-pt/39.png)

*Figura 5: A caixa de diálogo Corrigir erro/Corrigir todos os erros selecionados*

**Observação**: Quem possui um nível mais avançado ou é mais experiente vai gostar da possibilidade de consertar alguns problemas e ignorar outros, dependendo das necessidades. Caso contrário, recomendamos simplesmente consertar todos os problemas selecionados.

**Passo 6**. **Clique** em ![](/sbox/screen/ccleaner-pt/40.png) ou em ![](/sbox/screen/ccleaner-pt/41.png) para ver cada problema, e então **clique** em ![](/sbox/screen/ccleaner-pt/42.png) para consertar somente os que quiser.

**Passo 7**. **Clique** em ![](/sbox/screen/ccleaner-pt/43.png) para consertar *todos* os problemas escolhidos, e então **clique** em ![](/sbox/screen/ccleaner-pt/44.png) para completar o processo de limpeza.

**Dica**: Repita os **passos 2** ao **7** até não ver mais problemas a serem consertados.

O **Registro do Windows** acabou de ser limpo com sucesso.


<a name="4.2"></a>
## 4.2 Como recuperar o arquivo de backup do Registro ##

Se você suspeita que a limpeza do **Registro do Windows** tenha causado algum problema no funcionamento geral da máquina, a cópia de reserva (*backup*) do registro criada do **passo 3** ao **5** na seção **4.1** pode ser usada para restaurar o estado original e reduzir a interferência no sistema.

Para restaurar o registro original, siga os seguintes passos:

**Passo 1**. **Selecione Iniciar > Executar** para ativar a janela *Executar*, e então **digite** *regedit* dessa maneira:

![](/sbox/screen/ccleaner-pt/45.png)

*Figura 6: A janela Executar*

**Passo 2**. **Clique** em ![](/sbox/screen/ccleaner-pt/22.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/46.png)

*Figura 7: O Editor do Registro*

**Passo 3**. **Selecione Arquivo > Importar** na barra de menu do *Editor de Registro* para ativar a tela *Importar Arquivo do Registro*, e então **selecione** ![](/sbox/screen/ccleaner-pt/47.png).

**Passo 4**. **Clique** em ![](/sbox/screen/ccleaner-pt/48.png) para ativar a seguinte caixa de diálogo de confirmação:

![](/sbox/screen/ccleaner-pt/49.png)

*Figura 8: Uma caixa de diálogo do Editor do Registro confirmando que o arquivo de *backup* do registro foi restaurado*

**Passo 5**. **Clique** em ![](/sbox/screen/ccleaner-pt/22.png) para completar a restauração do arquivo de *backup* do registro.

