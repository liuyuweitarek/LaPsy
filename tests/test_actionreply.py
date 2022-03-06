class ActionReply:
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            setattr(self, attr, val)


if __name__ == "__main__":
    a = ActionReply(test = "1")
    assert  a.test == "1"