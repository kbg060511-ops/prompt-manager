prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 이미지 생성",
        "content": "제품의 특징을 살린 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무 자동화 도우미",
        "content": "반복 업무를 자동화하는 방법을 제안해주세요.",
        "category": "자동화",
        "favorite": False
    }
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


while True:
    show_menu()
    choice = input("선택: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("아직 구현되지 않은 기능입니다.")
