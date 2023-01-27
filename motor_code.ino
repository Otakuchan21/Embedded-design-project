int ENA = 5, N1 = 2, N2 = 4, N3= 7, N4 = 8, ENB = 6, SPEED = 80;
int data = 6;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ENA,OUTPUT);
  pinMode(N1,OUTPUT);
  pinMode(N2,OUTPUT);
  pinMode(N3,OUTPUT);
  pinMode(N4,OUTPUT);
  pinMode(ENB,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0)
  {
    int value = Serial.parseInt();
    if (value != 0)
    {
      data = value;
    }
  }
  Serial.println(data);
  
  if (data == 1)
  {
    //backward
    analogWrite(ENA, SPEED);
    analogWrite(ENB, SPEED);
    digitalWrite(N1,HIGH);
    digitalWrite(N2,LOW);
    digitalWrite(N3,HIGH);
    digitalWrite(N4,LOW);
    //Serial.println("im in backwards loop");
  }
  else if(data == 2)
  {
    //forward
    analogWrite(ENA, SPEED);
    analogWrite(ENB, SPEED);
    digitalWrite(N1, LOW);
    digitalWrite(N2, HIGH);
    digitalWrite(N3, LOW);
    digitalWrite(N4, HIGH);
    //Serial.println("im in forward loop");
  }
  else if (data == 3)
  {
    //right
    analogWrite(ENA, SPEED);
    analogWrite(ENB, SPEED);
    digitalWrite(N1, LOW);
    digitalWrite(N2, HIGH);
    digitalWrite(N3, HIGH);
    digitalWrite(N4, LOW);
  }
  else if (data == 4)
  {
    //left
    analogWrite(ENA, SPEED);
    analogWrite(ENB, SPEED);
    digitalWrite(N1, HIGH);
    digitalWrite(N2, LOW);
    digitalWrite(N3, LOW);
    digitalWrite(N4, HIGH);
  }
  else if(data == 5)
  {
    //steer left
    analogWrite(ENA, 50);
    analogWrite(ENB, SPEED);
    digitalWrite(N1, LOW);
    digitalWrite(N2, HIGH);
    digitalWrite(N3, LOW);
    digitalWrite(N4, HIGH);
    //Serial.println("im in forward loop");
  }

  else if(data == 6)
  {
    //steer right
    analogWrite(ENA, SPEED);
    analogWrite(ENB, 50);
    digitalWrite(N1, LOW);
    digitalWrite(N2, HIGH);
    digitalWrite(N3, LOW);
    digitalWrite(N4, HIGH);
    //Serial.println("im in forward loop");
  }
  else if(data == 7)
  {
    //stop
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
  }
}
