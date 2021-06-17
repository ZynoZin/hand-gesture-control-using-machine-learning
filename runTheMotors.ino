#include <SoftwareSerial.h>
SoftwareSerial HC05(12, 13); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11




void setup() {
  HC05.begin(9600); //Baudrate 9600 , Choose your own baudrate 
//  pinMode(8, OUTPUT);
//  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

}

void loop() {

  if(HC05.available() > 0) //When HC06 receive something
  {
    char receive = HC05.read(); //Read from Serial Communication
//    if(receive == '0') 
//    {
//      digitalWrite(8, HIGH); 
//      digitalWrite(9, HIGH); 
//      digitalWrite(10, LOW); 
//      digitalWrite(11, LOW);
//    }
    //forward
    if(receive == '2')
    {
   
      digitalWrite(10, HIGH); 
      digitalWrite(11, HIGH);
    }
    //left
    else if( receive == '3')
    {

      digitalWrite(10, HIGH); 
      digitalWrite(11, LOW);
    }
    //right
    else if( receive == '4')
    {

      digitalWrite(10, LOW); 
      digitalWrite(11, HIGH);
    }
    //stop65
    else if( receive == '5')
    {
  
      digitalWrite(10, LOW); 
      digitalWrite(11, LOW);
    }
    else{
      
    }
    
    
  }

}
