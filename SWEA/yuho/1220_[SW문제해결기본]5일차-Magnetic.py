# 처음엔 1의 시간이 흐를 때 마다의 상황을 시뮬레이션 하며 결과 반환하였음
# 일일이 시뮬레이션 하기엔 시간도 오래 걸리고 나올 수 있는 경우의 수가 꽤 있었음
# 이에 교착상태에 대한 규칙을 찾기 시작하였고,
# 빨간색이 파란색의 바로 위에 있는 지점에서 교착상태가 발생한다는 것을 알게 됨.

test = 0
while(True):
    try:
        # N*N 행렬맵 생성을 위한 입력(해당 문제에서는 100고정)
        n = int(input())
        arr = [input().split() for _ in range(n)]

        # 열 단위의 계산이 어렵기에 입력된 행렬맵의 전치행렬 생성
        c_arr = list(zip(*arr))
        cnt = 0

        # 열 단위 행렬맵에 대해서 한 줄씩 꺼낸 뒤
        for ar in c_arr:
            s = ''
            # 한 글자씩 검사
            for p in ar:
                # ('0' -> 빈공간)이 아니라면
                if p != '0':
                    # s에 문자열 추가
                    s += p
            # 빨간색이 파란색의 바로 위에 있는 경우에 대해서 카운트 증가
            cnt += s.count('12')
        test += 1
        print("#{0} {1}".format(test, cnt))
    except:
        break