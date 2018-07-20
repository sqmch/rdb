# get reddit data through praw and serve it as json

import json
import praw


class Rdb:
    """pulls data from praw (100 submissions from specified subreddit/sort mode) and serves to vue
    """

    def __init__(self):
        self.reddit = praw.Reddit("bot1", user_agent="rdb - testing")

    def get_submissions(self, subname="all", sortmode="hot"):
        """[summary]

        Keyword Arguments:
            subname {str} -- [description] (default: {'programming'})
            sortmode {str} -- [description] (default: {'top'})
        """
        if sortmode == "top":
            subreddit = self.reddit.subreddit(subname).top("all")
        elif sortmode == "hot":
            subreddit = self.reddit.subreddit(subname).hot(limit=50)
        elif sortmode == "new":
            subreddit = self.reddit.subreddit(subname).new()
        elif sortmode == "rising":
            subreddit = self.reddit.subreddit(subname).rising()
        elif sortmode == "controversial":
            subreddit = self.reddit.subreddit(subname).controversial()
        else:
            return {}

        onepacket = {}
        data = []
        for submission in subreddit:
            onepacket = {"id": submission.id, "title": submission.title}
            data.append(onepacket)

        json_sub_data = json.dumps(data)

        return json_sub_data

    def scan_submissions(self, selected_submissions):
        """[scan selected submissions and return comment data etc]
        """
        print("scan_submission START - selected_submissions = " + selected_submissions)
        comment_amounts = []
        # single sub code
        onepacket = {
            "cmnt_amt": str(
                len(self.reddit.submission(id=selected_submissions).comments.list())
            )
        }
        print("scan_submission PACKET SAVED")
        comment_amounts.append(onepacket)
        json_submission_data = json.dumps(comment_amounts)
        print("scan_submission END")
        return json_submission_data


""" for subid in selected_submissions:
    sub_list.append(self.reddit.submission(id=subid))

for sub in sub_list:
    sub.comments.replace_more(limit=None)

    onepacket = {
        'cmnt_amt': str(len(sub.comments.list()))
    }
    comment_amounts.append(onepacket) """
