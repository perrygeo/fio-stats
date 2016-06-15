from __future__ import division
from collections import defaultdict
import json

import click
from tabulate import tabulate
from cligj import features_in_arg


@click.command(short_help="Summary statistics for GeoJSON feature properties")
@click.option("--table", '-t', is_flag=True, default=False,
              help="Output a formated table")
@features_in_arg
@click.pass_context
def stats(ctx, features, table):
    """Calculate summary statistics for GeoJSON features."""
    attr_names = set()
    data = defaultdict(list)
    for feature in features:
        prop = feature['properties']
        for key, value in prop.items():
            attr_names.add(key)
            try:
                value = float(value)
            except (TypeError, ValueError):
                pass

            data[key].append(value)

    headers = "attr min mean max n n_unique".split()
    rows = []
    for attr in sorted(data.keys()):
        values = [v for v in data[attr] if v is not None]
        n = len(values)
        nu = len(set(values))

        total = None
        mean = None
        minv = None
        maxv = None
        if n > 0:
            try:
                total = sum(values)
                mean = total / float(n)
                minv = min(values)
                maxv = max(values)
            except TypeError:
                pass

        row = (attr, minv, mean, maxv, n, nu)
        rows.append(row)

    if table:
        click.echo(tabulate(rows, headers=headers))
    else:
        d = [dict(zip(headers, r)) for r in rows]
        click.echo(json.dumps(d, indent=2))

if __name__ == "__main__":
    stats()
