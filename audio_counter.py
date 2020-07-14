import sys
import os
import re



def count(): 
    the_file = open("july_dataset", "r")
    category_id=""
    while True:
        line = the_file.readline() 
        if line :
            if line=="gs://otsimo-eu/speech-data-june/:" or line=="" : continue
            num = line.count("/")
            count= 0
            if(num==5):
                while(True):
                    position1= the_file.tell()
                    line2 = the_file.readline() 
                    position2 = the_file.tell()
                    num2 = line2.count("/")
                    label= bool(re.match("^gs://otsimo-eu/", line2))
                    eof=re.search("^TOTAL", line2)
                    if num2==5 : #new folder
                        print(f"category_id: {category_id}, audio_files: {count}") 
                        the_file.seek(position1)
                        break
                    elif num2==6 and label  :  #name the folder
                        x = re.split("gs://otsimo-eu/speech-data-june/", line2)
                        y = re.split("/", x[1])
                        category_id = y[0]
                    elif bool(eof) :      # end of file 
                        print(f"category_id: {category_id}, audio_files: {count}")
                        print("finished")
                        break
                    elif line2=="" : continue
                    else : count += 1
        else : break
                
    the_file.close() 

if __name__ == "__main__":
    count() 
