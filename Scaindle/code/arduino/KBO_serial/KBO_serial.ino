
/* Interfaccia seriale unidirezionale con device rs485
lettura stato bottoni capacitivi
invio nuova stringa sulla sriale 

created 09/04/2014
by Caltabiano Daniele


*/
#define bottone_1 2
#define bottone_2 3

#include <SoftwareSerial.h>
#include <String.h>
// con il software serial ci si interfaccia alla comunicazione seriale della rs485. pin 10 RX pin 11 TX. Collega il pin RS485+ del device 
SoftwareSerial portOne(2, 12);
int buttons [] = {6,11,10,9,3,5};

bool inizio=false;
bool fine=false;
char pesata[6];
char appen[2];
byte index;
bool stat=false;

void setup()
{
  // Apertura porta seriale cn il pc
  Serial.begin(9600);
  
  // Apertura seconda porta seriale linkata con il device rs485
  portOne.begin(9600);
  for (int p=0; p<6; p++)
  {
  pinMode(buttons[p],INPUT);
  }

}

void loop()
{
 
//acquisisci caratteri fino a quando la comunicazione è disponibile
  while (portOne.available() > 0) {
    char inByte = portOne.read();
    // controllo che il carattere sia il marker di inizio della parola
    if (inByte=='N'){
      index=0;
      pesata[index]='\0';
      inizio=true;
      fine=false;
    }
    // conotrollo che il carattere sia quello di fine parola
    else if (inByte=='L')
    {      
      fine=true;
      break;
    }
    //caratteri che non sono ne inizio che fine riga
    else
    {
      if (index<6)
      {
        pesata[index]=inByte;
        index++;
        pesata[index]='\0';
      }
     }
  }
  //se siamo in mezzo al marker di inizio e fine della parola
  if (inizio && fine)
  {
    String pie="p";
    String stringa2;
    String SOP="%";
    String EOP="&";
    for (int i=0 ; i<6; i++ ){
         if (digitalRead(buttons[i])==HIGH){
           stringa2=pie+(i+1);
          // stat=true;
         }
   }
   /*if(stat==false)
     stringa2=pie+0;   
     Serial.println(stringa1); 
    stat = false;
   */
        String stringa1=SOP+pesata + stringa2+EOP;

        Serial.println(stringa1); 

    //stampo la stringa
   
    
    inizio=false;
    fine=false;
    index=0;
    pesata[index]='\0';
    delay(1);
  }
 
  
}

