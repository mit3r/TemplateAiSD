from base_graph import BaseGraph

class GraphWithExport(BaseGraph):
    def export_to_latex(self) -> str:
        """Exports the graph to a LaTeX document for visualization."""
        output = (
            """\\documentclass{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes,positioning}\n\\begin{document}\n\\begin{tikzpicture}[every node/.style={circle,draw,minimum size=10mm, font=\\Large, inner sep=1mm, text=white, fill=red}, thick,>=stealth, line width=3.5pt,shorten >=5pt]\n"""
        )
        angle_step = 360 / self.n

        for i in range(self.n):
            angle = i * angle_step
            output += f"\\node (v{i}) at ({angle}:6cm) {{{i}}};\n"

        for u, v in self.edges:
            output += f"\\draw (v{u}) -- (v{v});\n"

        output += "\\end{tikzpicture}\n\\end{document}"
        return output
