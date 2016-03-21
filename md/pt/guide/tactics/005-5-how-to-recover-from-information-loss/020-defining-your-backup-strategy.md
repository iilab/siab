

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Defining your backup strategy

---

Para fazer as cópias de reserva (*backup*) de todos os tipos de dados listados acima, será preciso uma combinação entre programas e soluções de processos. Essencialmente, é preciso assegurar que cada tipo de dado seja armazenado em, pelo menos, dois locais separados.

**Documentos eletrônicos** - crie uma cópia completa dos documentos em seu computador usando programas como o [*Cobian Backup*](/pt/glossary#Cobian_Backup), descrito com mais detalhes abaixo. Guarde o *backup* em algum dispositivo portátil para que possa ser levado para casa ou outro local seguro. HDs externos, CD/DVDs ou pen drives são alternativas possíveis. Algumas pessoas usam CDs ou DVDs para isso, já que o risco de sobrescrever (e perder) as cópias de reserva é menor. Essas mídias são baratas o suficiente para permitir usar uma nova a cada vez que um *backup* é gerado.

Como documentos eletrônicos costumam ser a categoria de dados que contêm as informações mais sensíveis, é particularmente importante proteger as cópias de reserva com criptografia. É possível ver como fazer isso no [***Capítulo 4: Como proteger os arquivos sensíveis do seu computador***](/pt/chapter-4) e no [***Guia Prático do TrueCrypt***](/pt/truecrypt_main).

**Bancos de dados de programas** - Uma vez que você saiba onde estão os bancos de dados dos programas, pode fazer as cópias de reserva (*backup*) da mesma forma que os documentos eletrônicos.

**E-mails** - Em vez de ler sua correspondência eletrônica apenas por um navegador de internet, instale um cliente de e-mail como o [*Thunderbird*](/pt/glossary#Thunderbird) e configure-o para acessar suas contas. O [***Guia Prático do Thunderbird***](/pt/thunderbird_main) explica em detalhes como fazer isso. A maioria dos serviços de e-mail também fornece instruções sobre como usar seus endereços eletrônicos com tais programas. Se optar por mover as mensagens antigas para o computador, de forma que não fiquem armazenadas no servidor (ex. por motivos de segurança), não se esqueça de inclui-las ao fazer o *backup* dos documentos eletrônicos, como descrito acima.

**Conteúdo de telefones celulares** - Para copiar os números de telefone e as mensagens de texto de seu celular, conecte-o ao computador com o software apropriado, geralmente disponível no site da empresa fabricante do aparelho. Talvez seja preciso comprar um cabo USB especial para isso.

**Documentos impressos** - Quando possível, você deveria fazer cópias digitalizadas de papéis importantes e guardá-las junto com os *backups* de outros documentos eletrônicos, como mencionado acima.

Ao fim, você deve estar com os dispositivos de armazenamento, tipos de dados e cópias de reserva (*backups*) reordenados de forma a serem bem mais resistentes a desastres:

<table width="100%" border="1">
<tbody>
<tr>
<th>Tipo de dado</th>
<th>Versão principal/Duplicata</th>
<th>Dispositivo de armazenamento</th>
<th>Localização</th>
</td>
</tr>
<tr>
<td>Documentos eletrônicos</td>
<td>Versão principal</td>
<td>Computador (disco rígido)</td>
<td>Escritório</td>
</tr>
<tr>
<td>Documentos eletrônicos</td>
<td>Duplicata</td>
<td>CDs</td>
<td>Em casa</td>
</tr>
<tr>
<td>Alguns documentos eletrônicos importantes</td>
<td>Duplicata</td>
<td>Pen drive</td>
<td>Comigo</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Tipo de dado</th>
<th>Versão principal/Duplicata</th>
<th>Dispositivo de armazenamento</th>
<th>Localização</th>
</td>
</tr>
<tr>
<td>Bancos de dados de programas</td>
<td>Versão principal</td>
<td>Computador (disco rígido)</td>
<td>Escritório</td>
</tr>
<tr>
<td>Bancos de dados de programas</td>
<td>Duplicata</td>
<td>CDs</td>
<td>Em casa</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Tipo de dado</th>
<th>Versão principal/Duplicata</th>
<th>Dispositivo de armazenamento</th>
<th>Localização</th>
</td>
</tr>
<tr>
<td>E-mails e contatos de e-mail</td>
<td>Duplicata</td>
<td>Conta do Gmail</td>
<td>Internet</td>
</tr>
<tr>
<td>E-mails e contatos de e-mail</td>
<td>Versão principal</td>
<td>Thunderbird no computador do escritório</td>
<td>Escritório</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Tipo de dado</th>
<th>Versão principal/Duplicata</th>
<th>Dispositivo de armazenamento</th>
<th>Localização</th>
</td>
</tr>
<tr>
<td>Mensagens de texto e contatos telefônicos</td>
<td>Versão principal</td>
<td>Telefone celular</td>
<td>Comigo</td>
</tr>
<tr>
<td>Mensagens de texto e contatos telefônicos</td>
<td>Duplicata</td>
<td>Computador (disco rígido)</td>
<td>Escritório</td>
</tr>
<tr>
<td>Mensagens de texto e contatos telefônicos</td>
<td>Duplicata</td>
<td>Cartão SIM de reserva (backup)</td>
<td>Em casa</td>
</tr>
</tbody>
</table>




<table width="100%" border="1">
<tbody>
<tr>
<th>Tipo de dado</th>
<th>Versão principal/Duplicata</th>
<th>Dispositivo de armazenamento</th>
<th>Localização</th>
</td>
</tr>
<tr>
<td>Documentos impressos</td>
<td>Versão principal</td>
<td>Gaveta da mesa</td>
<td>Escritório</td>
</tr>
<tr>
<td>Documentos digitalizados</td>
<td>Duplicata</td>
<td>CDs</td>
<td>Em casa</td>
</tr>
</tbody>
</table>




<div class="background" markdown="1">
Elena: Conheço algumas pessoas que mantêm todos os documentos importantes no Gmail, anexando-os a mensagens de 'rascunho' ou aos próprios e-mails. Isso contaria como uma 'segunda localização física' para os meus arquivos?

Nikolai: Isso pode te ajudar a recuperá-los caso perca um ou dois documentos muito importantes, mas é bem desajeitado. Sinceramente, quantas cópias de reserva de documentos por semana você faria dessa forma? Além disso, você tem que considerar se tais anexos estão mesmo seguros, especialmente caso se preocupe que seu e-mail possa estar sendo monitorado. Outra coisa: a menos que você se conecte ao Gmail de forma segura, isso seria como entregar suas informações sensíveis em uma bandeja de prata. Usar uma conexão HTTPS para entrar no Gmail e fazer cópias de pequenos volumes do TrueCrypt ou de bancos de dados do KeePass até é bem seguro, porque o conteúdo é criptografado, mas eu não te recomendaria adotar esse procedimento como uma estratégia geral de *backup*.
</div>

