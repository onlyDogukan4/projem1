def is_substring(sub,main):
    if len(sub)>len(main):
        return False
    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            return True
    return False
print(is_substring("aa","atahan"))