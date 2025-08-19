# 단어 사전 저장용 dict
dictionary = {}


# 단어 사전 파일 로드 함수
def load_dictionary(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('#')
            if len(parts) == 2:
                dictionary[parts[0]] = parts[1]


# 메인 루프 함수
def main():
    load_dictionary("DICTIONARY.TXT")

    while True:
        try:
            line = input()
            tokens = line.strip().split()
            vectors = []
            for token in tokens:
                key = token.lower()
                if key in dictionary:
                    vectors.append(dictionary[key])
            print(' '.join(vectors))
        except KeyboardInterrupt:
            print("\n종료합니다.")
            break


# 프로그램 실행
if __name__ == "__main__":
    main()