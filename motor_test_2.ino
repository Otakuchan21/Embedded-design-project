int ENB = 10, N4 = 8, N3 = 9, N2 = 12, N1 = 6, ENA = 11; 
int SPEED = 200;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ENA, OUTPUT);
  pinMode(N1, OUTPUT);
  pinMode(N2, OUTPUT);
  pinMode(N3, OUTPUT);
  pinMode(N4, OUTPUT);
  pinMode(ENB, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(ENA, SPEED);
  digitalWrite(N1, HIGH);
  digitalWrite(N2, LOW);
  analogWrite(ENB, SPEED);
  digitalWrite(N3, HIGH);
  digitalWrite(N4, LOW);
  delay(1000);
  analogWrite(ENA, LOW);
  analogWrite(ENB, LOW);
  delay(2000);

 
 

}
