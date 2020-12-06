from skimage import data, io, filters
from matplotlib import pyplot as plt

import numpy as np
import generator
import docopt
import test
import opencv
import os


if __name__ == '__main__':
    with open("data/settings/settings.tylski") as f:
        options = f.readlines()
    if options[0][0] == "y":
        stop_after_diagnosis = True
    else:
        stop_after_diagnosis = False
    if options[0][1] == "y":
        save = True
    else:
        save = False
    print("OPTIONS")
    print("1 - Test one banknote")
    print("2 - Test all banknotes")
    print("3 - Create samples for one banknote")
    print("4 - Train your cascade")
    print("5 - Generate negative description file")
    print("6 - Generate positive description file")
    print("7 - Change settings")
    print("Select option:")
    n = input()
    if n == "1":
        print("Choose banknote:")
        banknote = input()
        assert(banknote in ("10","20","50","100")), "Wrong banknote"
        print("Images:")
        print(", ".join(os.listdir("tests")[1:]).replace(".jpg","").replace(".JPG",""))
        print("Enter image name: ")
        filename = input()
        assert(filename+".jpg" in os.listdir("tests")), "Wrong image name"
        print("Testing "+str(banknote)+" pln")
        test.testImage(filename, banknote, stop_after_diagnosis, save)
    elif n == "2":
        print("Images:")
        print(", ".join(os.listdir("tests")[1:]).replace(".jpg", "").replace(".JPG", ""))
        print("Enter image name: ")
        filename = input()
        assert (filename + ".jpg" in os.listdir("tests")[1:]), "Wrong image name"
        print("Testing all banknotes")
        test.testImage(filename, "69", True, True)
    elif n == "3":
        print("Choose banknote:")
        banknote = input()
        assert (banknote in ("10", "20", "50", "100")), "Wrong banknote"
        print("Starting create samples for " + str(banknote) + " pln")
        opencv.createSamples(banknote)
        print("\033[92mIf " + "data/pos"+str(banknote)+".txt("+str(len(os.listdir("data/images/p"+str(banknote)))+1)+") : parse error appeared, process was successful \033[0m")
    elif n == "4":
        print("Choose banknote to training:")
        banknote = input()
        assert (banknote in ("10", "20", "50", "100")), "Wrong banknote"
        assert(len(os.listdir("data/cascade"+str(banknote))) == 0), "data/cascade"+str(banknote) + " directory must be empty to train"
        print("Starting train cascade for " + str(banknote) + " pln")
        opencv.trainCascade(banknote)
        print("\033[92mIf Required leaf false alarm rate achieved. Branch training terminated, process was successful \033[0m")
    elif n == "5":
        print("Choose banknote: ")
        banknote = input()
        assert (banknote in ("10", "20", "50", "100")), "Wrong banknote"
        generator.generate_negative_description_file()
    elif n == "6":
        print("Choose banknote: ")
        banknote = input()
        assert (banknote in ("10", "20", "50", "100")), "Wrong banknote"
        print("\033[93mWarning! If you have rectangles of your banknotes saved in the file data/pos" + str(
            banknote) + ".txt, make a backup before generating it otherwise all your work will disappear!\033[0m")
        print("Do you want to continue? (y/n)")
        d = input()
        assert(d in ("y", "n")), "Wrong input!"
        if d == "y":
            generator.generate_positive_description_file(banknote)
    elif n == "7":
        print("Do you want save your results after test banknotes? (y/n)")
        stop_after_diagnosis = input()
        assert(stop_after_diagnosis in ("y", "n")), "Wrong input! The settings have not been saved"
        print("Do you want save your results after test banknotes? (y/n)")
        save = input()
        assert(save in ("y", "n")), "Wrong input! The settings have not been saved"
        f = open('data/settings/settings.tylski',"w")
        f.write(stop_after_diagnosis)
        f.write(save)
        f.close()
        print("The settings have been changed successfully")



    else:
        print("Wrong option!")