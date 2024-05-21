import paho.mqtt.client as mqtt #biblioteca para usar o protocolo mqtt no Python 
#import bluetooth
from gtts import gTTS#API para conversão do texto em áudio 
from pygame import mixer#biblioteca para emitir son
from time import sleep # Está é um tipo de delay no Python 
import socket as x


broker="mqtt-dashboard.com"
port=8884
tp="bell/caf"
id='Bell'

def on_connect(cl, userdata, flags, rc, properteis) :#funcao que verificar a conexão ao broker 
  if rc == 0:
          print("Conectado")
         # cl.publish(tp,"conectado")
      
  else:
         print(f"desconectado codigo {str(rc)}")
  
def on_message(cl, userdata, msg):#funcao de recepção de sms do Brooker aqui acontece toda magia 🎙️
  data=str(msg.payload.decode("utf-8"))
  print(data)
  ms=gTTS(data,lang="pt-br")  
  ms.save("ms.mp3")
  mixer.init()
  voz= mixer.Sound("ms.mp3")
  
  l=0
  t=0
  pos=data.find("Intervalo")
  if  pos==0:
    #esta é a parte do programa fazerá o speaker do intervalo 
      while t<3:
                sino= mixer.Sound("sino.mp3")
                sino.play()
                voz.play()
                print("feito")
                t=t+1
                sleep(4)
              
              
      
  else:
       while l<3:
         #esta cuidará dos avisos e anúncio 
              voz.play() 
              l=l+1
              sleep(4)
                
               
      
  
cl = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
cl.on_connect = on_connect
cl.on_message = on_message
cl.connect(broker)
while True:
      cl.subscribe(tp)
      cl.loop_forever()
