from models.game import Game


def start_game():
    game = Game()
    game.welcome_to_game()
    game.return_attemps()
    game.request_user_name()
    game.validate_rounds()


start_game()
