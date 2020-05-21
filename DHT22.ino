
#include <dhtnew.h>

DHTNEW mySensor(6);

void setup()
{
  Serial.begin(9600);
//  mySensor.setHumOffset(0);
//  mySensor.setTempOffset(0);

}

void loop() {
  mySensor.read();
  delay(1000); // PYTHON İLE UYUMLU OLMALIDIR (TIMEOUT VE TIMER DEĞERLERİ İLE)
  
  Serial.print(mySensor.humidity, 2);
  Serial.print(",\t");
  Serial.println(mySensor.temperature, 2);

}
