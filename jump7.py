#逢7必跳过游戏
number=0 #产生数字变量初始化
count=0  #非跳过数个数
jumpcount=0 #跳过数个数
for number in range(1,101):
    
    if number%7==0:
        #print('此数{}是7的倍数，跳过'.format(number))
        jumpcount+=1
        continue
    elif number%10==7: 
        #print('此数{}个位数是7，跳过'.format(number))
        jumpcount+=1
        continue
    elif number//10==7: 
        #print('此数{}十位数是7，跳过'.format(number))
        jumpcount+=1
        continue
    count+=1
    # print('\033[6;32;43m]'+'数字：{0},非跳过数个数：{1}，跳过数个数：{2}'+'\033[0m'.format
#(number,count,jumpcount))
   #print('数字：{0} 非跳过数个数：{1} 跳过数个数：{2}'.format(number,count,jumpcount))
    print('{0}'.format(number))
count-=1
      
