a=[1,3,5,7,9,11,13]
for i in range(4): #上面的寫法不好，不應該寫死 數字的範圍
  print('第i的數字是',a[i])
print('上面的迴圈不好，下面迴圈才會伸縮自如/全部都照顧到')
N= len(a) #要先知道有幾個數字 a陣列的長度(iength)
for i in range(N): #才能在 for迴圈哩，得到正確的 range
  print('第i的數字是',a[i])