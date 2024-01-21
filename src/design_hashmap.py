class Bucket:
    def __init__(self):
        self.bucket = []

    def insert(self, key: int, value: int) -> None:
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                self.bucket[i][1] = value
                return
        self.bucket.append([key, value])
    
    def get(self, key: int) -> int:
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                return self.bucket[i][1]
        return -1

    def remove(self, key: int):
        for i in range(len(self.bucket)):
            if self.bucket[i][0] == key:
                del self.bucket[i]
                return

class MyHashMap:

    def __init__(self):
        self.table_size = 251
        self.table = [Bucket()] * self.table_size
        

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.table_size
        self.table[hash_key].insert(key, value)


    def get(self, key: int) -> int:
        hash_key = key % self.table_size
        return self.table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.table_size
        self.table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)