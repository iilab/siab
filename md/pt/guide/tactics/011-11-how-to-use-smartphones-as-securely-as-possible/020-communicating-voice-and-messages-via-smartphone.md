

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Como falar de forma segura ##

### Telefonia básica ###

Na seção sobre [***Funções básicas, rastreabilidade e anonimato***](/pt/chapter_10_2_2) do [***Capítulo 10: Como usar telefones celulares da forma mais segura possível***](/pt/chapter-10), discutimos as diferentes medidas que devem ser consideradas para diminuir o risco de interceptação fazer chamadas por voz usando a rede telefônica de sua operadora.

Uma forma mais segura de se comunicar com as pessoas é conectar o smartphone à internet, em conexões de dados ou WiFi, e usar um serviço de [*voz sobre IP (VoIP)*](/pt/Glossary#VoIP) aliado a técnicas de proteção do canal onde ocorre a conversa. Alguns aplicativos de smartphone também conseguem extender algo dessa proteção para além do VoIP, incluindo ligações entre telefones celulares (veja mais sobre o **Redphone** abaixo).

Aqui, listamos algumas ferramentas com seus prós e contras:


### Skype ###

O [*Skype*](/pt/glossary#Skype) é o programa comercial mais popular de [*voz sobre IP (VoIP)*](/pt/Glossary#VoIP). Está disponível para todas as plataformas de smartphone e funciona bem caso sua conexão sem fio seja confiável e não tão bem caso a conexão seja de dados (por exemplo, 3G ou 4G).

Na seção [***Como tornar seguras outras ferramentas de comunicação pela internet***](/pt/chapter_7_3) do [***Capítulo 7: Como manter sua comunicação por internet segura***](/pt/chapter-7), discutimos os riscos de usar o Skype e o porquê, se possível, deve ser evitado. Em suma, o Skype é um programa que tem o código fechado, o que torna muito difícil confirmar de forma independente seu nível de proteção. Além disso, pertence à Microsoft, que possui um interesse comercial em saber quando e de onde alguém o está usando. O Skype também pode permitir a agências governamentais ou policiais um acesso retrospectivo a todo histórico de comunicações.


### Outros programas de VoIP ###

Usar [*VoIP*](/pt/Glossary#VoIP) costuma ser grátis ou bem mais barato do que fazer uma ligação de telefone celular, e deixa poucos rastros de dados. Na verdade, uma chamada VoIP protegida pode ser a forma mais segura de se comunicar.

O [**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) é um cliente poderoso de VoIP para telefones Android. Bem mantido, vem com várias funções de ajuda à configuração para diferentes serviços de VoIP.

A [**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) e o servidor fornecido pelo projeto Guardian, o [**ostel.co**](https://ostel.co), oferecem atualmente uma das formas mais seguras de se comunicar por voz. Conhecer e confiar na organização que opera o servidor das suas chamadas de VoIP é um fator importante, que deve ser considerado.

Ao usar o CSipSimple, você nunca se comunica diretamente com seu contato. Em vez disso, todos os dados são desviados para passarem pelo servidor Ostel. Isso faz com que rastrear suas informações e descobrir com quem você está falando seja bem mais difícil. Além disso, o Ostel não guarda nenhum dado, exceto os relacionados à conta usada para fazer o login. Todos os sinais de voz são criptografados de forma segura e mesmo os metadados, que costumam ser muito difíceis de disfarçar, são borrados, uma vez que o tráfego usa o servidor ostel.co como [*proxy*](/pt/Glossary#Proxy). Se você baixar o CSipSimple do endereço ostel.co, o programa já vem pré-configurado para ser usado com o ostel, tornando-o muito fácil de instalar e usar.

O [**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) é um aplicativo [*livre e de código aberto*](/pt/Glossary#FOSS) que criptografa os dados de comunicação por voz enviados entre dois dispositivos que o tem instalados. É fácil de instalar e muito fácil de usar, pois se integra bem às funções comuns de discar para um contato e encontrá-lo na agenda. As pessoas com quem você quiser conversar também devem instalar o aplicativo. Para ser mais fácil de usar, o RedPhone utiliza o número do seu celular como identificador (como outros serviços de VoIP usariam o login). Porém, isso também torna mais fácil analisar o tráfego produzido por ele e rastreá-lo de volta a você, via o seu número de telefone. O RedPhone usa um servidor central, o que o coloca em uma posição de poder ao ter o controle de algumas dessas informações.

Guias Práticos para o CSipSimple, Ostel e Redphone estão sendo produzidos. Enquanto não ficam prontos, mais informações podem ser vistas nos links acima.


## Como enviar mensagens de forma segura ##

É preciso tomar precauções ao enviar mensagens SMS e ao usar programas de mensagens instantâneas ou de bate papo no seu smartphone.

### SMS ###

Como descrito no [***Capítulo 10***](/pt/chapter-10), na seção sobre [***Comunicações baseadas em texto***](/pt/chapter_10_2_3), a comunicação por SMS é insegura por padrão. Qualquer pessoa com acesso à rede de telefonia móvel pode interceptar tais mensagens facilmente e isso é uma ocorrência diária em várias situações. Não dependa de enviar mensagens SMS sem proteção em situações críticas. Também não há como autenticar mensagens SMS, então é impossível saber se o conteúdo passou por modificações entre os processos de envio e entrega ou se a mensagem realmente veio de quem parece ter vindo.


### Protegendo as mensagens SMS ###

O [**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) é uma [*ferramenta livre e de código aberto (FOSS)*](/pt/glossary#FOSS) para enviar e receber SMS protegidos em celulares Android. Funciona tanto para mensagens criptografadas como não criptografadas, então pode ser usado como o aplicativo padrão para envios de SMS. Para haver criptografia na troca de mensagens, o programa deve ser instalado em ambos os telefones - de quem envia e de quem recebe. Então, é melhor que todas as pessoas com quem você se comunica regularmente o tenham. O TextSecure detecta automaticamente quando uma mensagem criptografada é recebida, vindo de outro aparelho com TextSecure. Também é possível enviar textos criptografados para mais de uma pessoa. As mensagens são assinadas automaticamente, sendo quase impossível de serem alteradas. Em nosso Guia Prático, explicamos em detalhes suas funções e como usá-lo.

<div class=getstarted markdown=1>
Guia Prático - saiba usar o [*TextSecure*](/pt/textsecure_main)
</div>


### Bate papo protegido ###

A troca de mensagens instantâneas e os bate papos por telefone podem produzir muita informação que corre o risco de ser interceptada. Tais conversas podem ser usadas por adversários contra você posteriormente, portanto, tenha bastante cuidado sobre o que revela nessas conversas.

Há formas seguras de usar bate papos e os serviços de mensagem instantânea. A melhor é usar criptografia ponta-a-ponta, pois isso permitirá ter certeza de que a pessoa do outro lado é quem parece ser.

Recomendamos o [**Gibberbot**](/pt/gibberbot_main) como aplicativo para conversas de texto em telefones Android. O Gibberbot oferece criptografia fácil e robusta para suas conversas com o protocolo de mensagens [*Off-the-Record*](/pt/glossary#OTR). Este tipo de criptografia permite tanto a autenticação (você pode verificar se está falando com a pessoa certa) como a proteção independente para cada sessão. Assim, mesmo que a criptografia de uma conversa seja comprometida, outras sessões no passado ou no futuro continuarão seguras.

O Gibberbot foi projetado para trabalhar junto com o Orbot, de forma que seus bate papos sejam roteados pela rede de anonimato [*Tor*](/pt/glossary#Tor). Isso faz com que seja muito difícil rastreá-los ou mesmo descobrir que aconteceram.

<div class=getstarted markdown=1>
Guia Prático - saiba usar o [*Gibberbot*](/pt/gibberbot_main)
</div>

Para iPhones, o cliente [**ChatSecure**](https://chatsecure.org) fornece as mesmas funcionalidades, embora não seja fácil usá-lo junto à rede [*Tor*](/pt/glossary#Tor).

Um Guia Prático para o ChatSecure está sendo produzido. Enquanto não fica pronto, mais informações podem ser encontradas em seu [site](https://chatsecure.org). 

Seja qual for o aplicativo que você prefira usar, considere sempre a partir de qual conta fará a conversa. Por exemplo, ao usar o Google Talk/Hangout, suas credenciais e o tempo de sua conversa tornam-se conhecidos para o Google. Combine também com as pessoas com quem conversar não guardar históricos das sessões, em especial das que não estavam criptografadas.

  * [22/01/2014] *O Gibberbot agora é conhecido como ChatSecure. Uma versão atualizada do Guia Prático está sendo produzida.*

