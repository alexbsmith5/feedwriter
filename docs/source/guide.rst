Guide
=====

Required Tags
*************
The following tags are required for the channel and for every post. If these tags are missing, the show will fail Apple Podcast's feed validation blocking it from being listed.

Channel Tags
############
The following commands specified below must be called in order to pass validation.

    * :attr:`~feedwriter.podcast_feed.PodcastFeed.title`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.description`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.image`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.category`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.explicit`

Episode Tags
############
The following commands must be called for every single episode on the feed to pass validation.

These commands can be run by themselves, defaulting to the last created post or passing the index. Another option is to run the :attr:`~feedwriter.podcast_feed.PodcastFeed.new_post` function and pass in the corresponsing kwargs.

    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_title`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_enclosure`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_guid`

Recommended Tags
****************
While these tags are not required to pass Apple Podcast's feed validation, they can provide helpful information to users.

Channel Tags
############
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.author`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.link`

Episode Tags
############
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_date`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_description`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_duration`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_link`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_image`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_explicit`

Situational Tags
****************
Just like recommended tags, these tags are not necessarily required but they can be useful in certain situations.

Channel Tags
############
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.itunes_title`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.type`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.copyright`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.feed_url_new`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.block`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.complete`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.verify`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.generator`

Episode Tags
############
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_itunes_title`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_episode`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_season`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_type`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_chapters`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_transcript`
    * :attr:`~feedwriter.podcast_feed.PodcastFeed.post_block`
