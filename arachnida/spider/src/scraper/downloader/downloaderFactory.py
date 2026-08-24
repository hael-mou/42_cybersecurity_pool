
from .downloader import Downloader
# ===============================================================================
#
# Factory for registering and creating Downloader implementations.
#
# Maintains a registry of downloader classes and creates instances by name.
# ===============================================================================
class DownloaderFactory:
    _registry: dict[str, type[Downloader]] = {}

    @classmethod
    def register(cls, name: str):
        """
        - Register a downloader class by name.
        @param name: Name used to register the downloader class.
        @return: Decorator that registers the downloader class.
        """
        def decorator(downloader_class: type[Downloader]):
            if not cls._registry:
                cls._registry["default"] = downloader_class
            cls._registry[name] = downloader_class
            return downloader_class

        return decorator

    @classmethod
    def create(cls, name: str = "default") -> Downloader | None:
        """
        - Create a downloader instance by name.
        @param name: Name of the registered downloader.
        @return: Downloader instance or None if not found.
        """
        downloader_class = cls._registry.get(name, cls._registry.get("default"))
        if downloader_class is None:
            return None
        return downloader_class()
