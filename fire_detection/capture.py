import cv2 
import numpy as np
import playsound
import smtplib

fire_reported = 0
alarm_status = False
email_status = False

"""def play_audio():
    playsound.playsound("", True)"""
    
def send_email():
    recipientEmail = "martin.tin0042@gmail.com"
    recipientEmail = recipientEmail.lower()
    
    try: 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("system_email", 'password')
        server.sendmail('system_email', recipientEmail, "Se ha detectado fuego ahhhh")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
        print(e)        

video = cv2.VideoCapture("videos/fire.mp4")

while True:
    
    ret, frame = video.read()
    frame = cv2.resize(frame, (900, 600))
    blur = cv2.GaussianBlur(frame, (15,15),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    #rango de colores del fuego
    lower = [18,50,50]
    upper = [35,255,255]
    
    lower = np.array(lower,dtype="uint8")
    upper = np.array(upper,dtype="uint8")
    
    mask = cv2.inRange(hsv, lower, upper)
    
    output = cv2.bitwise_and(frame,hsv, mask=mask)
    
    size  =cv2.countNonZero(mask)
    threshold = 15000   #es el umbral de aceptación de que es fuego
                        #si el fuego es chiquito con 1000 ta bien si es más grande se puede incrementar 
                        #el valor
    
    if int(size) > threshold: 
        fire_reported = fire_reported + 1
        
        if fire_reported >= 1:
            if alarm_status == False: # este if es para la alarma
                pass
            if email_status == False:
                send_email()
                email_status = True
        
        pass
    if ret == False:
        break
    
    cv2.imshow("fire", output)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): #presionar q para cerrar programa
        break
    
cv2.destroyAllWindows()
video.release()