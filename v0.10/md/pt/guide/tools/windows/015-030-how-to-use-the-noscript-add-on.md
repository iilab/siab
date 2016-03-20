

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Seções nessa página:

- [**4.0 Sobre o NoScript**](#4.0)
- [**4.1 Como usar o NoScript**](#4.1)

-------

<a name="4.0"></a>
## 4.0 Sobre o NoScript ##

![](/sbox/screen/firefox-pt/noscript.png)

O **NoScript** é um complemento do **Mozilla** que pode ajudar na proteção de sites mal intencionados. Ele opera implementando uma 'lista branca' de sites que você considerou aceitáveis, seguros e confiáveis (como um site de banco ou um jornal online). Todos os outros sites são considerados potencialmente danosos e as suas funcionalidades são restritas até que você determine que os conteúdos desses sites não são perigosos; adicionando-os à 'lista branca'. 

O **NoScript** irá automaticamente bloquear todos os banners, publicidades em pop-ups, códigos **JavaScript** e **Java**, assim como outros atributos potencialmente perigosos do site. O **NoScript** não diferencia o conteúdo danoso do conteúdo necessário para mostrar o site corretamente; está nas suas mãos adicionar exceções para sites que você considera seguros.


<a name="4.1"></a>
<a name="4.1"></a>
## 4.1 Como usar o NoScript ##

Antes de começar a usar o **NoScript**, certifique-se que este tenha sido instalado corretamente selecionando **Ferramentas > Complementos**, para abrir a janela de Complementos e confirmar se está instalado.

**Dica**: Apesar de o **NoScript** parecer um pouco frustante no início (os sites que você costuma visitar podem não mostrar todos os elementos gráficos), você irá se beneficiar imediatamente do bloqueio de alguns elementos: ele restringirá as malditas publicidades, messagens pop-ups e códigos danosos construídos (ou hackeados) para páginas da internet.

O **NoScript** funcionará silenciosamente no fundo até detectar a presença de **JavaScript**, **Adobe Flash** ou outro conteúdo de script. Nesse momento, o **NoScript** bloqueará o conteúdo e uma barra de status aparacerá na parte de baixo da janela do **Firefox**, como segue: 

![](/sbox/screen/firefox-pt/50.png)

*Figura 1: A barra de status do NoScript*

A barra de status do **NoScript** mostra informações sobre qual *objeto* (por exemplo, publicidade e mensagens pop-up) ou *scripts* foram bloqueados de serem executados no seu sistema. As duas figuras seguintes são exemplos clássicos do **NoScript** trabalhando. Na *Figura 2*, o **NoScript** bloqueou com sucesso uma publicidade criada em **Adobe Flash Player** num site comercial. 

![](/sbox/screen/firefox-pt/51.png)

*Figura 2: Um exemplo do NoScript bloqueando a publicidade de um site comercial*

Na *Figura 3*, o site do **Twitter** notifica que o **JavaScript** deve ser habilitado (ao menos temporariamente) para visitar a página.

![](/sbox/screen/firefox-pt/52.png)

*Figura 3: O site Twitter requerendo que o Javascript seja habilitado*

O **NoScript** não diferencia entre códigos danosos ou não. Portanto, algumas características e funções chave (por exemplo, um menu de ferramentas) podem estar faltando. Algumas páginas apresentam conteúdo, incluindo conteúdo de scripts, provenientes de mais de um site. Por exemplo, um site como **www.twitter.com** tem duas fontes de scripts (*twitter.com* and *twimg.com*): 

![](/sbox/screen/firefox-pt/53.png)

*Figura 4: Um exemplo da barra de status do NoScript na opção do menu*

Nessas circunstâncias, para desbloquear os scripts selecione a opção *Temporariamente permitir [nome do site]* (nesse caso, temporariamente permitir o *twitter.com*). Contudo, se isso ainda não permitir a exibição da página que você quer, determine por um processo de tentativa e erro o mínimo de sites fonte necessários para ver aquele conteúdo. Por exemplo, no **Twitter**, você deverá **Selecionar** as opções *Temporariamente permitir twitter.com* e *Temporariamente permitir twimg.com*, para fazê-lo funcionar.

**Aviso**! Sob **nenhuma** circunstância você deverá selecionar a opção *Permitir Javascripts Globamente (perigoso)*. Sempre que possível, evite selecionar a opção *Permitir todos nessa página*, o que apenas ocasionalmenteserá necessário. Se for esse o caso, certifique-se de fazê-lo temporariamente para sites nos quais realmente confia, e apenas até o final da sua sessão online. É necessária apenas uma *única* injeção de código malicioso para comprometer toda a segurança e privacidae do seu sitema na rede.

Para sites que você confia e visita frequentemente, **selecione** a opção *Permitir [nome do site]* (no exemplo acima, *Permitir twitter.com* e *Permitir twimg.com* foram selecionados). Escolher essas opções permite ao **NoScript** adicioná-los à lista dos sites confiáveis.

