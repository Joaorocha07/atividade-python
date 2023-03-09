def mensagem_erro(msg):
    print("\033[1;49;31m-\033[m"*35)
    print(f"\033[1;49;31m{msg}\033[m")
    print("\033[1;49;31m-\033[m"*35)

def mensagem_certo(msg):
    print("\033[1;49;32m-\033[m"*35)
    print(f"\033[1;49;32m{msg}\033[m")
    print("\033[1;49;32m-\033[m"*35)