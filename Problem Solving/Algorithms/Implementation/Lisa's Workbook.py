nk = input().split()
n = int(nk[0])
k = int(nk[1])
problems_in_chapters = list(map(int, input().split()))
special_pages = 0
page = 1
for chapter_problems in problems_in_chapters:
    for current_problem in range(1,chapter_problems + 1):
        if current_problem == page:
            special_pages += 1
        if current_problem == chapter_problems or current_problem % k == 0:
            page += 1

print(special_pages)