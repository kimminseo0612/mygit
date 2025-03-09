def select_order_type():
    print("안녕하세요! 매장에서 드시나요? 포장해 가시나요?")
    while True:
        order_type = input("매장에서 드시면 '매장', 포장해 가시면 '포장'을 입력해주세요: ")
        if order_type in ['매장', '포장']:
            return order_type
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def select_ice_cream_type():
    ice_cream_types = [ ("싱글콘", 4000), ("싱글컵",4000), ("더블콘",5500), ("더블컵", 5500), ("파인트", 10000), ("쿼터", 15000), ("하프갤런", 25000)]
    print("아이스크림 종류를 선택해주세요:")

    for i in range(len(ice_cream_types)):
        print(f"{i+1}. {ice_cream_types[i][0]}")

    while True:
        choice = input("번호를 입력해주세요: ")
        if choice.isdigit() and 1 <= int(choice) <= len(ice_cream_types):
            return ice_cream_types[int(choice) - 1]
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def select_flavors(num_flavors):
    available_flavors = ["엄마는 외계인", "아몬드봉봉", "바닐라", "체리", "초코", "베리베리스트로베리", "피스타치오 아몬드", "뉴욕치즈케이크", "인절미"]
    selected_flavors = []
    print(f"{num_flavors}개의 아이스크림 맛을 선택해주세요:")
    for i in range(num_flavors):
        print("아이스크림 맛을 선택해주세요:")
        for j, flavor in enumerate(available_flavors, 1):
            print(f"{j}. {flavor}")
        while True:
            choice = input("번호를 입력해주세요: ")
            if choice.isdigit() and 1 <= int(choice) <= len(available_flavors):
                selected_flavors.append(available_flavors[int(choice) - 1])
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")
    return selected_flavors

def kiosk():
    done = False
    total_price = 0

    order_type = select_order_type()
    print(f"선택하신 옵션: {order_type}")
    while( not done ):
        ice_cream_type = select_ice_cream_type()
        print(f"선택하신 아이스크림: {ice_cream_type[0]}")

        if ice_cream_type[0] in ["싱글콘", "싱글컵","더블컵","더블콘"]:
            flavors = select_flavors(1)
        elif ice_cream_type[0] == "파인트":
            flavors = select_flavors(3)
        elif ice_cream_type[0] == "쿼터":
            flavors = select_flavors(4)
        elif ice_cream_type[0] == "하프갤런":
            flavors = select_flavors(6)
        else:
            flavors = []

        if flavors:
            print("선택하신 아이스크림 맛:")
            for flavor in flavors:
                print(f" - {flavor}")

        total_price += ice_cream_type[1]
        while True:
            answer = input("계속 주문하시겠습니까(네/아니오 ) ? : ")
            if answer == "아니오":
                done = True
                break
            elif answer == "네":
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")   

    print(f"총 가격은 {total_price} 입니다")

if __name__ == "__main__":
    kiosk()

