# Import click module
import click


@click.command()
# Add a name parameter to the main function
@click.option("--name", prompt="Enter your name", help="The person to greet.")
# Update the main function to accept the name parameter
def main(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
