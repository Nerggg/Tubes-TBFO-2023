import argparse
import os

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("pda", nargs = '?', help = "File konfigurasi PDA.")
    parser.add_argument("html", nargs = '?', help = "File HTML yang akan diperiksa.")
    args = parser.parse_args()

    if (args.pda is None or args.html is None):
        print("Tidak ada file yang diberikan.")
        print("\nUsage: python main.py <file_pda> <file_html>")
        return (False, "", "")

    else:
        filepda = args.pda
        filehtml = args.html

        if (os.path.isfile("pda\\" + filepda) == False):
            print(f"Konfigurasi PDA dengan nama file {filepda} tidak ada.")
            print("\nUsage: python main.py <file_pda> <file_html>")
            return (False, "", "")
        if (os.path.isfile("html\\" + filehtml) == False):
            print(f"File HTML dengan nama file {filehtml} tidak ada.")
            print("\nUsage: python main.py <file_pda> <file_html>")
            return (False, "", "")

        filepda = "pda\\" + args.pda
        filehtml = "html\\" + args.html

        print("\nFile berhasil dimuat!\n")
        return (True, filepda, filehtml)
