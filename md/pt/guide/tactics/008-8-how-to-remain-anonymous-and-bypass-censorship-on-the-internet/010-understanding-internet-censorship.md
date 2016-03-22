

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

Pesquisas conduzidas por organizações como a [OpenNet Initiative (ONI)](http://opennet.net/) e a [Repórteres Sem Fronteiras (RSF)](http://www.rsf.org/) indicam que muitos países filtram uma grande variedade de conteúdo social, político e 'de segurança nacional', embora raramente publiquem listas precisas do que está sendo bloqueado. Naturalmente, os governos interessados em controlar o acesso da população à internet também fazem esforços especiais para bloquear serviços conhecidos de [*proxies*](/pt/glossary#Proxy), assim como sites que ofereçam ferramentas ou instruções que ajudem a contornar tais filtros.

Apesar da garantia de livre acesso à informação contemplada no Artigo 19 da Declaração Universal dos Direitos Humanos, o número de países adeptos da censura à internet continuou a aumentar dramaticamente nos últimos anos. Porém, conforme a prática se espalha pelo mundo, também se difundem as ferramentas de [*circunvenção*](/pt/glossary#Circumvention) criadas, usadas e publicizadas por ativistas, programadores e voluntários.

Antes de explorar as várias formas de contornar a censura à internet, é preciso ter um conhecimento básico de como funcionam os filtros de conteúdo. Para tal, pode ser útil considerar um modelo bastante simplificado de sua conexão à rede mundial de computadores.

### A sua conexão de internet ###

![](/sites/securitybkp.ngoinabox.org/security/files/img/1-en.png)

O primeiro passo na sua conexão de internet tipicamente é feito por um *Provedor de Serviços de Internet*, ou [*ISP*](/pt/glossary#ISP), na sua casa, escritório, escola, biblioteca, lan house ou internet café. O [*provedor de internet*](/pt/glossary#ISP) atribui ao seu computador um [*endereço de IP*](/pt/glossary#IP_address), o qual é usado por vários serviços da rede para te identificar e para enviar a você informações como e-mails ou as páginas na qual queira entrar. Qualquer pessoa que saiba seu [*endereço de IP*](/pt/glossary#IP_address) pode descobrir a cidade onde você está. Algumas organizações bem conectadas em seu país, entretanto, podem usar esta informação para determinar sua localização exata.

  * O **provedor de internet** sabe em qual casa ou edifício você está e qual linha telefônica está sendo usada, caso a internet esteja sendo acessada por um modem.
  * O seu **escritório, lan house, internet café ou biblioteca** sabem qual computador você estava usando em determinado momento, assim como a qual porta ou ponto de acesso sem fio seu computador estava conectado.
  * As **agências governamentais** podem saber todos esses detalhes como resultado da influência que exercem nas organizações acima.

Neste ponto, o [*provedor de internet*](/pt/glossary#ISP) usa a infraestrututa de rede do seu país para conectar as pessoas, inclusive você, ao resto do mundo. Na outra ponta da conexão, o site ou serviço de internet que você está acessando passou por um processo similar, tendo recebido seu próprio [*endereço de IP*](/pt/glossary#IP_address) de um [*provedor de serviços de internet (ISP)*](/pt/glossary#ISP) em seu país de origem. Mesmo sem todos os detalhes técnicos, um modelo básico como este pode ser útil ao considerar as várias ferramentas que permitem contornar filtros de conteúdo e manter o anonimato na internet.


### Como os sites são bloqueados ###

De um modo geral, quando você abre uma página online, está mostrando o [*endereço de IP*](/pt/glossary#IP_address) daquela página ao seu [*provedor de internet*](/pt/glossary#ISP) e pedindo a ele que faça uma conexão com o [*provedor de internet*](/pt/glossary#ISP) da página. Se você possui uma conexão sem filtros, é exatamente isso o que vai acontecer. Porém, se está em um país onde haja censura à internet, o provedor vai primeiro consultar uma [*lista negra*](/pt/glossary#Blacklist) de sites proibidos para então decidir se atenderá ou não ao seu pedido. Em alguns casos, pode haver uma organização central que lida com os filtros no lugar dos [*provedores de internet*](/pt/glossary#ISP).

É comum às [*listas negras*](/pt/glossary#Blacklist) conterem [*nomes de domínio*](/pt/glossary#Domain_names) (por exemplo, www.blogger.com), em vez dos respectivos [*endereços de IP*](/pt/glossary#IP_addresses) daquele serviço. Em alguns países, os programas de filtragem monitoram a sua conexão em vez de tentar bloquear endereços específicos de internet. Tal tipo de software 'lê' os pedidos que você faz sobre as páginas que quer acessar, assim como as páginas que aparecem para você, em busca de palavras chave sensíveis e então decide se te deixa ver ou não o conteúdo delas.

Para piorar as coisas, quando uma página é bloqueada, pode ser que você nem saiba que isso aconteceu. Enquanto alguns filtros exibem uma 'página de bloqueio', explicando porque ela foi censurada, outros mostram mensagens de erro enganosas. Tais mensagens podem dar a entender que a página não foi encontrada ou que o endereço foi digitado errado, por exemplo.

Em geral, é mais fácil considerar sempre o pior cenário no que se refere à censura de internet, em vez de tentar pesquisar sobre todas as forças e fraquezas particulares das tecnologias de filtragem ativas em seu país. Em outras palavras, assuma sempre que:

  * O seu tráfego de internet é monitorado por palavras chave;
  * O filtro está implementado diretamente no nível do [*provedor de serviços de internet*](/pt/glossary#ISP);
  * Os sites bloqueados constam em uma [*lista negra*](/pt/glossary#Blacklist) tanto pelo [*endereço de IP*](/pt/glossary#IP_address) como pelo [*nome de domínio*](/pt/glossary#Domain_name);
  * Você receberá um motivo incerto como explicação sobre o porquê uma página não pode ser acessada.

Uma vez que as ferramentas mais eficazes de contorno à censura podem ser usadas independentemente de quais métodos de filtragem estejam ativos, não costuma fazer mal adotar uma postura pessimista.

<div class="background" markdown="1">
Mansour: Então, se eu descobrir um dia que não posso mais acessar o blog, mas uma amiga de outro país ainda conseguir vê-lo perfeitamente, pode ser que o governo o tenha bloqueado?

Magda: Não necessariamente. Pode ser um problema que afeta apenas as pessoas que tentam acessar o site daqui, ou no seu computador e que aparece apenas em algumas páginas da rede. Mas você está no caminho certo. Tente visitar o seu endereço usando uma ferramenta de contorno à censura. Afinal, a maioria delas usa servidores externos como ponte, o que é mais ou menos como pedir a um amigo de outro país para testar um site, exceto que você mesmo faria a checagem.
</div>

