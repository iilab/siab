

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

Ao usar uma ferramenta para apagar dados de forma segura, como as recomendadas neste capítulo, seria mais correto dizer que você estará substituindo, ou 'sobrescrevendo', as informações sensíveis, em vez de simplesmente apagando-as.

Vamos retomar o exemplo descrito acima, dos armários hipotéticos. Se imaginar que os documentos guardados lá dentro estão escritos a lápis, então o software para eliminar dados de forma segura não apenas apaga seu conteúdo, mas rabisca em cima de cada palavra. E, assim como em um papel, os escritos contidos naqueles documentos ainda poderão ser lidos, embora com dificuldade, mesmo depois de apagados e de ter algo rabiscado em cima.

Por este motivo, as ferramentas recomendadas aqui sobrescrevem os arquivos diversas vezes com dados aleatórios. Este processo é chamado em inglês de [*wiping*](/pt/glossary#Wiping), cuja tradução contextual seria 'esfregar'. Quanto mais vezes uma informação é sobrescrita, mais difícil fica para alguém recuperar o conteúdo original. Em geral, especialistas tendem a concordar que os espaços em disco devem ser sobrescritos (ou *esfregados*) três ou mais vezes para serem considerados 'limpos'; alguns padrões recomendam sete ou mais. Programas que [*apagam arquivos de forma segura*](/pt/glossary#Wiping) automaticamente fazem um número razoável de passagens, mas é possível mudá-lo se quiser.


### Apagando arquivos de forma segura ### 

Existem duas formas mais comuns de [*apagar de forma segura*](/pt/glossary#Wiping) informações sensíveis em discos rígidos de computadores ou outros dispositivos de armazenamento: é possível fazer isso com um arquivo único ou com todo o espaço 'não alocado'. Para tomar tal decisão, pode ser útil lembrar-se de outro exemplo proposto acima, o do longo relatório que pode ter deixado cópias de versões anteriores espalhadas no disco rígido (mesmo que apenas um arquivo seja visível).

Se você [*apagar de forma segura*](/pt/glossary#Wiping) apenas o arquivo, garantirá que a versão atual seja completamente eliminada, mas manterá as outras cópias onde estão. Na verdade, não há como alcançar tais cópias diretamente, pois são visíveis apenas por software especiais. Entretanto, ao [*apagar de forma segura*](/pt/glossary#Wiping) todo o espaço em branco do dispositivo de armazenamento (também chamado de espaço não alocado), é possível assegurar que toda a informação previamente apagada ali seja destruída.

Voltando à metáfora do armário mal etiquetado, o procedimento é equivalente a abrir todos os compartimentos do armário e então apagar e rabiscar repetidas vezes os documentos cujas etiquetas haviam sido removidas.

O [*Eraser*](/pt/glossary#Eraser) é uma ferramenta [*livre e de código aberto (FOSS)*](/pt/glossary#FOSS) extremamente fácil de usar. É possível usá-lo para [*apagar de forma segura*](/pt/glossary#Wiping) um arquivo único ou o conteúdo da **Lixeira**, assim como para [*limpar de forma segura*](/pt/glossary#Wiping) todo o espaço não alocado em um disco ou o conteúdo do [*arquivo de swap*](/pt/glossary#Swap_file) do Windows, como discutido abaixo.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Eraser - Remoção segura de arquivos*](/en/eraser_main)
</div>

Embora ferramentas de remoção segura não danifiquem arquivos visíveis a menos que você explicitamente as peça para fazê-lo, é importante ter cuidado com programas desse tipo. Afinal, acidentes acontecem, e é este o motivo pelo qual as pessoas acham **Lixeiras** e ferramentas de recuperação de dados tão úteis. Se você criar o hábito de sempre apagar os dados [*de forma segura*](/pt/glossary#Wiping) em vez de usar a forma mais comum, pode não ter mais como se recuperar de um erro simples. Tenha sempre cópias de reserva (*backup*) em outro lugar antes de [*apagar de forma segura*](/pt/glossary#Wiping) grandes quantidades de dados de um computador.

<div class="background" markdown="1">
Elena: Sei que programas de processamento de texto como Microsoft Word, Open Office e LibreOffice às vezes fazem cópias temporárias de um documento, quando estamos trabalhando nele. Outros aplicativos também fazem isso? Ou eu deveria me preocupar apenas com os arquivos que eu mesma crio e apago?

Nikolai: Na verdade, há um monte de lugares no seu computador onde os programas deixam traços de suas informações pessoais e atividades online. Estou falando dos sites que você visitou, rascunhos de e-mails feitos recentemente e coisas desse tipo. Tudo isso pode ser sensível, dependendo de quão frequentemente você usa aquele computador.
</div>


### Apagando dados temporários de forma segura ###

A função que permite ao [*Eraser*](/pt/glossary#Eraser) [*limpar de forma segura*](/pt/glossary#Wiping) todo o espaço não alocado em um disco não é tão arriscada quanto possa parecer, pois age apenas sobre conteúdo previamente apagado. Arquivos normais, visíveis, não são afetados.

Por outro lado, isso serve para evidenciar outra questão: o [*Eraser*](/pt/glossary#Eraser) não conseguirá remover os dados sensíveis que não foram apagados e que podem estar extremamente bem escondidos. Arquivos assim podem estar armazenados em pastas obscuras, ou possuir nomes sem qualquer significado. Isso não é um grande problema para documentos eletrônicos, mas pode ser muito importante no caso de informações coletadas automaticamente sempre que você usa o computador. Por exemplo:

  * Dados temporários guardados pelo navegador ao exibir páginas da internet, incluindo texto, imagens, [*cookies*](/pt/glossary#Cookie), informações de contas, informações pessoais usadas para preencher formulários online e histórico dos sites que você visitou.
  * Arquivos temporários salvos por vários aplicativos, com o objetivo de ajudar a recuperar trabalhos caso o computador pare de funcionar antes que você os termine. Essa categoria pode incluir textos, imagens, planilhas com dados e o nome de outros arquivos, além de outras informações potencialmente sensíveis.
  * Arquivos e links armazenados pelo Windows por conveniência, como atalhos para programas usados recentemente, links óbvios para pastas que você preferiria que estivessem escondidas e, claro, o conteúdo da **Lixeira**, caso tenha se esquecido de esvaziá-la.
  * O [*arquivo swap*](/pt/glossary#Swap_file) do Windows. Quando a memória do seu computador está cheia, o que pode acontecer, por exemplo, quando vários programas são usados ao mesmo tempo em computadores mais antigos, o Windows copia parte dos dados que estão sendo usados para um grande arquivo único. Como resultado, o [*arquivo swap*](/pt/glossary#Swap_file) (ou [*área de troca*](/pt/glossary#Swap_file)) pode conter quase qualquer coisa, incluindo páginas da internet, conteúdo de documentos, senhas ou chaves de criptografia. Mesmo quando a máquina é desligada, a [*área de troca*](/pt/glossary#Swap_file) não é esvaziada ou removida, então é preciso limpá-la manualmente.

Para remover arquivos temporários comuns de seu computador, você pode usar uma ferramenta freeware chamada [*CCleaner*](/pt/glossary#CCleaner), desenvolvida para eliminar os rastros deixados por programas como o Internet Explorer, Mozilla [*Firefox*](/pt/glossary#Firefox) e Microsoft Office - todos conhecidos por expor informações potencialmente sensíveis. O [*CCleaner*](/pt/glossary#CCleaner) também pode ser usado para limpar o próprio Windows e tem a função de [*limpar dados de forma segura*](/pt/glossary#Wiping), o que evita o trabalho extra de ter de fazer isso com o [*Eraser*](/pt/glossary#Eraser) em espaços não alocados do disco toda vez que usá-lo.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*CCleaner - Remoção segura de arquivos e limpeza da sessão de trabalho*](/pt/ccleaner_main)
</div>

