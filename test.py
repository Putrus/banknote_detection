import cv2


def testbanknote(banknote, img, gray, stop_after_diagnosis,sum):
    classifier = cv2.CascadeClassifier("data/cascade"+str(banknote)+"/cascade.xml")
    thresh = 50
    scale = 1.05
    color = (255,255,255)
    if banknote == 10:
        thresh = 80
        color = (0,255,255)
    elif banknote == 20:
        thresh = 40
        color = (0,0,255)
    elif banknote == 50:
        thresh = 55
        color = (255,0,0)
    elif banknote == 100:
        thresh = 100
        color = (0,255,0)
    banknotes = classifier.detectMultiScale(gray, scale, thresh)
    if banknotes is ():
        print(str(banknote)+" pln not found")
    for (x, y, w, h) in banknotes:
        sum+=int(banknote)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        if stop_after_diagnosis:
            cv2.imshow('Instantaneous value: ' + str(sum), img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    return sum

def testImage(filename, what_banknote, stop_after_diagnosis, save):
    img = cv2.imread("tests/" + filename + ".jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sum=0
    if what_banknote == "10":
        sum=testbanknote(10, img, gray, stop_after_diagnosis, sum)
    elif what_banknote == "20":
        sum=testbanknote(20, img, gray, stop_after_diagnosis, sum)
    elif what_banknote == "50":
        sum=testbanknote(50, img, gray, stop_after_diagnosis, sum)
    elif what_banknote == "100":
        sum=testbanknote(100, img, gray, stop_after_diagnosis, sum)
    else:
        sum+=testbanknote(10, img, gray, stop_after_diagnosis,sum)
        sum+=testbanknote(20, img, gray, stop_after_diagnosis, sum)
        sum+=testbanknote(50, img, gray, stop_after_diagnosis, sum)
        sum+=testbanknote(100, img, gray, stop_after_diagnosis, sum)
    cv2.imshow('banknotes value: ' + str(sum), img)
    cv2.waitKey(0)
    if save:
        cv2.imwrite("tests/results/" + filename + "_result.jpg", img)
    cv2.destroyAllWindows()
    print("\033[96mThe value of banknotes was: "+str(sum)+"\033[0m")