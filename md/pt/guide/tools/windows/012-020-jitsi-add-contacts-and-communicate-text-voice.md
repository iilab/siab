

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: Jitsi - Add contacts and communicate text & voice

---

Seções nessa página:

- [**3.1 Adicionar contatos (amigas e amigos) no Jitsi**](#3.1)
- [**3.2 Conversas de texto (mensagens instantâneas) com criptografia OTR**](#3.2)
- [**3.3 Conversas de voz e vídeo com criptografia ZRTP**](#3.3)


<a name="3.1"></a>
## 3.1 Adicionar contatos (amigas e amigos) no Jitsi ##

Após fazer o login e ter pelo menos uma conta relacionada ao Jitsi, é possível adicionar seus contatos e começar a se comunicar.

Para adicionar contatos ao **Jitsi**, siga os passos abaixo.

**Passo 1**. Para abrir a janela principal do programa, **clique em Iniciar > Jitsi** ou **de um duplo clique** no ícone do Jitsi em sua Área de Trabalho.

**Passo 2**. **Selecione *Ficheiro* > *Adicionar Contato***, que irá abrir a seguinte janela:

![](/sbox/screen/jitsi-pt/30.png)

*Figura 1: A janela de Adicionar Contatos*

**Passo 3**. **Selecione** para quais contas você gostaria de adicionar o contato (por exemplo: *guiajitsi@jit.si*).

**Opcional**: Também é possível adicionar pessoas a um *grupo* dentro dos seus contatos. Para isso, é preciso primeiro criar o grupo - selecione ***Ficheiro* > *Criar Grupo***, no menu.

**Digite** o nome do contato ou e-mail no campo de ***ID or Number*** (por exemplo: *contatojitsi@jit.si*).

Você pode escolher um nome ou apelido para essa pessoa, que ficará visível em sua lista de contatos, na janela principal do **Jitsi**. **Insira o nome desejado** no campo ***Display Name*** (nome a ser exibido).

**Passo 4**. **Clique** em *Adicionar* para fechar a janela de *Adicionar Contato* e voltar para a janela principal do programa. Em sua lista de contatos, a nova adição será exibida junto com a notificação "Waiting for authorization" (Aguardando autorização), como na imagem abaixo:

![](/sbox/screen/jitsi-pt/31.png)

*Figura 2: A janela principal do Jitsi com o contato adicionado aguardando autorização*

**Passo 5**. Quando seu contato (contatojitsi@jit.si) acessar sua respectiva conta, receberá um aviso como o abaixo, informando que você está pedindo permissão para adicioná-lo à sua lista de contatos:

![](/sbox/screen/jitsi-pt/32.png)

*Figura 3: Janela requerendo a autorização de um novo contato*

Seu contato pode escolher a opção *Ignorar*, caso em que sua solicitação vai continuar aguardando autorização; *Negar*, no qual você receberá um aviso de que seu pedido foi rejeitado; ou *Autorizar*, no qual você receberá uma mensagem de confirmação da autorização e o contato ficará ativo na sua lista de contatos.

![](/sbox/screen/jitsi-pt/33.png)

*Figura 4: A janela principal do Jitsi com o novo contato autorizado*


<a name="3.2"></a>
## 3.2 Conversas de texto (mensagens instantâneas) com criptografia OTR ##

Agora que você já adicionou e autorizou seu contato, é possível clicar em seu nome na lista de contatos e iniciar uma conversa de texto, fazer chamadas de voz ou vídeo e até compartilhar sua Área de Trabalho, selecionando um dos ícones que aparecem abaixo do nome:  

![](/sbox/screen/jitsi-pt/34.png)

*Figura 5: Contato selecionado na janela principal do Jitsi com os ícones para bate papo, chamadas de voz e vídeo e compartilhamento da Área de Trabalho*

**Passo 1**. Agora, vamos explorar uma das funções mais importantes do programa: a possibilidade de conversar de forma segura via texto, criptografando as mensagens com o [*OTR*](/pt/glossary#OTR). O OTR funciona de maneira similar ao [*GPG/PGP*](/pt/glossary#PGP), descrito em outras seções deste Kit de Ferramentas. Antes que as conversas possam ser criptografadas, você e seu contato precisam configurar o **Jitsi** para gerar chaves de criptografia. Você pode fazer isto no menu ***Ferramentas > Preferências*** e **selecionar** a aba ***Segurança*** e a sub-aba ***Conversar***. Você encontrará uma janela similar à abaixo:

![](/sbox/screen/jitsi-pt/35.png)

*Figura 6: Parte da janela de opções de bate papo, na qual você pode gerar as chaves de criptografia para suas conversas de texto*

**Passo 2**. **Clique** no botão **Gerar**. Você verá a **Assinatura digital** ('Fingerprint') da chave gerada:

![](/sbox/screen/jitsi-pt/36.png)

*Figura 7: Parte da janela de opções de bate papo mostrando a Assinatura Digital ('Fingerprint') do chat criptografado com OTR*

Uma chave é gerada para cada conta. Você só precisa fazer estes passos de novo se adicionar uma conta nova ou se instalar o **Jitsi** em algum outro dispositivo e não importar as chaves existentes para ele.

Agora já é possível se comunicar.

**Passo 3**. **Selecione um contato** da lista, na janela principal do Jitsi, e **clique** no ícone de enviar mensagem (o primeiro da esquerda, abaixo do nome do contato) para abrir uma janela de bate papo:

![](/sbox/screen/jitsi-pt/37.png)

*Figura 8: Janela de bate papo com o ícone de criptografia OTR **não** ativado em destaque*

Note o ícone de *Criptografar conversa com OTR*, o cadeado aberto no canto superior direito da janela. Este símbolo quase imperceptível informa se a conversa está ou não criptografada. Neste momento, o cadeado está aberto (há um espacinho entre a alça e o corpo do cadedo!).

**Passo 4**. **Clique** no ícone ***Criptografar conversa com OTR***. Note as mudanças na janela abaixo:

![](/sbox/screen/jitsi-pt/38.png)

*Figura 9: A janela de bate papo depois de habilitar "Criptografar conversa com OTR"*

Observe que o cadeado agora está fechado. Isso significa que, a partir de agora, todas as mensagens trocadas entre você e seu contato estarão criptografadas. Note o alerta de que esta é uma *Conversa privada não verificada* ('Unverified private conversation') e que você deve *autenticar* guiajitsi@jit.si.

**Passo 5**. **Clique no link *Authenticate guiajitsi@jit.si*** para abrir a janela de *Autenticar Contato* ('Authenticate Buddy'):

![](/sbox/screen/jitsi-pt/39.png)

*Figura 10: A janela de Autenticar Contato, com as Assinaturas Digitais ('Fingerprints') sua e de seu contato*

Veja que a mensagem te encoraja a comparar as Assinaturas Digitais ('Fingerprints') relacionadas à sua chave e à do seu contato por um outro canal de comunicação (não este bate papo). Ao fazer isso, é possível ter mais certeza de que você está realmente falando com quem deseja, e não com outra pessoa. Boas opções são checar as chaves presencialmente ou checá-las por comunicações de voz ou de vídeo, nas quais é mais fácil reconhecer a outra pessoa. Após comparar as Assinaturas Digitais, **selecione** a opção ***Eu tenho*** no menu expandido (que completa a frase *verified that this is in fact...*) e **clique em *Authenticate Buddy***:

![](/sbox/screen/jitsi-pt/40.png)

*Figura 11: Parte da janela de Autenticar Amigo após selecionar "Eu tenho a Fingerprint" do meu contato*

Feche a janela de *Autenticar Amigo* e volte para a janela do bate papo:

![](/sbox/screen/jitsi-pt/41.png)

*Figura 12: Janela de bate papo com a criptografia OTR autenticada*

Note que o cadeado não possui mais o triângulo laranja com o ponto de exclamação branco. Isso significa que você autenticou o seu contato. **A autenticação deve ser feita apenas uma vez por contato.** Se o triângulo com o ponto de exclamação voltar a aparecer, é porque você está conversando com alguém ainda não autenticado. Isso pode acontecer caso seu contato use outro dispositivo, com uma chave de criptografia diferente (outra instalação do Jitsi, outro programa com OTR habilitado etc.). Neste caso, é preciso refazer o processo de autenticação para ter certeza sobre a identidade da pessoa com quem você está se comunicando.

O **Jitsi** permite fazer bate papos com mais de uma pessoa ao mesmo tempo. Porém, a criptografia OTR funcionará apenas para conversas entre duas pessoas.


<a name="3.3"></a>
## 3.3 Conversas de voz e vídeo com criptografia ZRTP ##

O **Jitsi** permite fazer chamadas de voz e vídeo, que podem ser criptografadas de forma independente com o ZRTP, um padrão aberto de criptografia. Para iniciar um chamada criptografada, siga os passos abaixo:

**Passo 1**. **Selecione** o contato desejado na lista de contatos do **Jitsi** e **clique** no ícone de chamada de voz (o segundo da esquerda, abaixo do nome) ou no ícone de chamadas de vídeo (terceiro da esquerda) - veja a figura 5, acima. Aparecerá uma nova janela, indicando que o **Jitsi** está estabelecendo a conexão:

![](/sbox/screen/jitsi-pt/42.png)

*Figura 13: A janela de chamadas com status de Chamando*

Seu contato verá uma notificação de chamada recebida:

![](/sbox/screen/jitsi-pt/43.png)

*Figura 14: Notificação de chamada recebida*

**Passo 2**. Se seu contato **aceitar a chamada**, você verá a mensagem de Ligação Estabelecida:

![](/sbox/screen/jitsi-pt/44.png)

*Figura 15: Janela de chamada recebida sem criptografia ZRTP*

**Note** o cadeado aberto em vermelho. Isso significa que a chamada ainda não está criptografada com ZRTP.

**Passo 3**. **Aguarde...** O seu e o programa de seu contato estão estabelecendo uma conexão criptografada, o que pode levar um tempinho. Se o processo for bem sucedido, as letras *zrtp* aparecerão em um fundo laranja junto a um cadeado fechado, como na imagem abaixo; se não for, ainda será possível conversar, mas sem critografia. Você pode desconectar, reiniciar o **Jitsi** e tentar novamente para ver se desta vez os programas conseguem se conectar com a criptografia. O ZRTP pode não funcionar em ligações entre contas de diferentes provedores (como entre Google e Jit.si por exemplo).

![](/sbox/screen/jitsi-pt/45.png)

*Figura 16: Parte da janela de Chamada com a criptografia ZRTP ativada mas ainda não verificada*

**Passo 4**. **Observe** a caixa que aparece abaixo das letras *zrtp* e do cadeado, com a mensagem *Compare com:* seguida de quatro letras. **Leia** essas letras para a pessoa com quem você está se comunicando e pergunte se as que ela vê na tela dela são as mesmas. Se sim, a comunicação entre vocês está criptografada e ninguém está interferindo. **Clique** em ***Confirmar*** e o campo *rztp* amarelo se tornará verde:

![](/sbox/screen/jitsi-pt/46.png)

*Figura 17: Parte da janela de chamada com a criptografia ZRTP ativada*

**Passo 5**. Você pode fechar a área preta de confirmação clicando no x branco, no canto superior direito:

![](/sbox/screen/jitsi-pt/47.png)

*Figura 18: Parte da janela de chamada com a criptografia ZRTP ativada*

O **Jitsi** permite fazer chamadas de voz e vídeo para mais de uma pessoa ao mesmo tempo. Quando este for o caso, **note** que a criptografia ZRTP poderá ser ativada entre quem iniciou a chamada e os outros contatos, mas não os contatos entre eles.

