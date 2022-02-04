class Flags:
    IS_ASK = str            # '0':ASK '1':ASKed
    KEYWORD = str           # `;` Seperate diff keyword
    ID = str
    IS_ROOT = str           # '0':Not Root '1':ROOT
    TAG = str
    SPEAK_TEXT = str
    NEXT_TAG = str
    IS_LIMIT = str          # '0':Unlimit '1':limit
    VOLUME = str 
    SPEED = str
    PITCH = str
    ACTION_TYPE = str       # '1':Say '2':Say and Listen
    TIMELIMIT = str
    SPEC_PRIORITY = str     # '1':After timelimit have the highest priority
                            # '2':Leave auto mode 
    LOOP_MAX = str
    AFTER_LOOP_MAX = str
    MATCH_TYPE = str        # '1':Fuzzy '2':Exact
    IF_NONE_MATCH = str       #
    QNAME = str