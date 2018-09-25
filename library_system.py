#定义一个图书馆图书管理
#author：lmz
#Date: 2018-04-02

class Book(object):
    '''定义一个书籍类'''
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        msg = 'this book called %s, its author is %s.'%(self.name,self.author)
        return msg

class Brrow_card(object):
    '''定义一个借书卡类'''
    def __init__(self, owner_name, nums):
        self.owner_name = owner_name
        self.nums = nums
        self.borrow_date = 30
        self.container = []

    def __str__(self):
        msg = '这个借书卡是%s的，可以借阅图书的数量是%d,已经借阅的书籍有%s'%\
              (self.owner_name,self.nums,str(self.container))
        return msg

    def limit(self):
        '''限制借阅书籍数量'''
        if 0 <= len(self.container) < 3:
            return True
        else:
            return False

    def show_borrowbook(self):
        ''''查看当前借阅卡上已经借阅的书籍'''
        print('前借阅卡上已经借阅的书籍有：')
        for i in self.container:
            print(i,end=' ')
        print()

class Management(object):
    def __init__(self):
        self.bookrack = []
        self.record = {}

    def add(self,item):
        '''往图书馆书架上添加书籍'''
        self.bookrack.append(item)

    def show_bookrack(self):
        '''显示图书馆书架上都有哪些书'''
        return str(self.bookrack)

    def search_book(self):
        '''查询书籍是否被借阅'''
        bookname = input('请输入你想要搜索的书籍名字\n：')
        #判断图书馆是否有你查询的书籍
        if bookname in self.bookrack:
            if bookname not in self.record.keys():
                print('这本书没有被借走')
            else:
                print('这本书被人借走了')
        else:
            print('图书馆内没有馆存这本书')
        
    def borrow_book(self):
        '''使用借书卡借书～'''
        bookname = input('请输入你想要借阅的书籍名字\n：')
        ID_card = eval(input('请出示你的id卡号：'))
        if bookname in self.bookrack:
            if ID_card.limit():
                self.record[bookname] = ID_card.owner_name
                print('%s借阅成功')
                ID1.container.append(bookname)
                #从当前书架上拿走借阅的书籍
                self.bookrack.remove(bookname)
            else:
                print('你当前借阅书籍已经满三本了')
        else:
            print('本图书馆没有此书')

    def give_back(self):
        '''归还借阅对书籍'''
        ID_card = eval(input('请出示你的id卡号:'))
        bookname = input('请输入你想要归还的书籍名字\n：')
        if bookname in ID_card.container:
            ID_card.container.remove(bookname)
        else:
            print('你并未借阅此书，或者你书名输入错误')
        self.bookrack.append(bookname)

    def show_message(self):
        '''显示所有的借阅信息'''
        for k,v in self.record.items():
            print('%s借阅了%s'%(v,k))
        print()
    
    def process_msg(self):
        print('---查询图书馆当前书籍，请按数字1 -----')
        print('---查询要借阅图书信息，请按数字2 -----')
        print('---如需要借阅图书，请按数字3 ---------')
        print('---如需要归还图书，请按数字4 ---------')
        print('---如无需其他服务，按任意键退出！-----')
        
    def main(self):
        print('欢迎来到逸夫图书馆')
        print('图书馆目前只提供部分服务，以后会日渐添加更多服务，敬请期待～')
        while True:
            self.process_msg()
            num = input('请输入你想要操作的数字：')
            if num == '1':
                print(self.show_bookrack())
                print()
            elif num == '2':
                self.search_book()
                print()
            elif num == '3':
                self.borrow_book()
                print()
            elif num == '4':
                self.give_back()
                print()
            else:
                break


if __name__ == "__main__":   
    #定义对象
    yifu = Management()
    ID1 = Brrow_card('xiaoming',3)
    #增加图书信息
    book1 = Book('三国演义','罗贯中')
    book2 = Book('水浒传','施耐庵')
    book3 = Book('西游记','吴承恩')
    book4 = Book('红楼梦','曹雪芹')
    book5 = Book('物种起源','达尔文')
    book6 = Book('孙子兵法','孙武')
    yifu.add(book1.name)
    yifu.add(book2.name)
    yifu.add(book3.name)
    yifu.add(book4.name)
    yifu.add(book5.name)
    yifu.add(book6.name)
    #执行图书馆部分服务
    yifu.main()
