# 1. BMI(체질량지수) 계산기
# 자료형과 조건문을 배우는 코드
# If you're a beginner practicing, try improving this code.

height = float(input("키를 미터 단위로 입력하세요 (예: 1.75): "))
weight = float(input("몸무게를 kg 단위로 입력하세요: "))

bmi = weight / (height ** 2)

print(f"당신의 BMI: {bmi:.1f}")
if bmi < 18.5:
    print("저체중")
elif bmi < 25:
    print("정상")
elif bmi < 30:
    print("과체중")
else:
    print("비만")
