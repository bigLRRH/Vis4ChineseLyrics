from lyric_cleaner import LyricCleaner
from lyric_segmenter import LyricSegmenter
import ijson
import json
from tqdm import tqdm

# 输入和输出文件路径
input_paths = [
    "ChineseLyrics-master/lyrics1.json",
    "ChineseLyrics-master/lyrics2.json",
    "ChineseLyrics-master/lyrics3.json",
    "ChineseLyrics-master/lyrics4.json",
    "ChineseLyrics-master/lyrics5.json",
]
# input_file_path = 'data.json'
output_file_path = "output.json"


# 初始化清理器和分词器
lyricCleaner = LyricCleaner()
lyricSegmenter = LyricSegmenter()


def process_songs(input_paths):
    """
    逐项处理歌曲数据，统计词频
    - input_path: 输入 JSON 文件路径
    """
    for input_path in input_paths:
        print(f"正在处理 {input_path} ...")
        with open(input_path, "r", encoding="utf-8") as infile:
            total_songs = sum(1 for _ in ijson.items(infile, "item"))  # 获取总数
            infile.seek(0)
            songs = ijson.items(infile, "item")
            for song in tqdm(
                songs, desc="Processing songs", total=total_songs, mininterval=1.0
            ):
                try:
                    cleaned_lyric = lyricCleaner.clean_lyrics(
                        song.get("lyric", "")
                    )  # 使用 .get 避免 KeyError
                    lyricSegmenter.segment_lyrics(cleaned_lyric)
                except Exception as e:
                    print(f"处理歌曲时出错: {e}")


# 处理输入文件
process_songs(input_paths)

# 将词频统计结果写入文件
with open(output_file_path, "w", encoding="utf-8") as outfile:
    json.dump(lyricSegmenter.word_freq.most_common(), outfile, ensure_ascii=False)

print(f"词频统计结果已保存到 {output_file_path}")
