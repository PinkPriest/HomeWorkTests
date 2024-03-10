import task1_copy
from task1_copy import mentors_sort
from task1_copy import mentors_top


def mentors_tests(result_1, result_2):
    expected1 = "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"
    expected2 = "Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)"
    assert result_1 == expected1
    assert result_2 == expected2

mentors_tests(mentors_sort(), mentors_top())