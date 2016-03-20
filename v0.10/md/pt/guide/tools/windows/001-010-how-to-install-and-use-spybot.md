

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Use Spybot

---

Seções nessa página:

- [**2.0 Como instalar o Spybot**](#2.0)
- [**2.1 Sobre o Spybot**](#2.1)
- [**2.2 Como usar o Spybot pela primeira vez**](#2.2)
- [**2.3 Como atualizar as regras de detecção e os bancos de dados de imunização**](#2.3)
- [**2.4 Como imunizar o seu sistema**](#2.4)
- [**2.5 Como fazer varreduras por ameaças**](#2.5)
- [**2.6 Como desabilitar Cookies de rastreamento**](#2.6)
- [**2.7 Como restaurar um arquivo**](#2.7)

<a name="2.0"></a>
## 2.0 Como instalar o Spybot ##

**Passo 1**. **Dê um duplo clique** em ![](/sbox/screen/spybot-pt/01.png); A janela de diálogo *Abrir arquivo - Aviso de segurança* deve aparecer.  Se isso acontecer, **clique** em ![](/sbox/screen/spybot-pt/02.png) para ativar a janela a seguir:

![](/sbox/screen/spybot-pt/03.png)

*Figura 1: A tela de seleção de Idioma*

**Observação**: O **Spybot** não possui interface traduzida para o português. Este guia usará a interface original, em inglês, como referência.

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/04.png) para ativar a tela do ajudante de instalação *Setup - Spybot Password Safe – Welcome to the Spybot - Search & Destroy Setup Wizard*.

**Passo 3**. **Clique** em ![](/sbox/screen/spybot-pt/05.png) na tela de doação *Donations Welcome* e mantenha a opção padrão escolhida, que diz *I am installing Spybot for personal use, and will decide later* (*Estou instalando para uso pessoal e decidirei mais tarde*)

**Passo 4**. **Clique** em ![](/sbox/screen/spybot-pt/05.png) na tela de modo de instalação e uso *Installation and Usage Mode* e mantenha a opção padrão escolhida, que diz *I want to be protected without having to attend it myself* (*Quero proteção sem ter de me preocupar muito*).

**Passo 5**. **Clique** em ![](/sbox/screen/spybot-pt/05.png) na tela de licença de uso *License Agreement*. Leia os termos de uso do programa antes de continuar. 

**Passo 6**. **Clique** em ![](/sbox/screen/spybot-pt/06.png) na tela de *Ready to Install* (*Pronto para instalar*) para iniciar o processo de instalação.

![](/sbox/screen/spybot-pt/07.png)

*Figura 2: Instalando*

**Passo 7**. **Clique** em ![](/sbox/screen/spybot-pt/08.png) para completar o processo de instalação e abrir o **Spybot - Search & Destroy**. 

![](/sbox/screen/spybot-pt/09.png)

*Figura 3: Finalizando o assistente de instalação do Spybot - Search & Destroy*

Por padrão, a opção *Check for new malware signatures* (*Checar por novas assinaturas de malware*) está selecionada, como se vê acima. **Observação**: Caso não haja conexão com a internet disponível durante a instalação, **desmarque** esta opção e reveja a *Seção 2.3*.

![](/sbox/screen/spybot-pt/10.png)

*Figura 4: A tela de Atualização - Update (Spybot - Search & Destroy 2.4)*

**Passo 8**. **Clique** em ![](/sbox/screen/spybot-pt/11.png) para ativar a tela abaixo:

![](/sbox/screen/spybot-pt/12.png)

*Figura 5: Checando por atualizações do Antispyware*

![](/sbox/screen/spybot-pt/13.png)

*Figura 6: Atualizações do Antispyware instaladas*


<a name="2.1"></a>
## 2.1 Sobre o Spybot ##

Há basicamente dois passos para efetivamente usar o **Spybot**: 

- Atualizar as *Regras de detecção* (*Detection Rules*) e os *Bancos de dados de imunização* (*Immunization databases*) com as atualizações mais recentes e relevantes do **Spybot**. 

- Rodar o **Spybot**. Isso envolve imunizar o sistema a partir de regras de detecção e bancos de dados de imunização ou atualizações previamente baixadas da internet, e então varrer o sistema em busca de infestações de spyware e removê-las. 

**Observação**: Para uma breve visão geral das principais opções avançadas, veja a seção [**3.0 Opções avançadas**](/pt/spybot_advanced). 


<a name="2.2"></a>
## 2.2 Como usar o Spybot pela primeira vez ##

Após completar o processo de instalação e configuração, o **Spybot** será iniciado automaticamente na tela do *Start Center*:

![](/sbox/screen/spybot-pt/17.png)

*Figura 7: A tela de início Start Center*

A tela de início do Spybot também pode ser ativada em **Iniciar > Todos os programas > Spybot - Search & Destroy 2 > Spybot S&D Start Center** ou **dando um duplo clique** no ícone do Spybot, na Área de Trabalho:

![](/sbox/screen/spybot-pt/14.png)   

Antes de começar, é fortemente recomendável criar uma cópia de reserva (*backup*) dos arquivos de regostro. Para uma visão geral e mais informações sobre os **arquivos de registro do Windows**, veja o Guia Prático do [**CCleaner**](/pt/ccleaner_windowsregistry#4.0).

Siga os passos abaixo para criar uma cópia de backup dos registros do computador.

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/16.png) para exibir a opção *Advanced Tools* (*Ferramentas avançadas*).

![](/sbox/screen/spybot-pt/15a.png)

*Figura 8: As Ferramentas avançadas*

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/18.png) .

**Passo 3**. **Clique** em ![](/sbox/screen/spybot-pt/19.png) na janela de *Startup Tools* (*Ferramentas de inicialização*)

**Passo 4**. **Clique** em ![](/sbox/screen/spybot-pt/20.png), como se vê na imagem abaixo:

![](/sbox/screen/spybot-pt/21.png)

*Figura 9: As Ferramentas de inicialização (Startup Tools)*

**Passo 5**. **Selecione** um local e um nome de arquivo como exibido na *Figura 10*, abaixo, na janela de *Folder to save to* (*Salvar na pasta*).

**Passo 6**. **Clique** em ![](/sbox/screen/spybot-pt/23.png) 

![](/sbox/screen/spybot-pt/22.png)

*Figura 10: Salvar na pasta (Folder to save to)*


<a name="2.3"></a>
## 2.3 Como atualizar as regras de detecção e os bancos de dados de imunização ##

**Importante**: É vital manter o **Spybot** atualizado com as últimas definições. A função de atualização automática não está disponível na versão gratuita do *Spybot*, então é preciso executar este passo manualmente seguindo os passos abaixo:

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/24.png) na tela de início (*Start Center*) para ativar o *Atualizador* (*Updater*).

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/25.png) to activate as shown below

![](/sbox/screen/spybot-pt/26.png)

*Figura 11: A janela do Updater*

Clique em *Show Details* (*Exibir detalhes*) para ver uma lista de atualizações baixadas com sucesso.

![](/sbox/screen/spybot-pt/27.png)

*Figura 12: A tela de atualizações baixadas a instaladas*


<a name="2.4"></a>
## 2.4 Como imunizar o seu sistema ##

O **Spybot** ajuda a proteger o computador de spyware conhecidos ao "imunizá-lo". É como receber uma vacina contra novas doenças contagiosas.

Para imunizar o sistema, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/28.png) na tela de início do programa para ativar a janela de *Imunização* (*Immunization*):

![](/sbox/screen/spybot-pt/29.png) 

*Figura 13: A janela de Imunização (Immunization)*

**Observação**: Caso você tenha deixado o navegador de internet aberto por qualquer motivo, a seguinte tela aparecerá antes que o processo de imunização seja iniciado:

![](/sbox/screen/spybot-pt/31.png)

*Figura 14: O aviso de detecção de Navegador de internet aberto*

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/32.png) para começar a checar por arquivos imunizados (caso você ainda não tenha imunizado o sistema, poucos ou nenhum arquivo serão encontrados).

![](/sbox/screen/spybot-pt/33.png) 

*Figura 15: A checagem de imunização finalizada*

**Passo 3**. **Clique** em ![](/sbox/screen/spybot-pt/34.png) para começar a imunizar o sistema.

O processo de imunização pode levar vários minutos para ser executado.

![](/sbox/screen/spybot-pt/35.png)

*Figura 16: Imunizando o sistema...*

**Passo 4**. **Clique** em *Show Details* (*Exibir detalhes*) para ver os detalhes, como se vê abaixo:

![](/sbox/screen/spybot-pt/36.png)

*Figura 17: Aplicar a proteção passiva (Apply Passive Protection)*

**Observação**: Você pode reverter ou desfazer o processo de imunização caso suspeite que imunizar o sistema tenha afetado de forma negativa a performance geral do computador. Você pode **clicar** em ![](/sbox/screen/spybot-pt/30.png) para reverter o processo de imunização e restaurar o sistema ao estado anterior.


<a name="2.5"></a>
## 2.5 Como fazer varreduras por ameaças ##

**Lembrete**: Antes de começar a checar por possíveis ameaças, rode o *Atualizador* (*Updater*) do **Spybot**. 

Para checar por ameaças potenciais, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/14.png) para ativar a tela inicial do **Spybot**.

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-pt/37.png) para ativar a tela abaixo:

