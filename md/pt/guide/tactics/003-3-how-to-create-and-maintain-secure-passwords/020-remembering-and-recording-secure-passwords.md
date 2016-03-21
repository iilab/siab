

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Remembering and recording secure passwords

---

Ao ver a lista de sugestões da seção anterior, você deve estar se perguntando como lembrar senhas ou frases extensas e complexas que, às vezes, não tem significado. A importância de usar segredos diferentes para cada conta torna isso ainda mais difícil. Como fazer sem ter de escrevê-los ou sem uma memória fotográfica? 

Há alguns truques que ajudam a criar combinações fáceis de lembrar e, ao mesmo tempo, extremamente difíceis de adivinhar, mesmo para alguém usando tipos avançados de software de 'quebras de senha'. Há também a opção de armazená-las com uma ferramenta como o [*KeePass*](/pt/glossary#KeePass), criado especificamente para esse propósito. 


### Como lembrar senhas seguras ###

É importante usar tipos de caracteres diferentes ao escolher uma senha. Isso pode ser conseguido de várias formas:

  * Ao alternar maiúsculas e minúsculas, como em: 'Meu noME não é DeLiRiUM'
  * Ao substituir algumas letras por números, como em: 'muit0 tr4b4lh0 e pouc4 d1vers40'
  * Ao incorporar alguns símbolos, como em: 'o@panh4d0rnoCampod3(3nteiO'
  * Ao misturar línguas diferentes, como em: 'Vê s3 c()m3 tod0 o sOrBET au ch()col@T' 

Qualquer um desses métodos pode ajudar a aumentar a complexidade de um segredo que seria, de outra forma, simples. Assim, você pode escolher uma senha segura sem ter de abandonar a ideia de memorizá-la. 

Algumas das substituições mais comuns (como o uso do zero em vez de um 'o', ou do símbolo '@' em vez de um 'a') já estão incorporadas faz tempo nas ferramentas de quebra de senhas, mas ainda são uma boa ideia, pois aumentam o tempo que tais programas levam para fazê-lo. Em situações mais frequentes, nas quais esses software não podem ser usados, ajudam a evitar adivinhações por sorte.

Também é possível usar [*técnicas mnemônicas*](/pt/glossary#Mnemonic_device) tradicionais como acrônimos ou abreviações para memorizar senhas, transformando frases longas em palavras complexas, aparentemente randômicas: 

  * 'Um casal são duas pessoas, verdade?' torna-se '1C=2p,VDD?'
  * 'Você está feliz hoje?' torna-se 'VCt@flzHJ?'
  * Para termos em inglês, 'To be or not to be? That is the question' torna-se '2Bon2B?TitQ' 

Esses são apenas alguns exemplos. Crie o seu próprio método de codificar palavras e frases para torná-las ao mesmo tempo complexas e memoráveis, pois mesmo um esforço mínimo nessa direção gera grandes resultados.

Aumentar a extensão do segredo com apenas algumas letras, ou adicionar números e caracteres especiais à combinação a torna muito mais difícil de ser quebrada. Na tabela abaixo, vemos um exemplo de como o tempo para quebrá-la aumenta absurdamente conforme se torna cada vez mais complexa.

<table border="1">
    <tbody align="center">
        <tr>
            <th rowspan="2">Exemplo de senha</th>
            <th colspan="3">Tempo para quebrar usando um computador...</th>
        </tr>
        <tr>
            <th>comum</th>
            <th>dedicado</th>
            <th>para investigação de crimes</th>
        </tr>
        <tr>
            <td>bananas</td>
            <td>Menos de 1 dia</td>
            <td>Menos de 1 dia</td>
            <td>Menos de 1 dia</td>
        </tr>
        <tr>
            <td>bananalimonada</td>
            <td>Menos de 1 dia</td>
            <td>Menos de 1 dia</td>
            <td>Menos de 1 dia</td>
        </tr>
        <tr>
            <td>BananaLimonada</td>
            <td>2 dias</td>
            <td>Menos de 1 dia</td>
            <td>Menos de 1 dia</td>
        </tr>
        <tr>
            <td>B4n4n4L1m0n4d4</td>
            <td>1 década, 7 anos</td>
            <td>1 ano, 9 meses</td>
            <td>1 mês, 26 dias</td>
        </tr>
        <tr>
            <td>Nao Temos Bananas</td>
            <td>1215520 séculos</td>
            <td>121552 séculos</td>
            <td>12155 séculos</td>
        </tr>
        <tr>
            <td>Não T3m05 B4n4n45</td>
            <td>36531016477 séculos</td>
            <td>3653101648 séculos</td>
            <td>365310165 séculos</td>
        </tr>
        <tr>
            <td colspan="4">Obs.: valores para senha WPA em Julho de 2014. Fonte: https://passfault.appspot.com/password_strength.html</td>
        </tr>
    </tbody>
</table>



O tempo para quebrar qualquer uma das combinações acima varia muito dependendo da natureza do ataque e dos recursos disponíveis para quem o realiza. Vale lembrar que novos métodos são desenvolvidos constantemente. Ainda assim, a tabela cumpre o papel de demonstrar como as senhas se tornam muito mais difíceis de serem descobertas simplesmente ao variar caracteres, usar duas palavras ou, ainda melhor, uma frase curta.

A tabela acima se baseia nos cálculos do [Passfault](https://passfault.appspot.com/password_strength.html), um dos vários sites que permitem testar a força de combinações. Embora tais ferramentas sejam úteis para demonstrar a eficiência de diferentes tipos de senhas, evite informar uma que você realmente use nesses sites.


### Como armazenar senhas de forma segura ###

Embora um pouco de imaginação ajude a recordar todas as senhas, ter de trocá-las periodicamente significa que a criatividade pode acabar um dia. Uma alternativa é gerar combinações aleatórias para a maioria das contas ou serviços e simplesmente abandonar a ideia de lembrá-las. Em troca, elas seriam guardadas em um [*banco de dados seguro de senhas*](/pt/glossary#Secure_password_database) portátil e criptografado, como o [*KeePass*](/pt/glossary#KeePass).

<div class="getstarted" markdown="1">
Guia Prático: saiba usar o [***KeePass - Armazenamento Seguro de Senhas***](/pt/keepass_main)
</div>

Usar esse método torna particularmente importante criar e lembrar um segredo seguro para o [*KeePass*](/pt/glossary#KeePass) ou qualquer outra ferramenta similar. Sempre que precisar entrar em uma conta específica, basta acessá-lo usando apenas uma senha mestre, o que facilita muito os procedimentos descritos acima. O [*KeePass*](/pt/glossary#KeePass) também é portátil: você pode levar sua base de dados em um pen drive ou cartão USB, caso precise acessá-la quando estiver longe do computador principal.

Embora seja, provavelmente, a melhor opção para quem mantém muitas contas, há algumas desvantagens nesse método. 

Primeiro, se você perder ou apagar de forma acidental a sua única cópia do banco de dados de senhas, não terá mais acesso a nenhuma das contas. Torna-se extremamente importante ter cópias reserva (backup) dessa base do [*KeePass*](/pt/glossary#KeePass). Veja o [***Capítulo 5: Como se recuperar da perda de informações***](/pt/chapter-5) para saber mais sobre estratégias de backup. Felizmente, o fato de o banco de dados ser criptografado significa que você não precisa entrar em pânico caso perca cópias de reserva armazenadas em pen drives ou outros dispositivos.

A segunda grande desvantagem é ainda mais importante. Se você esquecer a senha mestre do [*KeePass*](/pt/glossary#KeePass), não há como recuperá-la, assim como não haveria como acessar o conteúdo do banco de dados de senhas. Assim, escolha uma senha mestre que seja tanto segura como fácil de lembrar!

A força desse método pode, em algumas ocasiões, ser a própria fraqueza. Se uma pessoa for forçada a revelar a senha mestre do KeePass, abrirá o acesso a todas as combinações armazenadas na base de dados. Caso essa seja uma situação que você vê como possível de enfrentar, pense em considerar seu banco de dados do KeePass como um arquivo sensível, protegendo-o como descrito no [***Capítulo 4: Como proteger os arquivos sensíveis do seu computador***](/pt/chapter-4). Você também pode criar uma base do KeePass separada, contendo senhas que protejam informações mais sensíveis, e ter cuidado extra com ela.

<div class="background" markdown="1">
Mansour: Espera um pouco. Se o KeePass usa só uma senha mestre para proteger todas as outras, como pode ser mais seguro do que usar a mesma senha para todas as contas? Quero dizer, se alguém mal intencionado aprende a senha mestre, acessa todo o resto, não?

Magda: É uma boa pergunta. Você está certo que proteger sua senha mestre é realmente importante, mas há algumas diferenças fundamentais. Primeiro, esse 'alguém mal intencionado' não precisaria apenas da sua senha, mas de sua base de dados, enquanto se você usar o mesmo segredo em todas as contas, apenas ele seria necessário. Além disso, sabemos que o KeePass é extremamente seguro. Bom, não se pode dizer o mesmo de todos os programas e sites. Alguns são bem menos protegidos do que outros, e você não quer que alguém invada um site e use o que aprendeu ali para entrar em contas mais confiáveis. E tem mais uma coisa. O KeePass permite trocar a senha mestre de forma bem fácil caso ache necessário. Queria eu ter essa sorte! Passei o dia todo atualizando minhas senhas.
</div>

