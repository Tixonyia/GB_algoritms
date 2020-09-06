import hashlib


def count_str(s):
    hash_ = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if hashlib.sha1((s[i:j]).encode('utf-8')).hexdigest()\
                    == hashlib.sha1((s).encode('utf-8')).hexdigest()\
                    or hashlib.sha1((s[i:j]).encode('utf-8')).hexdigest()\
                    == hashlib.sha1(('').encode('utf-8')).hexdigest():
                continue
            elif hashlib.sha1((s[i:j]).encode('utf-8')).hexdigest()\
                    not in hash_:
                hash_.append(hashlib.sha1((s[i:j]).encode('utf-8')).hexdigest())
    return len(hash_)


print(count_str('Like for teacher'))