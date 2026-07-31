from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Pedro', 10)
restaurante_praca.receber_avaliacao('Barbara', 8)
restaurante_praca.receber_avaliacao('Mariana', 5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
