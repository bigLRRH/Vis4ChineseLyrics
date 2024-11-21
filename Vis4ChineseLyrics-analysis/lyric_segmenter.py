import jieba

class LyricSegmenter:
    def __init__(self):
        jieba.enable_paddle()

    def segment(self, str):
        seg_list = jieba.cut(str,use_paddle=True)
        segmented_text = '/'.join(list(seg_list))   # 拼接分词结果
        return segmented_text
    
    def segment_lyrics(self, lyric):
        result = []
        for str in lyric:
            result.append(self.segment(str))
        return result