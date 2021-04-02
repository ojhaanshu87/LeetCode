'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user
followed or by the user themself. Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
'''

class User:
    def __init__(self):
        self.following = {}
        self.posts = []
    
    def post(self, tweetId, timestamp):
        self.posts.insert(0, (timestamp, tweetId))
    
    def follow(self, followeeId, followee):
        self.following[followeeId] = followee
        
    def unfollow(self, followeeId):
        if followeeId not in self.following:
            return
        self.following.pop(followeeId)

class Twitter(object):
    def __init__(self):
        self.users = {}
        self.timestamp = 0
    
    def getUser(self, uid):
        if uid not in self.users:
            self.users[uid] = User()
        return self.users[uid]
        
    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.users[userId] = User()
        self.timestamp -= 1
        self.users[userId].post(tweetId, self.timestamp)
        
    def getNewsFeed(self, userId):
        def getTenTweetsFrom(user):
            return user.posts if len(user.posts) <= 10 else user.posts[:10]
        def getTimestamp(item):
            return item[0]
        def getTweet(item):
            return item[1]
        
        user = self.getUser(userId)
        allfeeds = []
        allfeeds += getTenTweetsFrom(user)
        for each in user.following.values():
            allfeeds += getTenTweetsFrom(each)
        allfeeds = sorted(allfeeds, key=getTimestamp)
        allfeeds = allfeeds if len(allfeeds) <= 10 else allfeeds[:10]
        return list(map(getTweet, allfeeds))
        

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        self.getUser(followerId).follow(followeeId, self.getUser(followeeId))
        

    def unfollow(self, followerId, followeeId):
        self.getUser(followerId).unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
