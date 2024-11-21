import ijson
import json

def process_songs(input_path, output_path, process_func):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        songs = ijson.items(infile, 'item')
        outfile.write('[')
        first = True
        for song in songs:
            if not first:
                outfile.write(', ')
            processed_song = process_func(song)
            json.dump(processed_song, outfile, ensure_ascii=False)
            first = False
        outfile.write(']')