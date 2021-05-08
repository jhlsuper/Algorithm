import heapq
from collections import deque


def solution(k, num, links):
    parents = get_parents(links)
    children_sum = get_children_sum(num, parents, links)

    sum_hq = [(-children_sum[i], i) for i in range(len(children_sum))]
    heapq.heapify(sum_hq)

    for i in range(k-1):
        group(num, links, children_sum, sum_hq)

    (most_sum, id) = heapq.heappop(sum_hq)

    return -most_sum


def get_parents(links):
    parents = [-1 for i in range(len(links))]
    for parent, children in enumerate(links):
        for child in children:
            if child != -1:
                parents[child] = parent
    return parents


def get_children_sum(num, parents, links):
    heads = [0 for i in range(len(links))]
    added = [False for i in range(len(links))]

    for me, link in enumerate(links):
        if link == [-1, -1]:
            now = me
            sum_from_leaf = 0
            while True:
                parent = parents[now]
                if parent == -1:
                    break
                sum_from_leaf += num[now] if not added[now] else 0
                added[now] = True
                heads[parent] += sum_from_leaf

                now = parent
    return [heads[i] + num[i] for i in range(len(links))]


def group(num, links, children_sum, sum_hq):
    (biggest_sum, id) = heapq.heappop(sum_hq)
    if links[id][0] != -1 and links[id][1] != -1:
        to_cut = links[id][0] if children_sum[links[id][0]
                                              ] > children_sum[links[id][1]] else links[id][1]
    elif links[id][0] != -1:
        to_cut = links[id][0]
    elif links[id][1] != -1:
        to_cut = links[id][1]
    else:
        return

    new_children_sum = biggest_sum + children_sum[to_cut]
    heapq.heappush(sum_hq, (new_children_sum, id))
