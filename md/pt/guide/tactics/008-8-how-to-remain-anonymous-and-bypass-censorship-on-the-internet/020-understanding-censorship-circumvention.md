

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

Se não é possível acessar um site de forma direta pois ele está bloqueado por um dos métodos discutidos acima, é preciso encontrar uma forma de contornar a obstrução. Um servidor seguro que atue como intermediário (ou [*proxy*](/pt/glossary#Proxy)), localizado em um país que não filtre a internet, pode possibilitar esse tipo de desvio, acessando as páginas que você quer e as entregando para você. De perspectiva do seu [*provedor de internet*](/pt/glossary#ISP), vai parecer que você está se comunicando de forma segura com um computador desconhecido (o servidor [*proxy*](/pt/glossary#Proxy)), em algum lugar da rede.

![](/sites/securitybkp.ngoinabox.org/security/files/img/2-en.png)

Claro, a agência governamental a cargo da censura da internet no seu país (ou mesmo a empresa que fornece atualizações para o software de filtragem dela) podem eventualmente descobrir que este 'computador desconhecido' é na verdade um [*proxy*](/pt/glossary#Proxy) de circunvenção. Caso isso aconteça, o [*endereço de IP*](/pt/glossary#IP_address) daquele servidor pode ser adicionado à [*lista negra*](/pt/glossary#Blacklist) e não vai mais funcionar. Porém, costuma levar um tempo até que os [*proxies*](/pt/glossary#Proxy) sejam bloqueados, e as pessoas que criam e atualizam as ferramentas de contorno à censura estão bastante cientes da ameaça. Elas costumam contra-atacar com um dos ou ambos os seguintes métodos:

  * **Proxies escondidos** são mais difíceis de identificar. Este é um dos motivos porque é importante usar [*proxies*](/pt/glossary#Proxy) seguros, que tendem a ser menos óbvios. Porém, a [*criptografia*](/pt/glossary#Encryption) é apenas parte da solução. Os operadores de um [*proxy*](/pt/glossary#Proxy) também devem ter cuidado ao revelar sua localização a pessoas novas se querem permanecer ocultos.

  * **Proxies descartáveis** podem ser substituídos rapidamente após serem bloqueados. Neste caso, o processo de dizer às pessoas como achar os [*proxies*](/pt/glossary#Proxy) substitutos pode não ser particularmente seguro. Em vez disso, as ferramentas de circunvenção desse tipo costumam tentar distribuir novos [*proxies*](/pt/glossary#Proxy) mais rápido do que os endereços são bloqueados.
  
No fim, desde que seja possível usar um [*proxy*](/pt/glossary#Proxy) confiável para acessar os serviços que você precisa, basta fazer as requisições e ver o que retorna usando o aplicativo de internet apropriado. Tipicamente, os detalhes desse procedimento são processados de forma automática pelo programa de circunvenção que você esteja usando, modificando as configurações do navegador de internet ou apontando o navegador para uma página online de [*proxies*](/pt/glossary#Proxy). A rede de anonimato [*Tor*](/pt/glossary#Tor), descrita abaixo, usa o primeiro método. Em seguida, há uma discussão sobre as ferramentas simples de contorno à censura, de [*proxy*](/pt/glossary#Proxy) único, as quais funcionam uma um pouco diferente da outra.

