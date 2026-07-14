Tags
====

The information about the show and episodes of a podcast is transmitted with RSS feeds which use XML. The information in an XML document is found and created in it's tags. For Apple Podcasts, there are tags that are required, recommended, and situational. For the required tags, they must be present to pass the feed validation process. For recommended and situational tags, they are not necessarily required, but they can be important depending on the situation.

Required Tags
*************
The following tags are required for the channel and for every post. If these tags are missing, the show will fail Apple Podcasts' feed validation blocking it from being listed.

Channel Tags
############
The following commands specified below must be called in order to pass validation.

    * :meth:`~feedwriter.podcast_feed.PodcastFeed.title`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.description`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.image`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.category`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.explicit`

Episode Tags
############
The following commands must be called for every single episode on the feed to pass validation.

These commands can be run by themselves, defaulting to the last created post or passing the index. Another option is to run the :meth:`~feedwriter.podcast_feed.PodcastFeed.new_post` function and pass in the corresponding kwargs.

    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_title`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_enclosure`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_guid`

Recommended Tags
****************
While these tags are not required to pass Apple Podcasts' feed validation, they can provide helpful information to users.

Channel Tags
############
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.author`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.link`

Episode Tags
############
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_date`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_description`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_duration`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_link`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_image`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_explicit`

Situational Tags
****************
Just like recommended tags, these tags are not necessarily required but they can be useful in certain situations.

Channel Tags
############
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.itunes_title`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.type`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.copyright`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.feed_url_new`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.block`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.complete`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.verify`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.generator`

Episode Tags
############
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_itunes_title`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_episode`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_season`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_type`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_chapters`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_transcript`
    * :meth:`~feedwriter.podcast_feed.PodcastFeed.post_block`
