# 1. * 출력 줄 바꿈

# print('* 출력')
# n = int(input('how much print?'))
# w = int(input('how much line changed?'))
#
# for i in range(n):    # n번 반복
#   print('*', end='')
#   if i % w == w - 1:  # n번 판단
#     print()
#
# if n % w:
#   print()


# 1.2 개선(반복문 내 조건문은 비효율적)

# print('* 출력')
# n = int(input('how much print?'))
# w = int(input('how much line changed?'))
#
# for _ in range(n // w): # 나눈 몫만큼 출력
#   print('*' * w)
#
# rest = n % w    # 나머지 값을 rest에 저장하여 마지막에 출력
# if rest:
#   print('*' * rest)

# 3. 정수 입력 받아 합계 구하기

# print('1~n까지 정수의 합')
#
# while True:
#   n = int(input('insert n : '))
#   if n > 0:
#     break
#
# sum = 0
# i = 1
#
# for i in range(1, n + 1):
#   sum += i
#   i += 1
#
# print(f'1~{n}까지 합은 {sum}')

# 4. 직사각형 변의 길이 나열하기

# area = int(input('넓이 입력 : '))
#
# for i in range(1, area + 1):
#   if i * i > area: break
#   if area % i: continue
#   print(f'{i} x {area // i}')

# 5. 난수 생성 중 특정 수가 나오면 중단

# import random
#
# n = int(input('생성할 난수 개수 : '))
#
# for _ in range(n):
#   r = random.randint(10, 99)
#   print(r, end = ' ')
#   if r == 13:
#     print('\n프로그램 중단')
#     break
# else:
#   print('\n난수 생성 종료')

# 6. 특정 수 건너뛰기

# for i in range(1, 13):
#   if i == 8:
#     continue
#   print(i, end = ' ')
#
# print()

#  6-1. 개선

# for i in list(range(1, 8)) + list(range(9, 13)):
#   print(i, end = ' ')
# print()

# 7. 2자리 양수 입력받기

# print('2자리 양수 입력')
#
# while True:
#   no = int(input('값을 입력하세요 : '))
#   if 10 <= no <= 99:
#     break
#
# print(f'입력받은 양수는 {no}')
