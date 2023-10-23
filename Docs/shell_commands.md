---
title: Shell
tags:
  - programação
  - studies
use: Documentation
languages: Bash, Shell
dependences:
---
#to_review  #to_translate 

<details><summary>Table of Contents 🔖</summary>

- [Shell](#shell)
  - [Comandos shell](#comandos-shell)
  - [Atalhos](#atalhos)
  - [COMANDOS PARA MANIPULAÇÃO DE ARQUIVOS E TEXTOS E COMANDOS DE REDIRECIONAMENTO](#comandos-para-manipulação-de-arquivos-e-textos-e-comandos-de-redirecionamento)
  - [Obtendo as informações de um arquivo em outro arquivo:](#obtendo-as-informações-de-um-arquivo-em-outro-arquivo)
  - [DIRETÓRIOS DO LINUX E COMANDOS DE SISTEMA](#diretórios-do-linux-e-comandos-de-sistema)
  - [Fundamentos de Rede e Comandos Avançados:](#fundamentos-de-rede-e-comandos-avançados)
  - [COMANDOS TRACEROUTE E FINGER](#comandos-traceroute-e-finger)
  - [COMANDOS DIVERSOS DO LINUX](#comandos-diversos-do-linux)
  - [FAZER EXERCÍCIOS E COLOCAR NUM ARQUIVO PARA EXECUTAR AUTOMATICAMENTE. ](#fazer-exercícios-e-colocar-num-arquivo-para-executar-automaticamente)
  - [Controle de Usuários](#controle-de-usuários)
  - [COMO EXIBIR INFORMAÇÕES DE LOGIN E EXCLUIR USER](#como-exibir-informações-de-login-e-excluir-user)
  - [CONTROLE DE USUÁRIOS - Como criar grupos e gerenciar usuários](#controle-de-usuários---como-criar-grupos-e-gerenciar-usuários)
  - [PERMISSÕES](#permissões)
    - [Servidor para dono|grupo|outros users](#servidor-para-donogrupooutros-users)
  - [(Des)Compactação de Arquivos](#descompactação-de-arquivos)
- [APACHE](#apache)

</details>

---

# Shell
## Comandos shell
  > Autor: Luciano Hugo


`~$ man ls` : Neste caso estamos requisitando o manual do comando ls. Será mostrado informações a respeito do comando ls, e man pode ser utilizado para invocar qualquer outro manual de algum outro comando. </br>
`~$ cd [caminho_para_diretorio]`: Acessa pasta de arquivos de acordo com o caminho passado. </br>
`~$ cd ..`: Retorna para o diretório superior.
`~$ cd ../[caminho_para_diretorio]`: Retrocede e acessa passta de arquivos "irmã". </br>
`~$ history` : Exibe o histórico de todos os comandos digitados no terminal. </br>
`~$ !! `: Executa o último comando aplicado no terminal. </br>
`~$ ![numero_comando_histórico]`: Executa o comando em determinada linha do histórico. </br>
`~$ pwd `: Exibe o caminho ao qual se encontra no terminal. </br>
`~$ clear` : limpa o terminal. </br>
`~$ mv [nome_antigo] [nome_novo]`: Serve para renomear o diretório em questão mas também podemos utilizar para mover o diretório ao caminho determinado. </br>
`~$ cp [arquivo] [caminho_onde_sera_copiado]`: aqui criamos uma cópia de um arquivo ou diretório. </br>
`~$ rm [arquivo]` : Exclui um arquivo. </br>
`~$ rmdir [diretorio]`: Exclui um diretório. </br>
`~$ touch [nome_arquivo.ext]`: Serve para criar arquivos vazios no formato determinado pela extensão pretendida. </br>

## Atalhos
`Ctrl + w` : Apaga última palavra digitada. </br>
`Ctrl + u`: Apaga última linha digitada. </br>
`Ctrl + l` : "Limpa" o histórico de mensagens/comandos.
 
## COMANDOS PARA MANIPULAÇÃO DE ARQUIVOS E TEXTOS E COMANDOS DE REDIRECIONAMENTO
`~$ cat [arquivo]`: exibe as informações internas de um arquivo em ordem padrão. </br>
`~$ tac [arquivo]`: exibe as informações de arquivo em ordem decrescente de linhas. </br>
`~$ head [arquivo]`: exibe somente as 10 primeiras linhas do arquivo. </br>
`~$ tail [arquivo] `: exibe somente as 10 últimas linhas do arquivo. </br>
`~$ nano [arquivo]` : abre um arquivo em modo de edição. </br>

## Obtendo as informações de um arquivo em outro arquivo:
Aqui está a sintaxe que nos permite manipular os textos de um determinado arquivo. </br>
`~$ cat [arquivo] > [outro_arquivo]` : aqui nós conseguimos pegar as informações de um arquivo e inserir dentro de outro arquivo. A sintaxe dessa forma sobrescreve os dados já existentes nos arquivos.

Isso é possível utilizar não somente para textos mas também para comandos que podem ser executados no terminal, como é o exemplo de:

`~$ cal > calendario.txt `: Neste caso a função cal nos traz um calendário do mês corrente, e o mesmo vai para o arquivo calendario.txt. </br>
`~$ date >> calendario.txt` : para que possamos adicionar informações em um arquivo sem sobrescrever as informações já existentes, agora temos o calendário + data e hora dentro do arquivo calendario.txt. </br>
`~$ grep [palavra] [arquivo]` : exibe as linhas onde aparece a palavra que se busca dentro de um determinado arquivo. </br>
`~$ cat calendario.txt | grep Linux` : chamado de pipe essa “barra” é o que permite executar mais de um comando na mesma linha. </br>
`~$ sudo apt update && sudo apt upgrade `: essa é uma alternativa ao pipe, executa o comando de forma consecutiva somente se o primeiro for bem suscedido. </br>
`~$ sudo apt update & sudo apt upgrade` : executa os dois comandos de forma não consecutiva.
`~$ file [arquivo]` : este mostra o tipo de dado que estamos manipulando. </br>
`~$ whatis [comando]` : este mostra o que faz determinado comando. </br>
`~$ find [diretório] -name [arquivo]` : este mostra onde se encontra determinado arquivo.  </br>

## DIRETÓRIOS DO LINUX E COMANDOS DE SISTEMA
`/proc$ cat /proc/cpuinfo | more` : é exibido informações referentes a cpu. </br>
`~$ lscpu | more` : exibe informações relativas a cpu de forma melhor que o comando anterior. </br> 
`/proc$ cat /proc/meminfo | more` : é exibido informações referentes a memória ram. </br>
`~$ lshw | more` : exibe a lista de todos os hardwares encontrados pelo sistema. </br>
`~$ lshw -short` :exibe o caminho de todos os hardwares encontrados pelo sistema de forma. </br>
`~$ w` : exibe os usuários logado no sistema
`~$ lspci` : exibe os drivers conectados. </br>
`~$ lsusb | more` : exibe os dispositivos usb conectados ao sistema. </br>
`~$ arch` : exibe a arquitetura do sistema. </br>
`~$ uname` [atributo]`: exibe o nome da distro que estamos usando e com o atributo -r exibe a versão do sistema. </br>
`~$ free` : exibe informação relacionado ao uso da memória pelo sistema (memória física e virtual). </br>
`~$ du -h dire `: exibe informação do uso relacionado ao uso do hd. </br>
`~$ shutdown -h now` : desliga o computador no exato momento.

## Fundamentos de Rede e Comandos Avançados:

1.	O que é uma rede?
  -	Redes de computadores são o conjunto de equipamentos interligados de maneira a trocarem informações e compartilharem recursos. Cada dispositivo é um nó na rede.

2.	Tipos principais de Redes
    -	**WAN:** Rede de longa distância, segundo vários estudiosos a internet é o melhor exemplo deste tipo de rede.
      -	**MAN:** Rede metropolitana, que conecta várias redes LAN.
        -  **LAN:** Rede que conecta computadores a uma distância curta, permitindo que eles compartilhem dados, arquivos e recursos.

3.	Protocolos:
São linguagens que permitem a comunicação entre os dispositivos dentro de uma rede, de forma que eles consigam se entender. Dentre os vários tipos de protocolos, temos:
    -	**IP - Protocolo de Internet:** Números que identificam o computador em uma rede.
    -	**ICMP - Protocolo de Internet de Controle de Mensagens:** 	Tem objetivo de prover mensagens de controle na comunicação entre nós.
    -	**DNS - Servidor de Nome de Domínios:** Tem por função identificar endereços IPs e manter uma tabela com os endereços dos caminhos de algumas redes.

4.	Comunicação entre os protocolos:
Para que aconteça comunicação entre protocolos é necessário uma interface de rede. 
    -	**Interface de Rede:** Pode ser um software ou hardware que faz a comunicação em uma rede de computadore
      -	**Interface loopback:** É um tipo especial de interface que permite fazer conexões com você mesmo, com ela, você pode testar vários programas de rede sem interferir na sua rede.
    -	No Linux estão localizadas no diretório /dev


COMANDOS:
`~$ ifconfig [parametros]` : Com este comando podemos ver e mudar configurações da interface de rede no dispositivo.Para utilizar este comando precisamos baixar o pacote net-tools. </br>
`~$ hostname [parametros]` : exibe o nome do computador na rede. Com o parâmetro -I podemos visualizar o endereço IP, com o parâmetro -i podemos visualizar o endereço de loopback. </br>
`~$ who ` : Mostra como estamos logados na rede
  -	`~$ who -a`: Mostra todos que estão logados e seu pid, pode ser usado para encerrar o processo com o comando: `~$ kill [pid]` </br>

`~$ whoami`: Como é o nome do usuário que estou logado na rede </br>
`~$ ping [www.endereco.com] [parametros] `: É um utilitário que usa o protocolo ICMP para testar a conectividade enfintre equipamentos. Seu funcionamento consiste em envios de pacotes para o equipamento destino e na “escuta” das respostas. Se o equipamento estiver ativo, uma resposta é retornada ao dispositivo solicitante. </br>
`~$ dig [www.endereco.com]` : Traz informações de DNS

## COMANDOS TRACEROUTE E FINGER
`~$ traceroute [www.site.com]` : Esse comando vai exibir quantos nós existem entre o dispositivo até o site alvo (este comando requer instalação). </br>
`~$ dig [www.endereco.com]  +short`: Traz o número DNS como resposta. </br>
`~$ whois [www.endereco.com.br]` : Nos traz informação a respeiro do site, proprietário, provedor, servidor, email, dentre outras informações. </br>
`~$ finger`: Traz informações a respeito do usuário logado no nosso host. </br>

## COMANDOS DIVERSOS DO LINUX
`~$ history -c` : Apaga todo o histórico do terminal </br>
`~$ alias sd=shutdown` : Dá um nickname a um determinado comando </br>
`~$ nl [nome_arquivo.txt]` : Exibe o conteúdo de um arquivo contando as linhas </br>
`~$ wc [parâmetro]` : Traz o número de linhas de determinado arquivo com parâmetro -l, também possui outras possibilidades de contagens como caracteres, tamanho em bytes, dentre outros. </br>
`~$ sort [parâmetro]` : Este comando faz organização de acordo com o parâmetro selecionado </br>
`~$ last reboot` : Traz informações sobre os últimos reboots do sistema </br>
`~$ route -n `: mostra as tabelas de roteamento do kernel </br>
`~$ time [comando]` : mostra o tempo que é levado para processar determinado comando pelo usuário e pelo sistema </br>
`~$ uptime` : tempo em que o sistema está ligado </br>
`~$ cowsay` : Mostra uma vaquinha falando determinado palavras </br>
`~$ xcowsay` : Mostra uma vaquinha (moderna 3D) falando determinado palavras </br>
`~$ cmatrix` : exibe efeito que nem o do matrix filme, com caracteres caindo </br>
`~$ init 0 ou telnit 0 ou halt` : desliga o computador instantaneamente </br>
`~$ whereis [comando]` : exibe o local e o manual do programa </br>
`~$ which [comando]` : Exibe o caminho de um programa </br>
`~$ seq [parâmetros]` : Exibe uma sequência no terminal </br>


## FAZER EXERCÍCIOS E COLOCAR NUM ARQUIVO PARA EXECUTAR AUTOMATICAMENTE. 
- Gerenciamento de pacotes
- Gerenciadores de pacotes são “facilitadores” do processo de instalação de determinado programa e suas dependências, sendo assim, através deles podemos instalar e remover pacotes no nosso computador através deles a partir do terminal. Dentre os principais temos o apt, dpkg, rpm e yum.

`~$ apt [install/remove] [nome_pacote]` : Instala ou remove um programa a partir do gerenciador de pacotes apt. </br>
`~$ dpkg [parâmetro] [pacote]`: responsável por gerir pacotes debian (.deb). `-i`: Instala pacote; `-r`: remove um pacote; `-I`: Informações do pacote deb. </br>
`~$ yum [install/remove] [nome_pacote]` : Instala ou remove pacotes yum. (verificar distribuição Linux)

## Controle de Usuários 

[Site](https://bellard.org/jlinux) para emular um terminal linux dentre as opções existentes lá

`~$ useradd [nome_user]`: adiciona um usuário, precisa de privilégios elevados ou root.

Podemos adicionar o parâmetro no final para adicionar uma pasta para o mesmo
`~$ su` : Acessa o terminal como usuário root </br>
`~$ passwd [nome_user]` : Muda a senha do usuário (Método ZENIT/POLAR)

## COMO EXIBIR INFORMAÇÕES DE LOGIN E EXCLUIR USER
`~$ lastlog` : Exibe os usuários que já logaram no sistema. </br>
`~$ logname` : Mostra o usuário logado no sistema. </br>
`~$ id `: Exibe os grupos que o usuário faz parte no sistema. </br>
`~$ cat /etc/passwd` : Mostra todos os usuários. </br>
`~$ userdel -r [nome_user]` : Exclui um usuário.

## CONTROLE DE USUÁRIOS - Como criar grupos e gerenciar usuários
`~$ cat /etc/group` : exibe os grupos existentes. </br>
`~$ usermod [-g ou -G] [grupos] [usuário]` : Adicionar ao grupo ou lista de grupos tal usuário. </br> 
`~$ group` : exibe os grupos que o usuário logado faz parte. </br>
`~$ adduser [nomeuser]` : cria um usuário. </br>
`~$ addgroup` : Adiciona um grupo. </br>
`~$ adduser usuario [grupo]` : Adiciona usuário a um grupo. </br>
`~$ gpasswd -a [usuario] [grupo]` : adiciona um usuário a um grupo. </br>
`~$ gpasswd -d [usuario] [grupo]` : remove um usuário de um grupo. </br>
`~$ groupdel [grupo]` : apaga um grupo. </br>


## PERMISSÕES
Permissões dos arquivos são dados em trios relativo a usuário, grupo e outros, sendo as permissões :
`r` (1) - read </br>
`w` (2) - write </br>
`x` (4) - eXecution </br>

### Servidor para dono|grupo|outros users
`~$ ls` -[parâmetro] :
- [lh] exibe os arquivos com data, usuário e permissões
- [letra]* exibe as pastas e conteúdos interno das mesmas
    -	Ao invés de parâmetro podemos colocar uma fragmentos de um arquivo ou diretório de interesse, como por exemplo: 
- `~$ ls u?s*` - Isso implica dizer que o que procuramos na segunda letra não sabemos o que é, apenas a primeira e terceira letras conhecemos.
    -	Podemos também utilizar a seguinte notação para arquivos com mesmo nome mudando apenas a ordem numérica: </br>
      - `~$ ls arquivo[1-3]*` - Aqui juntamos os três arquivos para exibição, em uma pasta, de forma simplificada </br>
      - `~$ ls arquivo[1,3]*` - Aqui juntamos dois arquivo para exibição, em uma pasta, de forma simplificada </br>
      - `~$ ls arquivo[^1-3]*` - O acento circunflexo nega a exibição dos itens, seguindo a mesma lógica dos comando anteriores
- `~$ ls user/home/fulano/p*` - Utilizamos o comando com o final p* para ser exibido todo e qualquer arquivos e diretórios começando com a letra p e o “*” indica que não importa os caracteres que vem a seguir

`~$ chmod [numeros]` : muda permissão de determinado arquivo ou diretório para os usuários, as permissões podem ser somadas.
Vale a pena dar uma olhada na [Calculadora de Permições](https://chmod-calculator.com/).

 
## (Des)Compactação de Arquivos
- GZIP
  - `~$ gzip [arquivo.extenção]` : compactando um arquivo em .gz
  - `~$ gunzip [arquivo.extenção]` : descompactando um arquivo em .gz
  - `~$ gzip -9 [arquivo.extenção] `: compactando um arquivo em .gz maior compactação

- ZIP
  - `~$ zip [nome_compactado.zip] [arquivo(s).extenção]` : cria um arquivo compactado .zip podendo ser vários arquivos separados por espaço 
  - `~$ unzip [nome_compactado.zip]` : descompacta arquivos

- BZIP2
  - `~$ bzip2 [nome_arquivo.extencao]` : compacta em bz2
  - `~$ bzip2 -d [nome_arquivo.extencao]` : compacta em bz2

- RAR
Precisa ser instalado
  - `~$ rar [a_ou_x] [arquivo.rar] [arquivos_a_compactar]` : quando o parâmetro for a então estamos criando o arquivo compactado, quando for x estamos descompactando os arquivos.

- TAR (este é um arquivador)
  - `~$ tar -cf [arquivo.tar] [arquivos_a_compactar1.txt] [arquivos_a_compactar2.txt]` : Com isso juntamos um conjunto de arquivos. Podendo esse ser usado com qualquer um dos compactadores citados anteriormente.

- Para decompactar um arquivo .tar.gz :
  - `~$ tar -xvf [arquivo.tar.gz] [parâmetro]` : Este comando é usado pra descompactar o arquivo .tar. O parâmetro (-C [caminho]) é opcional 


# APACHE

`sudo service apache2 start` : inicia o serviço Apache. </br>
`sudo systemctl restart apache2`: Reinicia o serviço Apache. </br>
`sudo systemctl status apache2`: exibe o status do serviço Apache. </br>
`sudo systemctl stop apache2`: Encerra o serviço Apache.