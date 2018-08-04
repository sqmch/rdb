# get reddit data through praw and serve it as json

import json
import praw


class Rdb:
    """pulls data from praw (100 submissions from specified subreddit/sort mode) and serves to vue
    """

    def __init__(self):
        self.reddit = praw.Reddit("bot1", user_agent="rdb - testing")

    def get_submissions(self, subname="all", sortmode="hot"):
        """[Return 100 submissions from a specified subreddit + sort mode.]

        Keyword Arguments:
            subname {str} -- [subreddit name] (default: {'programming'})
            sortmode {str} -- [sorting option (top, hot, new, rising, 
                              controversial)] (default: {'top'})
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
        """[call reddit api through praw and return comment data]
            selected_submissions -- list of subreddit id-s
        """
        print(
            "scan_submission START -\nselected_submissions = "
            + str(selected_submissions)
        )
        data = []
        for i in selected_submissions:
            submission = self.reddit.submission(id=i)
            if i is not None:
                # fill an object with data and add it to data array
                onepacket = {
                    "id": i,
                    "title": submission.title,
                    "cmnt_amt": str(len(submission.comments.list())),
                    "score": str(submission.score),
                }
                data.append(onepacket)

        json_submission_data = json.dumps(data)
        print(f"json_submission_data = {json_submission_data}")
        print("scan_submission END")
        return json_submission_data

