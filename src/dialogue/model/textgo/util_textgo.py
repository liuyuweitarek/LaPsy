from logger import SystemLog
from textgo import TextSim
class TextGoModel:
    def __init__(self, log="TEST"):
        self.Log = SystemLog(self.__class__.__name__, log)
        self.ts = TextSim(lang='zh', method='bert', model_path='bert-base-chinese')
        
    def _get_similarity_max(self, target_text, compared_text):
        target = [target_text for _ in range(len(compared_text))]
        compared = list(compared_text)
        return self.ts.similarity(target, compared, mutual=False)
    
    def similarity_df2dict(self, target_text, df):
        _df = df
        _df.eval('''SIMILARITY = @self._get_similarity_max(@target_text, SPEAK_TEXT)''', inplace=True)
        _dict = _df.query('SIMILARITY == SIMILARITY.max()').to_dict('index')
        result = [ row for _, row in _dict.items()][0]
        return result