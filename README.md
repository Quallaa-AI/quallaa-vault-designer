# Quallaa Vault Designer

Interactive tool for designing compression-only masonry structures — vaults, domes, arches — composed of discrete brick voxels.

Each brick is a volumetric unit in 3D space. The design tool works directly in brick-space: the vault isn't a smooth surface that gets tiled — it **is** an assembly of bricks, and the compression geometry ensures the assembly stands.

Minecraft meets structural engineering meets robotics.

## Quick Start

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install
pip install -e ".[dev]"

# Launch notebooks
jupyter lab notebooks/
```

Open `01-getting-started.ipynb` and run the cells to generate your first vault.

## What's Inside

### Notebooks

| Notebook | What it does |
|----------|-------------|
| `01-getting-started` | COMPAS basics, first vault via Force Density Method |
| `02-force-density` | Parameter exploration — how force density shapes the vault |
| `03-custom-boundaries` | Non-rectangular floor plans |
| `04-brick-discretization` | Surface → individual brick positions |
| `05-pixel-patterns` | Color assignment, facade design |
| `06-construction-sequence` | Self-supporting build order |
| `07-cost-estimation` | Material cost calculator |

### Python Module (`src/vault_designer/`)

Reusable functions extracted from notebooks:

- `boundaries.py` — Floor plan boundary definitions
- `voxelize.py` — Vault surface → discrete brick voxels
- `sequence.py` — Self-supporting construction order
- `cost.py` — Material cost estimation
- `visualize.py` — Rendering helpers

## Built With

- [COMPAS](https://compas.dev) — computational framework for architecture, engineering, and fabrication
- [compas_tna](https://github.com/BlockResearchGroup/compas_tna) — Thrust Network Analysis
- [compas_fd](https://github.com/BlockResearchGroup/compas_fd) — Force Density Method
- [PyVista](https://pyvista.org) — 3D visualization
- [Jupyter](https://jupyter.org) — interactive notebooks

## Why

A robot builds the structure voxel by voxel, and the construction sequence is inherent in the design. This tool is the computational design layer in a design-to-construction pipeline for robotic masonry.

Part of [Quallaa](https://www.quallaa.com)'s long-term arc from AI communication to robotic construction.

## License

MIT
