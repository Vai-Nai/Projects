from vaisnav_word_count import get_word_count, get_unique_word_count, get_word_frequency, is_not_none
import logging
import logging.config
import configparser

config=configparser.ConfigParser()
config.read("word_count.ini")
logging.config.fileConfig("word_count.ini")

try:
    logger=logging.getLogger("main")
    file_name=input("\nEnter File Name: ")
    print("")
    if file_name=="":
        print("\nPlease enter a value!!")
    else:
        file=open(file_name,'r')
        text=file.read()
        ch=1
        while ch!=0:
            print("\n0.EXIT\n1.GET WORD COUNT\n2.GET UNIQUE WORD COUNT\n3.GET INDIVIDUAL COUNT")
            ch=int(input("Enter Choice: "))
            if(ch==1):
                total=get_word_count(text)
                print("\nThe Total Number of words is: ",total)
                if is_not_none(total):    
                    logger.info("Total Word Count: %d",total)
                else:
                    logger.info("Total Word Count: 0")
            elif(ch==2):
                total=get_unique_word_count(text)
                print("\nThe Total Number of Unique Words is: ",total)
                if is_not_none(total):
                    logger.info("Unique Word Count: %d",total)
                else:
                    logger.info("Unique Word Count: 0")
            elif(ch==3):
                Dict=get_word_frequency(text)
                print("\nIndividual Count is: ")
                for i in Dict:
                    print(i,Dict[i])
                if is_not_none(Dict):
                    logger.info("Word Frequency: %s",Dict)
            elif(ch==0):
                logger.info("Exiting")
                exit
            else:
                print("Please Enter a Valid Choice!!")
        file.close()
except FileNotFoundError:
    print("\nRecheck the Name of the file or Check if it exists!!")
    print("(Include file type also)")
    logger.error("Error in the Name of the File")
except TypeError:
    print("\nNo Words Exists in the File to Count")
    logger.error("Word Frequency: {}")
    
