"""Wordpress Reviews model."""

from typing import Dict, Generator, List, Union

from tap_wordpress_reviews.wordpress_reviews_list import WordpressReviewsList


class WordpressReviews(object):
    """Main logic for Wordpress reviws."""

    def __init__(
        self,
        plugins: Union[List[str], str],
        number: int = 30,
    ) -> None:
        """Initialize plugin reviews api.

        Arguments:
            plugins {Union[List[str], str]} -- Name of the plugins
            number {int} -- Number of reviews to yield (default: {30})
        """
        # Set plugin or plugins
        if isinstance(plugins, str):
            self.plugins = [plugins]
        else:
            self.plugins = plugins

        self.number = number

        # Initialize lists
        self.reviews_lists: Dict[str, WordpressReviewsList] = {}
        for plugin in self.plugins:
            self.reviews_lists[plugin] = WordpressReviewsList(plugin)

    def reviews(self) -> Generator:
        """Reviews property.

        Returns:
            Generator -- Object list of reviews
        """
        for plugin in self.plugins:

            try:
                for _ in range(0, self.number):
                    record: dict = next(self.reviews_lists[plugin]).to_dict()
                    record['plugin'] = plugin
                    yield record
            except StopIteration:
                break
