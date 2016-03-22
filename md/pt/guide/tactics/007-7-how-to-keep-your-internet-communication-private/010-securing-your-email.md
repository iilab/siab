

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

Existem alguns passos importantes que devem ser dados para aumentar a segurança de sua comunicação por e-mail. O primeiro é assegurar que a pessoa para quem você enviou a mensagem é a única capaz de lê-la. Isso é discutido nas seções [*Como manter seguros e-mails acessados online*](/pt/chapter_7_1) e  [*Como mudar para uma conta de e-mail mais segura*](/pt/chapter_7_1), abaixo. Além do básico, às vezes é crítico que seus contatos de e-mail possam verificar se uma mensagem específica realmente veio de você, e não de alguém tentando se passar por você. Uma forma de fazer isso é descrita em [*Segurança avançada de e-mail*](/pt/chapter_7_4), na seção [*Como criptografar e autenticar mensagens de e-mail*](/pt/chapter_7_4).

Também é bom saber o que fazer caso suspeite que a privacidade de sua conta de e-mail tenha sido violada. A seção [*Dicas sobre como agir no caso de suspeita de monitoramento de e-mails*](/pt/chapter_7_2) discorre sobre isso.

Lembre-se também que e-mails seguros não ajudam muito caso todos os textos digitados em um teclado estejam sendo gravados por um programa spyware e enviados periodicamente a alguém pela internet. O [*Capítulo 1: Como proteger seu computador de programas maliciosos e hackers*](/pt/chapter-1) dá alguns conselhos sobre como evitar esse tipo de coisa e o [*Capítulo 3: Como criar e manter senhas seguras*](/pt/chapter-3) vai ajudar a proteger as contas de e-mail e os programas de troca de mensagens instantâneas descritos abaixo.


### Como manter seguros e-mails acessados online ###

A Internet é uma rede aberta por meio da qual a informação tipicamente viaja em um formato legível. Se uma mensagem normal de e-mail é interceptada a caminho de um destinatário, seu conteúdo pode ser lido facilmente. Como a Internet não é mais do que uma grande rede mundial dependente de computadores intermediários para direcionar o tráfego, muitas pessoas diferentes podem ter a oportunidade de interceptá-la dessa forma.

