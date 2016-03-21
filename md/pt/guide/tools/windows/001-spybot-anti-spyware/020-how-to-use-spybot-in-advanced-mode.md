

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use Spybot in Advanced Mode

---

Seções nessa página:

- [**3.0 Sobre o modo Avançado**](#3.0)
- [**3.1 Ferramentas do modo Avançado**](#3.1)
- [**3.2 Modo Avançado - Varredura de Rootkit**](#3.2)


<a name="3.0"></a>
## 3.0 Sobre o modo Avançado ##

O **Spybot** possui as seções *Padrão* (*Default*) e *Avançado* (*Advanced*). O modo avançado (*Advanced Mode*) permite modificar configurações e executar tarefas adicionais.

**Clique** em ![](/sbox/screen/spybot-pt/16.png) na tela inicial do programa para exibir as opções de *Ferramentas avançadas* (*Advanced Tools*) e *Ferramentas profissionais* (*Professional Tools*).

![](/sbox/screen/spybot-pt/15a.png)

*Figura 1: As Ferramentas avançadas*


<a name="3.1"></a>
## 3.1 Ferramentas do modo Avançado ## 

A versão gratuita do *Spybot* permite usar apenas algumas das opções disponíveis nas seções de *Ferramentas avançadas* (*Advanced Tools*) e *Ferramentas profissionais* (*Professional Tools*):

- **Report Creator**. O *Gerador de relatórios* pode ser usado para ajudar as equipes de suporte técnico do *Spybot* caso você precise de ajuda com o programa. O nível de suporte disponível costuma depender da versão que você tem do programa - paga ou gratuita, por exemplo. Embora os fóruns de suporte sejam uma fonte útil de conhecimento para decidir se um arquivo é perigoso ou não, recomendamos cuidado antes de submeter quaisquer arquivos ou registros vindos do seu computador caso o anonimato seja uma questão importante para você.

- **Settings**. A seção de *Configurações* permite escolher o Idioma (*Language*), o Escopo da varredura (*Scope of scanning*), quais os navegadores serão escaneados pelo Spybot-S&D etc.

- **Startup Tools**. A seção de *Ferramentas de inicialização* permite rever em detalhes os processos ativos no computador, quais programas são iniciados junto com o sistema, quais as tarefas agendadas pelo sistema, plugins, serviços do sistema, programas instalados etc.

- **Rootkit Scan**. A seção de *Varredura de Rootkit* faz uma varredura no sistema operacional em busca de *rootkits*, programas maliciosos que ficam escondidos no nível do próprio sistema, o que os torna indetectáveis por ferramentas antimalware comuns.


<a name="3.2"></a>
## 3.2 Modo Avançado - Varredura de Rootkit ##

A *Varredura de Rootkit* (*Rootkit Scan*) pode ser usada para marcar arquivos suspeitos e entradas de registros para análise posterior ou para remoção. Os passos abaixo mostram como fazer uma *Varredura de Rootkit*.

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/61.png) no painel de *Ferramentas avançadas* (*Advanced Tools*) para ativar a janela abaixo. Note os resultados do escaneamento rápido exibidos na área *Quick scan test results*. 

![](/sbox/screen/spybot-pt/57.png)

*Figura 5: A Varredura de Rootkit*

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/58.png).

**Passo 3**. **Selecione** os discos e entradas de registro nos quais quer fazer uma varredura. Recomendamos selecionar todos os itens disponíveis. **Clique** em ![](/sbox/screen/spybot-pt/04.png). *Observe* que essa varredura pode levar bastante tempo (talvez cerca de uma hora) para ser executada.

![](/sbox/screen/spybot-pt/59.png)

*Figura 6: A Varredura de Rootkit - Selecione os discos*

![](/sbox/screen/spybot-pt/60.png)

*Figura 7: A Varredura de Rootkit em progresso*

Quando a varredura terminar, a tela de *Search for rootkits* exibirá os arquivos suspeitos encontrados. Você pode rever os arquivos e as opções para determinar se é um arquivo legítimo.

![](/sbox/screen/spybot-pt/62.png)

*Figura 7: A tela de Busca por rootkits - Search for rootkits*

**Passo 4**. **Clique com o botão direito do mouse** em qualquer dos itens exibidos para ver as opções relacionadas a ele:

![](/sbox/screen/spybot-pt/63.png)

*Figura 8: As opções de varredura por rootkit*

**Passo 5**. **Selecione** *Show properties* (*Ver propriedades*) para exibir os detalhes.

**Passo 6**. **Selecione** *Scan file for malware* (*Varrer arquivo em busca de malware*) caso esta opção esteja dispoível. Isso ativará a janela de *File Scan* (*Varredura em arquivo*). O resultado da varredura será exibido como o abaixo.

![](/sbox/screen/spybot-pt/64.png)

*Figura 9: Varredura em arquivo - um arquivo limpo*

**Observação**: Itens detectados com propriedades de rootkit não são necessariamente malware. Apagá-los pode gerar problemas em outros programas. Veja a seção **2.5 Como fazer varreduras por ameaças** e **2.6 Como restaurar um arquivo** ao lidar com os arquivos encontrados durante a *Varredura de Rootkit*.

**Passo 7**. Quando você tiver certeza de que o item encontrado é suspeito, poderá *Apagá-lo* (*Delete*) do sistema.

Se não tiver certeza sobre os arquivos encontrados, é possível pedir ajuda no [Fórum da Análises do Spybot](http://forums.spybot.info/forumdisplay.php?f=46) antes de apagar qualquer coisa. A remoção é definitiva e não pode ser recuperada pela *Quarentena*. Caso ainda queira remover os itens encontrados, é fortemente recomendável [criar um ponto de restauração do sistema](http://windows.microsoft.com/pt-br/windows/system-restore-faq#1TC=windows-7) antes de fazê-lo.

