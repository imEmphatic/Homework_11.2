def main():
    """"first func"""
    user_input = str(input("Введите текст для вывода с заглавными буквами: "))
    print(user_input.upper())


if __name__ == "__main__":
    main()


def main_2():
    """"second func"""
    user_input = str(input("Делаем первые две буквы заглавными: "))
    for i in user_input.split():
        print(i[:2].upper() + i[2:], end=' ')


if __name__ == "__main__":
    main_2()