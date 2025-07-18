import random

def deal_card():
    """1〜11のカードを1枚ランダムに返す"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # J, Q, K は10として扱う
    return random.choice(cards)

def calculate_score(cards):
    """現在の手札のスコアを計算"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # ブラックジャック！
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # エースは1としてカウント
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "引き分け！"
    elif computer_score == 0:
        return "あなたの負け…相手がブラックジャック！"
    elif player_score == 0:
        return "勝ち！ブラックジャック！"
    elif player_score > 21:
        return "バースト！あなたの負け！"
    elif computer_score > 21:
        return "相手がバースト！あなたの勝ち！"
    elif player_score > computer_score:
        return "あなたの勝ち！"
    else:
        return "あなたの負け！"

def play_game():
    print("=== ブラックジャックへようこそ！ ===")
    
    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"あなたのカード: {player_cards}, 合計: {player_score}")
        print(f"相手の最初のカード: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            next = input("もう1枚引きますか？ (y/n): ")
            if next.lower() == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nあなたの最終ハンド: {player_cards}, 合計: {player_score}")
    print(f"相手の最終ハンド: {computer_cards}, 合計: {computer_score}")
    print(compare(player_score, computer_score))

# ゲーム開始
if __name__ == "__main__":
    play_game()
