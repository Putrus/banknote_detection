import os
import subprocess


def createSamples(banknote):
    cmd = [
        os.path.join(os.path.abspath(os.getcwd()) + "\\data\\opencv\\build\\x64\\vc15\\bin", "opencv_createsamples.exe"),
        "-info data/pos"+str(banknote)+".txt",
        "-w 48",
        "-h 24",
        "-num 1000",
        "-vec data/vectors/pos"+str(banknote)+".vec"
    ]
    cmd = " ".join(cmd)
    subprocess.call(cmd, shell=True)


def trainCascade(banknote):
    file = open("data/pos"+str(banknote)+".txt")
    positive_count = 0
    for line in file:
        if line!="\n":
            positive_count+=1
    file.close()
    file2 = open("data/neg" + str(banknote) + ".txt")
    negative_count = 0
    for line in file2:
        if line != "\n":
            negative_count += 1
    file2.close()
    cmd = [
        os.path.join("D:\Python\PythonProjects\\beerdetection\\data\\opencv\\build\\x64\\vc15\\bin",
                     "opencv_traincascade.exe"),
        "-data data/cascade" + str(banknote)+"/",
        "-vec data/vectors/pos"+str(banknote)+".vec",
        "-bg data/neg"+str(banknote)+".txt",
        "-w 48",
        "-h 24",
        "-numPos "+str(positive_count),
        "-numNeg "+str(negative_count),
        "-numStages 10"
    ]
    cmd = " ".join(cmd)
    print(cmd)
    subprocess.call(cmd, shell=True)