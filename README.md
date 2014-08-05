#Code Exercise
This is my code for exercises from the book Python 3 Object Oriented Programming.

## Chapter 2
The files menu.py and audio_scraper.py are my two files for this chapter's exercise.  I rewrote my audio scraper (that pulls audio from
packet captures and rebuilds it as a raw audio file) to be object oriented.  To fit the chapter's goals, I used a similar menu driven system,
where the user inputs 1 for audio scraping, and then gets prompted to input the: pcap file name, the layer they want to scrape (i.e. rtp) and the
output filename they prefer.

After the user input, it sends the values back into the Audio_Scraper class, calling the scraper method to do it's magic (outputing a raw audio file
from the pcap provided.)