from time import sleep

your_name = "sãn"
your_age = " sàng"

for c in your_name +  your_age:
    print(c, end='', flush=True)
    sleep(0.1)
print()    
import random
def play_game():
    choices = ['Rock', 'Paper', 'Scissors']

    while True:
        # Nhập lựa chọn của người dùng
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
 # Kiểm tra lựa chọn hợp lệ của người dùng
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Tạo lựa chọn ngẫu nhiên cho máy
        computer_choice = random.choice(choices)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Xác định kết quả
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'Rock' and computer_choice == 'Scissors') or
            (user_choice == 'Paper' and computer_choice == 'Rock') or
            (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
         break
        
play_game()

       
