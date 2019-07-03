import sys
sys.path.append('.')

from lgy.algorithm.StdIOTestContainer import StdIOTestContainer as T

def go(temp_set, ):


def main():
    for x in range(int(input())):
        files = int(input())
        pages = []
        for i in range(files):
            pages.append(int(input()))

        for i in range(0, len(files) - 1):
            for j in range(1, len(files)):



user_input = '''
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''

expected = '''
300
864
'''

T.runningTest(user_input.strip(), expected.lstrip(), main)