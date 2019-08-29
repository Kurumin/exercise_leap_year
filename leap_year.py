# encoding: utf-8


def validate_input(input_):
    """ Checks input """
    return int(input_) if input_.isdigit() and 1 <= int(input_) else validate_input(input('Entrada inválida, digite novamente: '))

def is_bissextile(year_):
    return year_ % 400 == 0 or (year_ % 4 == 0 and year_ % 100 != 0)


if __name__ == '__main__':
    year = validate_input(input('Digite o ano para verificar se é bissexto: '))
    print('O ano {} {}é bissexto'.format(year, '' if is_bissextile(year) else 'não '))
