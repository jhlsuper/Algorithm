def solution(files):
    answer = []
    files_list = [['', '', '']] * len(files)
    check_list = [['01', '02', '03'], ['11', '12', '22']]
    print(check_list[1])
    print(files_list)
    for i in range(len(files)):
        temp = files[i].lower()
        print(temp)
        for j in temp:

            if files_list[i][1] == '':
                if j.isdigit():
                    files_list[i][1] = files_list[i][1]+j
                else:
                    files_list[i][0] += j
            else:
                if j.isdigit():
                    files_list[i][1] += j
                else:
                    files_list[i][2] += j
            # print(files_list)
    print(files_list)
    return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
