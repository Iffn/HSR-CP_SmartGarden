String myString = "";
int temp = 21;
int humEarth = 2;
int light = 10;

#include <Servo.h>

Servo myservo;

void setup()
{
  Serial.begin(9600);
  myservo.attach(A0);
  myservo.write(90);
}

void loop()
{
  while (Serial.available())
  {
    int ch = Serial.read();
    
    if(ch!='&') // \n = Zeilenumbruch
    {
      //Serial.println("rec");
      myString += char(ch);
    }
    else
    {
      if(myString != "")
      {
       // Serial.print("Recieved:");
        //Serial.println(myString);
        if(myString.toInt()==1)
        {
          Serial.println(temp);
          Serial.println(humEarth);
          Serial.println(light);
        }
        else if(myString.toInt()==2)
        {
          //It will rain
          //Serial.println("it will rain");
          myservo.write(180);
          delay(2000);
          myservo.write(90);
        }
        else if(myString.toInt()==3)
        {
          //It will not rain
          //Serial.println("it will not rain");
        }
        else
        {
          Serial.println("%");
          Serial.println("%");
          Serial.println("%");
        }
        //Serial.println("");
        myString = " ";
      }
    }
  }
}
