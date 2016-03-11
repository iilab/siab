

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Seções nessa página:

- [**5.0 Sobre volumes ocultos**](#5.0)
- [**5.1 Como criar um volume oculto**](#5.1)
- [**5.2 Como montar um volume oculto**](#5.2)
- [**5.3 Dicas sobre como usar a função de volume oculto de forma segura**](#5.3)


<a name="5.0"></a>
## 5.0 Sobre volumes ocultos ##

No **TrueCrypt**, um *Volume Oculto* é guardado dentro do seu *Volume Padrão* criptografado, mas sua existência fica escondida. Mesmo quando se 'monta' ou se abre o volume padrão, não é possível encontrar ou provar a existência de um volume oculto. Caso você sofra coerção para revelar a senha e a localização do seu volume padrão, o conteúdo armazenado ali será revelado, mas **não** a existência de um volume oculto dentro dele.

Imagine uma maleta com um compartimento secreto. Os documentos que poderiam ser confiscados ou perdidos são mantidos na seção normal da maleta, enquanto os arquivos importantes e privados ficam guardados na área secreta. O objetivo do compartimento secreto (especialmente o de um bem desenhado), é o de esconder sua própria existência e, com isso, os documentos dentro dele. 


<a name="5.1"></a>
## 5.1 Como criar um volume oculto ##

A criação de um *Volume Oculto* no **TrueCrypt** é similar à de um *Volume Padrão*: alguns dos painéis, telas e janelas são inclusive os mesmos.

**Passo 1**. **Abra** o **TrueCrypt**.

**Passo 2**. **Clique** em ![](/sbox/screen/truecrypt-pt/11.png) para ativar o *Assistente de Criação de Volume TrueCrypt*. 

**Passo 3**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para aceitar a opção padrão de *Criar um recipiente de arquivo criptografado*.

**Passo 4**. **Escolha** a opção *Volume oculto TrueCrypt*, como na imagem: 

![](/sbox/screen/truecrypt-pt/33.png)

*Figura 1: O Assistente de Criação de Volume TrueCrypt com a opção Crie um recipiente de arquivo criptografado escolhida*

**Passo 5**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/34.png)

*Figura 2: O Assistente de Criação de Volume TrueCrypt - janela de Modo de criação*

- *Modo direto*: Esta opção permite criar o *Volume Oculto* dentro de um *Volume Padrão*.

- *Modo normal*: Esta opção permite criar um novo *Volume Padrão* no qual guardar o *Volume Oculto*.

Neste exemplo, usaremos a opção *Modo direto*. 

**Observação**: Caso prefira criar um novo *Volume Padrão*, repita o processo descrito na Seção [**2.3 Como criar um volume padrão**](/pt/truecrypt_standardvolumes#2.3).

**Passo 6**. **Escolha** a opção *Modo direto* e então **clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a janela de *Criação do Volume - Localização do Volume*.

**Observação**: Assegure-se de que o *Volume Padrão* está desmontado antes de selecioná-lo. 

**Passo 7**. **Clique** em ![](/sbox/screen/truecrypt-pt/16.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/32.png)

*Figura 3: O Assistente de Criação de Volume TrueCrypt - janela de Selecione um Volume TrueCrypt*

**Passo 8**. **Encontre** o arquivo do volume usando a janela de *Selecione um Volume TrueCrypt*, como mostrado na *Figura 3*. 

**Passo 9**. **Clique** em ![](/sbox/screen/truecrypt-pt/16.png) para voltar ao *Assistente de Criação de Volume TrueCrypt*.

**Passo 10**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a tela de *Entre senha para...*.

**Passo 11**. **Digite** a senha usada na criação do *Volume Padrão* no campo de *Senha* para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/35.png)

*Figura 4: O Assistente de Criação de Volume TrueCrypt - painel de mensagem de Volume Oculto*

**Passo 12**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) após ler a mensagem para ativar a tela de *Opções de Criptografia do Volume Oculto*.

**Observação**: Mantenha as opções padrão de *Algoritmo de criptografia* e *Algoritmo de hash* conforme estão marcadas.

**Passo 13**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/36.png)

*Figura 5: O Assistente de Criação de Volume TrueCrypt - janela de Tamanho do Volume Oculto*

Nesta tela, você deverá escolher ou informar o tamanho do *Volume Oculto*.

**Observação**: Considere os tipos, quantidade e tamanho dos documentos a serem armazenados. Deixe algum espaço para o *Volume Padrão*. Caso selecione o valor máximo disponível para o *Volume Oculto*, não será possível colocar mais arquivos no *Volume Padrão* original.

Caso sei *Volume Padrão* tenha 10 Megabytes(MB) de tamanho e você especifique um tamanho de 5MB (como exibido na *Figura 6*, acima) para o *Volume Oculto*, você terá dois volumes (um oculto e um padrão) de cerca de 5MB cada. 

Assegure-se que os dados que armazenar no *Volume Padrão* não ocupem mais espaço do que os 5MB  configurados para o volume. Isso porque o **TrueCrypt** não detecta automaticamente a existência de um *Volume Oculto* e poderia sobrescrevê-lo acidentalmente, correndo o risco de perder todos os arquivos guardados ali. 

**Passo 14**. **Informe** o tamanho desejado para o volume oculto na caixa de texto correspondente, como mostra a *Figura 6*. 

**Passo 15**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a janela de *Senha do Volume Oculto*.

Agora, você deve gerar uma senha *diferente* da usada no volume padrão para proteger o volume oculto. Mais uma vez, lembre-se de escolher um segredo forte. Veja o [**Guia Prático do KeePass**](/pt/keepass_main) para saber mais sobre como criar senhas fortes.

**Dica**: Se o cenário de alguém usar força bruta para te forçar a revelar o conteúdo de seus volumes **TrueCrypt** é possível de acontecer, então guarde a senha do volume padrão no **KeePass** e crie uma combinação forte que apenas você saiba e lembre para o volume oculto. Isso ajudará a manter secreta a existência desse volume, já que não haverá traços de sua existência.

**Passo 16**. **

![](/sbox/screen/truecrypt-pt/37.png)

*Figura 6: O Assistente de Criação de Volume TrueCrypt - painel de Formatação de Volume Oculto*

Deixe as opções *Sistema de arquivos* e *Cluster* como estão.

**Passo 17**. **Mova** o cursor com o mouse pela tela para aumentar a força da criptografia e então **clique** em ![](/sbox/screen/truecrypt-pt/38.png) para formatar o volume oculto.

*Após formatar o volume oculto, a seguinte tela aparecerá:* 

![](/sbox/screen/truecrypt-pt/39.png)

*Figura 7: A tela de mensagem do Assistente de Criação de Volume TrueCrypt*

**Observação**: A *Figura 7* tanto confirma a criação do volume oculto como avisa sobre os perigos de sobrescrever os arquivos contidos nele ao guardar dados no volume padrão.

**Passo 18**. **Clique** em ![](/sbox/screen/truecrypt-pt/07.png) para ativar a janela de *Volume Oculto Criado* e então **clique** em ![](/sbox/screen/truecrypt-pt/24.png) e volte para o console do **TrueCrypt**.

O volume oculto está agora criado dentro do seu volume padrão. Você pode guardar documentos ali, que permanecerão invisíveis mesmo para alguém que tenha conseguido a senha daquele volume padrão específico.


<a name="5.2"></a>
## 5.2 Como montar um volume oculto ##

O método para montar ou tornar um *Volume Oculto* acessível para uso é exatamente o mesmo do para um *Volume Padrão*; a única diferença é que você usará apenas a senha recém criada do *Volume Oculto*.

Para *montar* ou abrir o *Volume Oculto*, siga os seguintes passos: 

**Passo 1**. **Selecione** um dispositivo da lista (neste exemplo, usaremos o dispositivo *M*):

![](/sbox/screen/truecrypt-pt/50.png)

*Figura 8: Um dispositivo selecionado como ponto de montagem na tela do Volume do TrueCrypt*

**Passo 2**. **Clique** em ![](/sbox/screen/truecrypt-pt/16.png) para ativar a janela de *Selecione um Volume TrueCrypt*. 

**Passo 3**. **Navegue** para e então **selecione** seu arquivo de volume *TrueCrypt* (o mesmo arquivo do volume padrão).

**Passo 4**. **Clique** em ![](/sbox/screen/truecrypt-pt/26.png) para voltar ao console do **TrueCrypt**.

**Passo 5**. **Clique** em ![](/sbox/screen/truecrypt-pt/27.png) para ativar a tela de *Entre senha para...*, como se vê na imagem:

![](/sbox/screen/truecrypt-pt/28.png)

*Figura 9: A tela de Entre senha para...*

**Passo 6**. **Digite** a senha usada na criação do volume oculto e então **clique** em ![](/sbox/screen/truecrypt-pt/07.png). 

Seu volume oculto agora está montado (ou aberto), como se vê na imagem:

![](/sbox/screen/truecrypt-pt/40.png)

*Figura 10: A janela principal do TrueCrypt exibindo o Volume Oculto recém montado*

**Passo 7**. **Dê um clique duplo** na entrada selecionada ou acesse-a via a janela de *Meu Computador*. 


<a name="5.3"></a>
## 5.3 Dicas sobre como usar a função de volume oculto de forma segura ##

O propósito da função de um volume oculto é escapar da situação potencialmente perigosa de *parecer* que você está entregando seus arquivos criptografados quando alguém na posição de poder demandá-los, quando na realidade as informações mais sensíveis não estão sendo reveladas. Além de proteger os dados, isso pode ajudar a evitar novos abusos com relação à sua segurança ou evitar expor colegas e parceiros. Para que esta técnica seja efetiva, é preciso criar uma situação na qual a pessoa que demanda ver os arquivos fique satisfeita com o que você estiver mostrando e te libere para ir embora.

Para tal, você pode querer implementar algumas das seguintes sugestões:

- Coloque alguns documentos confidenciais que possam eventualmente ser expostos no volume padrão. Tal informação deve ser sensível o suficiente para fazer sentido o fato de ela estar guardada dentro de um volume criptografado. 

- Saiba que uma pessoa que exija ver seus arquivos pode saber da existência de volumes ocultos. Se você estiver usando o **TrueCrypt** da forma correta, porém, aquela pessoa não conseguirá provar que seu volume oculto existe, o que torna sua negação mais crível.

- Atualize os arquivos guardados no volume padrão semanalmente. Isso criará a impressão de que você realmente usa tais documentos.

Sempre que montar um volume **TrueCrypt**, é possível escolher habilitar a função *Proteger disco oculto contra danos por gravações no volume externo*. Esta função, *muito* importante, permite que você coloque novos arquivos de 'embuste' no seu volume padrão sem o risco de apagar ou sobrescrever o conteúdo do volume oculto de forma acidental.

Como mencionado antes, exceder a capacidade de armazenamento de seu volume padrão pode destruir seus documentos ocultos. Não habilite a função *Proteger disco oculto* caso alguém te force a montar um volume **TrueCrypt**, pois fazê-lo requer informar a senha de acesso ao volume oculto e claramente revelará sua existência. Porém, ao atualizar os arquivos de embuste, de forma privada, *sempre* habilite a função.

Para usar a função de *Proteger disco oculto*, siga os seguintes passos:

**Passo 1**. **Clique** em ![](/sbox/screen/truecrypt-pt/41.png) na tela de *Entre senha para...*, mostrada na *Figura 9*, acima. Isso ativará a janela de *Opções de Montagem*, como se vê na imagem:

![](/sbox/screen/truecrypt-pt/42.png)

*Figura 11: A janela de Opções de Montagem*

**Passo 2**. **Habilite** a opção *Proteger disco oculto contra danos por gravações no volume externo*.

**Passo 3**. **Digite** a senha para o seu Volume Oculto e então **clique** em ![](/sbox/screen/truecrypt-pt/07.png).

**Passo 4**. **Clique** em ![](/sbox/screen/truecrypt-pt/27.png) para montar seu volume padrão. Após montá-lo, você poderá adicionar novos arquivos de embuste sem danificar o volume oculto.

**Passo 5**. **Clique** em ![](/sbox/screen/truecrypt-pt/31.png) para desmontar ou tornar seu volume padrão indisponível para uso ao terminar de modificar seu conteúdo.

**Lembre-se**: Só é necessário fazer isso ao atualizar os arquivos de seu Volume Padrão. Caso alguém te force a revelar seu Volume Padrão, você não deve habilitar a função *Proteger disco oculto*.


