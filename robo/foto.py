import os,datetime
name=datetime.datetime.utcnow()
s = name.strftime("%Y-%m-%d-%H%M%SZ")
filename = 'IMG_' + s + '.jpg'
print (filename)
os.system('raspistill -o /home/pi/pictures/' + filename)
