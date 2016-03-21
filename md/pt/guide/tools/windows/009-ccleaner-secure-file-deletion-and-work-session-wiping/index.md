

---

lang: pt
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 009
title: CCleaner - Secure File Deletion and Work Session Wiping

---

**Site**


[**www.ccleaner.com**](http://www.ccleaner.com)

**Esta ferramenta requer**

  * Qualquer versão do Windows

**Versão usada para este guia**

  * 4.15

**Licença de uso**

  * Freeware

**Última revisão deste capítulo**

  * Agosto de 2014

**Leitura requerida**

Capítulo [**6. Como destruir informações sensíveis**](/pt/chapter-6), do **Guia de Referência**.

**Nível**: 1: Iniciante, 2: **Médio**, 3: Intermediário, 4: Experiente, 5: Avançado

**Tempo necessário para começar a usar essa ferramenta**: 15 minutos

**O que você pode fazer com o programa**:

  * Remover permanentemente rastros de suas atividades e os arquivos temporários armazenados no seu computador.
  * Liberar espaço livre em discos conectados ao computador.
  * Limpar o **Registro do Windows**.
  * Controlar quais programas são iniciados junto com o computador.

**GNU Linux, Mac OS e outros programas compatíveis para Windows:**


Outro programa excelente para a remoção de arquivos temporários e/ou remoção segura, compatível com **GNU Linux** e **Microsoft Windows** é o [**BleachBit**](http://bleachbit.sourceforge.net/). O **BleachBit** permite limpar os arquivos temporários de 70 dos aplicativos mais populares, limpar arquivos temporários do Sistema Operacional e liberar espaço no disco rígido. Programa de código aberto com uma versão portátil, o **BleachBit** está disponível em 32 línguas.

Quem usa **Ubuntu Linux** também podem dar uma lida no guia [**Cleaning up all those unnecessary junk files…**](http://ubuntuforums.org/showthread.php?t=140920), em inglês, para saber mais sobre como limpar o sistema.

Quem usa **Mac OS** vai gostar das ferramentas gratuitas das empresas [**Titanium’s Software**, **OnyX** e **Maintenance**](http://www.titanium.free.fr/), que apagam vestígios da sessão de trabalho. Para limpar o *Lixo* de forma segura, abra o menu do *Finder* e **selecione** *Finder > Esvaziamento Seguro do Lixo*. Para que a limpeza da *Lixeira* seja feita sempre de forma segura, **selecione** *Finder > Preferências* e **clique** na aba *Avançado*. Depois, **marque** a opção *Esvaziar lixo com segurança*.


## 1.1 O que você precisa saber sobre a ferramenta antes de começar ##


Por padrão, as configurações do sistema operacional ou de navegadores de internet coletam e criam automaticamente um rastro de dados, que alguém com más intenções pode seguir - não muito diferente de um caçador seguindo uma presa.

Sempre que usamos um navegador de internet, processadores de texto ou outros programas, arquivos e dados temporários são gerados e ficam armazenados no sistema. O mesmo pode acontecer com listas de documentos vistos recentemente ou páginas visitadas na rede. Por exemplo, sempre que você digita um endereço no navegador, uma lista dos sites que começam com as mesmas letras pode ser exibida dessa maneira:

![](/sbox/screen/ccleaner-pt/00.png)

*Figura 1: A barra de endereços de um navegador mostrando diferentes URLs.*

Embora históricos de navegação sejam convenientes, também permitem a alguém identificar as páginas que você visitou. Além disso, suas atividades recentes podem ser expostas por dados temporários coletados de imagens que aparecem nesses sites, incluindo mensagens de e-mail ou outras informações digitadas em formulários da rede.

Se você fosse remover os dados temporários criados toda vez que usasse um programa, teria que abrir o diretório de cada aplicativo individualmente, identificar e remover manualmente os arquivos temporários de lá. O **CCleaner** simplifica essa tarefa exibindo uma lista de programas e deixando você escolher de quais deles devem ser removidos os arquivos temporários.

**Observação importante**: Embora o **CCleaner** só apague arquivos temporários, e não os próprios documentos salvos no computador, é **altamente recomendado** que você mantenha uma cópia de reserva atualizada (backup) de seus documentos (por favor veja o capítulo [**5. Como se recuperar da perda de informações**](/pt/chapter-5) do **Guia de Referência**).

Depois de executar o **CCleaner** você pode perder todo o histórico relacionado à navegação e a documentos recentes, assim como senhas salvas. No entanto, esse é *precisamente* o objetivo dessa ferramenta - minimizar as diferentes formas de infectar ou monitorar o sistema de seu computador.

