################################################################################
# Twitter Streaming
#

import json
from twitter import Twitter, TwitterStream, OAuth

################################################################################
# Twitter Streaming
#
def TwitterStreaming(accessToken, accessSecret, consumerKey, consumerSecret):
    oauth = OAuth(accessToken, accessSecret, consumerKey, consumerSecret)

    twitter_stream = TwitterStream(auth=oauth)

    iterator = twitter_stream.statuses.sample()

    tweet_count = 5

    for tweet in iterator:
        tweet_count -= 1

        print json.dumps(tweet, indent=2)

        if tweet_count <= 0:
            break


################################################################################
# main
#
def main(argv):
    accessToken    = argv[0]
    accessSecret   = argv[1]
    consumerKey    = argv[2]
    consumerSecret = argv[3]

    TwitterStreaming(accessToken, accessSecret, consumerKey, consumerSecret)


################################################################################
# Main entry point
#
if __name__ == "__main__":
    main(sys.argv[1:])
