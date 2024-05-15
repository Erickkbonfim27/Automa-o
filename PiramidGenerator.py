class Generator:
    def TrianguloInvertido(str):
        for i in range(5):
            x=f'{str} '
            x=x*(5-i)
            print(f'{x: ^10}')

    def Diamond(str):
        for i in range(5):
            x=f'{str} '
            x=x*i
            print(f'{x: ^10}')
        for i in range(5):
            x=f'{str} '
            x=x*(5-i)
            print(f'{x: ^10}')

    def TrianguloLadoDireito(str):
        for i in range(5):
            x=f'{str} '
            x=x*i
            print(f'{x: >10}')

    def TrianguloLadoEsquerdo(str):
        for i in range(5):
            x=f'{str} '
            x=x*i
            print(f'{x: <10}')

    def Triangulo(str):
        for i in range(5):
            x=f'{str} '
            x=x*i
            print(f'{x: ^10}')

Generator.TrianguloInvertido('k')
Generator.Diamond('5')
Generator.TrianguloLadoDireito('s')
Generator.TrianguloLadoEsquerdo('X')
Generator.Triangulo('Y')
