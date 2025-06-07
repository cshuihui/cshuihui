python = 3
math = 4
english = 4
physical = 2
military_theory = 2
philosophy = 2
# 补充你的代码
per = int(input())
fee = per * (python + math + english + physical + military_theory + philosophy)
print(f"你本学期选修了{python+math+english+physical+military_theory+philosophy}个学分。")
print(f"你应缴纳的学费为{fee}元。")
