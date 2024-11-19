import cmd
import os
from system.system import do_mem, do_ip, do_sys
from file_management.file_management import (
    do_in,
    do_out,
    do_create,
    do_delete,
    do_clean,
    do_list,
    do_size,
    do_unzip,
    do_zip,
)
from download.download import do_yt, do_ig
import readline


class Dimi(cmd.Cmd):
    dirprefix = os.getcwd()
    prompt = f"{dirprefix} (DIMI_CLI)> "

    def __init__(self):
        super().__init__()
        if os.name == "nt":
            try:
                import pyreadline3

                readline = pyreadline3.Readline()
                readline.parse_and_bind("tab: complete")
            except ImportError:
                print(
                    "Please install pyreadline3 for tab completion: pip install pyreadline3"
                )
        else:
            readline.parse_and_bind("tab: complete")

    def do_help(self, line):
        print(
            """
        DIMI CLI is a command line interface for general use with many commands aimed to make your life easier.

        help - show this help message
        exit - exit the program
        clear - clear the screen
              
        System:
            mem - show memory usage of the CLI in MB
            ip - show ip address
            sys - run system commands (e.g. sys ls)
              
        File Management:
            in - go into a directory (e.g. in C:\\Users\\)
            out - go up one directory
            create - create a file or directory (e.g. create file.txt)
            delete - delete a file or directory (e.g. delete file.txt)
            clean - clean the current directory
            list - list files in the current directory
              
        Download:
            yt - download youtube videos (mp3/mp4) (e.g. yt mp3 https://youtu.be/D1sGvTU-sZU)
            ig - download instagram photos/reels (e.g. ig https://www.instagram/reel/daswWDas)
        """
        )

    def do_clear(self, line):
        # clear screen
        os.system("cls" if os.name == "nt" else "clear")

    def do_exit(self, line):
        return True

    # system
    def do_mem(self, line):
        do_mem(self, line)

    def do_ip(self, line):
        do_ip(self, line)

    def do_sys(self, line):
        do_sys(self, line)

    # file management
    def do_in(self, line):
        do_in(self, line)

    def do_out(self, line):
        do_out(self, line)

    def do_create(self, line):
        do_create(self, line)

    def do_delete(self, line):
        do_delete(self, line)

    def do_clean(self, line):
        do_clean(self, line)

    def do_list(self, line):
        do_list(self, line)

    def do_size(self, line):
        do_size(self, line)

    def do_unzip(self, line):
        do_unzip(self, line)

    def do_zip(self, line):
        do_zip(self, line)

    def complete_in(self, text, line, begidx, endidx):
        """Tab completion for 'in' command"""
        return [f for f in os.listdir(".") if f.startswith(text) and os.path.isdir(f)]

    def complete_delete(self, text, line, begidx, endidx):
        """Tab completion for 'delete' command"""
        return [f for f in os.listdir(".") if f.startswith(text)]

    def complete_size(self, text, line, begidx, endidx):
        """Tab completion for 'size' command"""
        return [f for f in os.listdir(".") if f.startswith(text)]

    def complete_unzip(self, text, line, begidx, endidx):
        """Tab completion for 'unzip' command"""
        return [f for f in os.listdir(".") if f.startswith(text) and f.endswith(".zip")]

    def complete_zip(self, text, line, begidx, endidx):
        """Tab completion for 'zip' command"""
        return [f for f in os.listdir(".") if f.startswith(text)]

    # download
    def do_yt(self, line):
        do_yt(self, line)

    def do_ig(self, line):
        do_ig(self, line)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to DIMI CLI - type 'help' for a list of commands")
    Dimi().cmdloop()
