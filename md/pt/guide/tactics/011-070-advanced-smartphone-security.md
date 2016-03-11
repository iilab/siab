

---

lang: pt
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## Obtenha acesso integral ao seu smartphone ##

A maioria dos smartphones é capaz de fazer mais coisas do que os sistemas operacionais que vêm instalados, firmware de fabricantes e programas feitos pelas operadoras de telefonia permitem. Além disso, algumas funcionalidades vêm 'travadas', de modo a não poderem ser controladas ou alteradas, permanecendo fora de alcance.

Em muitos casos, tais funcionalidades são desnecessárias às pessoas que usam o smartphone. Entretanto, há aplicativos e funções que podem aumentar a segurança dos dados e das comunicações em um aparelho. Também há outras, existentes, que podem ser removidas para evitar riscos de segurança.

Por esses e outros motivos, algumas pessoas preferem manipular os diversos software e firmware que rodam em seus smartphones, de modo a ganhar os devidos privilégios de acesso que as permitem instalar determinadas funcionalidades ou remover/reduzir outras.

O processo de sobrepujar os limites impostos pelas operadoras de telefonia móvel ou fabricantes dos sistemas operacionais de um smartphone é chamado de *rooting*, em dispositivos Android, e *jailbreaking*, no caso de aparelhos iOS como o iPhone ou o iPad. Um processo bem sucedido de *rooting* ou *jailbreaking* resultará em obter todos os privilégios necessários para a instalação e uso de aplicações extras, modificação de configurações bloqueadas e controle total sobre o armazenamento de dados e memória do aparelho.

**AVISO**: O processo de *rooting* ou *jailbreaking* pode não ser reversível e requer experiência com a instalação e configuração de software. Considere o seguinte:

  * Existe o risco de tornar seu smartphone inoperante de forma permanente, ou de transformá-lo em um peso morto;
  * A garantia fornecida pelo fabricante ou operadora de telefonia pode ser invalidada;
  * Em alguns lugares, o processo pode ser ilegal.

Mas se você tiver cuidado, esta é uma forma direta de obter mais controle sobre o seu smartphone para deixá-lo mais seguro.


### Firmware alternativo ###

O termo 'firmware' refere-se a programas intimamente ligados a um dispositivo particular. Cooperam com o sistema operacional e são responsáveis por operações básicas de hardware, como o funcionamento de alto falantes, microfone, câmera, tela sensível ao toque, memória, antenas etc.

Se você tem um celular Android, pode considerar instalar firmware alternativos para ganhar mais controle sobre o aparelho. Observe que para instalá-los, é preciso fazer o processo de *rooting* do telefone.

Um exemplo de firmware alternativo para um celular Android é o [**Cyanogenmod**](http://www.cyanogenmod.com), que permite, por exemplo, desinstalar aplicativos de sistema do telefone, como é o caso dos instalados pelo fabricante ou pela operadora. Ao fazê-lo, é possível reduzir as formas pelas quais o dispositivo pode ser monitorado, como os dados enviados à operadora sem o seu conhecimento.

Além disso, o Cyanogenmod vêm por padrão com um aplicativo de OpenVPN, o que pode ser tedioso de instalar manualmente. As Redes Virtuais Privadas, ou VPN, são uma das formas seguras de desviar sua comunicação de internet por proxies (veja abaixo). 

O Cyanogenmod também oferece a possibilidade de navegação no modo incógnito, na qual o histórico não fica registrado no smartphone, além de várias outras funcionalidades. Porém, não pode ser instalado em todos os aparelhos Android. Antes de experimentá-lo, veja a [lista de dispositivos suportados](http://www.cyanogenmod.com/devices).
 
 
### Criptografia de volumes inteiros ###

Caso o seu telefone tenha passado pelo processo de *rooting*, você pode considerar criptografar todo o armazenamento de dados ou mesmo criar um volume criptografado no smartphone para proteger algumas informações.

O [**Luks Manager**](https://play.google.com/store/apps/details?id=com.nemesis2.luksmanager&hl=en) possibilita a criptografia fácil e robusta de volumes com uma interface de uso amigável. Também recomendamos fortemente instalar esta ferramenta antes de começar a guardar dados importantes no aparelho Android, e usar o *Encrypted Volumes*, fornecido pelo Luks Manager, para armazenar todas as suas informações.


### Rede Privada Virtual (Virtual Private Network - VPN) ###

Uma Rede Privada Virtual (VPN) fornece um túnel criptografado pela internet entre o seu dispositivo e um servidor de VPN. O meio é chamado de túnel pois, diferentemente de outros tipos de tráfego criptografado (como o https), esconde todos os serviços, protocolos e conteúdo. Uma conexão de VPN é configurada apenas uma vez e termina apenas quando você quiser.

Note que uma vez que todo o tráfego é direcionado a um proxy ou servidor de VPN, uma determinada pessoa precisa apenas ter acesso ao proxy para analisar suas atividades. Portanto, é importante escolher com muito cuidado qual serviço de proxy ou VPN usar. Também é aconselhável variar entre proxies e/ou VPNs diferentes, pois distribuir os fluxos de dados reduz o impacto em casos de serviços comprometidos.

Recomendamos usar o servidor [**RiseUp VPN**](https://help.riseup.net/en/vpn). É possível usar o RiseUp VPN em sistemas operacionais Android após instalar o Cyanogenmod (veja acima). Também é fácil configurar uma conexão para o RiseUp VPN em aparelhos iPhone - leia mais sobre isso [aqui](https://support.apple.com/kb/HT1424).

