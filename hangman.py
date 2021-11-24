# http://tinyurl.com/h9q2cpc

def hangman(word):
    # 不正解を格納する変数
    wrong=0
    # リストに登録
    stages=["",
        "───────　　　　　　　",
        "│                  　",
        "│         │         ",
        "│      (´д｀)        ",
        "│      /┃＿┃│       ",
        "│       /  │    　　 ",
        "│                  　",
    ]

    # 答えの文字列をリストに格納する  12345 ⇒ 1,2,3,4,5
    rletters = list(word)
    # 答えの文字数分 _ をリストに加える 12345 ⇒ _____
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    # 不正解数が stagesリスト -1 より大きくなったら繰り返し終了
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

import random
anslist=["cat","maccha","break","getfile","hangdman"]
x = random.choice(anslist)

hangman(x)
# http://tinyurl.com/j7rb8orss