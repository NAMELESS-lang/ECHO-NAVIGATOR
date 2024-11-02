#include <Servo.h> // biblioteca de configuração do servo motor
#include <Ultrasonic.h>
int Enviar = 3;
int Receber = 2; 
#define SERVO 6 // Diz que a porta digital número 6 chama-se SERVO
Servo servo_motor; // Cria um objeto da classe Servo
HC_SR04 sensor(3,2); // Cria um objeto da classe sensor
#define led 13
#define lazer 12
void setup(){

  // Associa a porta SERVO ao objeto servo_motor e posiciona o motor na posição 0
  servo_motor.attach(SERVO); 
  servo_motor.write(0);
  pinMode(led, OUTPUT);
  pinMode(lazer, OUTPUT);

  //Define que a omunicação da porta seria é de 9600 milisegundos
  Serial.begin(9600);
  digitalWrite(lazer, HIGH);
  digitalWrite(led, HIGH);
  delay(50);
  digitalWrite(led, LOW);
  delay(50);
  digitalWrite(led, HIGH);
  delay(50);
  digitalWrite(led, LOW);
}

void loop(){
  // Percorre de 0 a 180 graus
  for(int i = 0; i <=180; i++){
    servo_motor.write(i); // Diz em qual grau o motor deve ir
    if (sensor.distance()<= 30){ // Condição para enviar a informação ou não se a distânia for menor que tal valor, aí envia a informação
       Serial.println(i);
       Serial.println(sensor.distance());
       digitalWrite(led, HIGH);
       delay(1000); // Espera um tempo, para o arduino e o pc processar os dados,e depois continua a varredura
       digitalWrite(led, LOW); 
  }
    delay(50);
  }
  // Percorre de 180 a 0 graus
  for(int i = 180; i >=0; i--){
    servo_motor.write(i); // Diz em qual grau o motor deve ir
     if (sensor.distance() <=30){ // Condição para enviar a informação ou não se a distânia for menor que tal valor, aí envia a informação
       Serial.println(i);
       Serial.println(sensor.distance());
       digitalWrite(led, HIGH);
       delay(1000); // Espera um tempo, para o arduino e o pc processar os dados,e depois continua a varredura 
       digitalWrite(led, LOW);
  }
  delay(50);
  }
}
