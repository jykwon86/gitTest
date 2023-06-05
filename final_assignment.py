import pandas as pd

# 레벤슈타인 거리 구하기
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
    matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # 표 채우기 --- (※2)
    # print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
    return matrix[a_len][b_len]

# 챗본데이터 불러오기, 질문, 답변 리스트로 저장
data = pd.read_csv("ChatbotData.csv")
questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    
    # 가장 짧은 레벤슈타인 거리,질문,인덱스 초기화
    closest_distance = float('inf')
    closest_question = ""
    closest_index = -1

    # 레벤슈타인 거리 계산 및 가장 짧은 거리의 질문과 인덱스 찾기
    for i, question in enumerate(questions):
        distance = calc_distance(input_sentence, question)
        if distance < closest_distance:
            closest_distance = distance
            closest_question = question
            closest_index = i

    # 가장 짧은 거리의 질문의 인덱스로 해당 답변 반환
    closest_answer = answers[closest_index]
    # 가장 짧은 거리의 질문 출력
    # print('가장 짧은 거리의 질문:', closest_question )
    print('Chatbot:', closest_answer)
    
