/* Arduino Sketch when controlling car from computer.
   Not needed when using embedded board directly on car*/

int curState;
int prevState;
void setup() {
  pinMode(13, OUTPUT);    // connected to Forward
  pinMode(12, OUTPUT);    // connected to Backward
  pinMode(11, OUTPUT);    // connected to Left
  pinMode(10, OUTPUT);    // connected to Right
  Serial.begin(9600);
  curState = 'z';
  prevState = 'z';
}

void resetAll() {
  //pins are active low, setting them all to inactive
  digitalWrite(13, HIGH); 
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
}

void loop() {
  String tmp = Serial.readString();
  curState = tmp[0];
  
  if (curState != prevState){
    prevState = curState; 
    //pins are active low, enable them based on input command
    if (curState == 'w') digitalWrite(13, LOW);
    else if (curState == 's') digitalWrite(12, LOW); 
    else if (curState == 'a') digitalWrite(11, LOW); 
    else if (curState == 'd') digitalWrite(10, LOW);
    else resetAll();
  }
 
}
