#coding:gbk
"""
程序目标：完成RPSLS游戏
作者：王英吉
时间：2020年4月5日
"""

import random#电脑随机生成一个实数



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):#自定义函数,把用户输入的文字转化为数字
	"""
    将游戏对象对应到不同的整数
    """
	if name=="石头":
		a=0
	elif name=="史波克":
		a=1
	elif name=="布":
		a=2
	elif name=="蜥蜴":
		a=3
	elif name=="剪刀": 
		a=4
	else:	
		a="Error: No Correct Name"#如果输入的不是要的数据
	return a				
def number_to_name(number):#将电脑自动生成的数变为文字
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    if number==0:
        b="石头"
    elif number==1:
        b="史波克"
    elif number==2:
        b="布"
    elif number==3:
        b="蜥蜴"
    elif number==4: 
        b="剪刀" 
    return b
def rpsls(choice_name):#根据RPSLS规则，比较电脑生成的数和用户输入的数据
    player_choice_number=name_to_number(choice_name)
    x=player_choice_number
    comp_number=random.randrange(0,4)#将电脑随机生成的实数范围控制在0-4
    y=comp_number
    print("计算机的选择是：")
    print(number_to_name(y))#用自定义函数将电脑自动生成的数变为文字输出
    if x==y:
        print("平手咯")
    elif x==0 and (y==3 or y==4):
	    print("您赢了!")
    elif x==1 and (y==0 or y==4):
        print("您赢了!")
    elif x==2 and (y==0 or y==1):
        print("您赢了!")	 
    elif x==3 and (y==1 or y==2):
	    print("您赢了!")					
    elif x==4 and (y==2 or y==3):
	    print("您赢了!")
    elif x=="Error: No Correct Name":
	    print("Error: No Correct Name")
    else:
	    print("计算机赢了")    			
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


