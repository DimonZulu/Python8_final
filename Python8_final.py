"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def psychic_prediction(number: int = 1) -> int:
    """Угадываем число 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    min_b = 1
    max_b = 101
    
    count = 0

    while True:
        count += 1
        predict_number = (min_b + max_b) // 2  # предполагаемое число
        if predict_number > number:
            max_b = predict_number
        elif predict_number < number:
            min_b = predict_number
        else:
            break #конец игры выход из цикла        
    return count


def score_game(psychic_prediction) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        psychic_prediction ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(psychic_prediction(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(psychic_prediction)
