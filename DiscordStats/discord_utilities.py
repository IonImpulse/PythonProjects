import csv
import requests
import tkinter as tk
from tkinter import filedialog
import os
import sys
import pickle
import time
import shutil

def remove_punctuation(string) :
    bad_chars = [".", ",", "?", "\"", "\'", "!", "*", "&", "@", "#", "$", "%", "^", "(", ")", ":", ";", "<", ">", "\\", "/", "-", "_", "`",]
    
    output = string.lower()

    for bad_char in bad_chars :
        output = output.replace(bad_char, "")
    
    return output

class author :
    def __init__(self, name) :
        self.names = [name]
        self.message_count = 0
        self.word_count = 0
        self.character_count = 0

        self.time_ledger = []
        self.vocab_dict = {}
        self.attachments_ledger = []
    
    def process_message(self, name, time, message, attachments) :
        self.message_count += 1
        self.word_count += len(message.split(" "))
        self.character_count += len(message)

        for word in message.split(" ") :
            clean_word = remove_punctuation(word)

            if clean_word in self.vocab_dict :
                self.vocab_dict[clean_word] += 1
            else :
                self.vocab_dict[clean_word] = 1
        
        if name not in self.names :
            self.names.append(name)

        self.time_ledger.append(time)

        if attachments != "" :
            self.attachments_ledger += attachments.split(',')

    def sort_time(self, time_format) :
        self.time_ledger = sorted((time.strptime(d, time_format) for d in self.time_ledger), reverse=True)

class discord_utilities :
    def __init__(self, headless = True) :
        #Initialize some variables that will be used later
        #headless is essentially a debug switch
        self.headless = headless
        self.user = os.environ.get('USERNAME')
        self.state = "initalized"
        self.schema = ["AuthorID", "Author", "Date", "Content", "Attachments", "Reactions"]
        self.time_format = "%d-%b-%y %I:%M %p"
        
        self.SERVER_AUTHOR = author("SERVER_AUTHOR")

    def locate_data(self, input_path = "", output_path = "") :
        if self.headless == False :
            root = tk.Tk()
            root.withdraw()
            
            self.input_dir = filedialog.askdirectory().replace("/", "\\")
            self.output_dir = self.input_dir + "\\DU Output"
            
            #Create output dirs
            if os.path.exists(self.output_dir) == False :
                os.makedirs(self.output_dir)
            if os.path.exists(self.output_dir + '\\Attachments\\') == False :
                os.makedirs(self.output_dir + '\\Attachments\\')

        #Try to load author aliases from file, but creates a new one if it is not found
        try:
            with open(self.output_dir + "\\authors.list", 'rb') as f :
                self.author_list = pickle.load(f)

            shutil.copyfile(self.output_dir + "\\authors.list", self.output_dir + "\\authors.list.bak")

        except Exception as e:
            print(e)
            self.author_list = {}

        #Create list of all files, full name
        self.file_list = [name for name in os.listdir(self.input_dir) if name[-3:] == "csv"]

        #Create dictionary with the key being the unique channel ID number
        self.file_dict = {}

        #Loop through all files to create dict
        for full_name in self.file_list :
            temp = str(full_name[full_name.index(" - ") + 3:-4])
            
            name, number = temp.split(" ")
            number = number.replace("[", "").replace("]", "")

            self.file_dict[number] = [name, full_name]

        #Get name of server by indexing at the " - " seperator
        self.server_name = self.file_list[0][:self.file_list[0].index(" - ")]

        if self.headless == False :
            print("==" + str(self.server_name) + "==")
            print("Files found:")
            for index, name in enumerate(self.file_list) :
                print(str(index) + ": " + str(name[name.index(" - ") + 3:]))
        
        #Set state so someone doesn't try to run them out of order
        self.state = "located"

    def scrape_stats(self, file_number) :
        if self.state == "located" :

            input_file = self.file_dict[file_number][1]

            with open(self.input_dir + "\\" + input_file, newline = "", encoding="utf8") as f :
                data_set = [row for row in csv.reader(f, delimiter = ',')]
                #Delete header row
                data_set = data_set[1:]
            
            for message in data_set :
                #0 = Author ID
                if message[0] not in self.author_list :
                    #1 = Author Name
                    self.author_list[message[0]] = author(message[1])
                
                #1 = Author Name
                #2 = Date
                #3 = Content
                #4 = Attachments
                self.author_list[message[0]].process_message(message[1], message[2], message[3], message[4])
                self.SERVER_AUTHOR.process_message(message[1], message[2], message[3], message[4])
        
        self.save_aliases()

    def scrape_images_from_file(self, file_number) :
        if self.state == "located" :

            input_file = self.file_dict[file_number][1]
            
            image_prefix = self.file_dict[file_number][0] + "_"

            output_path = self.output_dir + '\\Attachments\\' + image_prefix + "\\"

            if os.path.exists(output_path) == False :
                os.makedirs(output_path)

            start = 0

            with open(self.input_dir + "\\" + input_file, newline = "", encoding="utf8") as f :
                raw_data = [row for row in csv.reader(f, delimiter = ',')]

            raw_data = raw_data[1:]

            photo_index = self.schema.index("Attachments")
            
            request_list = []
            
            for index, column in enumerate(raw_data) :
                if column[photo_index] != "" :
                    request_list.append(column[photo_index])

            counter = 0
            
            for index, url in enumerate(request_list) :
                temp_URLS = url.split(',')
                
                if self.headless == False :
                    print("Message " + str(index + 1) + " out of " + str(len(request_list)))
                    print("Found " + str(len(temp_URLS)) + " photo(s)")

                for i in temp_URLS :
                    try:
                        if index >= int(start) :
                            temp_img = requests.get(i)
                            output_path = output_path + image_prefix + str(counter) + '.' + temp_img.url.split('.')[-1]
                            open(output_path, 'wb').write(temp_img.content)
                        counter += 1
                    except Exception as e:
                        if self.headless == False :
                            print(e)
                            print("Could not get photo #" + str(i))
        
        else :
            print("Error: files not yet located. Try running locate_data() first...")
    
    def get_quotes(self, file_number) :
        pass
    
    def save_aliases(self) :
        with open(self.output_dir + "\\authors.list", 'wb') as f :
            pickle.dump(self.author_list, f)
    
    def bulk_scrape_stats(self, exclude=[]) :
        
    def export_stats(self) :
        pass

if __name__ == "__main__":
    scraper = discord_utilities(headless=False)
    scraper.locate_data()
    scraper.scrape_stats("607850285938901013")