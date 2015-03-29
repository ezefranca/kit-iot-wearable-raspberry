#Biblioteca para comando do Kit Wearable da Telefônica

Mais informações: http://iot.telefonicabeta.com/kit-iot-wearable/

##0) Observações importantes
- Esta biblioteca foi desenvolvida para uso com a Intel Galileo Gen 2 rodando o Intel IoT Developer Kit 1.0. Saiba mais em https://software.intel.com/en-us/iot/downloads

##1) Requisitos
- Intel Galileo Gen 2 (não testado na Gen 1, mas não há nada que impeça o uso)
- Sistema Intel IoT Developer Kit 1.0 devidamente instalado
- Dispositivo Bluetooth devidamente instalado e configurado na Intel Galileo
- Acesso ao terminal do Linux na Intel Galileo (via Ethernet, Wifi, Serial ou PoorMansTelnet)
- Dispositivo wearable da Telefônica com firmware devidamente instalado

##2) Dependências
- Esta biblioteca inclui na pasta *deps* os módulos Python necessários para execução dos scripts:
	- pexpect
	- ptyprocess
	- pybluez
- No IoT Developer Kit 1.0 não há nenhuma outra dependência pendente

##3) Instalação
1. Copie para o cartão SD de seu sistema Yocto em uma pasta conveniente (ex. /home/root/wearablePython) todos os arquivos desta biblioteca
2. Pela linha de comando do Yocto, execute a instalação de cada um dos módulos Python incluídos na pasta *deps*:
	- Abra a pasta correspondente
	- Execute o comando: $ python setup.py install

##4) Utilizando a biblioteca
- Antes de utilizar a biblioteca escreva o endereço MAC Low Energy de seu kit wearable (disponível na etiqueta atrás da bateria) no arquivo bltAddrWearable com o seguinte formato de exemplo: 00:0E:0B:00:39:AA (você pode utilizar um editor de texto comum caso esteja em um computador convencional ou o comando *vi* no Yocto - altamente não recomendado).
- Cada um dos scripts disponíveis controla uma função do kit wearable: acelerômetro, sensor de luminosidade, sensor de temperatura, buzzer, LED RGB e botões.
- IMPORTANTE: Antes de executar qualquer script é preciso habilitar o dispositivo Bluetooth na Intel Galileo! Utilize a seguinte sequência de comandos no terminal, supondo que seu dispositivo Bluetooth esteja endereçado no Linux como *hci0*:
	- $ rfkill unblock all
	- $ hciconfig hci0 up
- Os scripts são executados pelo comando: 
	- $ python nome_do_script.py [ARGUMENTOS]
- Todos os scripts aceitam o argumento *--h* para exibir um resumo de sua função e um exemplo de utilização

##5) Referência rápida
1. getAcel.py
	- Imprime a aceleração no eixo enviado como argumento
	- Argumentos: X, Y ou Z
	- Uso: python getAcel.py X
2. getLumi.py
	- Imprime a luminosidade lida pelo LDR da placa
	- Argumentos: NENHUM
	- Uso: python getLumi.py
3. getTemp.py
	- Imprime a temperatura, em celsius, lida pelo sensor da placa
	- Argumentos: NENHUM
	- Uso: python getTemp.py
4. sendCommand.py
	- Envia a cadeia de caracteres passada como argumento para o dispositivo wearable. Obs: O programa adiciona automaticamente o caractere *#* antes do comando e a cadeia *\r\n* depois do comando. Veja uma lista de comandos aqui: https://github.com/telefonicadigital/kit-iot-wearable-node/wiki/Comandos-padr%C3%B5es-do-Wearable
	- Argumentos: Uma cadeia de caracteres, sem espaço
	- Uso: python sendCommand.py cadeiaDeCaracteres
5. setBuzzer.py
	- Aciona o buzzer da placa com a frequência desejada (use 0 para desligar)
	- Argumentos: Frequência, um número inteiro entre 0 e 2000
	- Uso: python setBuzzer.py 1000
6. setLed.py
	- Configura a intensidade luminosa de cada uma das cores do LED RGB disponível na placa.
	- Argumentos: 3 números inteiros entre 0 e 255, representando a intensidade de cada cor do LED na sequência R (vermelho) G (verde) e B (azul).
	- Uso: python setLed.py 255 255 0
7. waitButton.py
	- Aguarda o pressionamento de um botão no kit wearable e imprime o número do botão pressionado (1 ou 2). Após um timeout (não configurável) se nenhum botão for pressionado o script imprime 0.
	- Argumentos: NENHUM
	- Uso: python waitButton.py
