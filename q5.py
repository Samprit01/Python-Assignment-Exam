'''
Question 5: Social Media Likes
A social media platform stores the number of likes received by five posts in a list. 
Write a function to find the post with the highest likes, 
calculate total likes, and display posts that received at least 100 likes.

'''
postlike = [100,20,300,40,340]

def likes(x):
    max_like= max(x)
    like_sum = sum(x)
    like_100 = [_ for _ in x if _>=100]
    print(f"Highest Like: {max_like} \nTotal Likes: {like_sum} \nLikes atleast 100: {like_100}")

likes(postlike)