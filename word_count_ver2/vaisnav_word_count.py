import logging
import logging.config
import configparser

config=configparser.ConfigParser()
config.read("word_count.ini")
logging.config.fileConfig("word_count.ini")

class file_empty_exception(Exception):
    pass

class word_functions:

    def __init__(self,text):
        self.logger=logging.getLogger("wordfunctions")
        self.text=text
        if self.text=="":
            self.not_none_value=False
            self.logger.error("Initialized with Empty File")
            raise file_empty_exception
        else:
            self.not_none_value=True
            self.logger.info("Initialized with File Length %d",len(text))

    def get_word_count(self):
        ''' Counts the total number of words in the file

            returns:
                int: Length of the Array that contains all the words'''
        try:
            text_array=self.text.split()
            self.logger.debug("Total Word Count: %d",len(text_array))
            return len(text_array)
        except file_empty_exception:
            print("File is Empty")

    def get_unique_word_count(self):
        '''Counts the unique words in the file

             returns:
                 int: Length of array that contains only unique elements'''
        try:
            text_Array=set(self.text.split())
            self.logger.debug("Unique Word Count: %d",len(text_Array))
            return len(text_Array)
        except file_empty_exception:
            print("File is Empty")

    def get_word_frequency(self):
        '''Counts the frequency of all words in the file

            returns:
                Dict: Dictionary that contains word and count pairs'''
        try:
            text_Array=self.text.split()
            temp_Dict={}
            j=""
            for i in text_Array:
                if i[0]=='\n':
                    j=i[i:len(i)-1]
                if j not in temp_Dict:
                    temp_Dict[i]=text_Array.count(i)
            self.logger.debug("Frequencies of Words: ",temp_Dict)
            return temp_Dict
        except file_empty_exception:
            print("File is Empty")
