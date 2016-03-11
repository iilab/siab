

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

Seções nessa página:

- [**2.0 Como instalar o CCleaner**](#2.0)
- [**2.1 Antes de começar a configurar o CCleaner**](#2.1)
- [**2.2 Como configurar o CCleaner**](#2.2)


<a name="2.0"></a>
## 2.0 Como instalar o CCleaner ##

Instalar o **CCleaner** é um procedimento relativamente fácil e rápido. Siga os seguintes passos:

**Passo 1**. **Clique duas vezes** em ![](/sbox/screen/ccleaner-pt/01.png) para começar o processo de instalação. A caixa de diálogo *Abrir Arquivo - Aviso de Segurança* pode aparecer.
Nesse caso, **clique** em ![](/sbox/screen/ccleaner-pt/02.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/03.png)

*Figura 1: Tela Bem-vindo ao Assistente de Instalação do CCleaner v4.15*

**Passo 2**. **Selecione** o idioma "Português Brasileiro" na caixa *Select your language*, e então **clique** em ![](/sbox/screen/ccleaner-pt/05-en.png) para abrir a mesma janela traduzida. **Clique** em ![](/sbox/screen/ccleaner-pt/05.png) para ativar a janela *Opções de Instalação - Selecione as opções adicionais*, e então **clique** em ![](/sbox/screen/ccleaner-pt/05.png) novamente para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/07.png)

*Figura 2: A janela sem título de Instalar Google Chrome como navegador padrão*

**Passo 3**. **Desmarque** ambas as opções de *Instalar Google Chrome como meu navegador padrão* e *Incluir também a Google Toolbar para Internet Explorer*, como mostra a **Figura 2** acima (elas vêm marcadas por padrão). Isso evita que tais programas sejam instalados automaticamente no seu computador. Note que essa tela pode não aparecer durante o processo de instalação.

**Passo 4**. **Clique** em ![](/sbox/screen/ccleaner-pt/08.png) para ativar a tela *Instalando*, que mostra a barra de progresso da instalação.

**Passo 5**. **Clique** em ![](/sbox/screen/ccleaner-pt/09.png) para completar a instalação do **CCleaner** e ativar o console principal do programa.

![](/sbox/screen/ccleaner-pt/12.png)

*Figura 4: O console principal do Piriform CCleaner*


<a name="2.1"></a>
## 2.1 Antes de começar a configurar o CCleaner ##

Como descrito em detalhes no capítulo [**6. Como destruir informações sensíveis**](/pt/chapter-6) do **Guia de Referência**, a remoção padrão de arquivos do **Microsoft Windows** não apaga de verdade os dados do disco (mesmo quando você esvazia a *Lixeira*). Isso também se aplica aos arquivos temporários.

Para [*remover permanentemente*](/pt/glossary#Wiping) os arquivos do disco, eles devem ser sobrescritos com dados aleatórios. Para que a remoção segura aconteça, o **CCleaner** deve ser configurado para sobrescrever quaisquer arquivos removidos pois, por padrão, não age assim. O **CCleaner** também pode apagar informações antigas de forma segura ao limpar o espaço vazio do disco (veja mais na seção **5.3 Como limpar o espaço livre em disco usando o CCleaner**).


<a name="2.2"></a>
## 2.2 Como configurar o CCleaner ##

Antes de começar a usar o **CCleaner**, o programa deve ser configurado para remover seguramente todos os arquivos temporários.

Para configurar o **CCleaner**, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/ccleaner-pt/13.png) ou **selecione Iniciar > Programas > CCleaner** para ativar o console do *Piriform CCleaner*.

**Passo 2**. **Clique** em ![](/sbox/screen/ccleaner-pt/14.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/15.png)

*Figure 6: A aba de Opções exibindo o painel Configurações*

**Passo 3**. **Clique** em ![](/sbox/screen/ccleaner-pt/16.png) para ativar o painel *Configurações*. O painel *Configurações* permite escolher a língua com a qual você se sente mais confortável em trabalhar e determina como o **CCleaner** vai remover arquivos temporários e limpar discos.

**Observação**: A seção *Exclusão segura* aparece com a opção *Exclusão normal de arquivos* habilitada.

**Passo 4**. **Clique** na opção *Exclusão segura de arquivos (Lenta)* para habilitar o *menu expandido*.

**Passo 5**. No **menu expandido** da lista *Exclusão segura de arquivos (Lenta)*, **selecione** o item *DOD 5220.22-M (3 passos)* para se parecer com a seguinte tela:

![](/sbox/screen/ccleaner-pt/17.png)

*Figura 5: O painel Configurações exibindo as opções de Exclusão segura*

Depois de habilitar essa opção, o **CCleaner** vai sobrescrever repetidamente com dados aleatórios arquivos e pastas escolhidos para remoção, como se [*os esfregasse*](/pt/glossary#Wiping) para fora disco rígido. Os *passos* na lista *Exclusão segura* se referem ao número de vezes que os dados serão sobrescritos por dados aleatórios. Isso reduz a possibilidade de recuperar documentos, arquivos e pastas, mas aumenta o tempo necessário para o processo de limpeza.

