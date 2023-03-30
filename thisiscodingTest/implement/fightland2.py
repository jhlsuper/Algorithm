## https://cieske.tistory.com/106

import heapq


def change_weapon(idx, y, x):
    # idx 검투사가 (x,y)에서 무기 선택하는 행위
    if field[y][x] and warriors[idx][4] > field[y][x][0]:
        # 현재 무기보다 해당 위치에 있는 가장 쎈 무기가 더 좋은 경우(음수)
        # 지금 무기 집어넣고 가장 좋은 무기 선택
        warriors[idx][4] = heapq.heappushpop(field[y][x], warriors[idx][4])

    war_field[y][x] = idx  # 해당 위치에 싸움꾼 정보 업데이트
    warriors[idx][0], warriors[idx][1] = y, x
    return


def throw_weapon(idx, y, x):
    # 현재 들고 있는 무기 버리기
    heapq.heappush(field[y][x], warriors[idx][4])
    warriors[idx][4] = 0  # 무기 버린 상태
    return


def fight(cur_idx, foe_idx):
    # 두 싸움꾼 번호가 주어졌을 때, 상대방의 승리 여부 체크
    cur_stat, cur_weapon = warriors[cur_idx][3], warriors[cur_idx][4]
    foe_stat, foe_weapon = warriors[foe_idx][3], warriors[foe_idx][4]

    # 무기는 음수 상태로 저장되어있다는 것 까먹지 말기
    if cur_stat - cur_weapon < foe_stat - foe_weapon:
        # 상대방의 스탯+무기 공격력이 더 큰 경우
        score[foe_idx] += (foe_stat - foe_weapon) - (cur_stat - cur_weapon)
        return True
    elif cur_stat - cur_weapon == foe_stat - foe_weapon and cur_stat < foe_stat:
        # 스탯+무기 공격력은 같은데, 상대방 기초 스탯이 더 높은 경우
        # 점수 업데이트는 없음
        return True
    # 이동한 싸움꾼이 이긴 경우
    score[cur_idx] += (cur_stat - cur_weapon) - (foe_stat - foe_weapon)
    return False


def loser_move(idx, y, x):
    # 패자 무기 버리고, 이동해서, 무기 교체하는
    throw_weapon(idx, y, x)  # 무기 현재 위치에 버림
    l_dir = warriors[idx][2]  # 패자 초기 방향
    for _ in range(4):
        n_y, n_x = y + dir[l_dir][0], x + dir[l_dir][1]
        if 0 <= n_y < n and 0 <= n_x < n and not war_field[n_y][n_x]:
            # 이동하고자 하는 곳이 필드 내부면서, 그 위치에 다른 싸움꾼이 없다면
            change_weapon(idx, n_y, n_x)  # 이동해서 무기 교체
            # 패자 정보 업데이트
            war_field[n_y][n_x] = idx
            warriors[idx][1], warriors[idx][0] = n_x, n_y
            warriors[idx][2] = l_dir
            return
        l_dir = (l_dir + 1) % 4  # 이동 못하면 방향 90도 전환
    return


def war_round():
    for idx in range(1, m + 1):
        cur_man = warriors[idx]  # idx번 검투사 움직일 차례
        cur_x, cur_y, cur_dir = cur_man[1], cur_man[0], cur_man[2]

        next_y, next_x = cur_y + dir[cur_dir][0], cur_x + dir[cur_dir][1]  # 움직인 위치
        if not (0 <= next_y < n and 0 <= next_x < n):  # 격자 바깥으로 나간다면
            cur_dir = (cur_dir + 2) % 4  # 방향 180도 전환
            warriors[idx][2] = cur_dir
            next_y, next_x = cur_y + dir[cur_dir][0], cur_x + dir[cur_dir][1]  # 움직인 위치

        war_field[cur_y][cur_x] = 0  # 이동했으니 원래 위치에서 싸움꾼 정보 제거

        if war_field[next_y][next_x]:  # 움직인 위치에 다른 싸움꾼이 있다면
            foe_idx = war_field[next_y][next_x]  # 해당 위치에 있던 싸움꾼 번호

            foe_win = fight(idx, foe_idx)  # 누가 이겼는지 체크

            if foe_win:  # 상대방 승리
                loser_move(idx, next_y, next_x)
                change_weapon(foe_idx, next_y, next_x)
            else:  # idx 싸움꾼 승리
                loser_move(foe_idx, next_y, next_x)
                change_weapon(idx, next_y, next_x)

        else:  # 움직인 위치에 상대방이 없다면
            change_weapon(idx, next_y, next_x)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]  # 무기 위치 저장되는 필드
    warriors = [0] + [list(map(int, input().split())) + [0] for _ in range(m)]  # 제공되는 싸움꾼 정보 + 무기 정보
    # 각 싸움꾼의 x, y, 방향, 능력치, 무기

    for y in range(n):
        for x in range(n):
            # 무기 위치 힙 사용하기 위해 지도 각 위치 리스트 처리
            # max heap 위해 무기 공격력 음수 처리
            if field[y][x]:
                field[y][x] = [-field[y][x]]
            else:
                field[y][x] = []

    war_field = [[0] * n for _ in range(n)]  # 싸움꾼의 위치를 저장하기 위한 필드
    for idx, man in enumerate(warriors):
        if idx == 0: continue
        man[0] -= 1
        man[1] -= 1
        x, y = man[1], man[0]  # idx번 싸움꾼의 좌표
        war_field[y][x] = idx  # 해당 위치에 몇 번 싸움꾼이 있는지 저장

    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌
    score = [0] * (m + 1)  # 점수 저장용

    for _ in range(k):
        war_round()

    print(*score[1:])
