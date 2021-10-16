class Logger():
    def LogInformation(message:str):
        print(f'[LOG-INFO]:    {message}')
    def LogError(message:str):
        print(f'[LOG-ERR]:     {message}')
    def LogWarning(message:str):
        print(f'[LOG-WARN]:    {message}')