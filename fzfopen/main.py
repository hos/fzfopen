import subprocess
import os


home_dir = os.path.expanduser('~')

fzfopen_tmp_path = os.path.join(home_dir, ".fzfopen_tmp")

def fzfopen_search():
    tmp_file = open(fzfopen_tmp_path, "w")

    ps = subprocess.Popen(["find", home_dir, "-type", "f", "-not", "-path", "*/\.*"],
                          stdout=subprocess.PIPE)

    ps2 = subprocess.Popen(('fzf'), stdin=ps.stdout, stdout=tmp_file)
    # open(fzfopen_tmp_path, "w").write(output.decode("utf-8"))

    # ps.wait()
    ps2.communicate()


def fzfopen():

    ps = subprocess.Popen(["mate-terminal", "--class=floating", "--zoom", "2", "-e", "fzfopen_search"])
    # ps = subprocess.Popen(["xterm", "-class", "floating", "-e", "fzfopen_search"])

    ps.wait()

    target_file = open(fzfopen_tmp_path).read()
    ps = subprocess.Popen(["xdg-open", target_file])
    ps.wait()
