import typer

app = typer.Typer()


@app.command()
def main(
    username: str,
    password: str = typer.Option(..., prompt=True, confirmation_prompt=True)
):
    print(f"Hello {username}. Doing something very secure with password.\n...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    app()