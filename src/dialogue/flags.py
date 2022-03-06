class Flags:
    IS_ASK = "IS_ASK"            # '0':ASK '1':ASKed
    KEYWORD = "KEYWORD"           # `;` Seperate diff keyword
    ID ="ID"
    IS_ROOT = "IS_ROOT"           # '0':Not Root '1':ROOT
    TAG = "TAG"
    SPEAK_TEXT = "SPEAK_TEXT"
    NEXT_TAG = "NEXT_TAG"
    IS_LIMIT = "IS_LIMIT"          # '0':Unlimit '1':limit
    VOLUME = "VOLUME" 
    SPEED = "SPEED"
    PITCH = "PITCH"
    ACTION_TYPE = "ACTION_TYPE"       # '1':Say '2':Say and Listen
    TIMELIMIT = "TIMELIMIT"
    SPEC_PRIORITY = "SPEC_PRIORITY"     # '1':After timelimit have the highest priority
                            # '2':Leave auto mode 
    LOOP_MAX = "LOOP_MAX"
    AFTER_LOOP_MAX = "AFTER_LOOP_MAX"
    MATCH_TYPE = "MATCH_TYPE"        # '1':Fuzzy '2':Exact
    IF_NONE_MATCH = "IS_NONE_MATCH"       #
    QNAME = "QNAME"
