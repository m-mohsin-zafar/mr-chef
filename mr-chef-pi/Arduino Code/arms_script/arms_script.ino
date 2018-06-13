#include <Servo.h>

Servo lBase;
Servo lShoulder;
Servo lElbow;
Servo lWristRot;
Servo lWristPitch;
Servo lWristRoll;
Servo lGripper;

Servo rBase;
Servo rShoulder;
Servo rElbow;
Servo rWristRot;
Servo rWristPitch;
Servo rWristRoll;
Servo rGripper;

String arm;
int angles[7];
int speed_[7]={15,15,15,15,15,15,15};

void setup(){
  Serial.begin(9600);
  setupPins();
  init_servos();
}

void loop(){
  if (Serial.available()) {
    String payload="";
    payload=Serial.readString();
    
    if(payload == "SYNC"){
      Serial.println("SYNC ACK");
      delay(4000);
    }
    else{
      int space_index=payload.indexOf(" ");
      String mode=payload.substring(0,space_index);
      genStrings(payload);      
      if(mode=="I"){
        moveArms(arm,angles); 
      }else if(mode=="S"){
        moveArms_Simultaneously(angles); 
      }
    }
  }
}

void genStrings(String payload){
  int space_index0=payload.indexOf(" ");
  int space_index1=payload.indexOf(" ",space_index0+1);
  int space_index2=payload.indexOf(" ",space_index1+1);
  int space_index3=payload.indexOf(" ",space_index2+1);
  int space_index4=payload.indexOf(" ",space_index3+1);
  int space_index5=payload.indexOf(" ",space_index4+1);
  int space_index6=payload.indexOf(" ",space_index5+1);
  int space_index7=payload.indexOf(" ",space_index6+1);
  int space_index8=payload.indexOf(" ",space_index7+1);
  int space_index9=payload.indexOf(" ",space_index8+1);
  int space_index10=payload.indexOf(" ",space_index9+1);
  int space_index11=payload.indexOf(" ",space_index10+1);
  int space_index12=payload.indexOf(" ",space_index11+1);
  int space_index13=payload.indexOf(" ",space_index12+1);
  int space_index14=payload.indexOf(" ",space_index13+1);
  
  arm=payload.substring(space_index0+1,space_index1);
  
  angles[0]=(payload.substring(space_index1+1,space_index2)).toInt();
  speed_[0]=payload.substring(space_index2+1,space_index3).toInt();
  
  angles[1]=payload.substring(space_index3+1,space_index4).toInt();
  speed_[1]=payload.substring(space_index4+1,space_index5).toInt();
  
  angles[2]=payload.substring(space_index5+1,space_index6).toInt();
  speed_[2]=payload.substring(space_index6+1,space_index7).toInt();
  
  angles[3]=payload.substring(space_index7+1,space_index8).toInt();
  speed_[3]=(payload.substring(space_index8+1,space_index9)).toInt();
  
  angles[4]=payload.substring(space_index9+1,space_index10).toInt();
  speed_[4]=payload.substring(space_index10+1,space_index11).toInt();
  
  angles[5]=payload.substring(space_index11+1,space_index12).toInt();
  speed_[5]=payload.substring(space_index12+1,space_index13).toInt();
  
  angles[6]=payload.substring(space_index13+1,space_index14).toInt();
  speed_[6]=payload.substring(space_index14+1).toInt();
}

void setupPins(){
  rBase.attach(7);
  rShoulder.attach(6);
  rElbow.attach(5);
  rWristRot.attach(4);
  rWristPitch.attach(3);
  rWristRoll.attach(2);
  rGripper.attach(44);
  
  lBase.attach(13);
  lShoulder.attach(12);
  lElbow.attach(11);
  lWristRot.attach(10);
  lWristPitch.attach(9);
  lWristRoll.attach(8);
  lGripper.attach(45);  
}

void init_servos(){
  rBase.write(0);
  rShoulder.write(90);
  rElbow.write(100);
  rWristRot.write(110);
  rWristPitch.write(110);
  rWristRoll.write(0);
  rGripper.write(95);
  
  lBase.write(180);
  lShoulder.write(90);
  lElbow.write(110);
  lWristRot.write(110);
  lWristPitch.write(110);
  lWristRoll.write(0);
  lGripper.write(95);  
  
}

