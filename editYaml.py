import sys
import os


if __name__ == '__main__':
    pathManifest=sys.argv[1]
    newImage=sys.argv[2]

    newfile=""

    with open(pathManifest,"r") as f:
        list_doc = f.readlines()
        for line in list_doc:
            wl=line
            if "image:" in wl:
                h=wl.split(":")
                wl=h[0]+ ": " +newImage + "\n"
            newfile=newfile+wl

    with open(pathManifest,"w") as f:
        f.write(newfile)
