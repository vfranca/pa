"""
Calcula o gap do dia
"""

import click


@click.command()
@click.argument("coy", envvar="COY", type=float)
@click.argument("ood", envvar="OOD", type=float)
@click.option("--digitos", "-d", type=int, default=0)
def gp(coy, ood, digitos):
    """Calcula o gap do dia"""
    gap = ood - coy
    click.echo("%.{0}f".format(digitos) % gap)


if __name__ == "__main__":
    gp()
