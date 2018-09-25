#@auther:lmz
#单链表实现 4.21

class Node(object):
    '''定义一个节点类'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None
    
class SingleLinkList(object):
    '''定义一个单链表类'''
    def __init__(self,node=None):
        self.__head = node
    
    def is_empty(self):
        '''检查链表是否为空'''
        return self.__head == None

    def length(self):
        '''获取链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def trace(self):
        '''遍历链表'''
        if self.is_empty():
            print('None')
        cur = self.__head
        while cur != None:
            print(cur.elem,end=' ')
            cur = cur.next      
        print()

    def append(self, item):
        '''尾插法：在链表尾部添加一个元素'''
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:    
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        '''头插法：在链表头部添加一个元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        '''在某个位置插入一个元素'''
        if pos > (self.length() - 1):
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            count = 0
            node = Node(item)
            cur = self.__head
            while pos < (self.length() - 1):
                count += 1
                cur = cur.next
                if count == pos:
                    #在保证原有链接不变的情况下，
                    # 先把新建的节点指向插入位置后一个节点
                    node.next = cur.next 
                    cur.next = node
                    break      

    def remove(self, item):
        '''删除某个节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
            
    
    def search(self, item):
        '''查找节点位置'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":

    sll = SingleLinkList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.add(10)
    sll.add(8)
    sll.insert(1,9)
    print(sll.length())
    sll.trace()
    sll.remove(1)
    sll.trace()
    sll.remove(8)
    sll.trace()
    sll.remove(4)
    sll.trace()
