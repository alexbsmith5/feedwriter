feedwriter documentation
========================

This library has two main classes:
* `Feed`: contains only functions to create a rss feed and add elements
* `PodcastFeed`: has specific functions to create elements for podcast players.

``PodcastFeed`` Class
---------------------

The ``PodcastFeed`` class is the child class to ``Feed``, and inherits all of the functionality found in ``Feed``.

To get started with creating a podcast RSS feed, go to the :doc:`tags` page where you will find which tags are required, recommended and situational for podcast players. When you need more information about a function, you can click on the link on the :doc:`tags` page and it will take you to the :doc:`podcastfeed_api`.

``Feed`` Class
--------------

The ``Feed`` class is relatively simple, and with that only has one page (currently) of documentation, and it is the :doc:`feed_api`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tags
   podcastfeed_api

   feed_api
