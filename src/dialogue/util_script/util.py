from pandas import DataFrame
from dialogue.flags import Flags
from cfg import NLPModel


class ScriptCase:
    available_root = {
        Flags.IS_ROOT:"1",
        Flags.IS_LIMIT:"0",
        Flags.TIMELIMIT:"0"
    }
def db_find(df, fields):
    error = None
    result = DataFrame([])
    
    try:
        query = []
        for flag, val in fields.items():
            query.append('{0} == "{1}"'.format(str(flag), str(val)))
        query = " & ".join(query)
        result = df.query(query)
        
        return error, result

    except Exception as e:
        error = e
        result = DataFrame([])
        return error, result

def db_find_available_root(df, fields=ScriptCase.available_root):
    error = None
    result = DataFrame([])
    error, result = db_find(df, fields)
    print(result)
    return error, result


def db_eval_root(target_text, df, model):
    error = None
    result = []
    try:
        result = model.similarity_df2dict(target_text, df)
        
        return error, result
        
    except Exception as err:
        error = str(err)
        result = []
        return error, result
    
