import time
import progressbar


data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print("檔案讀取完成，總共有", len(data), "筆資料")


sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print("留言平均長度為", sum_len/len(data))


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆留言長度小於100") 
print(new[0])
print(new[1])


good = []
for d in data:
    if "good" in d:
        good.append(d)
print("一共有", len(good), "筆留言提到GOOD")

good = [d for d in data if "good" in d]


# 文字的記數
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的KEY 進 wc 字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('總共花了', end_time - start_time, '秒')

print(len(wc))
while True:
    word = input('請輸入您想查詢的字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('謝謝您的使用!!')

