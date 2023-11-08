#include <WiFi.h>
WiFiServer server(80);
const char* ssid = "Youssef1";
const char* password = "Y11112002Tj";
const char* serverIp = "192.168.165.193";
String Motion;
int XCoordinate = 0;
int YCoordinate = 1;
#include <ESP32Servo.h>
Servo Gripper;

//Motor1 right
int EnableMotor1 = 11;
int motor1pin1 = 10;
int motor1pin2 = 9;
//Motor2 left
int EnableMotor2 = 14;
int motor2pin1 = 13;
int motor2pin2 = 12;

 
const int freq = 30000;
const int pwmChannel0 = 0;  //motor 1
const int pwmChannel1 = 1;  //motor 2
const int Resolution = 8;
int fast = 255;
int slow = 150;
int stop = 0;


void Stop()
{
  digitalWrite(motor1pin1,0);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,0);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,stop);
  ledcWrite(pwmChannel1,stop);

}
void Forward()
{
  digitalWrite(motor1pin1,1);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,1);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,fast);
  ledcWrite(pwmChannel1,fast);
}
void SForward()
{
  digitalWrite(motor1pin1,1);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,1);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,slow);
  ledcWrite(pwmChannel1,slow);

}
void Backward()
{
  digitalWrite(motor1pin1,0);
  digitalWrite(motor1pin1,1);
  digitalWrite(motor2pin1,0);
  digitalWrite(motor2pin1,1);
  ledcWrite(pwmChannel0,fast);
  ledcWrite(pwmChannel1,fast);

}
void SBackward()
{
  digitalWrite(motor1pin1,0);
  digitalWrite(motor1pin1,1);
  digitalWrite(motor2pin1,0);
  digitalWrite(motor2pin1,1);
  ledcWrite(pwmChannel0,slow);
  ledcWrite(pwmChannel1,slow);
}
void Right()
{
  digitalWrite(motor1pin1,1);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,0);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,fast);
  ledcWrite(pwmChannel1,fast);
}
void SRight()
{
  digitalWrite(motor1pin1,1);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,0);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,slow);
  ledcWrite(pwmChannel1,slow);
}
void Left()
{
  digitalWrite(motor1pin1,0);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,1);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,fast);
  ledcWrite(pwmChannel1,fast);
}
void SLeft()
{
  digitalWrite(motor1pin1,0);
  digitalWrite(motor1pin1,0);
  digitalWrite(motor2pin1,1);
  digitalWrite(motor2pin1,0);
  ledcWrite(pwmChannel0,slow);
  ledcWrite(pwmChannel1,slow);
}

void GripperExpand()
{
  for(int i = 0; i <= 180 ; i++)
  { if(Motion  != "S")
   {
    Gripper.write(i);
   }else
   {
    break; 
   }
 }
}

void GripperWrap()
{
 for(int i = 0; i <= 180 ; i++)
  { if(Motion  != "S")
   {
    Gripper.write(i);
  }else
   {
    break; 
   }
 }
}

void setup() {
  //Motor 1 Adjust
  pinMode(motor1pin1,OUTPUT);
  pinMode(motor1pin2,OUTPUT);
  pinMode(EnableMotor1,OUTPUT);
  pinMode(motor2pin1,OUTPUT);
  pinMode(motor2pin2,OUTPUT);
  pinMode(EnableMotor2,OUTPUT);
  ledcSetup(pwmChannel0, freq, Resolution);
  ledcAttachPin(EnableMotor1, pwmChannel0);
  ledcSetup(pwmChannel1, freq, Resolution);
  ledcAttachPin(EnableMotor2, pwmChannel1);
  
  // make esp32 make access point to connct my laptop to it
  Serial.begin(115200);
  delay(10);
  Serial.begin(9600);
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  server.begin();
}

void loop() { 
  WiFiClient client = server.available();

  if (client) {
    while (client.connected()) {
      if (client.available()) {
        Motion = client.readStringUntil(' ');
        if (Motion == "F")
        {
          Forward();
        }else if (Motion == "B")
        {
            Backward();
        }else if (Motion == "R")
        {
            Right();
        }else if (Motion == "L")
        {
            Left();
        }else if (Motion == "SF")
        {
           SForward();
        }else if (Motion == "SB")
        {
           SBackward();
        }else if (Motion == "SR")
        {
           SRight();
        }else if (Motion == "SL")
        {
           SLeft();
        }else if (Motion == "S")
        {
         Stop();
        }
        else if (Motion == "GE")
        {
          GripperExpand();
        }else if (Motion == "Gw")
        {
          GripperWrap();
        }
        // sending robot position
        client.print(XCoordinate);
        client.print(YCoordinate);
      }
    }

  }

