

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

As ferramentas e conceitos discutidos abaixo são recomendados para pessoas com mais experiência no uso de computadores.

### Como usar criptografia de chave pública em e-mails ###

É possível obter um nível alto de privacidade na troca de e-mails, mesmo em contas não seguras. Para isso, é preciso saber mais sobre a [**criptografia**](/pt/glossary#Encryption) de chave pública. Esta técnica permite codificar mensagens individuais, tornando-as ilegíveis a quaisquer pessoas que não os destinatários almejados. O lado engenhoso da [**criptografia**](/pt/glossary#Encryption) de chave pública é que você não precisa trocar nenhuma informação secreta com seus contatos sobre como vai codificar as mensagens no futuro.

<div class="background" markdown="1">
Pablo: Mas como funciona isso?
			
Claudia: É um uso criativo da Matemática! Você codifica as mensagens para um contato específico de e-mail usando a chamada 'chave pública' daquela pessoa. As 'chaves públicas' podem ser distribuídas sem problemas. Para ler as mensagens, aquela pessoa usa uma 'chave privada' pessoal, que deve ser mantida guardada com segurança. No caminho inverso, seu contato usa a chave pública que você forneceu a ele para criptografar as mensagens que enviará para você. Assim, vocês precisam trocar as chaves públicas entre si, mas podem fazê-lo abertamente, sem se preocupar.
</div>

Essa técnica pode ser usada com qualquer serviço de correio eletrônico, mesmo os que não possuem canais de comunicação seguros, pois as mensagens individuais são [**criptografadas**](/pt/glossary#Encryption) antes de deixar o computador.

Lembre-se que o uso de [**criptografia**](/pt/glossary#Encryption) pode atrair atenção. O tipo de [**criptografia**](/pt/glossary#Encryption) usado para acessar sites seguros na internet, incluindo contas online de e-mail, costuma ser visto como menos suspeita do que a de chave pública, discutida aqui. Em algumas circunstâncias, se um e-mail com este tipo de dados [**criptografados**](/pt/glossary#Encryption) for interceptado ou publicado em fóruns públicos de discussão, podem incriminar a pessoa que o enviou, independentemente do conteúdo da mensagem. Às vezes, você terá de escolher entre a privacidade das mensagens e a necessidade de se manter inconspícuo.


### Como criptografar e autenticar mensagens de e-mail ###

A [**criptografia**](/pt/glossary#Encryption) de chave pública pode parecer complicada no começo, mas é bastante direta depois de entender o básico. Além disso, as ferramentas não são difíceis de usar. Um programa simples, amigável e portátil chamado **gpg4usb** pode criptografar mensagens de e-mail e arquivos mesmo sem estar conectado à internet.

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [***gpg4usb portátil - Criptografia para textos e arquivos de e-mail***](/pt/gpg4usb_portable)
</div>

Para criptografar e decodificar mensagens de e-mail de forma fácil, o programa de e-mails **Mozilla** [**Thunderbird**](/pt/glossary#Thunderbird) pode ser usado com uma extensão chamada [**Enigmail**](/pt/glossary#Enigmail).

<div class="getstarted" markdown="1">
Guia Prático - saiba usar o [***Thunderbird com Enigmail e GPG - Cliente seguro de e-mail***](/pt/thunderbird_main)
</div>

A autenticidade dos e-mails também é outro aspecto importante para a segurança da comunicação. Qualquer pessoa com acesso à internet e as ferramentas apropriadas pode se passar por você, enviando mensagens a partir de um endereço de e-mail idêntico ao seu, mas falso. O perigo aqui é mais evidente se considerado do lado de quem recebe as mensagens. Imagine, por exemplo, o perigo de um e-mail que parece ser de um contato confiável mas é, na verdade, de alguém cujo objetivo é desmobilizar suas atividades ou descobrir informações sensíveis sobre sua organização.

Uma vez que não podemos ver ou ouvir quem está do outro lado da mensagem de um e-mail, tipicamente confiamos no endereço de emissão para validar uma identidade. É por isso que nos enganam de forma tão fácil com e-mails falsos. As [**assinaturas digitais**](/pt/glossary#Digital_signature), que também se baseiam na [**criptografia**](/pt/glossary#Encryption) de chave pública, fornecem um meio mais seguro de alguém provar a própria identidade ao enviar uma mensagem. O [***Guia Prático do gpg4usb portátil***](/pt/gpg4usb_portable) ou a seção [***Como usar o Enigmail com o Thunderbird***](/pt/thuderbird_encryption), do [***Guia Prático do Thunderbird***](/pt/thunderbird_main), explicam em detalhes como usar as [**assinaturas digitais**](/pt/glossary#Digital_signature).

<div class="background" markdown="1">
Pablo: Uma vez, um colega recebeu um e-mail meu que eu não havia enviado. Decidimos, no fim, que era apenas um spam, mas agora fico pensando o estrago que um e-mail falso poderia causar caso aparecesse na caixa de entrada da pessoa errada, no momento errado. Ouvi dizer que é possível evitar isso com assinaturas digitais, mas o que são elas?
			
Claudia: Uma assinatura digital é como um selo de cera com a sua letra dentro, fechando um envelope. Com a diferença que ela não pode ser forjada. Ela prova que você é quem realmente emitiu a mensagem e que seu conteúdo não foi modificado no meio do caminho.
</div>

