# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
from datetime import datetime
from pytz import timezone

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate ):
        self.guid = guid 
        self.title = title 
        self.description = description
        self.link = link 
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid 

    def get_title(self):
        return self.title 

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError



class PhraseTrigger(Trigger):
    def __init__(self, Trigger):
        self.Trigger = self.make_valid_phrase(Trigger)

    def get_Trigger(self):
        return self.Trigger

    def make_valid_phrase(self, phrase):
        phrase = phrase.lower()
        for punctuation in string.punctuation:
            phrase = phrase.replace(punctuation,' ')
        phrase = ' '.join(phrase.split())
        return phrase

    def is_phrase_in(self, text):
        Trigger = self.get_Trigger()
        text = self.make_valid_phrase(text)
        result = []
        Trigger_list = Trigger.split()
        for word in Trigger_list:
            if word in text.split() and Trigger in text:
                result.append(True)
            else:
                result.append(False)
        if all(result) == True:
            return True  
        else:
            return False 



class TitleTrigger(PhraseTrigger):

    def __init__(self,Trigger):
        self.Trigger = self.make_valid_phrase(Trigger)

    def get_Trigger(self):
        return self.Trigger
   
    def evaluate(self, NewsStory):
        text = self.make_valid_phrase(NewsStory.get_title())
        return self.is_phrase_in(text)

class DescriptionTrigger(PhraseTrigger):
    def __init__(self,Trigger):
        self.Trigger = self.make_valid_phrase(Trigger)

    def get_Trigger(self):
        return self.Trigger

    def evaluate(self, NewsStory):
        text = self.make_valid_phrase(NewsStory.get_description())
        return self.is_phrase_in(text)



class TimeTrigger(Trigger):
    def __init__(self,time):
        time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        self.time = time 

    def get_time(self):
        return self.time 

class BeforeTrigger(TimeTrigger):
    def __init__(self,time):
        time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        self.time = time.astimezone(pytz.timezone('US/Eastern'))

    def evaluate(self, NewsStory):
        time_of_news = NewsStory.get_pubdate()
        if type(time_of_news) == str:
            time_of_news = datetime.strptime(time_of_news, '%d %b %Y %H:%M:%S')
            time_of_news = time_of_news.astimezone(pytz.timezone('US/Eastern'))
        else:
            time_of_news = time_of_news.astimezone(pytz.timezone('US/Eastern'))
        if time_of_news < self.get_time():
            return True 
        else:
            return False

class AfterTrigger(TimeTrigger):
    def __init__(self,time):
        time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        self.time = time.astimezone(pytz.timezone('US/Eastern'))

    def evaluate(self, NewsStory):
        time_of_news = NewsStory.get_pubdate()
        if type(time_of_news) == str:
            time_of_news = datetime.strptime(time_of_news, '%d %b %Y %H:%M:%S')
            time_of_news = time_of_news.astimezone(pytz.timezone('US/Eastern'))
        else:
            time_of_news = time_of_news.astimezone(pytz.timezone('US/Eastern'))
        if time_of_news > self.get_time():
            return True 
        else:
            return False


class NotTrigger(Trigger):
    def __init__(self,TriggerObject):
        self.TriggerObject = TriggerObject

    def get_Trigger(self):
        return self.TriggerObject

    def evaluate(self,NewsStory):
        TriggerObject = self.get_Trigger()
        if TriggerObject.evaluate(NewsStory) == True:
            return False 
        else:
            return True 

class AndTrigger(Trigger):
    def __init__(self,TriggerObject1, TriggerObject2):
        self.TriggerObject1 = TriggerObject1
        self.TriggerObject2 = TriggerObject2

    def get_TriggerObject1(self):
        return self.TriggerObject1

    def get_TriggerObject2(self):
        return self.TriggerObject2

    def evaluate(self,NewsStory):
        TriggerObject1 = self.get_TriggerObject1()
        TriggerObject2 = self.get_TriggerObject2()
        if TriggerObject1.evaluate(NewsStory) == True and TriggerObject2.evaluate(NewsStory) == True:
            return True 
        else:
            return False

class OrTrigger(Trigger):
    def __init__(self,TriggerObject1, TriggerObject2):
        self.TriggerObject1 = TriggerObject1
        self.TriggerObject2 = TriggerObject2

    def get_TriggerObject1(self):
        return self.TriggerObject1

    def get_TriggerObject2(self):
        return self.TriggerObject2

    def evaluate(self,NewsStory):
        TriggerObject1 = self.get_TriggerObject1()
        TriggerObject2 = self.get_TriggerObject2()
        if TriggerObject1.evaluate(NewsStory) == True or TriggerObject2.evaluate(NewsStory) == True:
            return True 
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered_stories.append(story)

    filtered_stories = list((dict.fromkeys(filtered_stories))) 
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    def trigger_definition(line):
        '''input is a string in form e.g. 't1,DESCRIPTION,lego'
           returns a trigger based on text input '''
        if line_list[1] == 'DESCRIPTION':
            trigger = DescriptionTrigger(line_list[2])
        if line_list[1] == 'TITLE':
            trigger = TitleTrigger(line_list[2])
        if line_list[1] == 'AFTER':
            trigger = AfterTrigger(line_list[2])
        if line_list[1] == 'BEFORE':
            trigger = BeforeTrigger(line_list[2])
        if line_list[1] == 'NOT':
            trigger = NotTrigger(line_list[2])
        if line_list[1] == 'AND':
            trigger = AndTrigger(line_list[2],line_list[3])
        if line_list[1] == 'OR':
            trigger = OrTrigger(line_list[2],line_list[3])
        return trigger 

    trigger_list = []
    trigger_dictionary = {}
    for line in lines:
        line_list = line.split(',')
        if line.startswith('ADD'):
            for item in line_list[1:]: 
                trigger_list.append(trigger_dictionary[item])
        else:
            trigger_dictionary[line_list[0]] = trigger_definition(line_list)
    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("brexit")
        t2 = DescriptionTrigger("boris")
        t3 = DescriptionTrigger("boris")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        triggerlist = read_trigger_config('triggers.txt')

        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

