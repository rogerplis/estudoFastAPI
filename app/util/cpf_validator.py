import re


def validate(cpf: str) -> bool:
    # Verifica a formatação do cpf
    # if not re.match(r'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}', cpf):
    # return False

    # Obtem apenas os numeros do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 numeros ou se todos sao iguais
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # validação do primeiro digito verificador
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

        # validação do primeiro digito verificador
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


