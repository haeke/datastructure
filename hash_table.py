
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """input a string that's stored in the table """
        hashvalue = self.calculate_hash_value(string)
        if hashvalue != -1:
            if self.table[hashvalue] != None:
                self.table[hashvalue].append(string)
            else:
                self.table[hashvalue] = [string]

    def lookup(self, string):
        """ return the value if the string
        is already in the table return -1 """
        hashvalue = self.calculate_hash_value(string)
        if hashvalue != -1:
            if self.table[hashvalue] != None:
                if string in self.table[hashvalue]:
                    return hashvalue
        return -1

    def calculate_hash_value(self, string):
        """ helper function to calculate a hash value
        from a string """
        value = ord(string[0])*100 + ord(string[1])
        return value

#setup
hash_table = HashTable()

#test calculate_hash_value
print hash_table.calculate_hash_value('UDACITY')

#test lookup edge case
print hash_table.lookup('UDACITY')

#test store
hash_table.store('UDACITY')

print hash_table.lookup('UDACITY')

hash_table.store('UDACIOUS')

print hash_table.lookup('UDACIOUS')
