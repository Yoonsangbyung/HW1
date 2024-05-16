def get_user_input(prompt):
    """
    사용자로부터 입력을 받는 함수입니다.

    Args:
        prompt (str): 입력을 요청하는 메시지

    Returns:
        float: 사용자가 입력한 값
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")


def evaluate_explosion_risk(concentration, lower_explosive_limit, upper_explosive_limit):
    """
    특정 물질의 폭발 위험성을 평가합니다.

    Args:
        concentration (float): 물질의 농도 (%)
        lower_explosive_limit (float): 물질의 폭발 하한계 (%)
        upper_explosive_limit (float): 물질의 폭발 상한계 (%)

    Returns:
        str: 폭발 위험 여부
    """
    if lower_explosive_limit <= concentration <= upper_explosive_limit:
        return "폭발 위험 존재"
    else:
        return "폭발 위험 없음"


def main():
    """
    방폭 위험성 평가 프로그램의 메인 함수입니다.
    """
    print("방폭 위험성 평가 프로그램에 오신 것을 환영합니다.")

    while True:
        concentration = get_user_input("가연성 물질의 농도(%)를 입력하세요: ")
        lower_explosive_limit = get_user_input("폭발 하한계(%)를 입력하세요: ")
        upper_explosive_limit = get_user_input("폭발 상한계(%)를 입력하세요: ")

        result = evaluate_explosion_risk(concentration, lower_explosive_limit, upper_explosive_limit)
        print(f"폭발 위험 평가 결과: {result}")

        another = input("다른 값을 입력하시겠습니까? (y/n): ")
        if another.lower() != 'y':
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
