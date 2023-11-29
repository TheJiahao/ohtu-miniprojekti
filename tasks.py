from invoke import task


@task
def main(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)
    ctx.run("robot src/tests/robot", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src && coverage html", pty=True)


@task
def refactor(ctx):
    ctx.run("black src && pylint src", pty=True)
