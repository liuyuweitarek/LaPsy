import textgo
import numpy as np
import pandas as pd
from textgo import TextSim

data = pd.DataFrame({'ID': ["1", "2"],
                     'SPEAK_TEXT':  ["天氣真好", "你不錯"]})

ts = TextSim(lang='zh', method='bert', model_path='bert-base-chinese')
target="你不錯"
#sim = ts.similarity(target, data['SPEAK_TEXT'], mutual=True)

def simMax(target, all):
    t = [target for i in range(len(all))]
    all = list(all)
    return ts.similarity(t, all, mutual=False)
data.eval('''SIMILARITY = @simMax(@target, SPEAK_TEXT)''', inplace=True)
tmp_df = data.query('SIMILARITY == SIMILARITY.max()').to_dict('index')

print(tmp_df)
print(data)

#sim = ts.similarity(target, ["天氣真好", "你不錯"], mutual=True)


