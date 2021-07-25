"""Use this file to create wrappers around the functions you want to use in the CLI
"""
from typer import Option, Typer
from .media_controll import play_button

app = Typer()


@app.command("play_button")
def play_button_wrapper(display: bool = Option(False, "--display", "-d")) -> None:
	"""Wrapper around the play_button function to use it in the CLI

	Args:
		verbose (bool, optional): Flag to use in order to get the video feedback.
			 Defaults to Option(False, "--display", "-d").
	"""
	play_button(display)
