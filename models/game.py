import random


class Game:
    def __init__(self):
        self.random_number = random.randint(1, 100)
        self.score = 1000
        self.attempts = 0

    @staticmethod
    def welcome_to_game() -> None:
        print('**********************************')
        print('Bem vindos ao jogo de adivinhação!')
        print('**********************************')
        print('Tente adivinhar o número secreto!!')
        print('**********************************')

    def request_user_name(self) -> str:
        request_name = input('Digite seu nome: ')
        return request_name

    def request_user_number(self) -> int:
        request_number = input('Digite um número: ')
        print('**********************************')
        try:
            return int(request_number)
        except ValueError:
            print('Digite um número inteiro válido!!')
            self.request_user_number()

    def return_attemps(self) -> int:
        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")
        level = input('Digite o nível de dificuldade: ')
        try:
            if int(level) == 1:
                self.attempts = 20
            elif int(level) == 2:
                self.attempts = 10
            elif int(level) == 3:
                self.attempts = 5
            else:
                print('Digite uma dificuldade valida!!')
                self.return_attemps()
            return self.attempts
        except ValueError:
            print('Digite uma dificuldade valida!!')
            self.return_attemps()

    def validate_possibilities(self, guessed) -> bool:
        if guessed == self.random_number:
            print('Você acertou!!')
            print('**********************************')
            self.calc_score()
            print('**********************************')
            return True
        elif guessed != self.random_number:
            print('Você errou!!')
            print('**********************************')
            self.calc_score()
            print('**********************************')

    def validate_rounds(self):
        for attempts in range(1, self.attempts + 1):
            print("Tentativa {} de {}".format(attempts, self.attempts))
            print('**********************************')
            guessed = self.request_user_number()
            print("Você digitou ", guessed)
            if self.validate_possibilities(guessed):
                break
        print('Fim de jogo!')
        print(f'O número era {self.random_number}')
        self.calc_score()

    def calc_score(self) -> int:
        score = abs(self.random_number - self.score)
        self.score = score
        print(f'Pontuação: {score}')
        return self.score
