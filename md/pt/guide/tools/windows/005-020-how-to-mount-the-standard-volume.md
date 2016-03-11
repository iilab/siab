

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Seções nessa página:

- [**2.0 Como instalar o TrueCrypt**](#2.0)
- [**2.1 Como deixar a interface do TrueCrypt em português**](#2.1)
- [**2.2 Sobre o TrueCrypt**](#2.2)
- [**2.3 Como criar um volume padrão**](#2.3)
- [**2.4 Como criar um volume padrão em um pen drive**](#2.4)
- [**2.5 Como criar um volume padrão (Continuação)**](#2.5)


<a name="2.0"></a>
## 2.0 Como instalar o TrueCrypt ##

**Passo 1**. **Dê um clique duplo** em ![](/sbox/screen/truecrypt-pt/02.png). A caixa de *Abrir Arquivo - Aviso de Segurança* pode aparecer; caso apareça **Clique** em ![](/sbox/screen/truecrypt-pt/03.png) para ativar a tela de *Licença* do **TrueCrypt**.

**Passo 2**. **Marque** a opção *Eu aceito e concordo com os termos de licença* para habilitar o botão de *Aceitar*; **Clique** em ![](/sbox/screen/truecrypt-pt/03b.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/04.png)

*Figura 1: O modo 'Wizard' no modo de instalação padrão*

- Modo *Install* (Instalação): Esta opção é para quem não quer ou não precisa esconder o fato de que usa o **TrueCrypt** no computador.

- Modo *Extract* (Extração): Esta opção é para quem quer carregar uma versão portátil do **TrueCrypt** em um pen drive e não tê-la instalada no computador.

**Observação**: Algumas das opções (por exemplo, criptografia de disco ou partição inteira) não funcionarão quando o **TrueCrypt** for apenas extraído.

**Observação**: Embora o modo padrão de *Install* (Instalação) seja recomendado aqui, você ainda poderá usar o programa no modo portátil depois. Para saber mais sobre como usar o modo **TrueCrypt Viajante**, veja a seção [**TrueCrypt - Versão portátil**](/pt/truecrypt_portable).

**Passo 3**. **Clique** em ![](/sbox/screen/truecrypt-pt/03.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/05.png)

*Figura 2: A janela de Setup (Opções de configuração)*

**Passo 4**. **Clique** em ![](/sbox/screen/truecrypt-pt/06.png) para ativar a janela de *Instalação* e começar a instalar o programa no sistema.

**Passo 5**. **Clique** em ![](/sbox/screen/truecrypt-pt/07.png) e em ![](/sbox/screen/truecrypt-pt/08.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/09.png)

*Figura 3: A janela de confirmação do TrueCrypt Setup*

**Passo 6**. **Clique** em ![](/sbox/screen/truecrypt-pt/10a.png) para completar a instalação do **TrueCrypt**.

**Observação**: É altamente recomendável consultar a [documentação de ajuda do **TrueCrypt**](http://andryou.com/truecrypt/docs/index.php) (em inglês) após completar este tutorial. 


<a name="2.1"></a>
## 2.1 Como deixar a interface do TrueCrypt em português ##

Para deixar a interface do **Truecrypt** em português, é preciso baixar o pacote de idioma para versão que estamos usando, a 7.1a. Conforme mencionado na [Introdução deste Guia Prático](/pt/truecrypt_main), esta é uma versão mais antiga e, portanto, só é possível encontrar tais pacotes em arquivos da internet, como o repositório [truecrypt-archive](https://github.com/DrWhax/truecrypt-archive), hospedado no GitHub.

**Passo 1**. **Procure** e **clique** no arquivo **langpack-pt-br-0.1.0-for-truecrypt-7.1a.zip** na [pasta de línguas](https://github.com/DrWhax/truecrypt-archive/tree/master/langpacks) do repositório truecrypt-archive. Na tela que aparecerá, **clique** em ![](/sbox/screen/truecrypt-pt/truecrypt_language04.png) para começar o download. Alternativamente, **clique** [neste link](https://github.com/DrWhax/truecrypt-archive/blob/master/langpacks/langpack-pt-br-0.1.0-for-truecrypt-7.1a.zip?raw=true) para fazer o download diretamente.

**Passo 2**. **Extraia** todos arquivos do pacote zipado para a mesma pasta na qual o **Truecrypt** está instalado; esta é a mesma pasta onde o está o arquivo 'TrueCrypt.exe' (por exemplo, 'C:\Program Files\TrueCrypt').

![](/sbox/screen/truecrypt-pt/truecrypt_language03.png)

*Figura Tradução 1: O arquivo de idioma para português no repositório do GitHub em destaque*

**Passo 3**. **Abra** o programa e **escolha a opção "Settings > Language..."**, no Menu principal para ativar a tela de seleção de idiomas.

![](/sbox/screen/truecrypt-pt/truecrypt_language01.png)

*Figura Tradução 2: A janela principal do TrueCrypt, com a seleção de idiomas em destaque*

**Passo 4**. A tela de seleção de idiomas deve mostrar duas opções: inglês e português do Brasil. **Clique** na opção 'Português-Brasil' e **clique** em ![](/sbox/screen/truecrypt-pt/07.png) para ativá-la.

**Observação**: o link para download do pacote de idiomas desta tela não funciona mais, uma vez que estamos usando uma versão mais antiga do programa.

![](/sbox/screen/truecrypt-pt/truecrypt_language02.png)

*Figura Tradução 3: A janela principal do TrueCrypt, com a seleção de idiomas em destaque*


<a name="2.2"></a>
## 2.2 Sobre o TrueCrypt ##

O **TrueCrypt** é um programa que protege seus arquivos ao evitar que qualquer pessoa sem a senha correta os acesse. Funciona como um cofre eletrônico, permitindo que você tranque seus dados de modo que apenas alguém com a senha correta possa abri-los.

O **TrueCrypt** funciona criando *volumes* ou seções no computador, nos quais os dados serão armazenados. Quando um arquivo é criado ali, ou movido para tais volumes, o **TrueCrypt** automaticamente criptografa aquela informação. Ao abri-las ou levá-las para fora, é descriptografada automaticamente para uso. Esse processo é chamado de criptografia imediada ("*on-the-fly encryption*").


<a name="2.3"></a>
## 2.3 Como criar um volume padrão ##

O **TrueCrypt** permite criar dois tipos de volumes: *Oculto* e *Padrão*. Nesta seção, veremos como criar um *Volume Padrão* para guardar arquivos.

Para começar a usar o programa e criar um *Volume Padrão*, siga os seguintes passos:

**Passo 1**. **Dê um clique duplo** em ![](/sbox/screen/truecrypt-pt/52.png) ou **Selecione Início > Programas > TrueCrypt > TrueCrypt** para abrir o **TrueCrypt**.

**Passo 2**. **Selecione** um dos discos listados no painel do **TrueCrypt**, como se vê abaixo:

![](/sbox/screen/truecrypt-pt/10.png)

*Figura 4: O console do TrueCrypt*

**Passo 3**. **Clique** em ![](/sbox/screen/truecrypt-pt/11.png) para ativar o *Assistente de Criação de Volume TrueCrypt*, como na imagem abaixo:

![](/sbox/screen/truecrypt-pt/12.png)

*Figura 5: A janela do Assistente de Criação de Volume TrueCrypt* 

Na *Figura 5*, há três opções para criptografar um *Volume Padrão*. Neste capítulo, usaremos a de *Criar um recipiente de arquivo criptografado*. Veja a [**documentação oficial do TrueCrypt**](http://www.truecrypt.org/docs/) para a descrição das outras duas opções.

**Passo 4**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/14.png)

*Figura 6: A janela de Tipo de Volume*

A *janela de Tipo de Volume* do *Assistente de Criação de Volume TrueCrypt* permite escolher entre a criação de um volume *Padrão* ou *Oculto*. 

**Importante**: Para mais informações sobre *Como criar um volume oculto*, veja a seção [**Volumes ocultos**](/pt/truecrypt_hiddenvolumes).

**Passo 5**. **Escolha** a opção *Volume TrueCrypt Padrão*. 

**Passo 6**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte janela:

![](/sbox/screen/truecrypt-pt/15.png)

*Figura 7: O Assistente de Criação de Volume - painel de Localização de Volume*

Você pode escolher onde gostaria de criar seu *Volume Padrão* na tela de *Assistente de Criação de Volume - Localização de Volume*. O arquivo pode ser guardado como qualquer outro.

**Passo 7**. **Digite** o nome do arquivo no campo de texto ou **clique** em ![](/sbox/screen/truecrypt-pt/16.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/17.png)

*Figura 8: A janela de Selecione o Caminho e o Nome do Arquivo*

**Observação**: Um volume **TrueCrypt** fica contido dentro de um arquivo comum. Isso significa que pode ser movido, copiado ou mesmo apagado! É necessário lembrar tanto a localização como o nome do arquivo. Porém, é possível renomear o volume criado (veja também a seção [**2.4 Como criar um volume padrão em um pen drive**](#2.4)). Neste tutorial, criaremos um Volume Padrão na pasta **Meus Documentos** e o nomearemos *Meu Volume*, como visto na *Figura 8*, acima. 

**Dica**: Você pode usar qualquer nome de arquivo ou extensão. Por exemplo, é possível chamar o Volume Padrão de *receitas.doc*, de forma parecer um documento de *Word*, ou *video_amigo.mpg*, de modo a camuflá-lo como um vídeo. Esse é um dos modos que ajudam a disfarçar a existência de um Volume TrueCrypt no computador. 

**Passo 8**. **Clique** em ![](/sbox/screen/truecrypt-pt/25.png) para fechar a janela *Selecione o Caminho e o Nome do Arquivo* e voltar ao *Assistente de Criação de Volume TrueCrypt* como se vê na imagem:

![](/sbox/screen/truecrypt-pt/18.png)

*Figura 9: O Assistente de Criação de Volume TrueCrypt exibindo o painel de Localização de Volume*

**Passo 9**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a *Figura 10*. 


<a name="2.4"></a>
## 2.4 Como criar um volume padrão em um pen drive ##

Para criar um *Volume Padrão* do **TrueCrypt** em um pen drive, siga os passos 1 a 7 da seção [**2.2 Como criar um volume padrão**](#2.2), até a tela de *Localização do Volume*. Em vez de escolher a pasta *Meus Documentos* como local de destino, **navegue** até seu pen drive e **escolha-o**. Então, **digite** um nome de arquivo para criar o *Volume Padrão* ali.


<a name="2.5"></a>
## 2.5 Como criar um volume padrão (Continuação) ##

Neste ponto, já é possível escolher um método de criptografia específico (ou *algoritmo*, como aparece escrito na tela) para codificar a informação a ser armazenada no *Volume Padrão*. 

![](/sbox/screen/truecrypt-pt/19.png)

*Figura 10: O painel de Opções de Criptografia do Assistente de Criação de Volume*

**Observação**: Você pode manter as opções padrão aqui, conforme estão escolhidas. Todos os algoritmos existentes nesta tela são considerados seguros. 

**Passo 10**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela do *Assistente de Criação de Volume*:

![](/sbox/screen/truecrypt-pt/20.png)

*Figura 11: O Assistente de Criação de Volume exibindo o painel de Tamanho do Disco*

O painel de *Tamanho do Disco* permite especificar o tamanho do *Volume Padrão*. Neste exemplo, está configurado para 10 megabytes. Você pode escolher um tamanho diferente. Considere o tamanho dos documentos a dos tipos de arquivo que gostaria de guardar e escolha um tamanho de volume apropriado a eles.

**Dica**: Caso você queira fazer uma cópia de reserva (*backup*) de seu Volume Padrão em um CD mais tarde, o tamanho configurado aqui deve ser de 700MB ou menor.

**Passo 11**. **Digite** o tamanho do volume no campo de texto e então **clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/21.png)

*Figura 12: O Assistente de Criação de Volume exibindo a tela de Senha do Volume*

**Importante**: Escolher uma senha forte e segura é uma das tarefas mais importantes  ao criar um *Volume Padrão*. Uma boa senha protegerá o seu volume criptografado, e quanto mais forte ela for, melhor. Você não precisa criar seus próprios segredos, ou mesmo lembrá-los, caso use um programa de geração de senhas como o **KeePass**. Veja o guia do [**KeePass**](/pt/keepass_main), para saber mais sobre criação e armazenamento de senhas.

**Passo 12**. **Digite** sua senha e então **redigite-a** no campo de *Confirmar*.

**Importante**: O botão de *Avançar* permanecerá desabilitado até que a digitação nos dois campos seja a mesma. Caso seu segredo não seja suficientemente forte ou seguro, você verá um aviso. Considere mudá-lo! Embora o **TrueCrypt** funcionará com qualquer senha escolhida, seus dados podem não estar muito seguros.

**Passo 13**. **Clique** em ![](/sbox/screen/truecrypt-pt/13.png) para ativar a seguinte tela:

![](/sbox/screen/truecrypt-pt/22.png)

*Figura 13: O Assistente de Criação de Volume exibindo a tela de Formatação de Volume*

O **TrueCrypt** agora está pronto para criar um *Volume Padrão*. Mova seu mouse de forma aleatória dentro da janela do *Assistente de Criação de Volume* por alguns segundos. Quanto mais tempo você mover o mouse, melhor será a qualidade de sua chave de criptografia.

**Passo 14**. **Clique** em ![](/sbox/screen/truecrypt-pt/38.png) para começar a criar o volume padrão.

O **TrueCrypt** criará um arquivo chamado *Meu Volume* na pasta *Meus Documentos*, conforme vimos anteriormente. Tal arquivo conterá um *Volume Padrão* do **TrueCrypt** com 10 Megabytes de tamanho, que será usado para armazenar dados de forma segura.

Após a criação do *Volume Padrão*, o seguinte aviso aparecerá:

![](/sbox/screen/truecrypt-pt/23.png)

*Figura 14: A mensagem de confirmação de que o volume TrueCrypt foi criado com sucesso*

**Passo 15**. **Clique** em ![](/sbox/screen/truecrypt-pt/07.png) para completar a criação do *Volume Padrão* e retornar ao console do **TrueCrypt**.

**Passo 16**. **Clique** em ![](/sbox/screen/truecrypt-pt/24.png) para fechar o *Assistente de Criação de Volume*.

