# get reddit data through praw and serve it as json

import json
import praw
import requests


class Rdb:
    # pulls data from praw (100 submissions from specified subreddit/sort mode) and serves to vue
    def __init__(self):
        self.reddit = praw.Reddit('bot1', user_agent="rdb - testing")

    def get_submissions(self, subname='python', sortmode='top'):
        # input: subreddit name and sort mode
        # output: json table of subreddit submission data
        if sortmode == 'top':
            subreddit = self.reddit.subreddit(subname).top('all')
        elif sortmode == 'hot':
            subreddit = self.reddit.subreddit(subname).hot(limit=50)
        elif sortmode == 'new':
            subreddit = self.reddit.subreddit(subname).new()
        elif sortmode == 'rising':
            subreddit = self.reddit.subreddit(subname).rising()
        elif sortmode == 'controversial':
            subreddit = self.reddit.subreddit(subname).controversial()
        else:
            return {}

        index = 0
        onepacket = {}
        data = []
        for submission in subreddit:
            onepacket = {
                'id': index,
                'title': submission.title
            }
            data.append(onepacket)
            index += 1

        json_sub_data = json.dumps(data)

        return json_sub_data


"""
def main():
    rdb = Rdb()
    print(rdb.get_submissions('python', 'top'))


if __name__ == '__main__':
    main()
    """
