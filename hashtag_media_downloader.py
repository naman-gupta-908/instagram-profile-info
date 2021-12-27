L = instaloader.Instaloader()
hashtag=input("Enter the name of hashtag : ")
cnt=0
limit=input("Enter media count : ")
for post in instaloader.Hashtag.from_name(L.context,hashtag).get_posts():
    if cnt>=limit:
        break
    cnt+=1
    try:
        L.download_post(post, target='#'+hashtag)
    except:
        continue
print("media downloaded")
