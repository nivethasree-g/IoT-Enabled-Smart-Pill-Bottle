#define TRIG 9
#define ECHO 10

long duration;
int distance;

const int THRESHOLD = 10;   // cm
char lastState = 'X';      // Unknown at start

void setup() { 
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  Serial.println("Pill Monitor Started");
}

void loop() {

  // Trigger ultrasonic pulse
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // Read echo with timeout
  duration = pulseIn(ECHO, HIGH, 30000);
  if (duration == 0) return;

  // Convert to distance (cm)
  distance = duration * 0.034 / 2;

  char currentState;

  if (distance > THRESHOLD) {
    currentState = 'L';   // Pill Low
  } else {
    currentState = 'S';   // Stock In
  }

  // Send ONLY when state changes
  if (currentState != lastState) {

    //  Bluetooth data (DO NOT CHANGE)
    Serial.write(currentState);  
    Serial.write('\n');

    // Serial Monitor (for showcase)
    if (currentState == 'L') {
      Serial.println("PILL LOW");
    } else {
      Serial.println("STOCK IN");
    }

    lastState = currentState;
  }

  delay(300);   // smooth updates
}










