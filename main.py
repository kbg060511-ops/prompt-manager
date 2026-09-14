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

categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
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


def choose_category():
    print("\n카테고리 선택:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}) {category}")

    print("7) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return categories[int(choice) - 1]

        if choice == "7":
            while True:
                category = input("카테고리 입력: ").strip()

                if category:
                    return category

                print("카테고리를 입력해주세요.")

        print("올바른 번호를 입력해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목을 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용을 입력해주세요.")

    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print("프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    for i, category in enumerate(categories, start=1):
        print(f"{i}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            selected_category = categories[int(choice) - 1]
            break

        print("올바른 번호를 입력해주세요.")

    matched = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            matched.append(prompt)

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    if not matched:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(matched, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. {prompt["title"]}{star}')

    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip().lower()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if keyword in prompt["title"].lower() or keyword in prompt["content"].lower():
            results.append(prompt)

    print("\n검색 결과:")

    if not results:
        print("검색 결과가 없습니다.")
        return

    for i, prompt in enumerate(results, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{i}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        number = int(input("번호 입력: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    index = number - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    favorite = "⭐" if prompt["favorite"] else "아님"

    print("\n────────────────────────────")
    print(f'제목: {prompt["title"]}')
    print(f'카테고리: {prompt["category"]}')
    print(f'즐겨찾기: {favorite}')
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")


def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        number = int(input("프롬프트 번호 입력: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    index = number - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f'\'{prompt["title"]}\' 프롬프트를 즐겨찾기에 추가했습니다!')
    else:
        print(f'\'{prompt["title"]}\' 프롬프트를 즐겨찾기에서 해제했습니다!')


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, start=1):
        print(f'{i}. [{prompt["category"]}] {prompt["title"]} ⭐')

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


while True:
    show_menu()
    choice = input("선택: ").strip()

    if choice == "1":
        add_prompt()

    elif choice == "2":
        show_list()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        search_prompt()

    elif choice == "5":
        show_detail()

    elif choice == "6":
        manage_favorite()

    elif choice == "7":
        show_favorites()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 번호입니다. 다시 입력해주세요.")
