import secrets


def generate(length: int, characters: str):
    return "".join(secrets.choice(characters) for _ in range(length))
