

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

### Redes de anonimato ###

As redes de anonimato tipicamente fazem o seu tráfego de internet 'quicar' por vários [*proxies*](/pt/glossary#Proxy), ou computadores intermediários, seguros para disfarçar onde você está e o que está tentando acessar. Este modo de agir pode reduzir de forma significante a velocidade na qual as páginas e outros serviços de internet são carregados. Porém, no caso do [*Tor*](/pt/glossary#Tor), também produz um modo confiável, seguro e público de circunvenção, que evita ter de se preocupar se quem mantém os [proxies](/pt/glossary#Proxy) ou os sites que você quer visitar são ou não confiáveis. Como sempre, é preciso assegurar que você tenha uma conexão criptografada ([HTTPS](/pt/glossary#SSL)) a um site seguro antes de trocar informações sensíveis por navegador, como senhas e e-mails.

Para usar o [*Tor*](/pt/glossary#Tor) é necessário instalá-lo,  mas o resultado é uma ferramenta que fornece anonimato assim como contorno de censura. Cada vez que você se conecta à rede do programa, seleciona um caminho aleatório que passa por três [*proxies*](/pt/glossary#Proxy) seguros. Isso garante que nem o seu [*provedor de internet*](/pt/glossary#ISP) nem os próprios [*proxies*](/pt/glossary#Proxy) saibam o [*endereço de IP*](/pt/glossary#IP_address) do seu computador ou a localização dos serviços de internet que você quer acessar. É possível saber bem mais sobre esse aplicativo no Guia Prático do Tor.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Tor - Anonimato digital e contorno de censura*](/pt/tor_main)
</div>

Uma das forças do [*Tor*](/pt/glossary#Tor) é que ele não funciona apenas com um navegador, podendo ser usado com vários tipos de software de internet. Programas de e-mail (incluindo o Mozilla [*Thunderbird*](/pt/glossary#Thunderbird)) e de mensagens instantâneas (incluindo o [*Pidgin*](/pt/glossary#Pidgin)), podem funcionar via [*Tor*](/pt/glossary#Tor), seja para acessar serviços bloqueados, seja para esconder você de tais serviços.


### Proxies básicos de circunvenção ###

Existem três perguntas importantes a serem consideradas ao escolher um [*proxy*](/pt/glossary#Proxy) básico de circunvenção. Primeiro, é um serviço online ou requer que você mude as configurações/instale novos programas no computador? Segundo, é seguro? Terceiro, é privado ou público?


#### Proxies com base na rede e de outros tipos: ####

[*Proxies*](/pt/glossary#Proxy) baseados na rede são provavelmente os mais fáceis de usar. Requerem apenas apontar o navegador para uma página que agirá como intermediária ([*proxy*](/pt/glossary#Proxy)), informar o endereço bloqueado que você gostaria de ver e clicar em um botão. Então, o [*proxy*](/pt/glossary#Proxy) exibirá o conteúdo almejado dentro de sua própria página. Você poderá seguir os links normalmente ou digitar um novo endereço, caso queira ver uma página diferente. Não é preciso instalar programas ou modificar as configurações do navegador, o que significa que os [*proxies*](/pt/glossary#Proxy) online são:

  * Fáceis de usar;
  * Alcançáveis de computadores públicos, como as máquinas em LAN Houses e internet cafés, que podem não permitir a instalação de novos programas ou modificação de configurações;
  * Potencialmente mais seguros caso ter programas de circunvenção no computador for um problema.

[*Proxies*](glossary#Proxy) com base na internet tendem a ter também algumas desvantagens. Nem sempre exibem as páginas corretamente e muitos não conseguirão carregar sites complexos, incluindo endereços com *streaming* de áudio e vídeo como conteúdo. Qualquer [*proxy*](/pt/glossary#Proxy) fica mais lento conforme há mais pessoas usando, mas esse é um problema maior no caso dos [*proxies*](/pt/glossary#Proxy) públicos com base na rede. E, claro, funcionam apenas para exibir páginas - não é possível, por exemplo, usar programas de mensagens instantâneas ou um cliente de e-mail para acessar os serviços bloqueados. Finalmente, os [*proxies*](/pt/glossary#Proxy) seguros com base na rede oferecem confidencialidade limitada, pois são eles que devem acessar o conteúdo e modificar a informação para que você possa vê-las. Senão, seria impossível clicar em um link sem que o navegador deixasse o [*proxy*](/pt/glossary#Proxy) para trás e tentasse fazer uma conexão direta com determinado endereço na internet. Este ponto é discutido na seção seguinte.

Outros tipos de [*proxies*](/pt/glossary#Proxy) geralmente requerem instalar um aplicativo ou configurar um endereço externo de [*proxy*](/pt/glossary#Proxy) no navegador ou sistema operacional. No primeiro caso, o software de circunvenção deve ter alguma forma de ligar e desligar a função, informando ao navegador se este deve ou não usar o [*proxy*](/pt/glossary#Proxy). Programas como esse costumam permitir mudar os [*proxies*](/pt/glossary#Proxy) automaticamente caso algum seja bloqueado, como discutido acima. Se você tiver de configurar um endereço de [*proxy*](/pt/glossary#Proxy) externo no navegador ou sistema operacional, precisará saber a direção correta, o que pode mudar caso tenha sido bloqueado ou esteja com a velocidade tão lenta que seja praticamente inútil.

Embora possa ser um pouco mais difícil de usar do que um [*proxy*](/pt/glossary#Proxy) com base na rede, este método de contorno à censura tem mais chances de exibir páginas complexas corretamente e pode demorar mais a ficar lento conforme outras pessoas comecem a usar um dado servidor. Além disso, é possível encontrar [*proxies*](/pt/glossary#Proxy) para diversos usos da internet. Exemplos incluem [*proxies*](/pt/glossary#Proxy) HTTP para navegadores, [*proxies*](/pt/glossary#Proxy) SOCKS para programas de e-mail e bate papo e [*proxies*](/pt/glossary#Proxy) VPN, que podem redirecionar todo o seu tráfego de internet para evitar filtros.


#### Proxies seguros e não seguros: ####

O termo '[*proxy*](/pt/glossary#Proxy) seguro', neste capítulo, se refere a qualquer página ou computador que sirvam como intermediários e possibilitem conexões [*criptografadas*](/pt/glossary#Encryption) com quem os acessa. Um [*proxy*](/pt/glossary#Proxy) não seguro ainda permitirá contornar vários tipos de filtros, mas não funcionará caso a conexão de internet esteja sendo varrida em busca de palavras chave ou determinados endereços de site. É uma ideia particularmente ruim usá-los para acessar páginas que costumam estar [*criptografadas*](/pt/glossary#Encryption), como contas de e-mail e sites de bancos, pois, ao fazê-lo, informações sensíveis que normalmente estariam escondidas serão expostas. [*Proxies*](/pt/glossary#Proxy) não seguros também são mais fáceis de serem descobertos e bloqueados por agências que atualizam programas de filtragem e políticas de internet. No fim, o fato de que existem [*proxies*](/pt/glossary#Proxy) seguros, rápidos e gratuitos deixa poucos motivos para usar os não seguros.

É possível saber se um [*proxy*](/pt/glossary#Proxy) com base na internet é seguro se sua própria página pode ser acessada com um endereço [*HTTPS*](/pt/glossary#SSL). Pode ser que o site suporte conexões seguras e não seguras, como acontece com os serviços de e-mail online, então certifique-se de usar a primeira. Nesses casos, você pode receber um 'aviso de certificado de segurança' do navegador - isso acontece, por exemplo, com o [*proxy*](/pt/glossary#Proxy) [*Peacefire*](/pt/glossary#Peacefire), discutido abaixo. Avisos como esse significam que alguém, como o seu [*provedor de internet*](/pt/glossary#ISP) ou um hacker, podem estar monitorando a sua conexão ao serviço. Apesar deles, ainda é uma boa ideia usar [*proxies*](/pt/glossary#Proxy) seguros sempre que possível.

Quando depender de [*proxies*](/pt/glossary#Proxy) para contornar a censura, evite visitar sites seguros a menos que possa verificar a impressão digital (*fingerprint*) da [*SSL*](/pt/glossary#SSL) do serviço. Para fazê-lo, será preciso se comunicar de forma segura com a pessoa que administra o [*proxy*](/pt/glossary#Proxy). **É melhor não usar senhas ou trocar informações sensíveis ao usar proxies de rede em geral**. Evite sempre acessar dados delicados usando [*proxies*](/pt/glossary#Proxy) online, a menos que confie na pessoa que o mantém. Isso se aplica independentemente de ver ou não um aviso de certificado de segurança ao visitar a página do serviço. Também se aplica mesmo que você conheça quem o mantém suficientemente bem para verificar a impressão digital do servidor antes de direcionar seu navegador e receber tal aviso.

Quando você usa um único servidor de [*proxy*](/pt/glossary#Proxy) para fazer a circunvenção, quem o administra sempre saberá o seu [*endereço de IP*](/pt/glossary#IP_address) e quais sites está acessando. O ponto mais importante disso é que se o [*proxy*](/pt/glossary#Proxy) for baseado na rede, um operador mal intencionado pode ter acesso a toda informação trocada entre o seu navegador e os sites visitados, incluindo conteúdos de e-mail e senhas. 

Para [*proxies*](/pt/glossary#Proxy) não baseados na internet, talvez seja preciso pesquisar se é possível estabelecer conexões seguras. Todos indicados neste capítulo são seguros. O mesmo vale para as redes de anonimato.


#### Proxies privados e públicos: ####

[*Proxies*](/pt/glossary#Proxy) públicos aceitam conexões de qualquer pessoa enquanto os privados tipicamente pedem login e senha. Embora os [*proxies*](/pt/glossary#Proxy) públicos tenham a vantagem de estarem disponíveis de graça, assumindo que possam ser encontrados, tendem a ficar abarrotados muito rápido. Como resultado, embora possam ser tão bem mantidos e tecnicamente sofisticados quanto os privados, são normalmente mais lentos.

Já os [*proxies*](/pt/glossary#Proxy) privados costumam ser mantidos ou como forma de negócio ou por pessoas que criam contas para outras. Assim, é geralmente mais fácil saber os motivos porque um [*proxy*](/pt/glossary#Proxy) privado existe. Não assuma, porém, que os privados sejam necessariamente mais confiáveis. Afinal, a motivação do lucro já fez serviços online expor clientes no passado.

[*Proxies*](/pt/glossary#Proxy) públicos simples e não seguros podem ser achados com facilidade em mecanismos de busca, mas não dependa de serviços encontrados dessa forma. Se for possível escolher, é melhor usar um [*proxy*](/pt/glossary#Proxy) privado e seguro mantido por pessoas que você conheça, seja pessoalmente ou por reputação, e que tenham a habilidade técnica para manter o servidor protegido. Usar um [*proxy*](/pt/glossary#Proxy) baseado na internet dependerá de suas necessidades e preferências particulares.

Sempre que usar um [*proxy*](/pt/glossary#Proxy) para circunvenção, é uma boa ideia usar o navegador [*Firefox*](/pt/glossary#Firefox) e instalar o complemento [*NoScript*](/pt/glossary#NoScript), conforme descrito no [*Guia Prático do Firefox*](/pt/firefox_main). Isso ajuda a se proteger tanto de [*proxies*](/pt/glossary#Proxy) maliciosos como de sites que tentam descobrir seu [*endereço de IP*](/pt/glossary#IP_address) real. Finalmente, tenha em mente que mesmo um [*proxy*](/pt/glossary#Proxy) [*criptografado*](/pt/glossary#Encryption) não transformará um site não seguro em seguro. Ainda é preciso ter certeza de que há uma conexão [*HTTPS*](/pt/glossary#SSL) antes de enviar ou receber informações sensíveis.

Se você não é capaz de encontrar alguém, uma organização ou uma empresa cujo serviço de [*proxy*](/pt/glossary#Proxy) considere confiável, pagável e seja acessível de seu país, considere a rede de anonimato Tor, discutida na seção [*Redes de anonimato*](/pt/chapter_8_3), acima.