void moveArms(String arm,int angle[]){
  if(arm=="Left"){
     
     int current=lBase.read();
     if(current!=(180-angle[0])){
       if((180-angle[0]) > current){
         increase_angle(current,(180-angle[0]),lBase,speed_[0]);
       }
       else{
         decrease_angle(current,(180-angle[0]),lBase,speed_[0]);
       }
     }
     
     current=lShoulder.read();
     if(current!=angle[1]){
       if(angle[1] > current){
         increase_angle(current,angle[1],lShoulder,speed_[1]);
       }
       else{
         decrease_angle(current,angle[1],lShoulder,speed_[1]);
       }
     }
     
     current=lElbow.read();
     if(current!=angle[2]){
       if(angle[2] > current){
         increase_angle(current,angle[2],lElbow,speed_[2]);
       }
       else{
         decrease_angle(current,angle[2],lElbow,speed_[2]);
       }
     }
     
     current=lWristRot.read();
     if(current!=angle[3]){
       if(angle[3] > current){
         increase_angle(current,angle[3],lWristRot,speed_[3]);
       }
       else{
         decrease_angle(current,angle[3],lWristRot,speed_[3]);
       }
     }
     
     current=lWristPitch.read();
     if(current!=angle[4]){
       if(angle[4] > current){
         increase_angle(current,angle[4],lWristPitch,speed_[4]);
       }
       else{
         decrease_angle(current,angle[4],lWristPitch,speed_[4]);
       }
     }
     
     current=lWristRoll.read();
     if(current!=angle[5]){
       if(angle[5] > current){
         increase_angle(current,angle[5],lWristRoll,speed_[5]);
       }
       else{
         decrease_angle(current,angle[5],lWristRoll,speed_[5]);
       }
     }
     
     current=lGripper.read();
     if(current!=angle[6]){
       if(angle[6] > current){
         increase_angle(current,angle[6],lGripper,speed_[6]);
       }
       else{
         decrease_angle(current,angle[6],lGripper,speed_[6]);
       }
     }
  }
  
  if(arm=="Right"){
     
     int current=rBase.read();
     if(current!=angle[0]){
       if(angle[0] > current){
         increase_angle(current,angle[0],rBase,speed_[0]);
       }
       else{
         decrease_angle(current,angle[0],rBase,speed_[0]);
       }
     }
     
     current=rElbow.read();
     if(current!=angle[2]){
       if(angle[2] > current){
         increase_angle(current,angle[2],rElbow,speed_[2]);
       }
       else{
         decrease_angle(current,angle[2],rElbow,speed_[2]);
       }
     }
     
     current=rShoulder.read();
     if(current!=angle[1]){
       if(angle[1] > current){
         increase_angle(current,angle[1],rShoulder,speed_[1]);
       }
       else{
         decrease_angle(current,angle[1],rShoulder,speed_[1]);
       }
     }
     
     current=rWristRot.read();
     if(current!=angle[3]){
       if(angle[3] > current){
         increase_angle(current,angle[3],rWristRot,speed_[3]);
       }
       else{
         decrease_angle(current,angle[3],rWristRot,speed_[3]);
       }
     }
     
     current=rWristPitch.read();
     if(current!=angle[4]){
       if(angle[4] > current){
         increase_angle(current,angle[4],rWristPitch,speed_[4]);
       }
       else{
         decrease_angle(current,angle[4],rWristPitch,speed_[4]);
       }
     }
     
     current=rWristRoll.read();
     if(current!=angle[5]){
       if(angle[5] > current){
         increase_angle(current,angle[5],rWristRoll,speed_[5]);
       }
       else{
         decrease_angle(current,angle[5],rWristRoll,speed_[5]);
       }
     }
     
     current=rGripper.read();
     if(current!=angle[6]){
       if(angle[6] > current){
         increase_angle(current,angle[6],rGripper,speed_[6]);
       }
       else{
         decrease_angle(current,angle[6],rGripper,speed_[6]);
       }
     }
  }
}


 void increase_angle(int old_ang,int new_ang,Servo servo, int speed_){
   for(int ang=old_ang;ang<=new_ang;ang++){
       servo.write(ang);
       delay(speed_);
     }
 }
 
 void increase_angle_simultaneously(int old_ang,int new_ang,Servo servo1,Servo servo2, int speed_){
   for(int ang=old_ang;ang<=new_ang;ang++){
       servo1.write(ang);
       servo2.write(ang);
       delay(speed_);
     }
 }    
 
 void increase_angle_simultaneously_base(int old_ang,int new_ang,Servo servo1,Servo servo2, int speed_){
   int lCounter=180-old_ang;
   int rCounter=old_ang;
   for(int ang=old_ang;ang<=new_ang;ang++){
       servo1.write(lCounter--);
       servo2.write(rCounter++);
       delay(speed_);
     }
 }
     
     
 void decrease_angle(int old_ang,int new_ang,Servo servo,int speed_){
   for(int ang=old_ang;ang>=new_ang;ang--){
       servo.write(ang);
       delay(speed_);
     }
 }
 
 void decrease_angle_simultaneously(int old_ang,int new_ang,Servo servo1,Servo servo2,int speed_){
   for(int ang=old_ang;ang>=new_ang;ang--){
       servo1.write(ang);
       servo2.write(ang);
       delay(speed_);
     }
 }
 
  void decrease_angle_simultaneously_base(int old_ang,int new_ang,Servo servo1,Servo servo2,int speed_){
   int lCounter=180-old_ang;
   int rCounter=old_ang;
   for(int ang=old_ang;ang>=new_ang;ang--){
       servo1.write(lCounter++);
       servo2.write(rCounter--);
       delay(speed_);
     }
 }
     
     
 void getHome(){
   if(lBase.read()>90){
     decrease_angle(lBase.read(),90,lBase,speed_[0]);
   }else if(lBase.read()<90){
     increase_angle(lBase.read(),90,lBase,speed_[0]);
   }
   
   if(lElbow.read()>90){
     decrease_angle(lElbow.read(),90,lElbow,speed_[2]);
   }else if(lElbow.read()<90){
     increase_angle(lElbow.read(),90,lElbow,speed_[2]);
   }
   
   if(lShoulder.read()>90){
     decrease_angle(lShoulder.read(),90,lShoulder,speed_[1]);
   }else if(lShoulder.read()<90){
     increase_angle(lShoulder.read(),90,lShoulder,speed_[1]);
   }
   
   if(lWristRot.read()>110){
     decrease_angle(lWristRot.read(),110,lWristRot,speed_[3]);
   }else if(lWristRot.read()<110){
     increase_angle(lWristRot.read(),110,lWristRot,speed_[3]);
   }
   
   if(lWristPitch.read()>90){
     decrease_angle(lWristPitch.read(),90,lWristPitch,speed_[4]);
   }else if(lWristPitch.read()<90){
     increase_angle(lWristPitch.read(),90,lWristPitch,speed_[4]);
   }
   
   if(lWristRoll.read() > 0){
     decrease_angle(lWristRoll.read(),0,lWristRoll,speed_[5]);
   }
   
   if(lGripper.read()<95){
     increase_angle(lGripper.read(),95,lGripper,speed_[6]);
   } 
}

 void Both_getHome(){
   if(lBase.read()>90 && rBase.read()>90){
     decrease_angle_simultaneously(lBase.read(),90,lBase,rBase,speed_[0]);
   }else if(lBase.read()<90 && rBase.read()<90){
     increase_angle_simultaneously(lBase.read(),90,lBase,rBase,speed_[0]);
   }
   
   if(lElbow.read()>90 && rElbow.read()>90){
     decrease_angle_simultaneously(lElbow.read(),90,lElbow,rElbow,speed_[2]);
   }else if(lElbow.read()<90 && rElbow.read()<90){
     increase_angle_simultaneously(lElbow.read(),90,lElbow,rElbow,speed_[2]);
   }
   
   if(lShoulder.read()>90 && rShoulder.read()>90){
     decrease_angle_simultaneously(lShoulder.read(),90,lShoulder,rShoulder,speed_[1]);
   }else if(lShoulder.read()<90 && rShoulder.read()<90){
     increase_angle_simultaneously(lShoulder.read(),90,lShoulder,rShoulder,speed_[1]);
   }
   
   if(lWristRot.read()>110 && rWristRot.read()>110){
     decrease_angle_simultaneously(lWristRot.read(),110,lWristRot,rWristRot,speed_[3]);
   }else if(lWristRot.read()<110 && rWristRot.read()<110){
     increase_angle_simultaneously(lWristRot.read(),110,lWristRot,rWristRot,speed_[3]);
   }
   
   if(lWristPitch.read()>90 && rWristPitch.read()>90){
     decrease_angle_simultaneously(lWristPitch.read(),90,lWristPitch,rWristPitch,speed_[4]);
   }else if(lWristPitch.read()<90 && rWristPitch.read()<90){
     increase_angle_simultaneously(lWristPitch.read(),90,lWristPitch,rWristPitch,speed_[4]);
   }
   
   if(lWristRoll.read() > 0 && rWristRoll.read() > 0){
     decrease_angle_simultaneously(lWristRoll.read(),0,lWristRoll,rWristRoll,speed_[5]);
   }
   
   if(lGripper.read()<95 && rGripper.read()<95){
     increase_angle_simultaneously(lGripper.read(),95,lGripper,rGripper,speed_[6]);
   }
   
}

