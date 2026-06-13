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

    # recommended tags
    feed.author("Podcast Author")
    feed.link("https://website.com")

    # situational tags
    feed.itunes_title("Test RSS Feed")
    feed.copyright("2026 Podcast Author")
    feed.feed_url_new("https://website1.com/feed.xml")
    feed.block()
    feed.complete()
    feed.verify("token")
    feed.generator("https://github.com/alexbsmith5/feedwriter")

    # add new posts at once
    for i in range(5):
        feed.new_post(f"Post {i}", f"https://website.com/post-{i}.mp3", 5650880 + i, "audio/mpeg", guid=str(i))

    # add additional information to posts
    post_3 = feed.get_post_index("Post 3")
    if post_3 != -1: # check if get_post_index found valid index
        feed.post_guid("33", 3)


    # add new posts incrementally
    feed.new_post("Post 5", "https://website.com/post-5.mp3", 5650880, "audio/mpeg")
    # required tags
    # feed.post_enclosure("https://website.com/post-5.mp3", 5650880, "audio/mpeg")
    feed.post_guid("5")
    # recommended tags
    feed.post_date("Sat, 01 Apr 2023 19:00:00 GMT")
    feed.post_description("Description for post 5")
    feed.post_duration(6351)
    feed.post_link("https://website.com/post-5-info.html")
    feed.post_image("https://website.com/post-5.jpg")
    feed.post_explicit(True)
    # situational tags
    feed.post_itunes_title("Post 5")
    feed.post_episode_number(5)
    feed.post_season_number(1)
    feed.post_type("full")
    feed.post_chapters("https://website.com/post-5-chapters.json", "application/json+chapters")
    feed.post_transcript("https://website.com/post-5-transcript.vtt", "text/vtt")
    feed.post_block(True)

    # add new post with all kwargs
    feed.new_post(f"Post 6", f"https://website.com/post-6.mp3", 5650880,
                  guid="6",
                  date="Thu, 11 Jun 2026 10:00:00 +0000",
                  description="Description for post 6",
                  duration=6356,
                  link="https://website.com/post-6-info.html",
                  image="https://website.com/post-5.jpg",
                  explicit=True,
                  itunes_title="Post 6",
                  episode_number=6,
                  season_number=1,
                  type="full",
                  block=True
                  )

    # write feed
    feed.write("test_feed.xml")

if __name__ == "__main__":
    main()
