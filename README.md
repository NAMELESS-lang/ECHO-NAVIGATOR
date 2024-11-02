# ECHO-NAVIGATOR
Simulador de um sonar de submarino

O projeto consiste em um simulador de um sonar de submarino, que possui uma interface desenvolvida em python com a biblioteca customtkinter 
e com o arduino junto ao módulo sensor ultrassônico

Ele é divido em quatro scripts:
  conexão_ard.py: Realiza a conexão com o arduino;
  app.py: Cria a interface do aplicativo que simula o HUB de um sonar;
  criar_grafico.py: Responsável por criar os gráficos que indicam a localização dos corpos e o som do sonar;
  RADAR.ino: Este é usado no software arduino IDE, que é usado para programação do arduino.

Considerações importantes:

Ao usar o projeto, lembre-se de alterar os caminhos dos diretórios existentes nos scripts (app.py e criar_grafico.py) para os que coincidem com o do
seu computador para que funcionem corretamente.

O script RADAR.ino utiliza uma biblioteca que não está inclusa por padrão na IDE do arduino, por isso junto do projeto há um arquivo chamado "Ultrasonic-master.zip" que contém
esta biblioteca que foi utilizada, portanto basta somente incluí-la no arduino IDE.


