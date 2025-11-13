# 
import game

def get_user_menu_choice():
    menu_text = '''Game Menu:
    (1) PLay a new Game
    (2) Show scores
    (3) Quit.
    '''
    while True:
        print(menu_text)
        user_input = input().strip()
        if user_input not in ['1','2','3']:
            print("Invalid choice, choose again")
            continue
        else:
            return int(user_input)

def print_results(results):
    for result, val in results.items():
        if result == 'draw' or result == 'win':
            res = result + 's'
        else:
            res = result + 'es'    
        print (f" {res}: {val}")
    print("Thank You for playing")

def main():
    results = { 'win': 0, 'loss': 0, 'draw': 0 }
    while True:
        choice = get_user_menu_choice()
        if choice == 3:
            print_results(results)
            print("Exiting!")
            break
        elif choice == 1:
            new_game = game.Game()
            result = new_game.play()
            results[result] +=1
        else: ## choice is 2 for showing results
            print_results(results)

    
if __name__ == "__main__":
    main()        
