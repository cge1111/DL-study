#  PYTHONPATH=/Users/cge/Documents/yeardream/이어드림스쿨/MLOps/research-ci-example/0830 python addsub.py
# 파이썬 다른 파일에 있을 때 실행 방법
# pwd: 실행 시킬 파일에 들어감(cd 경로복사) 
# 실행시키고 싶은 함수를 PYTHONPATH경로에 복사하고 파이썬 실행시킬 파일 넣으면 됨!

from module import *
print(add(3,5))
print(sub(10,5))

def example():
    print("Hello world")

if __name__ == "__main__":
    c = add(1,2)
    print(c)
    d = sub(2,1)
    print(d)