class Node:
    def __init__(self, name, score, tel):
        # node properties
        self.name = name
        self.score = score
        self.tel = tel

        # for linking nodes
        self.next = None


class LinkedList:
    # for count nodes in linkedlist
    count = 0
    def __init__(self):
        # for linking nodes
        self.last = None
        self.root = None

    def push(self, node : Node):
        # add node to the root
        if self.root is None:
            self.root = node
            self.last = node
        else:
            node.next = self.root
            self.root = node
        self.count += 1

    def search_name(self, name):
        # search name in node
        cur = ds.root
        while True:
            if cur == None:
                # print('찾는 값이 없습니다.')
                return None
            if cur.name == name:
                return (cur.score, cur.tel)
            cur = cur.next
    
    def get_node(self, index):
        # get index number of node
        cnt = 0
        node = self.root
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def remove_name(self, name):

        self.count -= 1
        pass
    
    def print_all(self):
        cur = self.root
        total_ds_str = ''
        while cur is not None:
            new_ds = [cur.name, cur.score, cur.tel]
            new_ds_str = ' '.join(new_ds) + '\n'
            total_ds_str += new_ds_str
            cur = cur.next
        
        return total_ds_str

    

def load_datebase(ds: LinkedList):
    # 파일의 데이터를 읽어 Node 객체에 저장하고
    # Node를 LinkedList에 추가
    f = open('db.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        new_node = Node(*line.strip().split(" "))
        ds.push(new_node)

def register_member(ds: LinkedList):
    # 사용자로부터 정보를 입력 받아 Node를 구성
    # Node를 LinkedList에 추가

    name = input("이름을 입력하세요 : ")
    score = input("점수를 입력하세요 : ")
    tel = input("전화번호를 입력하세요 : ")

    new_node = Node(name, score, tel)
    ds.push(new_node)

    print(f'{name} 님이 추가되었습니다. ------- 총 회원 수 : {ds.count} 명 -------')

def search_member(ds: LinkedList):
    # 사용자로부터 정보를 입력 받아 LinkedList에 탐색 후 결과 출력
    member_name = input("검색할 회원 이름을 입력하세요 : ")
    search_result = ds.search_name(member_name)

    try:
        print(f"자산 : {search_result[0]} / 전화 : {search_result[1]}")
    except: 
        print('찾는 값이 없습니다.')


def remove_member(ds: LinkedList):
    # 사용자로부터 정보를 입력 받아 LinkedList에 탐색 후 Node를 제거    
    member_name = input("삭제할 회원 이름을 입력하세요 : ")
    ds.remove_name(member_name)

    try:
        print(f"{member_name} 님이 삭제되었습니다. ------- 총 회원 수 : {ds.count} 명 -------")
    except:
        print('찾는 값이 없습니다.')

def write_datebase(ds: LinkedList):
    # write a file
    f = open('db.txt','w', encoding='utf-8')
    f.write(ds.print_all())
    f.close()
    



# -----------------------------------------------------------------------------
# 프로그램의 시작

# 경로설정
import os

#os.chdir('./Desktop/code')
os.chdir('C:/Users/dseduoa.edu/Desktop/2. 테스트 코드 파일/data')

ds = LinkedList()

load_datebase(ds)

while True:
    print("----------------------------------------")
    print("   회  원  관  리  프  로  그  램   ")
    print("----------------------------------------\n")
    print("1) 회원 가입")
    print("2) 회원 검색")
    print("3) 회원 삭제")
    print("4) 종료")

    select = input("> ")

    if select == "1":
        register_member(ds)

    elif select == "2":
        search_member(ds)

    elif select == "3":
        remove_member(ds)

    else:
        break

write_datebase(ds)