O [*provedor de serviços de internet (em inglês, ISP)*](/pt/glossary#ISP) é a primeira parada de uma mensagem de e-mail em sua jornada para um destino final; da mesma forma, o [*provedor de internet*](/pt/glossary#ISP) do destinatário é a última parada antes de ela ser entregue. A menos que você tome algumas precauções, sua comunicação pode ser lida ou alterada em qualquer um desses pontos, ou em qualquer ponto entre eles.

<div class="background" markdown="1">
Pablo: Eu estava falando sobre tudo isso com uma parceira nossa e ela disse que tanto ela como suas colegas às vezes salvam mensagens importantes na pasta de 'Rascunhos' de uma conta online de e-mail, da qual todas sabem a senha. Parece meio estranho, mas você acha que funcionaria? Digo, isso não evitaria outras pessoas de ler as mensagens, já que não chegaram a ser enviadas?

Claudia: Toda vez que você lê um e-mail no seu computador, mesmo que seja somente um 'rascunho', o conteúdo daquela mensagem já foi enviado pela internet. Senão não apareceria na tela, entende? A parte importante é, se alguém está monitorando a sua conta, não monitora apenas as mensagens de e-mail. Essa pessoa pode monitorar todas as informações legíveis que chegam e saem do seu computador. Em outras palavras, o truque não funcionaria a menos que todas se conectassem de forma segura àquela conta conjunta de e-mail. E, se elas podem se conectar de forma segura, podem muito bem criar contas separadas e passar a enviar as mensagens.
</div>


Já é possível há algum tempo tornar segura a conexão entre o um computador e os sites visitados na internet. A tecnologia que torna isso possível chama-se *Secure Sockets Layer*, ou [*criptografia*](/pt/glossary#Encryption) [*SSL*](/pt/glossary#SSL). É comum encontrar esse tipo de segurança em páginas de preenchimento de dados e senha de cartões de crédito, e dá para saber se está sendo usada olhando com atenção a **barra de endereços** do navegador.

Todos os endereços da internet começam com as letras **HTTP**, como se vê no exemplo abaixo:

![](/sites/securitybkp.ngoinabox.org/files/u7/01.png)

Quando você visita um site seguro, o endereço começará com **HTTPS**. 

![](/sites/securitybkp.ngoinabox.org/files/u7/02.png)

O **S** ao final significa que o computador estabeleceu uma conexão segura com o site. Você também notará o símbolo de um 'cadeado', situado ou na **barra de endereços** ou na **barra de status** do navegador, na parte de baixo da janela. Esses sinais visuais querem dizer que pessoas monitorando sua conexão de internet não serão mais capazes de interceptar sua comunicação com aquele site de forma legível.

Além de proteger senhas e transações financeiras, esse tipo de [*criptografia*](/pt/glossary#Encryption) é perfeita para correios eletrônicos. O problema é que muitos provedores de e-mail não oferecem acesso seguro e outros requerem habilitá-lo de forma explícita, configurando o navegador ou digitando manualmente o **HTTPS**. Antes de fazer login, enviar ou ler uma correspondência eletrônica, tenha certeza de que a conexão é segura.

Você também deve prestar bastante atenção caso o navegador comece a emitir avisos sobre [*certificados de segurança*](/pt/glossary#Security_certificate) inválidos ao tentar acessar uma conta online segura de e-mails. Isso pode significar que alguém esteja interferindo na comunicação entre o seu computador e o servidor, de modo a interceptar as mensagens. Finalmente, se você depende de serviços online de e-mail para trocar informações sensíveis, é importante usar um navegador o mais seguro possível. Considere instalar o Mozilla [*Firefox*](/pt/glossary#Firefox) com seus complementos relacionados a segurança.


<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Firefox com complementos - Navegador seguro de internet*](/pt/firefox_main)
</div>			


<div class="background" markdown="1">
Pablo: Quando não está no trabalho, um dos caras que vão trabalhar conosco neste relatório costuma usar uma conta online de e-mail da Yahoo. Também lembro de mais alguém usar o Hotmail. Se eu mandar uma mensagem a qualquer um deles, elas podem ser lidas por outras pessoas?

Claudia: Provavelmente. O Yahoo, o Hotmail e vários outros provedores de e-mail online têm sites não seguros que não protegem a privacidade das mensagens. Vamos ter que mudar os hábitos de algumas pessoas se queremos discutir os depoimentos de forma segura.
</div>		


### Como mudar para uma conta de e-mail mais segura ###

Poucos serviços online de e-mail oferecem acesso com [*SSL*](/pt/glossary#SSL) à conta. O Yahoo e o Hotmail, por exemplo, estabelecem uma conexão segura *apenas* na tela de *login*, para proteger a senha, mas a comunicação é enviada e recebida de forma insegura. Além disso, Yahoo, Hotmail e outros provedores de e-mail online inserem o [*endereço de IP*](/pt/glossary#IP_address) do computador que você estiver usando em todas as mensagens enviadas.

Contas do Gmail, por outro lado, mantém conexões seguras desde a tela de *login*, passando por todo o uso da conta e até o *logout*, quando você sai dela. É possível confirmar isso na barra de endereços do navegador, onde a URL inicia a todo o momento com 'https' (o 's' denota uma conexão segura). Ao contrário do Yahoo ou Hotmail, o Gmail evita revelar o [*endereço de IP*](/pt/glossary#IP_address). 

Não é recomendável, entretanto, confiar inteiramente no Google para manter sigilosas comunicações sensíveis. O Google analisa e armazena para diversos fins o conteúdo das mensagens de seus clientes e, no passado, cedeu a demandas de governos que restringem a liberdade digital. Veja a seção [***Leitura extra***](/pt/chapter_7_5) para mais informações sobre a política de privacidade do Google.

Se possível, crie uma nova conta de e-mail no [*RiseUp*](/pt/glossary#RiseUp) em [*https://mail.riseup.net*](https://mail.riseup.net). O [*RiseUp*](/pt/glossary#RiseUp) fornece e-mail gratuito para ativistas ao redor do mundo e tem bastante cuidado na proteção da informação guardada em seus servidores. Há algum tempo que eles são uma fonte confiável para quem busca soluções seguras de e-mails. Ao contrário do Google, o [*RiseUp*](/pt/glossary#RiseUp) possui políticas bastante restritivas de proteção à privacidade de quem o usa, além de não ter interesses comerciais, o que poderia entrar em conflito com essas políticas em algum momento. Para criar uma nova conta, é preciso obter dois 'convites' em forma de código, sendo que tais códigos podem ser fornecidos por qualquer pessoa que já tenha uma conta no [*RiseUp*](/pt/glossary#RiseUp). Se você possui uma cópia física desse Guia de Referência, deve ter recebido seus 'convites' com ela. Caso contrário, será preciso encontrar duas pessoas que usam o serviço e pedi-los a elas.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*RiseUp - Serviço de e-mail seguro*](/pt/riseup_main)
</div>	

Tanto o Gmail como o [*RiseUp*](/pt/glossary#RiseUp) são mais do que apenas provedores de correio eletrônico online. Ambos podem ser usados com um programa cliente de e-mail como o Mozilla [*Thunderbird*](/pt/glossary#Thunderbird), que permite usar as técnicas descritas em [***Segurança avançada de e-mail***](/pt/chapter_7_4). Assegurar que o seu cliente de e-mails estabeleça uma conexão [*criptografada*](/pt/glossary#Encryption) com o provedor é tão importante quanto acessá-lo online usando **HTTPS**. Se você usar um cliente de e-mail, veja o [***Guia Prático do Thunderbird***](/pt/thunderbird_main) para mais detalhes. No mínimo, porém, você deve habilitar [*SSL*](/pt/glossary#SSL) ou [*criptografia*](/pt/glossary#Encryption) para os servidores de e-mail tanto de chegada como de saída.

<div class="background" markdown="1">
Pablo: Então eu deveria mudar para o RiseUp ou posso continuar usando o Gmail e só passar a usar o endereço seguro 'https'?

Claudia: Você quem sabe, mas há algumas coisas que  definitivamente deveria considerar ao escolher um provedor de e-mail. Primeiro, ele oferece uma conexão segura à sua conta? O Gmail sim, então até aí tudo bem. Segundo, você confia nos administradores para manter sua correspondência privada, não lê-la ou dividi-la com outras pessoas? Essa é com você. Finalmente, pense se é aceitável ou não você ser associado a um provedor. Em outras palavras, ter um endereço de correio eletrônico com final 'riseup.net', conhecido por ser usado por ativistas, vai te criar problemas ou você precisa de um endereço mais típico, com final 'gmail.com'?
</div>

Independentemente de quais ferramentas de e-mail seguro decida usar, lembre que cada mensagem tem alguém como remetente e uma ou mais pessoas como destinatárias. Você é apenas parte do conjunto. Mesmo que acesse sua conta de e-mail de forma segura, considere as precauções que seus contatos podem ou não tomar ao enviar, ler e responder mensagens.

Tente saber também onde são localizados os provedores de correio eletrônico de seus contatos, pois alguns países são mais agressivos que outros na questão da vigilância de e-mails. **Para ter certeza sobre a privacidade da comunicação, você e seus contatos devem usar serviços seguros de e-mail, hospedados em países relativamente seguros.** Para assegurar que as mensagens não sejam interceptadas entre os diferentes servidores dos provedores de correio eletrônico, considere usar contas do mesmo provedor. O [*RiseUp*](/pt/glossary#RiseUp) é uma boa escolha.

 
### Dicas extras sobre como melhorar a segurança do seu e-mail ### 

  * Tenha sempre cautela ao abrir arquivos anexos que você não estava esperando, vindos de alguém que você não conheça ou contenha assuntos suspeitos. Ao abri-los, tenha o antivírus atualizado e preste bastante atenção a quaisquer avisos exibidos pelo navegador de internet ou programa de e-mail.
  * Usar programas de anonimato como o [*Tor*](/pt/glossary#Tor), descrito no [***Capítulo 8: Como manter o anonimato e contornar a censura na internet***](/pt/chapter-8), podem ajudar a esconder o serviço de correio eletrônico que você usa de alguém monitorando sua conexão de internet. Dependendo da extensão dos filtros de censura à rede em seu país, talvez seja preciso usar o [*Tor*](/pt/glossary#Tor) ou outra das ferramentas de [*circunvenção*](/pt/glossary#Circumvention) descritas no [***capítulo 8***](/pt/chapter-8) para acessar provedores de correio eletrônico seguro como o [*RiseUp*](/pt/glossary#RiseUp) ou o Gmail.
  * Ao criar uma conta para ser usada de forma anônima dos próprios destinatários de suas mensagens ou em fóruns públicos nos quais seja possível publicar mensagens por e-mail, tome o cuidado de não registrar um *username* (nome de quem usa a conta) ou 'Nome completo' relacionado à sua vida pessoal ou profissional. Em tais casos, é importante evitar usar Hotmail, Yahoo e qualquer outro provedor que inclua o [*endereço de IP*](/pt/glossary#IP_address) nas mensagens enviadas.
  * Dependendo de quem tenha acesso físico ao seu computador, limpar rastros relacionados a correspondências eletrônicas nos arquivos temporários pode ser tão importante quanto proteger as mensagens em seu trajeto ao longo da internet. Veja o [***Capítulo 6: Como destruir informações sensíveis***](/pt/chapter-6) e o [***Guia Prático do CCleaner***](/pt/ccleaner_main) para mais detalhes.
  * Considere usar diversas contas anônimas diferentes ao se comunicar com grupos distintos de pessoas, de forma a proteger sua rede de contatos. Considere também usar contas diferentes em serviços da internet que requeiram e-mail para se registrar.
  * Depois de todas as precauções acima, ainda é muito importante tomar cuidado com o conteúdo das mensagens e seu impacto, caso caia em mãos erradas. Uma forma de aumentar a segurança da comunicação é desenvolver um sistema de código para informações sensíveis, para não precisar usar nomes reais de pessoas, endereços reais de lugares etc.

