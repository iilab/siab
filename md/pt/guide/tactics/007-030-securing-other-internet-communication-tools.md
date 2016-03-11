

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

Assim como em correios eletrônicos, programas de mensagens instantâneas e de [*voz sobre IP (VoIP)*](/pt/glossary#VoIP) podem ser seguros ou inseguros, dependendo das ferramentas escolhidas e de como são usadas.


**Tornando seguro o programa de mensagens instantâneas**

A troca de mensagens instantâneas, também conhecida como 'chat' ou 'bate-papo', costuma não ser segura e é tão vulnerável à vigilância como o e-mail. Há programas que ajudam a manter privadas as sessões de troca de mensagens, mas, assim como acontece com os e-mails, estabelecer um canal seguro de comunicações exige que as duas ou mais pessoas que se comunicam usem a mesma ferramenta e tomem as mesmas precauções de segurança.

Existe um software de bate-papo chamado [*Pidgin*](/pt/glossary#Pidgin), que suporta diversos protocolos existentes de mensagens instantâneas. Isso significa que é possível começar a usá-lo facilmente, sem ter de trocar o nome de sua conta ou recriar sua lista de contatos. Para fazer conversas privadas e [*criptografadas*](/pt/glossary#Encryption) pelo programa, é preciso instalar e ativar o plug-in *Off-the-Record* ([*OTR*](/pt/glossary#OTR)). Felizmente, este é um processo bastante simples.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Pidgin com OTR - Mensagens instantâneas seguras*](/pt/pidgin_main)
</div>

<div class="background" markdown="1">
Pablo: Se meu e-mail online da Yahoo não é seguro, o que se pode dizer sobre o Yahoo Chat? Também é vulnerável?
			
Claudia: O importante de lembrar é que se queremos usar ferramentas de mensagens instantâneas para discutir este relatório, temos de ter certeza que todas as pessoas envolvidas têm o Pidgin instalado com OTR. Se elas têm, podemos usar o bate papo do Yahoo ou qualquer outro serviço.
</div>


**Tornando seguro o programa de voz sobre IP (VoIP)**


Não é preciso dizer o quanto os programas de [*voz sobre IP (VoIP)*](/pt/glossary#VoIP) são úteis. Afinal, chamadas entre pessoas que usam o mesmo serviço costumam ser gratuitas e alguns programas permitem ainda ligar para telefones físicos, incluindo números internacionais, a preços baixos. Alguns dos aplicativos [*VoIP*](/pt/glossary#VoIP) mais populares de hoje são: [Skype](http://www.skype.com) (veja abaixo), [Jitsi](http://jitsi.org/), [Google Hangouts](http://www.google.com/hangouts) e [Yahoo! Voice](http://voice.yahoo.com/).

Normalmente, a comunicação por voz pela internet não é mais segura do que e-mails e mensagens instantâneas não protegidos. Para abordar informações sensíveis, é importante escolher uma ferramenta que criptografe a ligação por todo o caminho, desde o seu computador até o de quem a recebe. É sempre melhor usar programas [*livres e de código aberto (FOSS)*](/pt/glossary#FOSS), em especial os revistos, testados e recomendados por comunidades confiáveis. Considerando tais critérios, recomendamos o [*Jitsi*](http://jitsi.org/) para fazer chamadas de VoIP.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [*Jitsi - Áudio, vídeo e mensagens instantâneas de forma segura*](/pt/jitsi)
</div>


**Observação sobre a segurança do Skype**

O [*Skype*](/pt/glossary#Skype) é um programa de mensagens instantâneas e chamadas de VoIP que também permite fazer ligações para linhas terrestres e telefones celulares. Apesar de sua popularidade, várias questões o desqualificam como escolha segura. Algumas delas são descritas abaixo.

Segundo o Skype, tanto as mensagens de texto como as chamadas por voz são [*criptografadas*](/pt/glossary#Encryption). Porém, isso só acontece quando as duas ou mais pontas que se comunicam estão usando o programa, e o Skype não criptografa ligações para telefones ou textos enviados como mensagem SMS. Se as duas pontas estiverem usando o software (genuíno), a criptografia usada tornaria a chamada mais segura do que uma ligação comum feita por telefone. Porém, como o programa tem o código fechado, é impossível fazer uma auditoria ou avaliação sobre as alegações relacionadas a tal criptografia, sendo portanto impossível verificar quão bem o Skype protege as pessoas que o usam, suas informações e  comunicações.

O [***Capítulo 1: Como proteger seu computador de programas maliciosos e hackers***](/pt/chapter-1) fala sobre as vantagens do [*software livre e de código aberto (FOSS)*](/pt/glossary#FOSS) na seção [***Como manter os programas atualizados***](/pt/chapter_1_4).

Conforme mencionado, embora não possamos recomendar o Skype como ferramenta segura de comunicação, caso alguém ainda queira usá-lo para falar sobre informações sensíveis é bastante importante tomar algumas medidas:

  * Baixe e instale o programa apenas por meio do site oficial [www.skype.com](http://www.skype.com), para evitar uma versão que possa estar infectada por spyware. É importante checar com cuidado a URL para ter certeza de que é o site oficial. Em alguns países, a página do Skype é bloqueada e/ou várias páginas falsas alegando ser a oficial estão em operação. Nesses casos, a versão disponível muito provavelmente está infectada por malware desenvolvidos para espionar todas as comunicações. Use as ferramentas de contorno à censura descritas no [Capítulo 8](/pt/chapter-8) para conectar-se ao site oficial do Skype e baixar uma versão genuína do programa sempre que quiser instalá-lo ou atualizá-lo.
  * É extremamente importante mudar a senha de acesso ao Skype regularmente. O programa permite logins múltiplos de localizações diferentes e não informa sobre o número simultâneo de sessões abertas. Isso oferece um grande risco caso a senha de acesso seja comprometida, pois qualquer pessoa que a tenha pode fazer login ao mesmo tempo. Todas as sessões em vigor recebem toda comunicação por texto, assim como têm acesso ao histórico de chamadas. Mudar a senha é a única forma de desabilitar os acessos indesejados, pois forçam todas as sessões abertas a refazer o login.
  * Também é aconselhável modificar as configurações do programa para que o histórico das conversas não seja guardado.
  * É recomendável desabilitar a opção do Skype que aceita o recebimento automático de arquivos enviados, pois isso já foi usado para infectar máquinas com malware/spyware.
  * Verifique sempre de forma independente a identidade da pessoa com quem está se comunicando. É mais fácil fazer isso em conversas por voz, especialmente quando você conhece quem está do outro lado da linha.
  * Decida se o nome que aparece no Skype deve ser identificado ou ter relações com seu nome real, ou de sua organização.
  * Tenha sempre formas alternativas para se comunicar. Prepare-se para o caso de o Skype ficar indisponível.
  * Tenha cuidado com o que diz. Desenvolva um sistema de códigos para discutir tópicos sensíveis sem usar terminologias específicas.

Apesar da popularidade do Skype, as preocupações acima o tornam questionável para uma experiência segura. Recomendamos usar ferramentas como o Jitsi para chamadas de voz sobre IP e o [*Pidgin*](/pt/glossary#Pidgin) com o plugin [*OTR*](/pt/glossary#OTR) para a troca segura de mensagens instantâneas.

