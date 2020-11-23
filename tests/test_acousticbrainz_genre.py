# -*- coding: utf-8 -*-

import numpy as np

from mirdata.datasets import giantsteps_key
from mirdata import utils
from tests.test_utils import run_track_tests


def test_track():
    default_trackid = "3"
    data_home = "tests/resources/mir_datasets/giantsteps_key"
    track = giantsteps_key.Track(default_trackid, data_home=data_home)

    expected_attributes = {
        "data": "acousticbrainz-mediaeval-validation/be/be9e01e5-8f93-494d-bbaa-ddcc5a52f629.json",
    }

    expected_property_types = {
        "key": str,
        "genres": dict,
        "artists": list,
        "tempo": int,
    }


def test_to_jams():
    data_home = "tests/resources/mir_datasets/giantsteps_key"
    track = giantsteps_key.Track("3", data_home=data_home)
    jam = track.to_jams()
    assert jam["sandbox"]["key"] == "D major", "key does not match expected"

    assert (
        jam["file_metadata"]["title"]
        == "10089 Jason Sparks - Close My Eyes feat. J. Little (Original Mix)"
    ), "title does not match expected"
    sand_box = {
        "artists": ["Jason Sparks"],
        "genres": {"genres": ["Breaks"], "sub_genres": []},
        "tempo": 150,
        "key": "D major",
    }
    assert dict(jam["sandbox"]) == sand_box, "title does not match expected"


def test_load_key():
    key_path = (
        "tests/resources/mir_datasets/giantsteps_key/keys_gs+/10089 Jason Sparks - Close My Eyes feat. J. "
        + "Little (Original Mix).txt"
    )
    key_data = giantsteps_key.load_key(key_path)

    assert type(key_data) == str

    assert key_data == "D major"

    assert giantsteps_key.load_key(None) is None


def test_load_meta():
    meta_path = (
        "tests/resources/mir_datasets/giantsteps_key/meta/10089 Jason Sparks - Close My Eyes feat. J. "
        + "Little (Original Mix).json"
    )
    genres = {"genres": ["Breaks"], "sub_genres": []}
    artists = ["Jason Sparks"]
    tempo = 150

    assert type(giantsteps_key.load_genre(meta_path)) == dict
    assert type(giantsteps_key.load_artist(meta_path)) == list
    assert type(giantsteps_key.load_tempo(meta_path)) == int

    assert giantsteps_key.load_genre(meta_path) == genres
    assert giantsteps_key.load_artist(meta_path) == artists
    assert giantsteps_key.load_tempo(meta_path) == tempo

    assert giantsteps_key.load_genre(None) is None
    assert giantsteps_key.load_artist(None) is None
    assert giantsteps_key.load_tempo(None) is None