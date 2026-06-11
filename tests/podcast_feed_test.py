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

    for i in range(5):
        feed.post(f"Post {i}", f"https://website.com/post-{i}.mp3", f"{5650880+i}", "audio/mpeg", str(i))

    feed.write("test_feed.xml")

if __name__ == "__main__":
    main()
