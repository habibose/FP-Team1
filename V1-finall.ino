#include <math.h>
int left_encoder = 3;
int right_encoder = 2;
unsigned long start_time = 0;
unsigned long end_time = 0;
int stepsL = 0;
int stepsL_old = 0;
int stepsR = 0;
int stepsR_old = 0;
//float rps = 0;
float dL = 0;
float dR = 0;
float Rw = 5;
int noRevL = 0;
int noRevR = 0;
int circum = 220;
float x = 0;
float y = 0;
float angleindegrees;
float d;
const float pi = 3.14159265359;

void leftEncoderInterrupt()
{
  stepsL += 1;
  dL = stepsL * circum / 20;
}

void rightEncoderInterrupt()
{
  stepsR += 1;
  dR = stepsR * circum/20;
}

void setup()
{
  Serial.begin(9600);
  pinMode(left_encoder, INPUT_PULLUP);
  pinMode(right_encoder, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(left_encoder), leftEncoderInterrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(right_encoder), rightEncoderInterrupt, RISING);
}

void loop()
{
  //start_time = millis();
  //end_time = start_time + 1000;
 // while (millis() < end_time)
  //{

    Serial.print("\tstepsLeft:");
    Serial.print(stepsL);
    Serial.print("\tdistanceLeft:");
    Serial.print(dL);
      

    Serial.print("\tstepsRight:");
    Serial.print(stepsR);
    Serial.print("\tdistanceRight:");
    Serial.print(dR);
   

    d = (dR + dL) / 2;
    angleindegrees = ((dR - dL) / 2 * Rw) * (pi / 180);

    x = d * cos(angleindegrees);
    y = d * sin(angleindegrees);
    x+=x;
    y+=y;

    Serial.print("\tX=");
    Serial.print(x);
    Serial.print("\tY=");
    Serial.println(y);
    Serial.print("\tangle:");
    Serial.print(angleindegrees);
  //}
}