from src.feedwriter import podcast_feed

def main():
    feed = podcast_feed.PodcastFeed()
    # required channel tags
    feed.title("Test RSS Feed")
    feed.description("Description for \"Test RSS Feed\".")
    feed.image("https://website.com/image.jpg")
    feed.language("eng")
    feed.category("Comedy")
    feed.explicit(True)

    # add new posts at once
    for i in range(5):
        feed.new_post_required(f"Post {i}", f"https://website.com/post-{i}.mp3", f"{5650880+i}", "audio/mpeg", str(i))

    # add additional information to posts
    post_3 = feed.get_post_index("Post 3")
    if post_3 != -1: # check if get_post_index found valid index
        feed.post_guid("33", 3)

    # add new posts incrementally
    feed.new_post("Post 5")
    feed.post_enclosure("https://website.com/post-5.mp3", "5650880", "audio/mpeg", 5)
    feed.post_guid("5")

    # write feed
    feed.write("test_feed.xml")

if __name__ == "__main__":
    main()
