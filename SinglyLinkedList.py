class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SinglyLinkedList: 

    def __init__(self):
        
        self.tail = None
        self.lenght = 0
    
    def append(self,value):
        node = Node(value)

        if(self.tail == None):
            self.tail = node
        else:
            current = self.tail

            while current.next: 
                current = current.next
            current.next = node
        self.lenght +=1

        return self
    
    def size(self):
        return str(self.size)

    def iterator(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val #Crea variables en tiempo de ejecución, no los almacena.



    def delete(self,value):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == value:
                if current == self.tail:
                    self.tail = current.next
                else: 
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            previous = current
            current = current.next

    def search(self,value):
        for node in self.iterator():
            if value == node:
                print(f"Data {value} found!")
    
    def clear(self):
        self.tail = None
        self.tail = None
        self.lenght =0

words = SinglyLinkedList()
words.append("egg")
words.append("bread")
words.append("ham")

def imprimirLista():
    current = words.tail
    while current: 
        print(current.data)
        current = current.next


imprimirLista()
words.delete("egg")
imprimirLista()