

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Advanced Options, FAQ and Review

---

Seções nessa página:

- [**5.0 Opções avançadas**](#5.0)
- [**5.1 Como desinstalar programas usando o CCleaner**](#5.1)
- [**5.2 Como desabilitar o início automático de programas no CCleaner**](#5.2)
- [**5.3 Como limpar o espaço livre em disco usando o CCleaner**](#5.3)
- [**5.4 Perguntas Frequentes e Revisão**](#5.4)
- [**5.5 Perguntas de revisão**](#5.5)


<a name="5.0"></a>
## 5.0 Opções avançadas ##

Duas funcionalidades do **CCleaner** que podem melhorar a eficiência geral do computador são *Desinstalar* e *Programas iniciados com o sistema*, descritas na seção seguinte. Você também verá como [*limpar de forma segura*](/pt/glossary#Wiping) qualquer espaço livre em um disco especificado.


<a name="5.1"></a>
## 5.1 Como desinstalar programas usando o CCleaner ##

**Importante**: Tenha certeza de que o programa a ser removido ou desinstalado não é essencial para o funcionamento do computador antes de começar a seguir esses passos.

Ao remover programas indesejados ou obsoletos, você pode remover também seus arquivos e pastas temporários. Faça-o antes de executar o **CCleaner**, pois isso pode reduzir o número de arquivos e pastas temporários a serem removidos pelo programa, assim como o tempo levado para o processo de limpeza.

A funcionalidade *Desinstalar* do **CCleaner** é equivalente ao **Adicionar ou Remover Programas**, do Microsoft Windows. A funcionalidade *Desinstalar* lista os programas mais clara e rapidamente.

Para começar a desinstalar programas obsoletos, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/ccleaner-pt/13.png) ou **selecione Iniciar > Programas > CCleaner** para ativar o console do *Piriform CCleaner*.

**Passo 2**. **Clique** em ![](/sbox/screen/ccleaner-pt/50.png) e então **clique** em ![](/sbox/screen/ccleaner-pt/51.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/52.png)

*Figura 1: A opção Ferramentas exibindo o painel Desinstalar*

**Observação**: Os botões à direita da lista só são habilitadas depois de o programa ser selecionado para remoção.

**Passo 3**. **Selecione** um programa da lista *Programas para remover* e então **clique** em ![](/sbox/screen/ccleaner-pt/53.png) para desinstalá-lo.

**Dica**: Pessoas com conhecimento mais avançado ou mais experientes vão achar as funcionalidades *Renomear entrada* e *Remover entrada* úteis para manter privada a existência de certos programas. Ambas garantem que só você saberá da existência de determinado programa, mantendo-o a salvo de pessoas hostis ou malignas que possam usar a função **Adicionar/Remover Programas do Microsoft Windows** ou o **CCleaner** para vê-lo.

**Passo 4**. **Clique** em ![](/sbox/screen/ccleaner-pt/54.png) para renomear o programa. Alternativamente, **clique** em ![](/sbox/screen/ccleaner-pt/55.png) para remover um programa dessa lista, mas *sem* realmente desinstalá-lo.


<a name="5.2"></a>
## 5.2 Como desabilitar o início automático de programas no CCleaner ##

Programas com início automático são aqueles configurados para abrir logo que você liga o computador. Eles podem começar a demandar os recursos finitos do sistema, ou tornar o computador mais lento durante a inicialização.

**Passo 2**. **Clique** em ![](/sbox/screen/ccleaner-pt/50.png) e então **clique** em ![](/sbox/screen/ccleaner-pt/56.png) para ativar a seguinte tela:

![](/sbox/screen/ccleaner-pt/57.png) 

*Figura 2: A opção Ferramentas exibindo o painel Programas iniciados com o sistema*

**Passo 3**. **Selecione** um dos programas listados no painel *Programas iniciados com o sistema* e então **clique** em ![](/sbox/screen/ccleaner-pt/58.png) para que ele não mais seja iniciado automaticamente quando ligar o computador.


<a name="5.3"></a>
## 5.3 Como limpar o espaço livre em disco usando o CCleaner ##

No sistema operacional **Windows**, o ato de apagar um arquivo meramente remove uma referência a ele, mas pode não eliminar seus dados de verdade. É como se ele continuasse no mesmo lugar, oculto apenas aos olhos do sistema, que agora enxerga aquele local como espaço livre.

Embora a área onde aquele arquivo se encontra no disco será eventualmente sobrescrita por novos dados, pode ser que ela seja sobrescrita apenas em parte, tornando possível a uma pessoa habilidosa remontar algumas ou até mesmo todas as partes daquele arquivo.

Você pode evitar que isso aconteça fazendo uma [*limpeza segura*](/pt/glossary#Wiping) do espaço livre em seu disco rígido. O **CCleaner** também lhe permite limpar o **Master File Table**.

O **Master File Table (MFT)** é um índice com todos os nomes de arquivo, suas localizações e outras informações. Quando o **Microsoft Windows** remove um arquivo, só marca sua entrada de índice como removida por questões de eficiência; sua entrada **MFT**, assim como seu conteúdo continuam no disco.

**Observação**: Executar uma limpeza do disco rígido e do **Master File Table** consome uma quantidade considerável de tempo, sendo que o tempo necessário depende do número configurado de passadas.

Para definir o disco ou pendrive que você deseja limpar, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/ccleaner-pt/61.png) e então **clique** em ![](/sbox/screen/ccleaner-pt/62.png) para ativar o painel *Limpeza do dispositivo*.

**Passo 2**. **Clique** em *Limpar* ![](/sbox/screen/ccleaner-pt/04.png) para ativar seu *menu expandido* e então **selecione** um dos itens *Apenas espaço livre* ou *Remover todos os dados*, e então **selecione** ![](/sbox/screen/ccleaner-pt/59.png) no *menu expandido* de *Segurança*.

**Aviso**: Somente selecione o item *Remover todos os dados* se você tiver *certeza* de que quer seus documentos, arquivos, pastas *e* espaço livre apagados.

**Passo 3**. **Clique** na caixinha de marcar associada ao disco/pendrive a ser limpo, e habilite o ![](/sbox/screen/ccleaner-pt/64.png); sua janela agora deve se parecer com isso:

![](/sbox/screen/ccleaner-pt/65.png)

*Figura 3: O painel Limpeza do dispositivo com as opções relevantes habilitadas*

**Passo 4**. **Clique** em ![](/sbox/screen/ccleaner-pt/64.png) para começar a limpar o(s) disco(s) selecionado(s).


<a name="5.4"></a>
## 5.4 Perguntas Frequentes e Revisão ##

Elena e Nikolai acham o **CCleaner** fácil de usar, mas ainda têm algumas perguntas sobre como e quando usá-lo

<div class="background" markdown="1">

***P**: Se eu desinstalar o **CCleaner**, o material que removi antes ainda continuará removido?*

***R**: Sim. Se você configurou e rodou o **CCleaner** corretamente, os arquivos removidos continuarão removidos - permanentemente.*

***P**: Se eu copiar o **CCleaner** para um pendrive, posso usá-lo no computador de uma lan house para apagar vestígios do meu trabalho por lá? Há alguma razão para eu não usá-lo dessa maneira?*

***R**: Sim! Há uma versão portátil do **CCleaner** (veja a seção **CCleaner - Portable** na página de downloads da [**www.piriform.com/ccleaner/builds**](http://www.piriform.com/ccleaner/builds)). Se a lan house na qual você está trabalhando te deixar rodar programas de um pendrive, então sim, você pode usar a versão portátil do **CCleaner** para pagar vestígios de que você trabalhou por lá. No entanto, lembre-se que você pode estar sendo monitorado em uma lan house. Também há o risco de infecção ao conectar seu pendrive no computador de uma lan house.*

***P**: Se eu usar só uma passada do **CCleaner**, é possível que alguém recupere meus dados? E se eu usar 7 passadas?*

***R**: Uma ótima pergunta! Quanto mais passos forem usados para limpar os dados, menos chance alguém terá de recuperá-los. No entanto, aumentar o número de passos usados ao limpar dados também aumenta a duração do processo de limpeza.*

***P**: Limpar o **Registro do Windows** é suficiente para remover todos os sinais óbvios de que instalei e usei temporariamente certos programas no meu computador?*

***R**: Sim. Idealmente, você deve remover todos os arquivos temporários e limpar o **Registro do Windows** para remover todos os vestígios de software e de tarefas que você fez nele. No entanto, se o tempo é limitado, limpar o **Registro do Windows** é um bom começo!*

</div>


<a name="5.5"></a>
## 5.5 Perguntas de revisão ##

  * Que tipo de dados o **CCleaner** remove do seu computador?
  * Como ele faz isso?
  * Que diferença faz o número de passos que você escolhe quando sobrescreve os dados seguramente?
  * O que é o **Registro do Windows**, e por que recomendamos que você o limpe?
  * O que você deve fazer antes de limpar o **Registro do Windows**?

