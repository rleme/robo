     
#https://developer.ibm.com/answers/questions/355347/watson-visual-recognition-python-api-request-probl/ 
try:
         url = 'https://watson-api-explorer.mybluemix.net/visual-recognition/api/v3/detect_faces?api_key=<EnterAPIKeyHere>&version=2016-05-20'
     
         with open("C:/<FileLocation>.jpg", 'rb') as image:
             filename = image.name
             mime_type = mimetypes.guess_type(
                 filename)[0] or 'application/octet-stream'
             files = {'images_file': (filename, image, mime_type)}
             r = requests.request(method = "POST", url= url, files=files)
             print(r.text)
     
     except:
         print("An Error occured uploading files")
