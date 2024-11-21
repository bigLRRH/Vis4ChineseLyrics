import re
import opencc
from typing import List

class LyricCleaner:
    keywords = {
        "主歌", "副歌", "间奏", "过渡", "结尾", "作词", "作曲", "编曲", "和声", "混音", "吉他", "制作人", 
        "后期", "旁白", "调 ", "调：", "演唱", "标签", "录音", "监制", "编配", "弦乐", "钢琴", "鼓 ", "鼓：", "贝斯", 
        "键盘", "制作", "配器", "主题曲", "片尾曲", "插曲", "特别感谢", "鸣谢", "监制人", "出品人", 
        "策划", "制作团队"
    }

    def __init__(self):
        self.cc = opencc.OpenCC('t2s')
        self.redundant_line_pattern = re.compile(r"^(" + "|".join(self.keywords) + r"|$)")

    @staticmethod
    def remove_punctuation_numbers_whitespace(text: str) -> str:
        """
        清除字符串中的标点符号、数字和多余空格。
        :param text: 原始字符串
        :return: 清理后的字符串
        """
        return re.sub(r'[^\w\s]|[\d]|[\s]+', '', text)
    
    def convert_traditional_to_simplified(self, text: str) -> str:
        """
        将繁体中文转换为简体中文。
        :param text: 原始繁体字符串
        :return: 转换后的简体字符串
        """
        return self.cc.convert(text)
        
    def clean_lyrics(self, lyrics: List[str]) -> List[str]:
        """
        清理歌词内容。
        1. 过滤指定关键词行。
        2. 移除标点、数字、空格。
        3. 转换繁体为简体。
        
        :param lyrics: 歌词行列表
        :return: 清理后的歌词行列表
        """
        cleaned_lyrics = []

        for line in lyrics:
            if self.redundant_line_pattern.match(line):
                # 如果符合过滤条件则跳过
                continue
            # 清理每行的标点符号、数字、空格
            cleaned_line = self.remove_punctuation_numbers_whitespace(line)
            # 转换繁体为简体
            simplified_line = self.convert_traditional_to_simplified(cleaned_line)
            cleaned_lyrics.append(simplified_line)
        
        return cleaned_lyrics
