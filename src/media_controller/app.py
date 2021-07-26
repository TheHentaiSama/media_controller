"""Use this file to create wrappers around the functions you want to use in the CLI
"""
from typer import Option, Typer
from .media_controll import main

app = Typer(help="Interface to launch various applications for computer vision")


@app.command("play_button", help="Application using the webcam to control your computer")
def main_wrapper(display: bool = Option(False, "--display", "-d")) -> None:
	"""Wrapper around the main function to use it in the CLI

	Args:
		display (bool, optional): Flag to use in order to get the video feedback.
	"""
	main(display)
