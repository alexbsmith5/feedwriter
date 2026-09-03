from .feed import Feed


class ArticleFeed(Feed):
    def __init__(self) -> None:
        """
        Create ArticleFeed class.
        """
        namespaces: dict[str, str] = {"xmlns:atom": "http://www.w3.org/2005/Atom"}
        Feed.__init__(self, namespaces)