void moveArms_Simultaneously(int angle[]){
  int current=rBase.read(); 
   if(current!=angle[0]){
     if(angle[0] > current){
       increase_angle_simultaneously_base(current,angle[0],lBase,rBase,speed_[0]);
     }
     else{
       decrease_angle_simultaneously_base(current,angle[0],lBase,rBase,speed_[0]);
     }
   }
   
   current=lShoulder.read();
   if(current!=angle[1]){
     if(angle[1] > current){
       increase_angle_simultaneously(current,angle[1],lShoulder,rShoulder,speed_[1]);
       increase_angle(rShoulder.read(),(rShoulder.read()+6),rShoulder,speed_[1]);
     }
     else{
       decrease_angle_simultaneously(current,angle[1],lShoulder,rShoulder,speed_[1]);
       increase_angle(rShoulder.read(),(rShoulder.read()+6),rShoulder,speed_[1]);
     }
   }
   
   current=lElbow.read();
   if(current!=angle[2]){
     if(angle[2] > current){
       increase_angle_simultaneously(current,angle[2],lElbow,rElbow,speed_[2]);
       decrease_angle(rElbow.read(),(rElbow.read()-10),rElbow,speed_[2]);
     }
     else{
       decrease_angle_simultaneously(current,angle[2],lElbow,rElbow,speed_[2]);
       if(current>10){
         decrease_angle(rElbow.read(),(rElbow.read()-10),rElbow,speed_[2]);
       }
     }
   }
//   
   current=lWristRot.read();
   if(current!=angle[3]){
     if(angle[3] > current){
       increase_angle_simultaneously(current,angle[3],lWristRot,rWristRot,speed_[3]);
       decrease_angle(rWristRot.read(),(rWristRot.read()-15),rWristRot,speed_[3]);
     }
     else{
       decrease_angle_simultaneously(current,angle[3],lWristRot,rWristRot,speed_[3]);
       if(current>15){
         decrease_angle(rWristRot.read(),(rWristRot.read()-15),rWristRot,speed_[3]);
       }
     }
   }
//   
   current=lWristPitch.read();
   if(current!=angle[4]){
     if(angle[4] > current){
       increase_angle_simultaneously(current,angle[4],lWristPitch,rWristPitch,speed_[4]);
     }
     else{
       decrease_angle_simultaneously(current,angle[4],lWristPitch,rWristPitch,speed_[4]);
     }
   }
   
   current=lWristRoll.read();
   if(current!=angle[5]){
     if(angle[5] > current){
       increase_angle_simultaneously(current,angle[5],lWristRoll,rWristRoll,speed_[5]);
       decrease_angle(rWristRoll.read(),(rWristRoll.read()-30),rWristRoll,speed_[5]);
     }
     else{
       decrease_angle_simultaneously(current,angle[5],lWristRoll,rWristRoll,speed_[5]);
       if(current>40){
         decrease_angle(rWristRoll.read(),(rWristRoll.read()-30),rWristRoll,speed_[5]);
       }
     }
   }
   
   current=lGripper.read();
   if(current!=angle[6]){
     if(angle[6] > current){
       increase_angle_simultaneously(current,angle[6],lGripper,rGripper,speed_[6]);
       decrease_angle(rGripper.read(),rGripper.read()-10,rGripper,speed_[6]);
     }
     else{
       decrease_angle_simultaneously(current,angle[6],lGripper,rGripper,speed_[6]);
       decrease_angle(rGripper.read(),rGripper.read()-10,rGripper,speed_[6]);
     }
   }
}
