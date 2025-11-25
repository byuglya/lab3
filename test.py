import pytest
from lesson_testing import (
    square_eq_solver,
    main_first_script,
    is_palindrome_iterative,
    main_second_script,
    compute_factorial,
    main_third_script,
    main
)

@pytest.mark.parametrize("a, b, c, expected", [
    (1, -3, 2, {1.0, 2.0}),
    (1, 2, 1, {-1.0}),
    (1, 0, 1, set()),
])
def test_square_eq_solver_param(a, b, c, expected):
    result = set(square_eq_solver(a, b, c))
    assert result == expected

def test_first_script(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '1 -3 2')
    main_first_script()
    captured = capsys.readouterr()
    assert 'Корень номер' in captured.out

@pytest.mark.parametrize("input_str, expected_result, expected_output", [
    ("Lol", True, "является палиндромом"),
    ("Laugh", False, "не является палиндромом"),
])
def test_is_palindrome_iterative(input_str, expected_result, expected_output, capsys):
    result = is_palindrome_iterative(input_str)
    captured = capsys.readouterr()
    assert result == expected_result
    assert expected_output in captured.out

def test_second_script(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'Lol')
    result = main_second_script()
    captured = capsys.readouterr()
    assert result is True
    assert "является палиндромом" in captured.out

@pytest.mark.parametrize("n, expected_factorial", [
    (5, 120),
    (0, 1),
    (3, 6),
])
def test_compute_factorial_param(n, expected_factorial, capsys):
    val = compute_factorial(n)
    captured = capsys.readouterr()
    assert val == expected_factorial
    assert f"Факториал числа {n} равен {expected_factorial}" in captured.out

def test_main_first_script_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '1 2 -3')
    main_first_script()
    captured = capsys.readouterr()
    assert "Корень номер" in captured.out

def test_main_second_script_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'lol')
    result = main_second_script()
    captured = capsys.readouterr()
    assert result is True
    assert "палиндромом" in captured.out

def test_main_third_script_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    result = main_third_script()
    captured = capsys.readouterr()
    assert result == 120
    assert "Факториал" in captured.out

@pytest.mark.parametrize("user_input, second_input", [
    ('1', '1 2 3'),
    ('2', 'lol'),
    ('3', '5'),
    ('4', ''),
])
def test_main(monkeypatch, user_input, second_input, capsys):
    inputs = iter([user_input, second_input])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    if user_input == '4':
        with pytest.raises(SystemExit):
            main()
    else:
        main()