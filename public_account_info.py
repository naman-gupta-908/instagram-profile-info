#Public account info
L = instaloader.Instaloader()
username=input("Enter Public Account's Username : ")
profile = instaloader.Profile.from_username(L.context,username)

count=0
limit=input("Enter post count to be downloaded : ")
try:
    for post in profile.get_posts():
        if count>limit:
            break
        count+=1
        L.download_post(post, target=profile.username)
except:
    pass
print("Required posts downloaded")

print('total media count : ',profile.mediacount)

print('total no. of followers : ',profile.followers)

print('total no. of following : ',profile.followees)

print("profile's bio : ",profile.biography)

print('Link to the profile pic : ',profile.profile_pic_url)
