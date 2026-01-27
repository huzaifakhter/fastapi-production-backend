def read_user(username):
    with open("datafile.txt", "r") as df:
        if username in df.read():
            return True
        else:
            return False

def write_user(username):
    with open("datafile.txt", "a") as df:
        df.write(username + "\n")