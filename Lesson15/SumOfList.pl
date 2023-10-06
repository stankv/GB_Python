% Сумма элементов списка, язык Prolog
sum_of_list([], 0).
% Вызываем функцию рекурсивно
sum_of_list([H|T], Sum) :-
    sum_of_list(T, SumTemp), Sum is SumTemp + H.

% Запрос
?- sum_of_list([1, 2, 3, 4, 5], Sum)