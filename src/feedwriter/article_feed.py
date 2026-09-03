from .feed import Feed


class ArticleFeed(Feed):
    def __init__(self) -> None:
        """
        Create ArticleFeed class.
        """
        namespaces: dict[str, str] = {"xmlns:atom": "http://www.w3.org/2005/Atom"}
        Feed.__init__(self, namespaces)

    def title(self, text):
        """
        Set title.

        :param text: title.
        :type text: string
        """
        self.channel_tag("title", text)

    def description(self, text: str, cdata: bool = False):
        """
        Set description.

        :param text: description.
        :type text: string
        :param cdata: whether or not rich html is included. Ex. ``<a>``, ``<p>``, ``<li>``, etc.
        :type cdata: bool
        """
        if cdata:
            self.channel_tag("description", f"<![CDATA[ {text} ]]>")
        else:
            self.channel_tag("description", text)
