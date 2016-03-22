

---

lang: pt
community: guide
type: tools
legacy: True
child: True
os: android
weight: 2
depth: 3
title: KeePassDroid - Advanced usage

---

## 3. Uso avançado do KeePassDroid

- [**3.0 Como editar uma entrada**](#3.0)
- [**3.1 Como gerar senhas aleatórias**](#3.1)
- [**3.2 Como travar o banco de dados do KeePassDroid**](#3.2)
- [**3.3 Como criar um cópia de reserva do arquivo de senhas do KeePassDroid**](#3.3)
- [**3.4 Como alterar sua senha mestre**](#3.4)
- [**3.5 Como alterar o tempo de espera**](#3.5)
    - [**3.5.1 O tempo de espera da Área de Transferência**](#3.5.1)
    - [**3.5.2 O tempo de espera para travar o banco de dados**](#3.5.2)

-------

<a name="3.0"></a>
## 3.0 Como editar uma entrada ##
Você pode alterar uma senha ou modificar outros detalhes armazenados na entrada. É considerado boa prática de segurança alterar suas senhas a cada 3 ou 6 meses.

**Passo 1**. **Toque** no *Grupo* que contém a entrada que você deseja editar e depois **toque** na entrada para visualizar seu conteúdo.

![](/sbox/screen/keepassdroid-pt/020.png)

*Figura 1: O conteúdo de uma Entrada.*

**Passo 2**. **Toque** em ![](/sbox/screen/keepassdroid-pt/021.png) para editar as informações. 

![](/sbox/screen/keepassdroid-pt/023.png)

*Figura 2: Editando as informações.*

**Passo 3**. Quando terminar, **toque** em ![](/sbox/screen/keepassdroid-pt/022.png) para salvar as alterações.


<a name="3.1"></a>
## 3.1 Como gerar senhas aleatórias ##
Senhas longas e aleatórias são fortes e seguras pois são criadas com base em princípios matemáticos e porque não podem ser simplesmente adivinhadas por alguém tentando invadir alguma de suas contas. O **KeePassDroid** oferece um *Gerador de Senhas*, para ajudar neste processo.

![](/sbox/screen/keepassdroid-pt/024.png)

*Figura 3: A tela de Edição da entrada de senha*

**Passo 1**. **Toque** em ![](/sbox/screen/keepassdroid-pt/025.png) ou na tela de *Adicionar Entrada* ou na tela de *Editar Entrada* (*Fig. 3*, acima), para ativar o *Gerador de Senha*, como a imagem abaixo:

![](/sbox/screen/keepassdroid-pt/026.png)

*Figura 4: O Gerador de Senhas.*

O tela do *Gerador de Senha* gera automaticamente uma senha aleatória curta, de 8 caracteres. Entretanto, é recomendável usar senhas mais longas. Você pode gerar uma senha mais longa e mais segura seguindo os seguintes passos do nosso exemplo:

- **Tamanho** pelo menos 16 caracteres
- **Marque** a opção Letras Maiúsculas
- **Marque** a opção Letras Minúsculas
- **Marque** a opção Dígitos
- **Marque** a opção Menos
- **Marque** a opção Underline
- **Marque** a opção Parênteses

**Observação**: Para gerar senhas mais longas do que 16 caracteres, substitua o número no campo 'Tamanho' pelo desejado.

Veja a *Fig. 4*, acima.

**Passo 2**. **Toque** em ![](/sbox/screen/keepassdroid-pt/027.png) para que o **KeePassDroid** gere a nova senha aleatória.

**Passo 3**. **Toque** em ![](/sbox/screen/keepassdroid-pt/028.png) para copiar a senha gerada para a sua entrada de senha e voltar para a janela de Informações.

![](/sbox/screen/keepassdroid-pt/029.png)

*Figura 5: As informações da Entrada*

**Passo 4**. **Toque** em ![](/sbox/screen/keepassdroid-pt/030.png) para aceitar as alterações e voltar para a tela de entradas, como abaixo:

![](/sbox/screen/keepassdroid-pt/031.png)

*Figure 6: A tela de Entradas*


<a name="3.2"></a>
## 3.2 Como travar o banco de dados do KeePassDroid ##
**Toque** no **Ícone do Cadeado** (![](/sbox/screen/keepassdroid-pt/032.png)), localizado no topo da tela principal do **KeePassDroid**. Isso bloqueará instantaneamente o seu banco de dados. A tela inicial aparecerá, na qual é preciso inserir a *senha mestre* para destravá-lo.

![](/sbox/screen/keepassdroid-pt/033.png)

*Figure 7: O banco de dados bloqueado*


<a name="3.3"></a>
## 3.3 Como criar um cópia de reserva do arquivo de senhas do KeePassDroid ##
O arquivo de senhas **KeePassDroid** do seu dispositivo Android possui a extensão *.kdb*. Você pode copiar este arquivo para o computador ou pen drive. Sem a senha mestra, ninguém mais conseguirá abri-lo.

Por padrão, o banco de dados é armazenado em uma pasta chamada *keepass*, no seu aparelho celular. A localização mais provável é */mnt/sdcard/keepass*.

**Observação**: É preciso ter o **KeePass** instalado no computador, ou uma versão portátil do KeePass no pen drive, para conseguir abrir o banco de dados copiado do seu aparelho Android.

Veja o [**Guia Prático sobre o KeePass**](/pt/keepass_main) para mais informações. 


<a name="3.4"></a>
## 3.4 Como alterar sua senha mestre ##
É possível alterar a senha mestre a qualquer momento. Isso pode ser feito após abrir o banco de dados de senhas.

**Passo 1**. **Toque** no ícone do menu (![](/sbox/screen/keepassdroid-pt/016.png)), que se encontra no canto superior direito da tela principal.

![](/sbox/screen/keepassdroid-pt/034.png)

*Figura 8: O menu de Opções*

**Passo 2**. **Toque** em ![](/sbox/screen/keepassdroid-pt/035.png) para ativar a seguinte janela:

![](/sbox/screen/keepassdroid-pt/036.png)

*Figura 9: Digite a nova senha.*

**Passo 3**. Digite a sua nova senha mestre nos campos **Senha** e **Confirmação de Senha**, e depois **toque** em OK.

![](/sbox/screen/keepassdroid-pt/037.png)

*Figura 10: Entre a nova Senha.*


<a name="3.5"></a>
## 3.5 Como alterar o tempo de espera

<a name="3.5.1"></a>
### 3.5.1 O tempo de espera da Área de Transferência
Para maior segurança, a senha copiada fica na Área de Transferência por apenas um período limitado de tempo antes de ser automaticamente apagada. É possível escolher essa duração entre **30 segundos**, **1 minuto** ou **5 minutos**.

Também existe a opção **Nunca**, mas não é aconselhável selecioná-la.

Você pode acessar essas opções na tela a seguir em: **Menu** (![](/sbox/screen/keepassdroid-pt/016.png)) > **Configurações** > **Aplicativo** > **Tempo limite para o clipboard**

![](/sbox/screen/keepassdroid-pt/038.png)

*Figura 11: As opções de limite de tempo para a Área de Transferência (Clipboard).*


<a name="3.5.2"></a>
### 3.5.2 O tempo de espera para travar o banco de dados
Também é possível travar o banco de dados de senhas quando o aplicativo estiver inativo por determinado período de tempo. O banco de dados se travará automaticamente após 5 minutos sem ser utilizado. Se quiser encurtar este período, **toque** em: **Menu** (![](/sbox/screen/keepassdroid-pt/016.png)) > **Configurações** > **Aplicativo** > **Tempo Limite do Aplicativo**

![](/sbox/screen/keepassdroid-pt/039.png)

*Figura 12: As opções de Tempo limite do aplicativo.*

**Selecione** **30 segundos**, **1 minuto** ou o padrão, **5 minutos**. Como antes, existe uma opção de **Nunca**, mas não é aconselhável selecioná-la.


