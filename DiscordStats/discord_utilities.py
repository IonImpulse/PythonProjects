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
    bad_chars = [".", ",", "?", "\"", "\'", "!", "*", "&", "@", "#", "$", "%", "^", "(", ")", ";", "<", ">", "\\", "/", "-", "_", "`"]
    
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

        #Break the ingested message into each word, spliting by space
        for word in message.split(" ") :

            #Clean each word by removing any punctuation
            clean_word = remove_punctuation(word)

            #Check to make sure word is not just 
            #punctuation and therefore empty space
            if clean_word != "" :
                
                #If the word exists, increment by one
                #Otherwise, create a dictionary value and set to 1
                if clean_word in self.vocab_dict :
                    self.vocab_dict[clean_word] += 1
                else :
                    self.vocab_dict[clean_word] = 1
        
        #Add name to name dictionary if it doesn't exist
        if name not in self.names :
            self.names.append(name)

        #Add time to ledger
        self.time_ledger.append(time)

        #Add any attachments to ledger
        if attachments != "" :
            self.attachments_ledger += attachments.split(',')

    def sort_time(self, time_format) :
        
        #Sort the time ledger by formating each time value as a strptime value
        self.time_ledger = sorted((time.strptime(d, time_format) for d in self.time_ledger), reverse=True)

