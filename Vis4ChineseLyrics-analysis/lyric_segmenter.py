import jieba
from collections import Counter

class LyricSegmenter:
    def __init__(self):
        jieba.enable_paddle()
        self.word_freq = Counter()

    def segment(self, text):
        seg_list = list(jieba.cut(text, use_paddle=True))
        self.word_freq.update(seg_list)
    
    def segment_lyrics(self, lyrics):
        for line in lyrics:
            self.segment(line)
