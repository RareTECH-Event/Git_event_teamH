def main():
    while True:
        print("選択してください：")
        print("1: hiiro")
        print("2:ゆーせー")
        print("3: koko")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("こんにちわ")
        elif choice == "2":
            print("睡眠命")
        elif choice == "3":
            print("おやすみなさい")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
