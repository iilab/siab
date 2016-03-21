

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

O problema de ter um cofre em casa ou no ambiente de trabalho - e, por que não, de carregar um no bolso - é que sua presença ali é óbvia. Muitas pessoas ficam preocupadas de serem incriminadas por usar [*criptografia*](/pt/glossary#Encryption) e o fato de que os motivos legítimos para [*criptografar*](/pt/glossary#Encryption) informações são mais numerosos do que os ilegítimos não torna essa ameaça menos real. Essencialmente, há duas razões pelas quais você pode recear usar uma ferramenta como o [*TrueCrypt*](/pt/glossary#TrueCrypt): o risco de autoincriminação e o risco de expor claramente onde estão suas informações mais sensíveis.


### Sobre o risco de autoincriminação ###

A [*criptografia*](/pt/glossary#Encryption) é ilegal em alguns países, o que significa que os atos de baixar, instalar ou usar programas dessa natureza podem ser considerados crimes. Além disso, se dentre os grupos dos quais você quer proteger suas informações estiver a polícia, as forças militares ou os serviços de inteligência, violar essas leis pode fornecer um pretexto para que suas atividades sejam investigadas ou haja perseguição à sua organização.

Na verdade, ameaças assim podem sequer estar relacionadas à legalidade das ferramentas em questão. Onde quer que a mera associação a algum software de [*criptografia*](/pt/glossary#Encryption) seja suficiente para expor alguém a acusações de atividades criminosas ou espionagem (independentemente do conteúdo real contido nos volumes [*criptografados*](/pt/glossary#Encryption)), é melhor pensar com cuidado se tais ferramentas são apropriadas ao seu contexto.

Se esse for o seu caso, há algumas opções:

  * Você pode evitar completamente o uso de programas de segurança de informação, o que implica guardar apenas informações não confidenciais ou inventar um sistema de palavras de código para proteger os elementos principais de arquivos mais sensíveis.
  * Você pode usar uma técnica chamada [*esteganografia*](/pt/glossary#Steganography) para ocultar informações sensíveis, em vez de criptografá-las. Há ferramentas que podem ajudar nesse processo, mas usá-las da forma correta requer uma preparação bastante cuidadosa e você ainda correrá o risco de autoincriminação caso alguém saiba qual software foi usado.
  * Você pode tentar guardar todas as informações sensíveis em uma conta segura de e-mail, mas isso depende de uma conexão confiável e de um conhecimento relativamente sofisticado sobre computadores e serviços de internet. Essa técnica pressupõe que a [*criptografia*](/pt/glossary#Encryption) de rede seja menos incriminatória do que a de arquivos, e que você terá como evitar copiar dados sensíveis de forma acidental para o computador e esquecê-los ali.
  * Você pode manter as informações sensíveis fora do computador, guardando-as em um pen drive ou HD externo. Porém, tais dispositivos costumam ser ainda mais vulneráveis do que computadores à perda e confisco. Carregar dados importantes e não criptografados por aí costuma ser uma má ideia.
	
Se preciso, é possível usar um pouco de cada tática. Entretanto, mesmo em situações nas quais você se preocupe com a questão da autoincriminação, pode ser mais seguro usar o [*TrueCrypt*](/pt/glossary#TrueCrypt) e tentar disfarçar o volume [*criptografado*](/pt/glossary#Encryption) da melhor forma possível.

Para deixar um volume criptografado menos óbvio, é possível renomeá-lo de forma a camuflá-lo como um arquivo comum. A extensão '.iso', usada para imagens de CD, é uma boa opção para volumes que tenham cerca de 700 MB. Para volumes menores, outras extensões apresentariam maior verossimilhança. Seria como esconder o cofre atrás de um quadro na parede do escritório: pode não funcionar em inspeções rigorosas, mas ainda assim oferece algum tipo de proteção. Também é possível renomear o próprio programa [*TrueCrypt*](/pt/glossary#TrueCrypt), assumindo que você o tenha guardado no pen drive ou disco rígido como um arquivo comum, em vez de instalá-lo como um programa. O [***Guia Prático do TrueCrypt***](/pt/truecrypt_main) mostra como fazer isso.


### Sobre o risco de expor onde estão as informações sensíveis ###

Frequentemente, o problema de 'descobrirem' programas de [*criptografia*](/pt/glossary#Encryption) em seu computador ou pen drive é menor do que o fato de que um volume criptografado indica exatamente onde as informações mais importantes ficam guardadas. Embora seja verdade que ninguém mais pode lê-las, um intruso saberá que estão ali e que você tomou precauções para protegê-las. Isso te expõe a vários métodos não técnicos pelos quais alguém pode tentar ganhar acesso àqueles dados, como intimidação, chantagem, interrogatório e tortura. É nesse contexto que a função de negação do [*TrueCrypt*](/pt/glossary#TrueCrypt), discutida com mais detalhes abaixo, torna-se importante.

A função de 'negação' do [*TrueCrypt*](/pt/glossary#TrueCrypt) é um dos motivos pelos quais esta ferramenta de [*criptografia*](/pt/glossary#Encryption) de arquivos difere das outras. Ela pode ser vista como uma forma peculiar de [*esteganografia*](/pt/glossary#Steganography), que disfarça as informações mais sensíveis, ocultas, com outras menos importantes. Seria o equivalente a instalar um discreto 'botão falso' dentro do não tão discreto cofre do escritório. Caso alguém roube a chave ou te intimide a fornecer a combinação do cofre, encontrará um material de 'isca' convincente, mas não os dados que você realmente quer proteger.

Apenas você sabe que o cofre possui um compartimento secreto nos fundos. Isso te permite 'negar' que há mais segredos além dos já fornecidos e pode ajudar em situações nas quais te obriguem a revelar sua senha por qualquer motivo. Tais motivos podem incluir ameaças legais ou físicas à sua segurança, ou à de pessoas que você conhece, como sócios ou familiares. O objetivo da negação é ganhar uma chance de escapar de uma situação potencialmente perigosa, mesmo que você opte por continuar a proteger seus dados. Porém, como discutido na seção [***Sobre o risco de autoincriminação***](/pt/chapter_4_2), essa função torna-se bem menos útil se o mero ato de ser pego com um cofre no escritório for suficiente para levar a consequências inaceitáveis.

A função de negação do [*TrueCrypt*](/pt/glossary#TrueCrypt) cria um 'volume oculto' dentro do volume [*criptografado*](/pt/glossary#Encryption) comum. É possível abri-lo com uma senha diferente da que seria usada normalmente. Mesmo que alguém com conhecimento técnico sofisticado ganhe acesso ao volume padrão, será incapaz de provar que há um volume oculto. Claro, tal pessoa pode saber que o [*TrueCrypt*](/pt/glossary#TrueCrypt) é capaz de ocultar informações dessa forma, então não há garantias de que as ameaças cessarão assim que a senha de isca seja revelada. Porém, muitas pessoas usam o [*TrueCrypt*](/pt/glossary#TrueCrypt) sem habilitar a função de negação e é geralmente considerado impossível determinar, por análise, se determinado volume [*criptografado*](/pt/glossary#Encryption) contém esse tipo de 'botão falso'.

Dito isso, cabe a você não revelar o volume oculto por modos menos técnicos, como ao deixá-lo aberto ou permitir que outros programas criem atalhos para arquivos contidos ali. A seção [***Leitura extra***](/pt/chapter_4_3), abaixo, traz mais referências sobre isso.

<div class="background" markdown="1">
Claudia: Certo! Vamos então deixar umas tralhas no volume padrão. Aí podemos mover todos os nossos depoimentos para o volume oculto. Você tem alguns PDFs antigos ou outras coisas que possamos usar?

Pablo: Eu estava pensando sobre isso. Veja, a ideia é entregar a senha de isca caso não tenhamos escolha, não é? Só que, para isso ser convincente, precisamos usar arquivos que pareçam importantes, não te parece? Senão, por que teríamos nos dado o trabalho de criptografá-los? Talvez devamos usar alguns documentos financeiros não relacionados ao caso, uma lista de senhas de sites ou algo assim.
</div>

