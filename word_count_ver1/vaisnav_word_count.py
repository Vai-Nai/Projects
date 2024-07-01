import logging
import logging.config
import configparser

config=configparser.ConfigParser()
config.read("word_count.ini")
logging.config.fileConfig("word_count.ini")

logger=logging.getLogger("wordfunctions")
class file_empty_exception(Exception):
    pass

def is_not_none(value):
    ''' Check if the value is None or not
        args:
            any: value to be checked

        returns:
            bool: True if value id None, else False'''
    if value == None:
        return False
    else:
        return True

def get_word_count(text):
    ''' Counts the total number of words in the file
        args:
            text (string): File content as String 

        returns:
            int: Length of the Array that contains all the words'''
    try:
        if text=="":
            raise file_empty_exception
            logger.error("Empty File is Initialized")
            length=0
        text_array=text.split()
        if is_not_none(len(text_array)):
            logger.debug("Total Word Count: %d",len(text_array))
        else:
            logger.debug("Total Word Count: 0")
        return len(text_array)
    except file_empty_exception:
        print("File is Empty")

def get_unique_word_count(text):
    '''Counts the unique words in the file
        args:
            text (String): File content as String

         returns:
             int: Length of Temporary Array that contains only unique elements'''
    try:
        if text=="":
            raise file_empty_exception
            logger.error("Empty File is Initialized")
        text_Array=set(text.split())
        if is_not_none(len(text_Array)):
            logger.debug("Unique Word Count: %d", len(text_Array))
        else:
            logger.debug("Unique Word Count: 0")
        return len(text_Array)
    except file_empty_exception:
        print("File is Empty")

def get_word_frequency(text):
    '''Counts the frequency of all words in the file
        args:
            text (String): File content as String

        returns:
            Dict: Dictionary that contains word and count pairs'''
    try:
        if text=="":
            raise file_empty_exception
            logger.error("Empty File is Initialized")
        text_Array=text.split()
        temp_Dict={}
        j=""
        for i in text_Array:
            if i[0]=='\n':
                j=i[i:len(i)-1]
            if j not in temp_Dict:
                temp_Dict[i]=text_Array.count(i)
        if is_not_none(temp_Dict):
            logger.debug("Word Frequency: %s", temp_Dict)
        else:
            logger.debug("Word Frequency: {}")
        return temp_Dict
    except file_empty_exception:
        print("File is Empty")
        
        
        
    
    


