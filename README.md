# Sockets de Rede
Implementação em Python de *sockets* de rede baseada no paradigma cliente-servidor.

## Introdução
*Sockets* correspondem a extremidades de um fluxo de comunicação entre
processos através de uma rede. Cada uma dessas extremidades possui um
identificador único, composto pelo endereço (IP) da máquina e o
identificador local da porta usada pelo processo. O método de
comunicação no modelo de implementação de *sockets* se baseia na
arquitetura cliente e servidor, um paradigma de aplicação distribuída na
qual há fornecedores de recursos, os servidores, e requerentes de
serviço, os clientes.

Para que se estabeleça uma comunicação nesse padrão, é necessário seguir
uma sequência de operações pré-definidas. Inicialmente, o servidor é
alocado em uma porta específica e aguarda uma ligação a essa porta.
Dessa maneira, o cliente deve saber, previamente, o endereço do servidor
e a respectiva porta em que o mesmo se encontra. Em seguida, para
realizar a conexão, o cliente solicita uma ligação ao servidor. Caso a
ligação seja estabelecida com êxito, o servidor aceita a conexão e então
é criado um canal de comunicação entre cliente e servidor.

## Modo de usar
Para iniciar a comunicação, primeiro é necessário executar o *script*
`servidor.py`. É possível especificar parâmetros de execução na linha de
comando, conforme ilustra o comando abaixo.

    python servidor.py --host endereco_do_host --porta numero_da_porta

Posteriormente, `cliente.py` deve ser iniciado em uma janela separada,
por meio do comando abaixo. Serão exibidas as opções, com 1 para enviar
mensagem e 2 para sair. Ao selecionar a opção 1, serão requisitados o
assunto e o texto da mensagem. Após a entrada do texto, a mensagem pode
ser enviada ao pressionar a tecla `Enter`.

    python cliente.py --host endereco_do_host --porta numero_da_porta

## Implementação
A implementação de sockets de rede em Python se dá por meio do módulo
`socket`, disponível no conjunto de módulos padrão da linguagem.
Conforme o paradigma cliente e servidor, dois *scripts* foram
desenvolvidos: um faz o papel de servidor, capaz de receber mensagens; o
outro atua como cliente e apenas envia mensagens. O servidor precisa ser
configurado e iniciado primeiro, uma vez que a conexão se estabelece por
meio do endereço IP e da porta especificada em seu *socket*.

### Configuração do servidor
O arquivo `servidor.py` contém o *script* necessário para a criação do
socket. Primeiramente, os módulos `socket` e `argparse` são importados,
para a configuração do servidor e dos parâmetros de execução,
respectivamente. Em seguida, o objeto `datetime` é importado a partir do
módulo `datetime`, para ser utilizado na exibição da data e hora nas
mensagens.

Com o auxílio de `argparse`, são especificados os parâmetros de execução
do *script*: `--host` e `--porta`. *Host* especifica o endereço ao qual
o servidor será vinculado. Caso *host* não seja especificado na linha de
comando, o *hostname* da máquina local é utilizado por padrão. O
parâmetro *porta* determina a porta da camada de transporte por meio da
qual o servidor aguardará conexões. O protocolo padrão utilizado é o
TCP.

Após *host* e *porta* serem vinculados ao *socket*, mediante o uso da
função `bind`, o servidor está pronto para iniciar seu funcionamento. A
função `listen` monitora de forma assíncrona a porta especificada, até
que uma conexão se estabeleça. Quando isso ocorre, `accept` retorna um
objeto para manipular a conexão. Um laço de repetição é, pois, iniciado
e o *script* passa a receber as mensagens por intermédio de `recv`.
Foram delimitados 1024 *bytes* para o tamanho máximo da mensagem.

### Configuração do cliente
A configuração inicial do cliente se dá de forma semelhante ao servidor,
os mesmos parâmetros `--host` e `--porta` são especificados e o objeto
*socket* é iniciado. A função `bind` não é utilizada para criar uma
conexão do tipo cliente, mas sim `connect`. Dentro do *loop*, a entrada
do usuário é solicitada. Caso a opção 2 seja escolhida, o programa
solicitará o assunto e o texto da mensagem que será enviada. A `string`
é construída com elementos de formatação para melhorar a legibilidade.
Em seguida, a mensagem é enviada com o auxílio do método `sendall`. Caso
o usuário opte pela opção 2, o servidor envia para o cliente um
*payload* com a mensagem `CODIGO_SAIDA` para comunicá-lo de seu término.
A conexão é, por fim, encerrada.

## Autores
* [Abner Nascimento](https://github.com/abnersn)
* [Mauro Falcão](https://github.com/maurofalc)
