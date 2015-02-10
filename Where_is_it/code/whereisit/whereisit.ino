int inputs[] = {14,15,16,17,18,19,3,5,6};
int outputs[] = {2,4,7,8,9,10,11,12,13};

// Button INPUTS:
// A0, A1, A2, A3, A4, A5, 3, 5, 6

// LED OUTPUTS:
// 2, 4, 7, 8, 9, 10, 11, 12, 13

void setup() {
  for (int i = 0; i < 9; i++) {
    pinMode(inputs[i], INPUT);
  }
  for (int i = 0; i < 9; i++) {
    pinMode(outputs[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 9; i++) {
    digitalWrite(outputs[i], digitalRead(inputs[i]));
  }
}
