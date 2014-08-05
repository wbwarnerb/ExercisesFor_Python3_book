from audio_scraper import Audio_Scraper
import sys

class Menu(Audio_Scraper):
    def __init__(self):
        self.choices = {
            "1": self.audio_scraper,
            "5": self.quit
        }
    def display_menu(self):
        print("""
        PCAP Menu

        1. Scrape audio from pcap
        5. Quit
        """)
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("That is not a valid option")
    def audio_scraper(self):
        pcap = input("Enter the name of your pcap file in this folder: ")
        filter_type = input("What layer do you want to filter on? (rtp) ")
        output_file = input("Provide your desired output filename: ")
        Audio_Scraper(pcap,filter_type,output_file).scraper()

    def quit(self):
        print("Thank you for using the PCAP app.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()