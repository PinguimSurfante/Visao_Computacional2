import cv2
print(cv2._version_)

rastreador = cv2.legacy.TrackerCSRT_create()

video = cv2.VideoCapture('WhatsApp Video 2022-11-19 at 21.32.22.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)
# print(bbox)


ok = rastreador.init(frame,bbox)
# print(ok)

while True:
    ok, frame = video.read()
    if not ok:
        break
    
    ok, bbox = rastreador.update(frame)
    print(bbox)

    if ok:
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2,1)
    else:
        cv2.putText(frame, 'falha no rastreamento', (100,80),
            cv2.FONT_HERSHEY_COMPLEX,.75, (0,0,255), 2)
        
    cv2.imshow('Rastreamento', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break