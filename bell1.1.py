import paho.mqtt.client as mqtt 
#import bluetooth
from gtts import gTTS
from pygame import mixer
from time import sleep 
broker="mqtt-dashboard.com"
port=8884
tp="bell/caf"
id='Bell'

def on_connect(cl, userdata, flags, rc, properteis) :
  if rc == 0:
          print("Conectado")
         # cl.publish(tp,"conectado")
      
  else:
         print(f"desconectado codigo {str(rc)}")
  
def on_message(cl, userdata, msg):
  data=str(msg.payload.decode("utf-8"))
  print(data)
  ms=gTTS(data,lang="pt-br")  
  ms.save("ms.mp3")
  mixer.init()
  voz= mixer.Sound("ms.mp3")
  
  l=0
  t=0
  if  "Intervalo" in data:
    #esta é a parte do programa fazerá o speaker do intervalo 
      while t<3:
                sino= mixer.Sound("sino.mp3")
                sino.play()
                voz.play()
                print("feito")
                l=l+1
                sleep(3)
              
              
      
  else:
       while l<3:
         #esta cuidará dos avisos e anúncio 
              voz.play() 
              t=t+1
              sleep(3)
                
               
      
  
cl = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
cl.on_connect = on_connect
cl.on_message = on_message
cl.connect(broker)
while True:
      cl.subscribe(tp)
      cl.loop_forever()
