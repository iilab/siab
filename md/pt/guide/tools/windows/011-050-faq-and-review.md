

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: FAQ and Review

---

<a name="5.0"> </a> 
## 5.0 Perguntas Frequentes e Revisão ## 

<div class="background" markdown="1"> 
***P: Posso usar o Pidgin-OTR para fazer bate-papos tanto no MSN como no Yahoo?***

***R**: Embora o **Pidgin-OTR** suporte vários serviços de bate-papo e mensagens, na maioria das vezes é preciso usar um provedor igual para iniciar uma sessão de mensagens instantâneas (**MI**) com alguém. Ambos precisam usar um **IRC** ou uma **conta ICQ**, por exemplo. Porém, serviços que utilizam o protocolo **XMPP** (como o **RiseUp**, **Google Talk**, **Facebook** e outros) podem permitir bate-papos cruzados entre as respectivas contas. Isso quer dizer que você pode trocar mensagens entre uma conta do **RiseUp** e outra do **Google Talk**, por exemplo. Observe também que no **Pidgin** você pode cadastrar e ficar online com várias contas de **MI** ao mesmo tempo. Essa é a vantagem de usar um cliente de **MI** multiprotocolo.*

***P: Como posso acessar a minha conta Pidgin-OTR em outro computador?***

***R**: Um modo é gerar uma nova chave privada para ser usada com a conta de **MI** no outro computador. Você pode iniciar uma conversa com alguém usando a nova chave, mas precisará autenticar a sessão novamente. Outra opção é copiar as chaves de criptografia existentes para o novo computador (é possível encontrá-las em %APPDATA%\\.purple, no Windows, e em ~/.purple, no Linux ou Mac).* 

***P: E se eu esquecer a senha de login da minha conta de MI? Ou se alguém roubá-la? Será que eles terão acesso às minhas conversas passadas e futuras?*** 

***R**: Esta é uma pergunta muito importante. Antes de tudo, caso você esqueça sua senha e não seja capaz de redefini-la usando as opções oferecidas pelo provedor de sua conta, terá de gerar uma nova conta de **MI**. Depois disso, é necessário informar seus contatos via e-mail seguro e autenticado ou por meio de uma conversa de voz, na qual vocês possam se reconhecer.* 

*Finalmente, você e seus contatos devem se autenticar. Se alguém obteve a senha de sua conta de **MI**, tal pessoa poderia tentar se passar por você ao usar o **Pidgin**. Felizmente, ela não será capaz de autenticar a sessão sem ter suas chaves de criptografia ou saber a palavra de código combinada entre vocês, deixando seu contato com receio de se comunicar com ela. É por isso que a autentificação é **tão** importante.* 

*Além disso, se você seguiu as instruções acima e configurou as preferências da aba 'Config' do **OTR** conforme o recomendado, mesmo que alguém roube sua senha ou use seu computador, este alguém não terá acesso a conversas passadas, já que o programa havia sido configurado para não registrá-las.* 
</div> 

<a name="5.1"> </a> 
## 5.1 Perguntas de revisão ## 

- Quantas vezes você precisa "autenticar" a sessão de bate-papo com uma determinada amiga? 
- É possível fazer login e usar várias contas de **MI** simultaneamente no **Pidgin**? 
- O que é uma impressão digital no **Pidgin**? 
- O que acontece com as preferências configuradas no **OTR** (incluindo as impressões digitais de chaves recebidas) quando você instala o **Pidgin-OTR** em outro computador? 
- O que é necessário para iniciar uma sessão de bate-papo privada e autenticada no **Pidgin**? 
- Quais são os requisitos para a criação de uma conta no **Pidgin**?

