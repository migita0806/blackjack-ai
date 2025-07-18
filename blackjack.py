import random

def draw_card():
    card = random.randint(1, 11)
    return card

def play_blackjack():
    print("ブラックジャックを始めます！")
    while True:
        player_cards = [draw_card(), draw_card()]
        dealer_cards = [draw_card(), draw_card()]

        print(f"あなたのカード: {player_cards} 合計: {sum(player_cards)}")
        print(f"ディーラーの見えているカード: {dealer_cards[0]}")

        # プレイヤーのターン
        while sum(player_cards) < 21:
            choice = input("カードを引きますか？ (y/n): ")
            if choice.lower() == 'y':
                player_cards.append(draw_card())
                print(f"あなたのカード: {player_cards} 合計: {sum(player_cards)}")
            else:
                break

        player_total = sum(player_cards)
        if player_total > 21:
            print("バースト！あなたの負け！")
        else:
            # ディーラーのターン
            print(f"ディーラーのカード: {dealer_cards} 合計: {sum(dealer_cards)}")
            while sum(dealer_cards) < 17:
                dealer_cards.append(draw_card())
                print(f"ディーラーが引きました: {dealer_cards} 合計: {sum(dealer_cards)}")

            dealer_total = sum(dealer_cards)
            if dealer_total > 21 or player_total > dealer_total:
                print("あなたの勝ち！")
            elif player_total == dealer_total:
                print("引き分け！")
            else:
                print("あなたの負け！")

        again = input("もう一度プレイしますか？ (y/n): ")
        if again.lower() != 'y':
            print("ゲームを終了します。")
            break

play_blackjack()
