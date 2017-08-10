import os

def scandir(path = "./", rotation=True):
    res = []
    for t in os.listdir(path):
        if os.path.isdir(t):
            if rotation:
                res.extend(scandir(os.path.join(path, t)))
            else:
                res.append(os.path.join(path, t))
        res.append(os.path.join(path, t))
    return(res)


if __name__ == '__main__':
    for t in scandir():
        if t[-3:] == '.cc':
            os.rename(t, "{0}{1}".format(t[:-3], '.cpp'))
            print(t)
