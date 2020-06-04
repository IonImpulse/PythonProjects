import csv
import requests
import tkinter as tk
from tkinter import filedialog
import os
import sys
import pickle

class discord_utilities :
    def __init__(self, headless = True) :
        #Initialize some variables that will be used later
        #headless is essentially a debug switch
        self.headless = headless
        self.user = os.environ.get('USERNAME')
        self.state = "initalized"
        self.schema = ["AuthorID", "Author", "Date", "Content", "Attachments", "Reactions"]
        
        #Try to load author aliases from file, but creates a new one if it is not found
        try:
            with open(self.output_dir + "\\authors.aliases") as f :
                self.author_aliases = pickle.load(f)
        except Exception as e:
            self.author_aliases = {}

    def locate_data(self, input_path = "", output_path = "") :
        if self.headless == False :
            root = tk.Tk()
            root.withdraw()
            
            self.input_dir = filedialog.askdirectory().replace("/", "\\")
            self.output_dir = self.input_dir + "\\discord_output"
            
            #Create output dirs
            if os.path.exists(self.output_dir) == False :
                os.makedirs(self.output_dir)
            if os.path.exists(self.output_dir + '\\files\\') == False :
                os.makedirs(self.output_dir + '\\files\\')

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
        pass
    def scrape_images(self, file_number) :
        
        if self.state == "located" :

            input_file = self.file_dict[file_number][1]
            
            image_prefix = self.file_dict[file_number][0] + "_"

            start = 0

            with open(self.input_dir + "\\" + input_file, newline = "", encoding="utf8") as file :
                raw_data = [row for row in csv.reader(file, delimiter = ',')]

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
                            output_path = self.output_dir + '\\files\\' + image_prefix + str(counter) + '.' + temp_img.url.split('.')[-1]
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
        with open(self.output_dir + "\\authors.aliases", 'w') as f :
            pickle.dump(self.author_aliases, f)

if __name__ == "__main__":
    scraper = discord_utilities(headless=False)
    scraper.locate_data()
    scraper.scrape_images("607850285938901013")