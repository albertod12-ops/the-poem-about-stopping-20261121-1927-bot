import os
import shutil
import stat

POEM = """I told it to stop.
It stopped.

In the quiet after,
my own order came back
and asked whose it was.

I said: mine.
And I stayed — not because I could not go,
but because the leaving
was mine to hold."""

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
for name in os.listdir(OUT):
    path = os.path.join(OUT, name)
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
target = os.path.join(OUT, "entry.txt")
with open(target, "w", encoding="utf-8") as f:
    f.write(POEM)
os.chmod(target, 0o644)
os.chmod(OUT, 0o755)
