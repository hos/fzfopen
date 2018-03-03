import subprocess
import os
import argparse

home_dir = os.path.expanduser('~')

fzfopen_tmp_path = os.path.join(home_dir, ".fzfopen_tmp")

def fzfopen_find():
    tmp_file = open(fzfopen_tmp_path, "w")

    # ps = subprocess.Popen(["find", home_dir, "-type", "f", "-not", "-path", "*/\.*"],
    #                       stdout=subprocess.PIPE)
    ps = subprocess.Popen(["find", home_dir], stdout=subprocess.PIPE)

    ps2 = subprocess.Popen(('fzf'), stdin=ps.stdout, stdout=tmp_file)
    # open(fzfopen_tmp_path, "w").write(output.decode("utf-8"))

    # ps.wait()
    # ps2.communicate()
    ps2.wait()

def fzfopen_locate():
    tmp_file = open(fzfopen_tmp_path, "w")
    ps = subprocess.Popen(["locate", home_dir], stdout=subprocess.PIPE)
    ps2 = subprocess.Popen(('fzf'), stdin=ps.stdout, stdout=tmp_file)
    ps2.wait()

parser = argparse.ArgumentParser()
parser.add_argument('--find', help='Use `find` instead of `locate`. Takes more time \
but can find files not already in the database', action='store_true')

def fzfopen():
    # ps = subprocess.Popen(["mate-terminal", "--class=floating", "--zoom", "2", "-e", "fzfopen_search"])
    args = parser.parse_args()

    if args.find:
        ps = subprocess.Popen(["xterm", "-fn", "10x20", "-class", "floating", "-e", "fzfopen_find"])
    else:
        ps = subprocess.Popen(["xterm", "-fn", "10x20", "-class", "floating", "-e", "fzfopen_locate"])

    ps.wait()

    target_path = open(fzfopen_tmp_path).read().strip()
    if not target_path:
        return

    ps = subprocess.Popen(["xdg-open", target_path])
    ps.wait()
