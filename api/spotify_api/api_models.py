# Models in this file do not represent objects in DB,
# they are just helper dataclasses for data collected from external Spotify API
from dataclasses import dataclass
from typing import List, Optional


class ListAttr:
    """Helper class for managing list type attributes of data classes"""

    @staticmethod
    def _process_list_attr(class_object, json_objects_list):
        """Parse list of JSON objects into list of model objects
        @param class_object:        model class of incoming data
        @type class_object:         type
        @param json_objects_list:   list of JSON objects (dicts) from API
        @type json_objects_list:    List
        @return:                    list containing model objects
        @rtype:                     List
        """

        class_fields = class_object.__annotations__

        objects_list = list()

        for obj in json_objects_list:
            obj_args = {key: value for key, value in obj.items() if key in class_fields}
            objects_list.append(class_object(**obj_args))

        return objects_list


@dataclass
class Artist:
    """Spotify API artist object"""
    id: str
    name: str


@dataclass
class Image:
    """Spotify API image (album cover) object"""
    height: int
    width: int
    url: str


@dataclass
class Track:
    """Spotify API track object"""
    id: str
    name: str
    track_number: int
    preview_url: Optional[str]


@dataclass
class SearchItem(ListAttr):
    """Object representing data received from search endpoint"""
    id: str
    name: str
    artists: List[Artist]
    images: List[Image]

    def __post_init__(self):
        self.artists = self._process_list_attr(Artist, self.artists)
        self.images = self._process_list_attr(Image, self.images)


@dataclass
class Album(ListAttr):
    """Object representing data received from album endpoint"""
    id: str
    name: str
    release_date: str
    artists: List[Artist]
    tracks: List[Track]
    images: List[Image]

    def __post_init__(self):
        self.artists = self._process_list_attr(Artist, self.artists)
        self.tracks = self._process_list_attr(Track, self.tracks)
        self.images = self._process_list_attr(Image, self.images)
