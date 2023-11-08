#include <math.h>

// Encoder pins for left and right wheels
int encoderLeft = 3;
int encoderRight = 4;

// Variables for left wheel
int stepsLeft = 0;
float distLeft = 0;
int noRevLeft = 0;
int circumLeft = 220;
float x = 0;

// Variables for right wheel
int stepsRight = 0;0
float distRight = 0;
int noRevRight = 0;
int circumRight = 220;
float y = 0;

float angleindegrees = 0;

void setup() {
  Serial.begin(9600);
  pinMode(encoderLeft, INPUT_PULLUP);
  pinMode(encoderRight, INPUT_PULLUP);
}

void loop() {
  // Read encoder for left wheel
  if (digitalRead(encoderLeft)) {
    stepsLeft = stepsLeft + 1;
    if (stepsLeft == 20) {
      noRevLeft += 1;
      stepsLeft = 0;
    }
    distLeft = noRevLeft * circumLeft;
  }

  // Read encoder for right wheel
  if (digitalRead(encoderRight)) {
    stepsRight = stepsRight + 1;
    if (stepsRight == 20) {
      noRevRight += 1;
      stepsRight = 0;
    }
    distRight = noRevRight * circumRight;
  }

  // Calculate X position
  x = distLeft * cos(angleindegrees * (M_PI / 180.0)); // Calculate X position

  // Calculate Y position
  y = distRight * sin(angleindegrees * (M_PI / 180.0)); // Calculate Y position

  // Calculate angle
  angleindegrees = atan2(y, x) * (180.0 / M_PI); // Calculate angle in degrees

  Serial.print("Left Steps: ");
  Serial.println(stepsLeft);
  Serial.print("Left Distance: ");
  Serial.println(distLeft);
  Serial.print("Right Steps: ");
  Serial.println(stepsRight);
  Serial.print("Right Distance: ");
  Serial.println(distRight);
  Serial.print("Angle (degrees): ");
  Serial.println(angleindegrees);
  Serial.print("X Position: ");
  Serial.println(x);
  Serial.print("Y Position: ");
  Serial.println(y);
}