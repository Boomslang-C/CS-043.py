
class Simpledb:
        def __init__(self, file):
                self.file = file

        def __repr__(self, file):
                return ("<" + self.__class__.__name__ +
        " file=" + str(self.file) +
        ">")

        def insert(self, key, value):
                f = open('../../../Python Creations/Telephone_Directory.txt', 'a')
                f.write(key + '\t' + value + '\n')
                f.close()

        def select_one(self, key):
                f = open('../../../Python Creations/Telephone_Directory.txt', 'r')
                for row in f:
                        (k, v) = row.split('\t', 1)
                        if k == key:
                                return v[:-1]
                f.close()

        def delete(self, key):
                f = open('../../../Python Creations/Telephone_Directory.txt', 'r')
                result = open('result.txt', 'w')
                for (row) in f:
                        (k, v) = row.split('\t', 1)
                        if k != key:
                                result.write(row)
                f.close()
                result.close()
                import os
                os.replace('result.txt', '../../../Python Creations/Telephone_Directory.txt')

        def update(self, key, value):
            f = open('../../../Python Creations/Telephone_Directory.txt', 'r')
            result = open('result.txt', 'w')
            for (row) in f:
                (k, v) = row.split('\t', 1)
                if k == key:
                        result.write(key + '\t' + value + '\n')
                else:
                        result.write(row)
            f.close()
            result.close()
            import os
            os.replace('result.txt', '../../../Python Creations/Telephone_Directory.txt')
            
