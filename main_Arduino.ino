const int sensorPin = A5;
float temp_obj = 0.0;
float histeresis = 1.0;

const int peltierDirPin = 13;            // Dirección
const int peltierPwmPin = 11;            // PWM
const int peltierBrakePin = 8;           // Freno

bool temp_recibida = false;
String estado_actual = "";

void setup() {
  Serial.begin(9600);

  pinMode(peltierDirPin, OUTPUT);
  pinMode(peltierPwmPin, OUTPUT);
  pinMode(peltierBrakePin, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    if (input.startsWith("SET:")) {
      String tempStr = input.substring(4);
      float newTemp = tempStr.toFloat();
      if (newTemp != 0.0 || tempStr == "0" || tempStr == "0.0") {
        temp_obj = newTemp;
        temp_recibida = true;
        //Mensaje de confirmación
        Serial.print("SET_OK:");
        Serial.println(temp_obj);
      }
    }
  }

  if (!temp_recibida) {
    return;
  }

  int value = analogRead(sensorPin);
  float millivolts = (value / 1024.0) * 5000;
  float temp_dut = millivolts / 10; 
  // Enviar temperatura con formato "VAL:"
  Serial.print("VAL:");
  Serial.println(temp_dut);

   // Control ON/OFF con histéresis
  if (temp_dut > (temp_obj + histeresis)) {
    Serial.println("DUT debe enfriarse");
    digitalWrite(peltierDirPin, HIGH);    // Dirección para enfriar
    estado_actual = "DUT debe enfriarse";
  } else if (temp_dut < (temp_obj - histeresis)) {
    Serial.println("DUT debe calentarse");
    digitalWrite(peltierDirPin, LOW);     // Dirección para calentar
    estado_actual = "DUT debe calentarse";
  } else {
    Serial.println(estado_actual);
  }
  digitalWrite(peltierBrakePin, LOW);   // Quitar freno
  analogWrite(peltierPwmPin, 255);      // Potencia máxima

  delay(1000);
}
