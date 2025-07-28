class State:
    def __init__(self, score, arr, ope, pre):
        self.score = score
        self.arr = arr
        self.ope = ope
        self.pre = pre

    def __lt__(self, other):
        return self.score < other.score


WIDTH = 5000
T = int(input())
PQR = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(T)]
beams = []
x = [0] * 20
beams.append([State(0, x, None, -1)])
for i in range(T):
    p, q, r = PQR[i]
    candidates = []
    for j in range(len(beams[i])):
        new_arr = beams[i][j].arr[::]
        new_arr[p] += 1
        new_arr[q] += 1
        new_arr[r] += 1
        score = beams[i][j].score + new_arr.count(0)
        ope_a = State(score, new_arr, "A", j)
        candidates.append(ope_a)

        new_arr = beams[i][j].arr[::]
        new_arr[p] -= 1
        new_arr[q] -= 1
        new_arr[r] -= 1
        score = beams[i][j].score + new_arr.count(0)
        ope_b = State(score, new_arr, "B", j)
        candidates.append(ope_b)

    candidates.sort(reverse=True)
    beams.append(candidates[: min(WIDTH, len(candidates))])

ans = []
pos = 0
for i in reversed(range(1, T + 1)):
    ans.append(beams[i][pos].ope)
    pos = beams[i][pos].pre

for a in reversed(ans):
    print(a)

# 参考
# https://github.com/fumtas1k/kyopro-tessoku/blob/main/ruby/A49.rb
