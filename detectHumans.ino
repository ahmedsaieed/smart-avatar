/*
  DetectHumans
 
 Reads Sharp 2Y0A02 Proximity Sensor status, and sends it to PC upon request.
 
 This code is in the public domain.
 */

#define SENSE_THRESHOLD 70
#define SENSOR A0


char rcv_buff;



void setup() {
  Serial.begin(9600);
}

void loop() {

  rcv_buff=0;
  
  if(Serial.available()){
    delay(10);

    rcv_buff = Serial.read();

    if(rcv_buff == 'A'){
      delay(100);
      // Check for 3 positive consecutive readings
      if (analogRead(SENSOR) >= SENSE_THRESHOLD) {
        delay(100);
        if (analogRead(SENSOR) >= SENSE_THRESHOLD) {
          delay(100);
          if (analogRead(SENSOR) >= SENSE_THRESHOLD) {
            // Send 1 if Positive
            Serial.println("1");
          }
          else
            // Send 0 if Negative
          { 
            Serial.println("0"); 
          }
        }
        else 
        { 
          Serial.println("0"); 
        }
      }
      else 
      { 
        Serial.println("0"); 
      }

    }
  }    
}



