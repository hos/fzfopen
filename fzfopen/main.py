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
    # ps2.communicate()
    ps2.wait()


def fzfopen():
    # ps = subprocess.Popen(["mate-terminal", "--class=floating", "--zoom", "2", "-e", "fzfopen_search"])
    ps = subprocess.Popen(["xterm", "-fn", "10x20", "-class", "floating", "-e", "fzfopen_search"])

    ps.wait()

    target_path = open(fzfopen_tmp_path).read().strip()
    if not target_path:
        return

    ps = subprocess.Popen(["xdg-open", target_path])
    ps.wait()