class discord_utilities :
    def __init__(self, headless = True) :
        #Initialize some variables that will be used later
        #headless is essentially a debug switch
        self.headless = headless
        self.user = os.environ.get('USERNAME')
        self.state = "initalized"
        self.schema = ["AuthorID", "Author", "Date", "Content", "Attachments", "Reactions"]
        self.author_list = {}
        self.time_format = "%d-%b-%y %I:%M %p"
        
        self.SERVER_AUTHOR = author("SERVER_AUTHOR")

    def locate_data(self, input_path = "") :
        
        #Check which mode to run in
        if self.headless == False :

            #If it's in user-interface mode, create and launch a dir opener
            root = tk.Tk()
            root.withdraw()
            
            self.input_dir = filedialog.askdirectory().replace("/", "\\")
        else :
            self.input_dir = input_path
        self.output_dir = self.input_dir + "\\DU Output"
            
        #Create output dirs
        if os.path.exists(self.output_dir) == False :
            os.makedirs(self.output_dir)
        if os.path.exists(self.output_dir + '\\Attachments\\') == False :
            os.makedirs(self.output_dir + '\\Attachments\\')
        if os.path.exists(self.output_dir + '\\Users\\') == False :
            os.makedirs(self.output_dir + '\\Users\\')

        #Create list of all files, full name
        self.file_list = [name for name in os.listdir(self.input_dir) if name[-3:] == "csv"]

        #Create dictionary with the key being the unique channel ID number
        self.file_dict = {}

        #Loop through all files to create dict
        for full_name in self.file_list :
            temp = str(full_name[full_name.index(" - ") + 3:-4])
            
            temp = temp.split("- ")
            name, number = temp[1].split(" ")
            number = number.replace("[", "").replace("]", "")

            self.file_dict[number] = [name, full_name]

        #Get name of server by indexing at the " - " seperator
        self.server_name = self.file_list[0][:self.file_list[0].index(" - ")]

        #Print out info if in user-interface mode
        if self.headless == False :
            print("==" + str(self.server_name) + "==")
            print("Files found:")
            for index, name in enumerate(self.file_list) :
                print(str(index) + ": " + str(name[name.index(" - ") + 3:]))
        
        #Set state so someone doesn't try to run them out of order
        self.state = "located"

    def scrape_stats(self, file_number, mode="no-keep") :
        if self.state == "located" :
            
            input_file = self.file_dict[file_number][1]

            with open(self.input_dir + "\\" + input_file, newline = "", encoding="utf8") as f :
                data_set = [row for row in csv.reader(f, delimiter = ',')]
                #Delete header row
                data_set = data_set[1:]

            if mode == "no-keep" :                
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

            elif mode == "return" : 
                return data_set
                
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
                            temp_img_suffix = url.split('.')[-1]
                            temp_img_name = url.split('.')[-2].split('/')[-1]                           
                            
                            print(temp_img_name)
                            temp_output_path = output_path + image_prefix + str(counter) + "_" + temp_img_name + '.' + temp_img_suffix
                            print("Out as:", temp_output_path)

                            if os.path.isfile(temp_output_path) == False :
                                with open(temp_output_path, 'wb') as f :
                                    temp_img = requests.get(i)
                                    f.write(temp_img.content)
                            else :
                                print("Skipping!")
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
            pickle.dump([self.author_list, self.SERVER_AUTHOR], f)
    
    def bulk_scrape_stats(self, exclude=[]) :
        for channel in self.file_dict :
            if channel not in exclude :
                self.scrape_stats(channel)

    def bulk_scrape_images(self, exclude=[]) :
        for channel in self.file_dict :
            if channel not in exclude :
                self.scrape_images_from_file(channel)

    def load_data(self) :
        if self.state == "located" :
        
            shutil.copyfile(self.output_dir + "\\authors.list", self.output_dir + "\\authors.list.bak")

            with open(self.output_dir + "\\authors.list", 'rb') as f :
                self.author_list, self.SERVER_AUTHOR = pickle.load(f)
                
    def create_text_file(self, exclude=[]) :
        all_data = []
        
        for channel in self.file_dict :
            if channel not in exclude :
                all_data += self.scrape_stats(channel, mode="return")

        output_text_array = []

        for row in all_data :
            output_text_array += ["[" + row[1] + "] " + row[3].replace("\n", "") + "\n"]

        with open(self.output_dir + "\\combined.txt", "w", newline='', encoding="utf8") as target :
            target.writelines(output_text_array)


    def export_stats(self) :
        with open(self.output_dir + "\\" + self.server_name + "_Master.csv", "w", newline='', encoding="utf8") as target :
            csv_writer = csv.writer(target, dialect="excel")
            csv_writer.writerow(["Statistics for:", str(self.server_name)])
            
            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Total Messages:", "Total Words:", "Total Characters:", "Total Attachments:"])
            csv_writer.writerow([self.SERVER_AUTHOR.message_count, self.SERVER_AUTHOR.word_count, self.SERVER_AUTHOR.character_count, str(len(self.SERVER_AUTHOR.attachments_ledger))])            
            csv_writer.writerow(["-----------------------------"])     
            
            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["List of Users:", ])
            csv_writer.writerow(["-----------------------------"])           
            for author_id in self.author_list :
                csv_writer.writerow([author_id + ":"] + self.author_list[author_id].names)

            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Message Count per User:"])
            csv_writer.writerow(["-----------------------------"])
            temp_sorted = sorted(self.author_list.items(), key=lambda author_id: author_id[1].message_count, reverse=True)
            for author_id in temp_sorted :
                csv_writer.writerow([author_id[1].names[-1] + ":", author_id[1].message_count])

            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Word Count per User:"])
            csv_writer.writerow(["-----------------------------"])
            temp_sorted = sorted(self.author_list.items(), key=lambda author_id: author_id[1].word_count, reverse=True)
            for author_id in temp_sorted :
                csv_writer.writerow([author_id[1].names[-1] + ":", author_id[1].word_count])

            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Character Count per User:"])
            csv_writer.writerow(["-----------------------------"])
            temp_sorted = sorted(self.author_list.items(), key=lambda author_id: author_id[1].character_count, reverse=True)
            for author_id in temp_sorted :
                csv_writer.writerow([author_id[1].names[-1] + ":", author_id[1].character_count])
            
            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Attachment Count per User:"])
            csv_writer.writerow(["-----------------------------"])
            temp_sorted = sorted(self.author_list.items(), key=lambda author_id: len(author_id[1].attachments_ledger), reverse=True)
            for author_id in temp_sorted :
                csv_writer.writerow([author_id[1].names[-1] + ":", len(author_id[1].attachments_ledger)])

            csv_writer.writerow(["-----------------------------"])
            csv_writer.writerow(["Top 50 Words:"])
            csv_writer.writerow(["-----------------------------"])
            top_words = sorted(self.SERVER_AUTHOR.vocab_dict.items(), key=lambda word: word[1], reverse=True)
            for index, word in enumerate(top_words[:1000]) :
                csv_writer.writerow([str(index + 1) + ":", word[0], word[1]])

        for author_id in self.author_list :
            output_name = "".join(x for x in self.author_list[author_id].names[-1] if x.isalnum())
            with open(self.output_dir + "\\Users\\" + output_name + ".csv", "w", newline='', encoding="utf8") as target :
                csv_writer = csv.writer(target, dialect="excel")
                csv_writer.writerow(["Statistics for:", str(self.server_name)])
                
                csv_writer.writerow(["-----------------------------"])
                csv_writer.writerow(["Total Messages:", "Total Words:", "Total Characters:", "Total Attachments:"])
                csv_writer.writerow(["-----------------------------"])
                csv_writer.writerow([self.author_list[author_id].message_count, self.author_list[author_id].word_count, self.author_list[author_id].character_count, str(len(self.author_list[author_id].attachments_ledger))])

                csv_writer.writerow(["-----------------------------"])
                csv_writer.writerow(["Top 50 Words not in Server 50:"])
                csv_writer.writerow(["-----------------------------"])
                temp_top_words = sorted(self.author_list[author_id].vocab_dict.items(), key=lambda word: word[1], reverse=True)
                count = 0
                index = 0
                output_list = []
                while count < 50 and index < len(temp_top_words) :
                    if temp_top_words[index][0] not in [x[0] for x in top_words[:50]] :
                        count += 1
                        output_list.append(temp_top_words[index])
                    index += 1

                for index, word in enumerate(output_list) :  
                    csv_writer.writerow([str(index + 1) + ":", word[0], word[1]])   

        with open(self.output_dir + "\\" + self.server_name + "_Timemap.csv", "w", newline='', encoding="utf8") as target :
            time_list = []
            for ampm in range(2) :
                for hour in range(12) :
                    for minute in range(60) :
                        if ampm == 0 :
                            half = "AM"
                        else :
                            half = "PM"
                        time_list.append([str(hour) + ":" + str(minute) + " " + half, 0])

            self.SERVER_AUTHOR.sort_time(self.time_format)

            for time_min in self.SERVER_AUTHOR.time_ledger :
                time_list[(time_min[3] * 60) + time_min[4]][1] += 1

            csv_writer = csv.writer(target, dialect="excel")
            csv_writer.writerow(["Timemap for:", str(self.server_name)])
            csv_writer.writerows(time_list)

#C:\\Users\\ionim\\Documents\\Ethan\\Programs\\Discord\\Logs\\Pullcord\\ALWEG\\Temp
#V:\\Programming\\Neural Networks\\lstm_lyrics_discord_server\\corpora\\Raw Data

if __name__ == "__main__":
    scraper = discord_utilities(headless=False)
    scraper.locate_data(input_path="V:\\Programming\\Temp CSVs")
    scraper.bulk_scrape_stats()
    scraper.load_data()
    scraper.export_stats()
    scraper.create_text_file()
    scraper.bulk_scrape_images()