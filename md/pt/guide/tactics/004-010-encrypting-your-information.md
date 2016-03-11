

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: Mas meu computador já está protegido pela senha de login do Windows! Já não está bom assim?

Claudia: Na verdade, as senhas de login do Windows costumam ser bem fáceis de quebrar. Além disso, qualquer pessoa com acesso à sua máquina por tempo suficiente para reiniciá-la com um LiveCD pode copiar os dados sem nem ter de se preocupar com a senha. Caso possam levar o computador, é ainda pior. Não são apenas com as senhas do Windows com que você deveria se preocupar; você não deveria confiar também nas senhas do Microsoft Word ou do Adobe Acrobat.
</div>

[*Criptografar*](/pt/glossary#Encryption) dados é um pouco como mantê-los trancados em um cofre. Apenas quem possui a chave ou sabe a combinação para abri-lo (uma chave ou senha de [*criptografia*](/pt/glossary#Encryption), neste caso) pode acessá-los. A analogia é particularmente apropriada ao [*TrueCrypt*](/pt/glossary#TrueCrypt) e a ferramentas semelhantes, que criam compartimentos seguros chamados 'volumes criptografados' em vez de proteger os arquivos um por vez. É possível colocar um grande número de arquivos em um volume [*criptografado*](/pt/glossary#Encryption), mas esses programas não protegerão nada do que estiver fora dele, em outras pastas do computador, pen drives ou mídias removíveis.

<div class="getstarted" markdown="1">
**Guia Prático - saiba usar o** [***TrueCrypt - Armazenamento seguro de arquivos***](/pt/truecrypt_main)
</div>

Ainda que outros programas possuam uma força similar de *[criptografia](/pt/glossary#Encryption)*, o [*TrueCrypt*](/pt/glossary#TrueCrypt) tem algumas funcionalidades importantes, que ajudam a elaborar uma estratégia para a segurança da informação. Ele permite **criptografar todo o disco de um computador** de forma permanente, o que inclui todos os arquivos, todos os arquivos temporários criados em uma sessão de trabalho, todos os programas instalados e todos os arquivos relacionados ao sistema operacional Windows; permite criar volumes *[criptografados](/pt/glossary#Encryption)* em dispositivos portáteis de armazenamento de dados; e possui ainda funções de 'negação', descritas na seção [***Como ocultar informações sensíveis***](/pt/chapter_4_2), abaixo. Além disso, o TrueCrypt é um [*programa livre e de código aberto (FOSS)*](/pt/glossary#FOSS).

<div class="background" markdown="1">
Pablo: Certo, agora você me deixou preocupado. E as outras pessoas, que usam o mesmo computador? Elas conseguem abrir os arquivos da pasta 'Meus Documentos'?

Claudia: Gosto do jeito que você está pensando! Se a senha do Windows não o protege de intrusos, como pode protegê-lo de pessoas que têm contas no mesmo computador? Na verdade, a sua pasta de 'Meus Documentos' costuma ficar visível a qualquer um, então outras pessoas não teriam de fazer nada muito elaborado para ler arquivos não criptografados. Mas está certo, mesmo que a pasta seja tornada 'privada', você ainda não está seguro a não ser que use algum tipo de criptografia.</i>
</div>


### Dicas para usar criptografia de arquivos de forma segura ###

Guardar informações confidenciais pode ser um risco tanto para você como para as pessoas com quem trabalha. A *[criptografia](/pt/glossary#Encryption)* reduz esse risco, mas não o elimina. O primeiro passo para se proteger é reduzir a quantidade de dados sensíveis que você mantém à volta. A menos que você tenha um bom motivo para guardar um determinado arquivo, ou um tipo específico de informação contida em um arquivo, deveria simplesmente apagá-lo (veja o [***Capítulo 6: Como destruir informações sensíveis***](/pt/chapter-6) para ver como fazer isso de forma segura). O segundo passo é usar uma boa ferramenta de [*criptografia*](/pt/glossary#Encryption) de dados, como o [*TrueCrypt*](/pt/glossary#TrueCrypt).

<div class="background" markdown="1">
Claudia: Bom, talvez não precisemos realmente guardar informações que podem ser usadas para identificar as pessoas que nos deram os depoimentos. O que te parece?

Pablo: Concordo. Provavelmente, deveríamos escrever o mínimo possível sobre isso. Também poderíamos pensar em um código simples, que podemos usar para proteger os nomes e locais que de fato precisamos registrar.
</div>

Voltando à analogia de um cofre trancado, há algumas coisas que você deve ter em mente ao usar o [*TrueCrypt*](/pt/glossary#TrueCrypt) e ferramentas similares. Independentemente de quão forte seja o cofre, deixar a porta aberta não vai ajudar. Quando o volume [*TrueCrypt*](/pt/glossary#TrueCrypt) estiver 'montado' (sempre que é possível acessar seu conteúdo), os dados podem estar vulneráveis. Mantenha-o fechado, exceto quando estiver efetivamente lendo ou modificando os arquivos contidos ali.

Há algumas situações nas quais é especialmente importante lembrar-se de deixar os volumes [*criptografados*](/pt/glossary#Encryption) desmontados (não acessíveis):

  * Desmonte-os sempre que sair de perto do computador, por qualquer período de tempo. Mesmo que você costume deixar a máquina ligada à noite, é preciso ter certeza de que os arquivos sensíveis não estarão acessíveis a alguém que tenha acesso físico ou remoto a eles enquanto você não estiver ali.
  * Desmonte-os antes de colocar o computador em espera, para economizar energia. Isso vale tanto para as funções de 'suspender' como de 'hibernar', que são tipicamente usadas em laptops, mas que também existem em computadores desktops.
  * Desmonte-os antes de permitir a alguém usar seu computador. Quando houver chances de passar por postos policiais, postos de imigração ou cruzar fronteiras, é importante desmontar todos os volumes [*criptografados*](/pt/glossary#Encryption) e desligar completamente a máquina.
  * Desmonte-os antes de inserir pen drives ou outros dispositivos de memória não conhecidos (como HDs externos); isso inclui os pertencentes a amigas, amigos e colegas.
  * Se você mantém um volume [*criptografado*](/pt/glossary#Encryption) em um pen drive, lembre-se de que apenas desconectá-lo do computador pode não desmontá-lo imediatamente. Mesmo que tenha de proteger os arquivos rapidamente, é necessário desmontar o volume da forma correta para então remover o pen drive ou HD externo via sistema operacional (*'remover hardware com segurança'*) e, finalmente, desconectá-lo fisicamente da máquina. Talvez você queira praticar até encontrar a forma mais rápida de fazer todas essas etapas.
	
Caso opte manter seu volume [*TrueCrypt*](/pt/glossary#TrueCrypt) em um pen drive, também é possível manter uma cópia do programa [*TrueCrypt*](/pt/glossary#TrueCrypt) com ele, o que permitirá acessar os arquivos criptografados no computador de outras pessoas. Porém, as regras gerais ainda se aplicam: se você não tem certeza de que aquela máquina está livre de [*malware*](/pt/glossary#Malware), provavelmente não deveria usá-la para digitar senhas ou acessar arquivos sensíveis.

