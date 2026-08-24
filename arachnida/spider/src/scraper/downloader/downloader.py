
from abc import ABC, abstractmethod

# ===============================================================================
#
# Abstract base class for page downloaders.
#
# Defines the common interface for loading pages, querying elements,
# and releasing resources.
# ===============================================================================
class Downloader(ABC):

    @abstractmethod
    def load(self, url: str) -> bool:
        """
        - Load the page from the given URL.
        @param url: URL of the page to load.
        @return: True if the page loaded successfully, otherwise False.
        """
        pass

    @abstractmethod
    def query_selector_all(self, selector: str) -> list:
        """
        - Query all matching elements from the page.
        @param selector: selector used to find elements.
        @return: List of matching page elements.
        """
        pass

    @abstractmethod
    def close(self):
        """Close all resources."""
        pass
