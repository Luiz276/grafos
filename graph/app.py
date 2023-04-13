from graph.graph import Graph
from pathlib import Path

from reader import import_graph

def main(*args) -> None:
    if args:
        path = Path.resolve(__file__)
        path = path.parents[0]
        filepath = path / args
    graph = import_graph(filepath)