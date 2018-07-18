# get reddit data through praw and serve it as json

import json
import praw


class Rdb:
    """pulls data from praw (100 submissions from specified subreddit/sort mode) and serves to vue
    """

    def __init__(self):
        self.reddit = praw.Reddit('bot1', user_agent="rdb - testing")

    def get_submissions(self, subname='programming', sortmode='top'):
        """[summary]

        Keyword Arguments:
            subname {str} -- [description] (default: {'programming'})
            sortmode {str} -- [description] (default: {'top'})
        """
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

        onepacket = {}
        data = []
        for submission in subreddit:
            onepacket = {
                'id': submission.id,
                'title': submission.title
            }
            data.append(onepacket)

        json_sub_data = json.dumps(data)

        return json_sub_data

    def scan_submissions(self, selected_submissions):
        """[summary]

        Arguments:
            selected_submissions {[type]} -- [description]
        """
        for sub in selected_submissions:
            pass