![](/sbox/screen/spybot-pt/38.png)

*Figura 18: A tela de varredura do sistema - System Scan (Spybot - Search & Destroy)*

**Passo 3**. **Clique** em ![](/sbox/screen/spybot-pt/40.png) para iniciar uma varredura pelo sistema. *Observação - Caso você tenha muitos dados, arquivos, programas etc, este processo pode levar entre 20 minutos e 1 hora para ser executado*.

![](/sbox/screen/spybot-pt/39.png)

*Figura 19: System Scan (Spybot - Search & Destroy)*

Após finalizar a varredura do sistema, o número e os tipos de malware potenciais encontrados serão listados como se vê abaixo:

![](/sbox/screen/spybot-pt/41.png)

*Figura 20: A varredura finalizada exibindo os malware em potencial*

**Passo 4**. **Selecione** o arquivo e revise a caixa de *Detalhes* (*Details*) ao lado esquerdo da tela para cada ameaça potencial encontrada para determinar se o malware é uma ameaça genuína.

**Lembre-se** - um *falso positivo* (*false positive*) significa que arquivos, pastas, programas ou arquivos de registro inofensivos poderiam ser categorizados como malware. Apagá-los poderia causar problemas em outros programas.

![](/sbox/screen/spybot-pt/42.png)

