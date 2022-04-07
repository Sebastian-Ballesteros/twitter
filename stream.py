from tweepy import Stream
import credentials


# Subclass Stream to print IDs of Tweets received
class TextPrinter(Stream):

    def on_status(self, status):
        print(f"{status.author.name} says:\n {status.text}\n\n")

printer = TextPrinter(
    credentials.API_KEY, credentials.API_SECRET, credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

# Filter realtime Tweets by keyword
printer.filter(track=["Cristiano"])