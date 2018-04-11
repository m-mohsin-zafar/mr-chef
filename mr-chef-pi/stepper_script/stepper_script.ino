int minLoc=0;
int maxLoc=62;
int lower=-62;
int upper=62;

int LCurrent=0;
int RCurrent=0;
int BCurrent=0;

String message[3];

const int LstepPin = 26; 
const int LdirPin = 28; 
const int RstepPin = 36; 
const int RdirPin = 34;
float min_speed;
float range;
float max_speed;

void setup(){
  Serial.begin(9600);
  // Sets the two pins as Outputs
  pinMode(LstepPin,OUTPUT); 
  pinMode(LdirPin,OUTPUT);
  pinMode(RstepPin,OUTPUT); 
  pinMode(RdirPin,OUTPUT);
  pinMode(24,OUTPUT);
  pinMode(30,OUTPUT);
  digitalWrite(24,LOW);
  digitalWrite(30,LOW);
}

void loop(){
  if (Serial.available()) {
    String payload=Serial.readString();
    genStrings(payload);
    move_stepper(message[0],message[1],(message[2]).toInt());
    Serial.println(LCurrent);
    Serial.println(RCurrent);
    Serial.println(BCurrent);
  }
}

void genStrings(String payload){
  int space_index1=payload.indexOf(" ");
  int space_index2=payload.indexOf(" ",space_index1+1);
  message[0]=payload.substring(0,space_index1);
  message[1]=payload.substring(space_index1+1,space_index2);
  message[2]=payload.substring(space_index2+1); 
}


void move_stepper(String stepper,String dir,int steps){
  
  range = 62.25*steps;  
  max_speed = 500;
  min_speed = 1500;
 
  int speed_range = min_speed - max_speed;
  if(stepper=="R"){
    move_right_stepper(speed_range,dir,steps);
  }
  if(stepper=="L"){
    move_left_stepper(speed_range,dir,steps);
  }
  if(stepper=="B"){
    move_both_stepper(speed_range,dir,steps);
  }
   
}


void move_left_stepper(int speed_range,String dir,int distance){
  if(dir=="+"){
    digitalWrite(LdirPin,LOW);
    if(LCurrent+distance<=maxLoc){
      LCurrent+=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }else if(dir=="-"){
    digitalWrite(LdirPin,HIGH);
    if(LCurrent-distance>=minLoc){
      LCurrent-=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }
}

void move_right_stepper(int speed_range,String dir,int distance){
  
  if(dir=="+"){
    digitalWrite(RdirPin,HIGH);
    if(RCurrent+distance<=maxLoc){
      RCurrent+=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed);
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }else if(dir=="-"){
    digitalWrite(RdirPin,LOW);
    if(RCurrent-distance>=minLoc){
      RCurrent-=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed);
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }
}

void move_both_stepper(int speed_range,String dir,int distance){
  if(dir=="+"){
    digitalWrite(RdirPin,HIGH);
    digitalWrite(LdirPin,HIGH);
    if(BCurrent+distance<=upper){
      BCurrent+=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH);
        digitalWrite(LstepPin,HIGH);
        delayMicroseconds(min_speed);
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW);
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(RstepPin,HIGH); 
        digitalWrite(LstepPin,HIGH);
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);;
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH);
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }else if(dir=="-"){
    digitalWrite(RdirPin,LOW);
    digitalWrite(LdirPin,LOW);
    if(BCurrent-distance>=lower){
      BCurrent-=distance;
      for (int y = 0 ; y < (range*0.2) ; y++){
        
        min_speed = min_speed - ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH);
        digitalWrite(LstepPin,HIGH);
        delayMicroseconds(min_speed);
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW);
        delayMicroseconds(min_speed);
        
      }
      
      for (int x = 0 ; x < (range*.6) ; x++){
        
        digitalWrite(RstepPin,HIGH); 
        digitalWrite(LstepPin,HIGH);
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);
        
      }
      
      for (int z = 0 ; z < (range*.2) ; z++){
        
        min_speed = min_speed + ((speed_range)/(range*.2));
        
        digitalWrite(RstepPin,HIGH);
        digitalWrite(LstepPin,HIGH); 
        delayMicroseconds(min_speed); 
        digitalWrite(RstepPin,LOW);
        digitalWrite(LstepPin,LOW); 
        delayMicroseconds(min_speed);   
        
      }
    }
  }
}