*Figura 21: Os detalhes de uma varredura por malware* 

**Dica**: O *Nível da ameaça* (*Threat Level*) é exibido por uma barra colorida. Uma gradação de *Perigo estimado* (*Estimated Danger*) que varie entre *Marginal* (*Marginal*) e *Muito baixo* (*Very Low*) será exibida como verde. Conforme o nível de ameaça aumenta para *Médio* (*Medium*) e *Alto* (*High*), a coloração mudará do laranja para vermelho. Será possível avaliar rapidamente a ameaça potencial. Por exemplo, a maioria dos navegadores de internet usam *Cookies de rastreamento* (*Tracking Cookies*) quando entram em um site. Caso a informação armazenada por eles não seja excessiva, a avaliação de *Perigo estimado* (*Estimated Danger*) estará entre *Marginal* (*Marginal*) e *Muito baixa* (*Very Low*). Você pode optar por manter os cookies de certos sites por conveniência.

**Passo 5**. Caso escolha apagar um ou mais arquivos, **selecione-os** e **clique** em ![](/sbox/screen/spybot-pt/44.png).

Você também pode escolher fazer varreduras em arquivos e pastas individuais usando a opção *File Scan* (*Varredura de arquivos*) na tela inicial do programa - o processo é similar ao de *Varredura do sistema* (*System Scan*), descrito acima.

**Observação**: É geralmente uma boa ideia fazer varreduras semanais no sistema.


<a name="2.6"></a>
## 2.6 Como desabilitar Cookies de rastreamento ##

Um *Cookie de restreamento* é um pequeno arquivo salvo no seu computador por um navegador de internet quando você visita um site, guardando informações que podem te identificar para aquele mesmo site. Dentre as informações guardadas, pode haver logins, senhas, dados pessoais usados para preencher campos de formulários online, hábitos de navegação de internet etc. Embora os cookies possam ser convenientes, também podem ser um risco ao anonimato na rede.

O *Spybot Search & Destroy* permite desabilitar os *cookies de rastreamento* em todos os navegadores instalados a partir de uma localização central.

Para desabilitar os *cookies de rastreamento*, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-en-1/37.png) para ativar a seguinte tela:

![](/sbox/screen/spybot-en-1/65.png)

*Figura 22: A tela de rastreamento de cookies do Spybot Search & Destroy*

**Passo 2**. **Clique** em ![](/sbox/screen/spybot-en-1/66.png) para exibir os perfis dos navegadores instalados no computador, como exibido acima. *Note - pode haver outros perfis de navegadores no seu computador*.

![](/sbox/screen/spybot-en-1/67.png)

*Figura 23: O Spybot Search & Destroy bloqueando cookies de terceiros*

**Passo 3**. **Selecione** o perfil e **clique** em ![](/sbox/screen/spybot-en-1/68.png)

![](/sbox/screen/spybot-en-1/69.png)

*Figura 24 : O rastreamento de cookies desabilitado pelo Spybot Search & Destroy*

Para reabilitar os *cookies de rastreamento*, **clique** na seta para baixo ao lado de ![](/sbox/screen/spybot-en-1/66.png) e **selecione** ![](/sbox/screen/spybot-en-1/70.png).


<a name="2.7"></a>
## 2.7 Como restaurar um arquivo ##

A ferramenta de *Quarentena* (*Quarantine*) permite recuperar itens previamente apagados ou reparados. Isso é possível porque o **Spybot** cria uma cópia de reserva (*backup*) de cada item apagado. Caso um arquivo removido cause mal funcionamento no sistema, é possível restaurá-lo usando a ferramenta de *Quarentena*.

Para recuperar itens previamente apagados, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/spybot-pt/45.png) a partir da tela inicial do programa para ativar a seguinte tela:

![](/sbox/screen/spybot-pt/46.png)

*Figura 25: A Quarentena - Quarantine (Spybot - Search & Destroy)* 

**Passo 2**. **Marque** os itens que gostaria de recuperar na listagem de itens apagados e então **clique** em ![](/sbox/screen/spybot-pt/47.png).

**Passo 3**. Também é possível **clicar** em ![](/sbox/screen/spybot-pt/48.png) para remover os arquivos marcados de forma definitiva. Porém, saiba que esta ação não pode ser desfeita e tais arquivos não poderão mais ser recuperados.

