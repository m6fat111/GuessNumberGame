import random

def guess_the_number():
    # 生成一個1到100的隨機數字
    secret_number = random.randint(1, 100)
    attempts = 0

    print("歡迎來到猜數字遊戲！")
    print("我已經選好一個1到100之間的數字，你來猜猜看吧。")

    while True:
        try:
            # 讓玩家輸入猜測的數字
            guess = int(input("請輸入你的猜測："))
            attempts += 1

            # 檢查玩家的猜測
            if guess < secret_number:
                print("太小了，再猜大一點。")
            elif guess > secret_number:
                print("太大了，再猜小一點。")
            else:
                print(f"恭喜你猜對了！你用了 {attempts} 次猜中了數字 {secret_number}。")
                break
        except ValueError:
            print("請輸入有效的數字。")

if __name__ == "__main__":
    guess_the_number()
