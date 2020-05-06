/* Arduino Sketch when controlling car from computer.
   Not needed when using embedded board directly on car*/

int curState;
int prevState;
void setup() {
  pinMode(13, OUTPUT);    // connected to Forward
  pinMode(12, OUTPUT);    // connected to Backward
  pinMode(11, OUTPUT);    // connected to Left
  pinMode(10, OUTPUT);    // connected to Right
  resetAll();
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

void moveRight(){
  digitalWrite(13, HIGH); 
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, LOW);

}

void moveLeft(){
  digitalWrite(13, HIGH); 
  digitalWrite(12, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, LOW);

}

void moveForward(){
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(13, LOW); 
}

void moveBackward(){
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW); 
}

void loop() {
  String tmp = Serial.readString();
  curState = tmp[0];
  
  if (curState != prevState){
    prevState = curState; 
    //pins are active low, enable them based on input command
    if (curState == 'w') moveForward();
    else if (curState == 's') moveBackward(); 
    else if (curState == 'a') moveLeft(); 
    else if (curState == 'd') moveRight();
    else if (curState == 'z') resetAll();
  }
 
}
