# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:37:55 2020

@author: natuk
"""

'''
小游戏：汉语拼音转换测验
'''

import random
import datetime
import xpinyin

# 声明汉字列表
question_list = ['北京', '天津', '上海', '河北',
                 '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽',
                 '福建', '江西', '山东', '河南', '湖北', '湖南',
                 '广东', '海南', '四川', '贵州', '云南',
                 '甘肃', '青海', '台湾', '内蒙古', '广西',
                 '宁夏', '新疆', '香港', '澳门']
# '西藏','重庆','山西','陕西',
# 注：多音字的拼音可能不正确

score_list = []  # 空的成绩列表

# 打印欢迎信息
print('**************************')
print('**  欢迎来玩汉语拼音游戏  **')
print('**************************')

#用函数制定一轮游戏
def one_game():
    mytime1 = datetime.datetime.now()  # 记时间用
    # 用cnt记录答对的次数
    cnt = 0

    # 从列表中随机出题
    for i in range(3):
        question = random.choice(question_list)
        print(question)
        ans = input('请输入你的答案：')
        # 显示正确答案用
        p = xpinyin.Pinyin()
        if ans == p.get_pinyin(question, ' ', tone_marks='numbers'):
            print('答对了！')
            cnt += 1
        else:
            print('答错了，正确答案是' + p.get_pinyin(question, ' ', tone_marks='numbers'))
        

    mytime2 = datetime.datetime.now()
    delay = mytime2 - mytime1  # 计算出时间差
    print('本轮你答对了' + str(cnt) + '次!')  # 显示答对数用
    
    if cnt == 3:
        print('恭喜你全部答对！') 
    print('本轮你花了', delay.seconds, '秒')  # 打印出时间差的秒值
    score_list.append(delay.seconds) #写在成绩表上
    if delay.seconds == min(score_list):
        print('恭喜创造新纪录！')
    print('********  成绩榜  ********')
    for score in score_list: # 依次打印列表中的每个元素
        print(score, end='秒 ')



game_status = input('准备好了吗？按y键开始游戏-->')  # 游戏开始的提示信息
if game_status == 'y':  # 标记游戏运行状态
    one_game()
    while True:
        game_restart = input('还想玩吗？按y键进入下一轮-->')
        if game_restart == 'y':  # 标记游戏运行状态
            one_game()
        else:
            print('游戏结束')
            break
            
else:
    print('不想玩啊？那就算了')
