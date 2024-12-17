from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')
BASE_URL = env('BASE_URL')