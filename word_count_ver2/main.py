from vaisnav_word_count import word_functions, file_empty_exception
import logging
import logging.config
import configparser

config=configparser.ConfigParser()
config.read("word_count.ini")
logging.config.fileConfig("word_count.ini")


logger=logging.getLogger("main")
try:
    file_name=input("\nEnter File Name: ")
    print("")
    if file_name=="":
        print("\nPlease enter a value!!")
    else:
        file=open(file_name,'r')
        text=file.read()
        wf=word_functions(text)
        ch=1
        while ch!=0:
            print("\n0.EXIT\n1.GET WORD COUNT\n2.GET UNIQUE WORD COUNT\n3.GET INDIVIDUAL COUNT")
            ch=int(input("Enter Choice: "))
            if(ch==1):
                total=wf.get_word_count()
                print("\nThe Total Number of words is: ",total)
                logger.info("Total Word Count: %d",total)
            elif(ch==2):
                total=wf.get_unique_word_count()
                print("\nThe Total Number of Unique Words is: ",total)
                logger.info("Unique Word Count: %d",total)
            elif(ch==3):
                Dict=wf.get_word_frequency()
                print("\nIndividual Count is: ")
                for i in Dict:
                    print(i,Dict[i])
                logger.info("Word Frequency",Dict)
            elif(ch==0):
                exit
                logger.info("Exiting")
            else:
                print("Please Enter a Valid Choice!!")
        file.close()
except file_empty_exception:
    print("File Empty")
    logger.error("File Empty")
except FileNotFoundError:
    print("\nRecheck the Name of the file or Check if it exists!!")
    print("(Include file type also)")
    logger.error("Error in the name of the File")
except TypeError:
    print("No Words Exists in the File to count")
    logger.error("Word Frequency: {}")
