from aptbot import scrape
import settings
import time
import sys
import traceback

if __name__=="__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        try:
            scrape()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Succesful scrape".format(time.ctime()))
        time.sleep(settings.SLEEP_INTERVAL)
