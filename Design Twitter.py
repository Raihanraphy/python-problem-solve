
'''

most recent = largest time (max heap), (time increases so t = 1, t = 2, etc..)

1. postTweet(int userId, int tweetId): create tweet(tweetId,userId) (tweetId is unique)
2. getNewsFeed(int userId): fetch 10 MOST recent tweet ID. Tweet must be by following or user themselves
- ordered from most recent to least recent

3. follow(int followerId, int followeeId): followerId follows followeeId

4. unfollow(int followerId, int followeeId): followerId unfollows followeeId
'''


class Twitter:
    def __init__(self):
        self.users = {} # self.users[userId] = [[tweets], set()] (following is a list of userIds)
        #each tweet object is (time, tweetId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [[], set()]
        users = self.users
        tweet_object = (self.time, tweetId)

        users[userId][0].append(tweet_object)
        self.time += 1 # time only matters w.r.t tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        user = self.users[userId]
        tweet_list = set()
        tweet_heap = []
        tweet_most_ood = []

        for x in user[0]:# user's own tweets are incl.
            tweet_list.add(x[1])

            heapq.heappush(tweet_heap,(-x[0],x[1]))
            heapq.heappush(tweet_most_ood,(x[0],x[1]))

        following_list = user[1]
        for userId in following_list:
            user_object = self.users[userId]
            following_tweets = user_object[0]
            for tweet in following_tweets:
                tweet_age = tweet[0]
                tweet_id = tweet[1]
                if tweet_id in tweet_list:
                    continue
                tweet_list.add(tweet_id)
                if len(tweet_list) >= 10: # at capacity, we need to kick someone out
                    most_ood = tweet_most_ood[0]

                    # update new oldest
                    if most_ood[0] > tweet_age: # t = 3, t = 0
                        heapq.heappop(tweet_most_ood)
                        heapq.heappush(tweet_most_ood,(tweet[0],tweet[1]))
                    else: # t = 0, t= 3
                    # we only want to add a tweet IFF it's more recent than our oldest tweet
                        heapq.heappush(tweet_heap,(-tweet[0],tweet[1]))
                else:
                    heapq.heappush(tweet_heap, (-tweet[0],tweet[1]))
                    heapq.heappush(tweet_most_ood, (tweet[0],tweet[1]))

        result = [x[1] for x in heapq.nsmallest(10, tweet_heap)]
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[], set()]
        if followeeId not in self.users:
            self.users[followeeId] = [[], set()]
        
        self.users[followerId][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[], set()]
        if followeeId not in self.users:
            self.users[followeeId] = [[], set()]
        
        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
