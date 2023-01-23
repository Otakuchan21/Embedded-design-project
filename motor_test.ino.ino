
int ENA = 11, N1 = 8, N2 = 12;
int sp = 200;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ENA, OUTPUT);
  pinMode(N1, OUTPUT);
  pinMode(N2, OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(ENA, sp);
  digitalWrite(N1, HIGH);
  digitalWrite(N2, LOW);
  delay(2000);

}
