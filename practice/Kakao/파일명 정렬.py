import re
def solution(files):
    files_split = []
    for i in files:
        tmp = re.split("([0-9]+)", i)
        files_split.append(tmp)
    
    files_sorted = sorted(files_split, key = lambda x : (x[0].upper(), int(x[1])))
    
    res = []
    for i in files_sorted:
        res.append("".join(i))
        
    return res



print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))


