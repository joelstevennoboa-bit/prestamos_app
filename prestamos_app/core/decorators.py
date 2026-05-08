def log_action(func):

    def wrapper(*args, **kwargs):

        print(f"\n[LOG] Ejecutando: {func.__name__}")

        return func(*args, **kwargs)

    return wrapper
    