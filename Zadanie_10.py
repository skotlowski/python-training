# with open('log.txt') as f:
#     data = f.read()

#print(data)


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, val, traceback):
        self.file_obj.close()


with File('log.txt', 'r') as f:
    data = f.read()

print(data)
