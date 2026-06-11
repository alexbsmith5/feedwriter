from src.feedwriter import podcast_feed

def main():
    feed = podcast_feed.PodcastFeed()
    feed.title("Test RSS Feed")
    feed.description("Description for \"Test RSS Feed\".")
    feed.image("https://website.com/image.jpg")
    feed.language("eng")
    feed.category("Comedy")
    feed.explicit(True)
    feed.write("test_feed.xml")

if __name__ == "__main__":
    main()
