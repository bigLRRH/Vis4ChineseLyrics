from file_io import process_songs
from lyric_cleaner import LyricCleaner
from lyric_segmenter import LyricSegmenter

input_file_path = 'ChineseLyrics-master/lyrics1.json'
# input_file_path = 'data.json'
output_file_path = 'output.json'

lyricCleaner = LyricCleaner()
lyricSegmenter = LyricSegmenter()


def process_song(song):
    cleaned_lyric = lyricCleaner.clean_lyrics(song['lyric'])
    segmented_lyric = lyricSegmenter.segment_lyrics(cleaned_lyric)
    song['lyric'] = segmented_lyric
    return song

process_songs(input_file_path, output_file_path, process_song)