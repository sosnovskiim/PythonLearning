def order(*preferences):
    coffee, milk, cream = (
        "coffee", "milk", "cream"
    )
    espresso, cappuccino, macchiato, viennese, latte, con_panna = (
        "Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"
    )
    for drink in preferences:
        if drink == espresso and in_stock[coffee] >= 1:
            in_stock[coffee] -= 1
            return espresso
        if drink == cappuccino and in_stock[coffee] >= 1 and in_stock[milk] >= 3:
            in_stock[coffee] -= 1
            in_stock[milk] -= 3
            return cappuccino
        if drink == macchiato and in_stock[coffee] >= 2 and in_stock[milk] >= 1:
            in_stock[coffee] -= 2
            in_stock[milk] -= 1
            return macchiato
        if drink == viennese and in_stock[coffee] >= 1 and in_stock[cream] >= 2:
            in_stock[coffee] -= 1
            in_stock[cream] -= 2
            return viennese
        if drink == latte and in_stock[coffee] >= 1 and in_stock[milk] >= 2 and in_stock[cream] >= 1:
            in_stock[coffee] -= 1
            in_stock[milk] -= 2
            in_stock[cream] -= 1
            return latte
        if drink == con_panna and in_stock[coffee] >= 1 and in_stock[cream] >= 1:
            in_stock[coffee] -= 1
            in_stock[cream] -= 1
            return con_panna
    return "К сожалению, не можем предложить Вам напиток"


if __name__ == '__main__':
    in_stock = {"coffee": 4, "milk": 4, "cream": 0}
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))
