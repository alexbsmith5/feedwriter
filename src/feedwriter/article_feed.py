from .feed import Feed


class ArticleFeed(Feed):
    def __init__(self) -> None:
        """
        Create ArticleFeed class.
        """
        namespaces: dict[str, str] = {"xmlns:atom": "http://www.w3.org/2005/Atom"}
        Feed.__init__(self, namespaces)

    def item(self, **kwargs):
        """
        Add a new item, using optional keyword arguments to add tags. Each parameter is calling a specific episode tag function with ``item_{keyword}`` format.

        :param title: (optional) post title.
        :type title: string
        """
        self.new_item()

        func_map = {
            "title": self.item_title,
        }

        self._parse_kwargs(func_map, **kwargs)
