

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

Seções nessa página:

- [**4.0 Antes de começar**](#4.0)
- [**4.1 Um guia rápido sobre como lidar com surtos de vírus**](#4.1)
- [**4.2 Uma visão geral sobre a interface principal do avast!**](#4.2)
- [**4.3 Como fazer varreduras em busca de malware e vírus**](#4.3)
- [**4.4 Como fazer uma varredura completa do sistema**](#4.4)
- [**4.5 Como fazer uma varredura em uma pasta**](#4.5)
- [**4.6 Como fazer uma varredura ao iniciar o sistema**](#4.6)
- [**4.7 Como lidar com vírus**](#4.7)
- [**4.8 Como usar a Quarentena**](#4.8)
- [**4.9 Métodos avançados de remoção de vírus**](#4.9)
- [**4.10 O Escaneamento inteligente**](#4.10)



<a name="4.0"></a>
### 4.0 Antes de começar ###

Existem dois momentos principais ao lidar com malware e outros vírus ao usar o **avast!**. O primeiro é fazer uma varredura (ou *escaneamento*) de forma a identificar tais ameaças. O segundo envolve apagar ou mover tais ameaças para a *Quarentena*. Apagar ou mover malware e vírus para a *Quarentena* evita de forma efetiva que interajam com outros programas ou arquivos do computador.

Pode parecer estranho guardar os malware ou vírus na *Quarentena*. Porém, caso essas ameaças tenham se ligado a informações sensíveis ou importantes, você pode querer recuperar o documento, arquivo ou programa infectado o mais que puder. Também pode acontecer, embora seja raro, que o **avast!** identifique de forma errada arquivos ou programas legítimos como malware ou vírus, o que costuma ser chamado de 'falsos positivos'. Tais arquivos ou programas podem ser importantes para você ou para o funcionamento do seu sistema e você vai querer examiná-los com cuidado, desinfectá-los e recuperá-los.

A *Quarentena* do **avast!** é uma 'zona morta' eletrônica na qual é possível examinar o vírus e determinar sua ameaça potencial, seja pesquisando a seu respeito na internet, seja submetendo-o a um laboratório de pesquisas sobre vírus - uma opção disponível ao clicar com o botão direito do mouse em um vírus listado na *Quarentena*. Dar um duplo clique em um vírus na *Quarentena* *não* o ativará ou o executará, pois ele está isolado do resto do sistema.

**Dica**: De forma alternativa, você pode transferir informações importantes ou sensíveis para a *Quarentena* do **avast!** para mantê-los seguros em casos de ataques de vírus.


<a name="4.1"></a>
### 4.1 Um guia rápido sobre como lidar com surtos de vírus ###

Há diversas precauções que você pode tomar para limitar as ameaças ao sistema do seu computador. Como exemplos, usar versões atualizadas de programas antivírus ou antispyware como o **avast!** e o **Spybot**, evitar sites dúbios ou problemáticos na internet, evitar documentos suspeitos enviados a você, e ter cuidado extremo ao inserir mídias removíveis na máquina. Leia mais sobre esses temas na seção [Como prevenir contaminações de vírus](/pt/chapter_1_1) do Capítulo [1. Como proteger seu computador de programas maliciosos e hackers](/pt/chapter-1), do **Guia de Referência**.

Apesar de todas as precauções, às vezes nosso computador ainda é infectado com um vírus. Os seguintes pontos são levantados para consideração ao lidar com um ataque de vírus:
 
- Desconecte o computador da internet e da rede local - fisicamente. Caso tenha uma conexão sem fio, desconecte o computador dessa rede. Se possível, desligue e/ou remova sua placa de conexão sem fio. Desconecte da internet todos os computadores que dividem uma rede local com a máquina infectada.

- Agende uma varredura (*escaneamento*) de inicialização para todos os computadores da rede. Escreva os nomes dos vírus que encontrar para pesquisá-los - e então remova-os ou mova-os para a *Quarentena* do **avast!**. Para saber mais sobre como fazer uma varredura de inicialização, veja a seção [**4.6 Como fazer varredura ao iniciar o sistema**](#4.6).

- Ainda que um vírus tenha sido apagado ou reparado, repita o passo anterior e faça varreduras de inicialização em *todos* os computadores até que o **avast!** não exiba mais mensagens de aviso. Dependendo da gravidade do ataque de malware ou vírus, talvez seja necessário fazer mais do que uma varredura de inicialização.

Para mais informações sobre como lidar com malware ou vírus, veja a seção [**4.9 Métodos avançados de remoção de vírus**](#4.9).


<a name="4.2"></a>
### 4.2 Uma visão geral sobre a interface principal do avast! ###

A interface principal do **avast!** exibe várias abas ao lado esquerdo, incluindo: *Visão Geral*, *Escaneamento*, *Ferramentas* e *Configurações*. As abas de *Escaneamento*, *Ferramentas* e *Configurações* contêm menus com itens discutidos abaixo.

Para ativar a interface principal, **clique** em ![](/sbox/screen/avast-pt/22.png) na bandeja do sistema (normalmente, no canto inferior direito da tela do seu computador).

![](/sbox/screen/avast-pt/56.png)

*Figura 1: A interface principal do programa* 

A seguinte lista descreve brevemente as funções das abas principais e de seus submenus:

**Visão Geral**: A página principal exibe o status de funcionamento do **avast!**.

**Escaneamento**: Esta aba pode ser usada para ativar diferentes opções de varredura (ou *escaneamento*), incluindo:

- O *Escaneamento inteligente* pode fazer as varreduras abaixo isoladamente;
- *Buscar por vírus* pelos seguintes meios: *Escaneamento rápido*, *Escaneamento completo do sistema*, *Escaneamento de mídia removível*, *Selecione uma pasta para escanear* e *Escaneamento de inicialização* - discutidos em detalhes, abaixo;
- *Buscar programas desatualizados*;
- *Buscar por ameaças na rede* pode checar as configurações de segurança do roteador de sua casa e aconselhar a modificação de algumas configurações;
- *Buscar por questões relacionadas à performance* - esta opção é disponível de forma integral apenas na versão paga do **avast!**;

**Ferramentas**: Esta aba exibe um submenu de ferramentas, incluindo o *Software Update* (*Atualizador de programas*), *Browser Cleanup* (*Limpador de navegadores de internet*) e *Disco de Recuperação*, descritas na seção [**3.2 Ferramentas adicionais do avast!**](/pt/howtouseavast#3.2)

**Configurações**: Esta aba exibe um menu de funções, incluindo *Geral*, *Proteção Ativa*, *Antivírus* e *Atualização*, conforme descritas abaixo:

- **Geral** inclui uma seção sobre 'Manutenção', onde é possível configurar os tamanhos e históricos de *Registros* e *Quarentena*.

- O menu de **Proteção Ativa** permite configurar os parâmetros para as varreduras de *Sistema de arquivos*, *E-mail* e *Internet*. **Observação**: é recomendável não mudar as configurações padrão a menos que você entenda o impacto de habilitar/desabilitar as configurações específicas.

- O menu de **Antivírus** permite configurar os parâmetros globais de varredura, incluindo *Exclusões* e *Alertas*.

- O menu de **Atualização** exibe as versões atuais instaladas do *Programa* e das *Definições de vírus* e permite a atualização manual de ambas, conforme descrito na seção [**3.1 Como fazer atualizações manuais no avast!**](/pt/howtouseavast#3.1).


<a name="4.3"></a>
### 4.3 Como fazer varreduras em busca de malware e vírus ###

Nesta seção, você verá as opções disponíveis para varredura (ou *escaneamento*) e como usá-las. Também verá como fazer uma varredura completa do sistema, apenas em uma pasta ou durante a inicialização.

O painel *Escaneamento* exibe as cinco opções disponíveis no **avast!**. Para vê-las:

**Passo 1**. **Clique** em ![](/sbox/screen/avast-pt/57.png).

**Passo 3**. **Clique** em ![](/sbox/screen/avast-pt/95.png) para ativar a seguinte tela:

![](/sbox/screen/avast-pt/96.png)

*Figura 2: A aba de Escaneamento exibindo a opção padrão de Escaneamento rápido*

As seguintes descrições te ajudarão a escolher a opção apropriada de varredura:

**Escaneamento rápido**: Esta opção é recomendada para quem está com tempo limitado para buscar por ameaças potenciais ou suspeitas.

**Escaneamento completo do sistema**: Esta opção é recomendada para quem está com tempo suficiente para fazer uma varredura completa do sistema. Ela também é recomendada caso seja a primeira vez que você esteja usando um programa antivírus na máquina. A duração desse processo depende do número de documentos, arquivos pastas e discos rígidos no computador, assim como de sua velocidade. Veja a seção [**4.4 Como fazer uma varredura completa do sistema**](#4.4) para mais informações.

**Escaneamento de mídia removível**: Esta opção é recomendada para fazer varreduras em HDs externos, pen drives e outras mídias removíveis, em especial nas que não sejam suas. Ela fará uma varredura em qualquer dispositivo removível por programas maliciosos que são ativados sempre que ele esteja conectado.

**Selecione uma pasta para escanear**: Esta opção é recomendada para fazer uma varredura em uma pasta específica ou em um conjunto de pastas, especialmente se você suspeita ou saber que um diretório em particular possa estar infectado. Veja a seção [**4.5 Como fazer uma varredura em uma pasta**](#4.5) para mais informações.

**Escaneamento de inicialização (*Boot-time scan*)**: O escaneamento de inicialização permite fazer uma varredura completa no seu disco rígido antes de o sistema operacional **Microsoft Windows** ser iniciado. Esta opção é recomendada para uma varredura completa e profunda do seu sistema e pode exigir bastante tempo. Veja a seção [**4.6 Como fazer uma varredura ao iniciar o sistema**](#4.6) para mais informações.

**Dica**: **Clicar** em ![](/sbox/screen/avast-pt/59.png) permite ver e refinar os detalhes sobre determinada varredura, por exemplo, onde ela ocorrerá.


<a name="4.4"></a>
### 4.4 Como fazer uma varredura completa do sistema ###

**Passo 1**. **Selecione** a opção *Escaneamento completo do sistema* no menu (veja a *Figura 2*, acima).

**Passo 2**. **Clique** em ![](/sbox/screen/avast-pt/60.png) para ativar a seguinte tela:

![](/sbox/screen/avast-pt/61.png)

*Figura 3: O painel de Escaneamento exibindo a execução da varredura completa* 

Após completar a varredura, o painel de Escaneamento completo do sistema deve ser parecido com o abaixo:

![](/sbox/screen/avast-pt/62.png)

*Figura 4: O Escaneamento completo exibindo que Nenhuma ameaça foi encontrada*

Caso a varredura tenha encontrado ameaças, **clique** no botão ![](/sbox/screen/avast-pt/69.png) para abrir uma página de resultados. Veja a seção [**4.7 Como lidar com vírus**](#4.7) para os passos seguintes.


<a name="4.5"></a>
### 4.5 Como fazer varredura em uma pasta ###

**Passo 1**. **Selecione** a opção do menu *Selecione uma pasta para escanear* (veja a *Figura 2*, acima).

**Passo 2**. **Clique** em ![](/sbox/screen/avast-pt/60.png) para ativar a seguinte tela:

![](/sbox/screen/avast-pt/63.png)

*Figura 5: A caixa de diálogo Selecionar as áreas*

A tela de *Selecionar as áreas* permite selecionar os locais a serem escaneados. É possível escolher mais de uma pasta onde fazer a varredura. Conforme você marca as caixas ao lado de cada pasta, o caminho daquele diretório é exibido no campo de texto *Caminhos selecionados:*. 

**Passo 3**. **Clique** em ![](/sbox/screen/avast-pt/64.png) para começar uma varredura em suas pastas e ativar a seguinte tela:

![](/sbox/screen/avast-pt/65.png)

*Figura 6: O escaneamento de pastas em progresso* 

**Dica**: O **avast!** permite fazer varreduras em pastas individuais via um menu pop-up que aparece sempre que você clica com o botão direito do mouse em uma pasta. Basta que você **selecione** o item *![](/sbox/screen/avast-pt/66.png) Escanear...*, que aparece ao lado do nome da pasta selecionada.

Caso a varredura de pastas revele alguma ameaça, **clique** no botão ![](/sbox/screen/avast-pt/69.png) para abrir a página de resultados. Veja a seção [**4.7 Como lidar com vírus**](#4.7) para mais informações.


<a name="4.6"></a>
### 4.6 Como fazer varredura ao iniciar o sistema ###

A varredura de inicialização de sistema (*boot-time scan*) do **avast!** permite fazer um escaneamento integral do disco rígido antes que o sistema operacional **Microsoft Windows** seja iniciado completamente.

No momento que a varredura de inicialização é realizada, todos os (ou a maioria dos) programas malware e vírus ainda estão dormentes, ou seja, não tiveram ainda a oportunidade de se ativarem ou interagir com outros processos. Assim, podem ser expostos e removidos mais facilmente. A varredura de inicialização também acessa diretamente o disco, evitando drivers do sistema de arquivos do **Windows**, que podem estar infectados. Isso ajuda a encontrar mais vírus e 'rootkits' - nome dado a uma forma particularmente maléfica de malware. 

É **altamente recomendável** que você faça uma varredura de inicialização mesmo que haja apenas uma suspeita remota de que o sistema esteja comprometido ou infectado. As opções de **varredura de inicialização** (*boot-time scan*) e **disco de recuperação** (descrito na seção [3.2.3 Disco de recuperação](/pt/howtouseavast#3.3.3)) são as varreduras mais completas e profundas oferecidas pelo **avast!**.

A varredura de inicialização pode exigir algum tempo, dependendo da velocidade de processamento do computador e da quantidade de informações e discos rígidos contidos nele. Para escanear o sistema durante a inicialização, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/avast-pt/57.png) para ativar o painel de *Escaneamento*.

**Passo 2**. **Selecione** a opção ![](/sbox/screen/avast-pt/67.png) do menu expandido.

**Passo 3**. **Clique** em ![](/sbox/screen/avast-pt/60.png) para agendar uma varredura de inicalização para a próxima vez que o computador for iniciado.

**Passo 3**. **Reinicie o computador** para começar a varredura.

**Observação**: Uma varredura de inicialização é iniciada antes de o sistema operacional (assim como a interface do sistema) ser carregado completamente. Por este motivo, o progresso do escaneamento é exibido em modo de texto na tela, como se vê na imagem abaixo:

![](/sbox/screen/avast-pt/68.png)

*Figura 7: A Varredura de inicialização do avast!*

O **avast!** perguntará o que fazer caso encontre quaisquer vírus. Você poderá selecionar algumas ações possíveis pressionando as respectivas teclas numéricas do teclado. Recomendamos que você **selecione a tecla 2**, de *Consertar tudo automaticamente*, para que o **avast!** lide com as ameaças de forma automática.

Observe que mover um arquivo infectado para a *Quarentena* ou removê-lo pode resultar em informações ou funcionalidades do sistema tornarem-se inacessíveis. Em situações extremas, quando um vírus infecta arquivos vitais para o funcionamento do sistema operacional, movê-lo para a *Quarentena* ou removê-lo pode resultar no computador ser incapaz de reiniciar o sistema operacional.


<a name="4.7"></a>
### 4.7 Como lidar com vírus ###

As seções 4.5 e 4.6 acima demonstraram fazer varreduras manuais em busca de vírus com o **avast!**. Quando um vírus é encontrado em qualquer um daqueles escaneamentos, o programa exibe uma tela como a vista na *Figura 8*. Para lidar com quaisquer malware ou vírus detectados, siga os seguintes passos:

![](/sbox/screen/avast-pt/100.png)

*Figura 8: A tela de Escaneamento completo - ameaça detectada*

**Passo 1**. **Clique** em ![](/sbox/screen/avast-pt/69.png) para ativar a seguinte tela:

![](/sbox/screen/avast-pt/70.png)

*Figura 9: A janela de Resultados do Escaneamento exibindo o aviso de Ameaça Encontrada!*

**Passo 2**. Para exibir a listagem do menu expandido de ações possíveis, **clique** na seta abaixo de *Ações*, conforme se vê abaixo.

![](/sbox/screen/avast-pt/72.png)

*Figura 10: Ações - Mover para a Quarentena*

**Observação**: Nestes exemplos, queremos mover os arquivos infectados para a *Quarentena*. Porém, a listagem do menu expandido exibe mais três opções, descritas abaixo:

**Reparar**: Esta ação tentará reparar o arquivo infectado.

**Excluir**: Esta ação removerá o arquivo infectado de forma permanente.

**Não fazer nada**: Esta ação faz exatamente o que diz e *definitivamente não é recomendada* para lidar com ameaças potencialmente perigosasa de malware ou vírus.

**Passo 3**. **Selecione** a opção *Mover para a Quarentena* e então **clique** em ![](/sbox/screen/avast-pt/71.png).

![](/sbox/screen/avast-pt/73.png)

*Figura 11: A ameaça detectada foi movida para a Quarentena*

O **avast!** também monitora o computador por vírus e malware ao fundo de forma constante. Ao detectar malware ou arquivos suspeitos, exibirá um alerta como o visto na imagem abaixo.

![](/sbox/screen/avast-pt/81.png)

*Figura 12: O alerta de vírus encontrado*

A ação padrão será mover o arquivo para a *Quarentena*. A seção seguinte descreve como lidar com malware ou vírus detectados e movidos para a *Quarentena*.


<a name="4.8"></a>
### 4.8 Como usar a Quarentena ###

Durante o processo de instalação, a *Quarentena* do **avast!** foi criada no seu disco rígido. A *Quarentena* é uma pasta especial isolada do resto do sistema e é usada para armazenar malware e vírus detectados durante o escaneamento, assim como documentos, arquivos ou pastas infectados ou ameaçados. 

Você pode acessar o conteúdo da *Quarentena* e decidir como lidar com os arquivos armazenados ali:

**Passo 1**. **Clique** em ![](/sbox/screen/avast-pt/57.png) e **clique** em ![](/sbox/screen/avast-pt/74.png) para ativar a seguinte tela:

![](/sbox/screen/avast-pt/75.png)

*Figura 13: A Quarentena exibindo um vírus*

**Passo 2**: **Clique** com o botão direito do mouse em cada item para exibir o menu de ações que podem ser aplicadas em um arquivo selecionado, como se vê abaixo:

![](/sbox/screen/avast-pt/76.png)

*Figura 14: O menu pop-up de ações para vírus na Quarentena*

**Observação**: Dar um duplo clique em um item dentro da *Quarentena* não ativará, abrirá ou executará o arquivo; exibirá apenas suas propriedades, basicamente a mesma informação que você obteria ao selecionar o item *Propriedades* do menu.

A lista seguinte descreve as ações usadas para lidar com vírus existentes no menu pop-up:

**Excluir**: O arquivo será removido da *Quarentena* de forma irreversível.

**Restaurar**: O arquivo será restaurado à sua localização original.

**Extrair**: O arquivo será copiado para a pasta que você especificar.

**Escaneamento**: O arquivo será escaneado.

**Enviar para análise da AVAST Software...**: Selecionar esta opção ativará um formulário de envio para submeter o vírus a uma análise mais profunda pelo laboratório da empresa avast!. Não submeta arquivos que contenham informações sensíveis!

**Propriedades**: Esta opção revelará mais detalhes sobre o arquivo.

**Acrescentar...**: Esta opção permite navegar pelo sistema por outros arquivos que você gostaria de adicionar à *Quarentena*. Isso pode ser potencialmente útil caso haja arquivos que você gostaria de proteger durante uma contaminação por vírus.

**Atualizar todos os arquivos**: Esta opção atualizará a lista de arquivos na *Quarentena*, de forma que você veja os arquivos mais recentes.


<a name="4.9"></a>
### 4.9 Métodos avançados de remoção de vírus ###

Às vezes, a proteção oferecida pelo **avast!**, **Comodo Firewall** e **Spybot** simplesmente não é suficiente. Apesar dos melhores esforços, nosso sistema de computação pode ser infectado por malware e outros vírus. Na seção [**4.1 Um guia rápido sobre como lidar com surtos de vírus**](#4.1), vimos alguns métodos para lidar com malware e vírus persistentes. Entretanto, *há* mais que pode ser feito para eliminar tais ameaças do computador.

**Método A: Usar CDs/DVDs ou Pen drives de recuperação Antimalware**

Algumas empresas de software antimalware oferecem um CD/DVD gratuito de recuperação antivírus. Eles podem ser baixados no formato de imagem ISO (ou seja, um formato que pode ser facilmente gravado em um CD ou DVD, ou colocado em um pen drive).

Para usar esses CDs/DVDs/USB de recuperação antimalware, execute as seguintes tarefas:

1. Baixe o ISO específico de recuperação (veja a lista abaixo) e queime o programa de recuperação antimalware em um CD/DVD ou grave-o em um pen drive USB.<br>
*Você pode usar um programa gratuito como o [**ImgBurn**](http://www.imgburn.com/) para gravar a imagem na mídia ou usar um programa também gratuito como o [**Universal USB Installer**](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/) para gravar a imagem no pen drive USB*<br>
**Observação:** É melhor executar esta etapa em um computador não infectado, caso seja possível.

2. Insira a mídia no reprodutor de CD/DVD ou conecte o pen drive nos computadores infectados. Reinicie o computador a partir do pen drive ou CD/DVD.  <br>
*Normalmente, é possível fazer isso pressionando as teclas F10 ou F12 ou Esc no teclado logo após ligar o computador. Preste atenção às instruções na tela durante a inicialização para ver como fazer isso na sua máquina. Busque por instruções na internet sobre como iniciar (*dar boot*) no computador a partir de pen drives ou CD/DVD. As instruções podem ser diferentes para cada computador.*

3. Uma vez que o computador infectado inicie a partir do pen drive/CD/DVD, reconecte-o à internet para que o programa de recuperação antimalware possa atualizar suas definições de vírus, caso seja necessário. <br>
*Pode ser melhor conectar-se à internet usando uma conexão via cabo, se disponível*.

4. Inicie uma varredura dos discos rígidos do computador para remover infecções e ameaças de malware.

A seguir, há uma listagem das imagens de recuperação disponíveis disponíveis de forma gratuita:

- [**AVG Rescue CD**](http://www.avg.com/pt-pt/avg-rescue-cd) (página em português)
- [**Dr.Web Live Rescue CD**](http://www.freedrweb.com/livedisk/?lng=es) (página em espanhol)
- [**Avira AntiVir Rescue CD**](https://www.avira.com/en/download/product/avira-rescue-system) (em inglês)
- [**BitDefender Rescue CD**](http://www.bitdefender.com/support/How-to-create-a-BitDefender-Rescue-CD-627.html) (em inglês)
- [**F-Secure Rescue CD**](http://www.f-secure.com/en/web/labs_global/rescue-cd) (em inglês)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/) (em inglês)

Você também pode achar interessantes e úteis os seguintes links com mais informações, ferramentas e métodos extras:

- [**Como limpar de forma simples um computador infectado (Guia de remoção de Malware)**](http://malwaretips.com/blogs/malware-removal-guide-for-windows/) (em inglês)
- [**Guia de remoção de Malware para Windows**](http://www.selectrealsecurity.com/malware-removal-guide) (em inglês)

**Observação:** Você pode usar cada ferramenta listada acima separadamente para maximizar sua habilidade de limpar o computador de forma efetiva.

**Método B: Reinstalar o sistema operacional Microsoft Windows**

Em raras ocasiões, um vírus pode ser *tão* destrutivo que as ferramentas recomendadas podem se tornar inúteis. Em situações como essa, recomendamos executar as seguintes tarefas:

***Observação**: Antes de começar, assegure-se de estar com todas as licenças e números seriais, assim como com as cópias de instalação do sistema operacional **MS Windows** e dos programas que você usa. Este procedimento pode exigir bastante tempo, mas valerá o esforço caso não seja possível eliminar as ameaças de malware e vírus de outra forma.*

1. Crie uma cópia de reserva (*backup*) de todos os seus arquivos pessoais no computador.

2. Reinstale o sistema operacional **Microsoft Windows** e formate todo o disco rígido.

3. Atualize o sistema operacional **Microsoft Windows** após a instalação ser completada.

4. Instale o **avast!** (ou o seu programa antivírus preferido) e atualize-o.

5. Instale os demais programas que você costuma usar. Lembre-se de baixar as últimas versões de cada programa. <br><br>**Observação**: Sob nenhuma circunstância você deve conectar o seu HD externo ou mídia removível com as cópias de reserva (*backup*) *antes* de haver finalizado as tarefas acima. Você correrá o risco de infectar o computador novamente.

6. Conecte o HD externo ou mídia removível com as cópias de reserva (*backup*) dos arquivos e faça uma varredura profunda para detectar e eliminar quaisquer problemas existentes.

7. Após detectar e apagar os problemas, você poderá finalmente copiar os arquivos de volta ao computador.


<a name="4.10"></a>
### 4.10 O Escaneamento inteligente ##

O *Escaneamento inteligente* pode executar várias das varreduras discutidas neste capítulo de uma vez só. Esta é uma forma conveniente de fazer uma 'checagem de rotina' em busca de malware, atualizações de programas e segurança da rede. No exemplo abaixo, o Escaneamento inteligente detecta alguns programas desatualizados. 

**Passo 1**. **Clique** em ![](/sbox/screen/avast-pt/57.png) e em ![](/sbox/screen/avast-pt/36.png) para ativar a tela exibida abaixo:

![](/sbox/screen/avast-pt/84.png)

*Figura 19: O Escaneamento inteligente*

Quando o *Escaneamento inteligente* estiver completo, o status de cada varredura será exibido conforme se vê na imagem abaixo.

![](/sbox/screen/avast-pt/85.png)

*Figura 20: Escaneamento inteligente - problemas encontrados*

**Passo 2**. **Clique** em ![](/sbox/screen/avast-pt/86.png) para revisar as questões encontradas. *Observação* o GrimeFighter não está disponível na versão gratuita do **avast!**.*

![](/sbox/screen/avast-pt/39.png)

*Figura 21:A tela do Atualizador de programas (Software Updater)*

**Passo 3**. **Clique** em ![](/sbox/screen/avast-pt/40.png) para começar a atualizar os aplicativos que requerem atualização.

![](/sbox/screen/avast-pt/38.png)

*Figura 22: O programa sendo atualizado*

**Passo 4**. Siga os passos 1 a 3, acima, para assegurar a vitalidade do sistema.

