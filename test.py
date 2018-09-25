
"""
@author:liang_Henry

@date:2015-06-12

"""


"""
选自http://blog.sina.com.cn/s/blog_474a358f0100lakt.html

本心理测试是由中国现代心理研究所以著名的美国兰德公司（战略研究所）
拟制的一套经典心理测试题为蓝本，
根据中国人心理特点加以适当改造后形成的心理测试题，
目前已被一些著名大公司，
如联想、长虹、海尔、诺基亚等公司作为对员工心理测试的重要辅助试卷，
据说效果很好。现在已经有人建议将来作为对公务员的必选辅助心理测试推广使用。
快来测试一下，很准的！
"""
import time



print ("start：")

#由于计算总值
your_sum=0

#所有的问题，通过键值对进行存储
question1={"question":"1、你更喜欢吃那种水果？","answer":["A、草莓","B、苹果","C、西瓜","D、菠萝","E、橘子"]}
question2={"question":"2、你平时休闲经常去的地方？","answer":["A、郊外","B、电影院","C、公园","D、商场","E、酒吧","F、练歌房"]}
question3={"question":"3、你认为容易吸引你的人是？","answer":["A、有才气的人","B、依赖你的人","C、优雅的人","D、善良的人","E、性情豪放的人"]}
question4={"question":"4、如果你可以成为一种动物，你希望自己是哪种？","answer":["A、猫","B、马","C、大象","D、猴子","E、狗","F、狮子"]}
question5={"question":"5、天气很热，你更愿意选择什么方式解暑？","answer":["A、游泳","B、喝冷饮","C、开空调"]}
question6={"question":"6、如果必须与一个你讨厌的动物或昆虫在一起生活，你能容忍哪一个？","answer":["A、蛇","B、猪","C、老鼠","D、苍蝇"]}
question7={"question":"7、你喜欢看哪类电影、电视剧？","answer":["A、悬疑推理类","B、童话神话类","C、自然科学类","D、伦理道德类","E、战争枪战类"]}
question8={"question":"8、以下哪个是你身边必带的物品？","answer":["A、打火机","B、口红","C、记事本","D、纸巾","E、手机"]}
question9={"question":"9、你出行时喜欢坐什么交通工具？","answer":["A、火车","B、自行车","C、汽车","D、飞机","E、步行"]}
question10={"question":"10、以下颜色你更喜欢哪种？","answer":["A、紫","B、黑","C、蓝","D、白","E、黄","F、红"]}
question11={"question":"11、下列运动中挑选一个你最喜欢的（不一定擅长）？","answer":["A、瑜珈","B、自行车","C、乒乓球","D、拳击","E、足球","F、蹦极"]}
question12={"question":"12、如果你拥有一座别墅，你认为它应当建立在哪里？","answer":["A、湖边","B、草原","C、海边","D、森林","E、城中区"]}
question13={"question":"13、你更喜欢以下哪种天气现象？","answer":["A、雪","B、风","C、雨","D、雾","E、雷电"]}
question14={"question":"14、你希望自己的窗口在一座30层大楼的第几层？","answer":["A、七层","B、一层","C、二十三层","D、十八层","E、三十层"]}
question15={"question":"15、你认为自己更喜欢在以下哪一个城市中生活？","answer":["A、丽江","B、拉萨","C、昆明","D、西安","E、杭州","F、北京"]}


#所有的答案，通过键值对进行存
scoring1={"A":2,"B":3,"C":5,"D":10,"E":15}
scoring2={"A":2,"B":3,"C":5,"D":10,"E":15,"F":20}
scoring3={"A":5,"B":10,"C":15}
scoring4={"A":2,"B":5,"C":10,"D":15}
scoring5={"A":2,"B":2,"C":3,"D":5,"E":10}
scoring6={"A":2,"B":3,"C":5,"D":8,"E":12,"F":15}
scoring7={"A":2,"B":3,"C":5,"D":8,"E":10,"F":15}
scoring8={"A":1,"B":3,"C":5,"D":8,"E":10,"F":15}

#所有性格
personality1="意志力强，头脑冷静，有较强的领导欲，事业心强，不达目的不罢休。\n外表和善，内心自傲，对有利于自己的人际关系比较看重，\n有时显得性格急噪，咄咄逼人，得理不饶人，不利于自己时顽强抗争，不轻易认输。\n思维理性，对爱情和婚姻的看法很现实，对金钱的欲望一般。"
personality2="聪明，性格活泼，人缘好，善于交朋友，心机较深。\n事业心强，渴望成功。思维较理性，崇尚爱情，\n但当爱情与婚姻发生冲突时会选择有利于自己的婚姻。金钱欲望强烈。"
personality3="爱幻想，思维较感性，以是否与自己投缘为标准来选择朋友。\n性格显得较孤傲，有时较急噪，有时优柔寡断。\n事业心较强，喜欢有创造性的工作，不喜欢按常规办事。\n性格倔强，言语犀利，不善于妥协。\n崇尚浪漫的爱情，但想法往往不切合实际。\n金钱欲望一般。"
personality4="好奇心强，喜欢冒险，人缘较好。\n事业心一般，对待工作，随遇而安，善于妥协。\n善于发现有趣的事情，但耐心较差，敢于冒险，但有时较胆小。\n渴望浪漫的爱情，但对婚姻的要求比较现实。\n不善理财。"
personality5="性情温良，重友谊，性格塌实稳重，但有时也比较狡黠。\n事业心一般，对本职工作能认真对待，但对自己专业以外事物没有太大兴趣，\n喜欢有规律的工作和生活，不喜欢冒险，家庭观念强，比较善于理财。"
personality6="散漫，爱玩，富于幻想。\n聪明机灵，待人热情，爱交朋友，但对朋友没有严格的选择标准。\n事业心较差，更善于享受生活，意志力和耐心都较差，我行我素。\n有较好的异性缘，但对爱情不够坚持认真，容易妥协。\n没有财产观念。"


def show_question_answer(question,scoring):
    """此方法为了将所有问题和所有答案进行展示使用"""
    print question.get("question")
    l=question["answer"]
    for allans in l:
        print allans
    yourans=raw_input("> ")
    score=scoring.get(yourans.upper())
    if score==None:
        print "您输入的答案不存在，请再次查看问题："
        show_question_answer(question,scoring)
        return
    global your_sum
    your_sum+=score

show_question_answer(question1,scoring1)
show_question_answer(question2,scoring2)
show_question_answer(question3,scoring1)
show_question_answer(question4,scoring2)
show_question_answer(question5,scoring3)
show_question_answer(question6,scoring4)
show_question_answer(question7,scoring1)
show_question_answer(question8,scoring5)
show_question_answer(question9,scoring1)
show_question_answer(question10,scoring6)
show_question_answer(question11,scoring7)
show_question_answer(question12,scoring1)
show_question_answer(question13,scoring1)
show_question_answer(question14,scoring1)
show_question_answer(question15,scoring8)

print "您的总得分是:%d"%your_sum
print "揭晓答案：\n"

if your_sum>=180:
    print personality1
elif your_sum>=140 and your_sum<180:
    print personality2
elif your_sum>=100 and your_sum<140:
    print personality3
elif your_sum>=70 and your_sum<100:
    print personality4
elif your_sum>=40 and your_sum<70:
    print personality5
elif your_sum<40:
    print personality6
else:
    print "程序出现异常，导致计算结果无法正常显示"

time.sleep(30) 