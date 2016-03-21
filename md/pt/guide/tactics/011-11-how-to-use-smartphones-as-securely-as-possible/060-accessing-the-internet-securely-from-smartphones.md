

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

Conforme discutido no [***Capítulo 7: Como manter sua comunicação por internet segura***](/pt/chapter-7) e no [***Capítulo 8: Como manter o anonimato e contornar a censura na internet***](/pt/chapter-8), o acesso a conteúdos da internet, ou a publicação de material online como fotos e vídeos, deixa muitos rastros sobre quem é você, onde estava e o que estava fazendo. Isso pode te colocar em risco. Usar um smartphone para entrar na internet aumenta este risco.

### Acesso por WiFi ou conexão de dados ###

Os smartphones permitem escolher a forma de entrar na internet. Pode ser via uma conexão sem fio (WiFi) fornecida por um ponto de acesso, como acontece em um Internet Café; ou via uma conexão de dados, como GPRS, EDGE ou UMTS, fornecida pela operadora de telefonia celular.

Usar o WiFi reduz os rastros de dados que você deixará para a operadora de telefonia móvel ao não relacionar sua conexão a uma conta de telefone. Entretanto, às vezes a única forma de entrar online é uma conexão de dados. Infelizmente, os protocolos de conexão de dados para celulares (como o EDGE ou o UMTS) não são abertos, o que significa que desenvolvedores independentes e engenheiros de segurança não podem examiná-los para ver como são implementados pelas operadoras.

Em alguns países, as operadoras de telefonia móvel operam sob uma legislação diferente da dos provedores de internet, o que pode resultar em uma vigilância mais direta por governos ou das próprias empresas.

Mas seja qual for o caminho escolhido para sua comunicação digital com smartphones, os riscos de exposição de dados podem ser reduzidos pelo uso de ferramentas de anonimato e criptografia.


### Anonimato ###

Para acessar conteúdo online de forma anônima, é possível usar um aplicativo de Android chamado [**Orbot**](https://www.torproject.org/docs/android.html.en), que canaliza a comunicação por internet pela rede de anonimato Tor.

<div class=getstarted markdown=1>
Guia Prático - saiba usar o [*Orbot*](/pt/Orbot_main)
</div>

Outro aplicativo, o Orweb, é um navegador de internet com funcionalidades de aumento de privacidade, como a possibilidade de usar [*proxies*](/pt/glossary#Proxies) e não manter um histórico local de navegação. Juntos, o Orbot e o Orweb podem contornar filtros e firewalls de redes, assim como possibilitar a navegação anônima.

<div class=getstarted markdown=1>
Guia Prático - saiba usar o [*Orweb*](/pt/Orweb_main)
</div>


### Proxies ###

A versão para smartphones do [*Firefox*](/pt/glossary#Firefox), o [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox), pode ser equipada com complementos de proxy. O tráfego é direcionado para um servidor intermediário e, de lá, segue para o site que você quer acessar. Isso é útil em locais onde haja censura, mas ainda pode revelar as requisições de endereço - a menos que a conexão de seu cliente para o proxy seja criptografada. Recomendamos o complemento chamado [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/) (também do [**Guardian Project**](https://guardianproject.info/)), que facilita todo o processo. Esta também é a única forma de canalizar as comunicações do Firefox mobile para o Orbot e usar a rede de anonimato [*Tor*](/pt/glossary#Tor).

