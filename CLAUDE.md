# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
pip install -e ".[dev]"        # Install package with dev dependencies
jupyter lab notebooks/          # Launch notebooks
python -m pytest               # Run tests (none yet)
```

## What This Is

Interactive tool for designing compression-only masonry structures (vaults, domes, arches) as discrete brick assemblies. The structure IS an assembly of bricks — not a smooth surface that gets tiled. Compression geometry ensures the assembly stands. A robot builds voxel by voxel; the construction sequence is inherent in the design.

Part of Quallaa's arc from AI communication to robotic construction (Phase 2: computational design).

## Architecture

**Stack:** Python 3.10+, COMPAS ecosystem, Jupyter notebooks, matplotlib/PyVista

| Layer | Tool | Purpose |
|-------|------|---------|
| Form-finding | `compas_fd` (`fd_numpy`) | Force Density Method — finds compression-only vault shapes |
| Analysis | `compas_tna`, `compas_cra` | Thrust Network Analysis, rigid block stability |
| Geometry | `compas` (Mesh, etc.) | Mesh data structures, boundary detection |
| Visualization | matplotlib, PyVista | 3D surface plots, height-mapped coloring |
| Interaction | Jupyter notebooks | Primary user interface |

### Core FDM Workflow

The fundamental pattern used throughout the project:

1. Create a `compas.datastructures.Mesh` from a floor plan (e.g., `Mesh.from_meshgrid`)
2. Extract: vertices (xyz), edges, fixed boundary vertices, loads (gravity), force densities (one per edge)
3. Solve with `compas_fd.solvers.fd_numpy(vertices, fixed, edges, forcedensities, loads)`
4. Flip Z coordinates to convert hanging net (tension) to vault (compression)

Force density (q) controls shape: higher q = flatter vault, lower q = taller vault. Asymmetric q values per edge direction create directional vaults (barrel vaults, etc.).

## Project State

Currently at **v0.1** — first vault via FDM form-finding with visualization.

**Implemented:**
- `src/vault_designer/boundaries.py` — rectangular floor plan mesh creation
- `src/vault_designer/visualize.py` — `plot_vault()` and `plot_vault_colored()` (matplotlib 3D)
- `notebooks/01-getting-started.ipynb` — complete FDM walkthrough

**Stubs (planned, not yet implemented):**
- `voxelize.py` — vault surface to discrete brick positions (v0.2)
- `sequence.py` — self-supporting construction order via `compas_cra` (v0.3)
- `cost.py` — material cost estimation (v0.4)
- Notebooks 02-07 are planned in README but not yet created

## Roadmap Milestones

- v0.2 — Brick voxelization (surface to discrete blocks)
- v0.3 — Construction sequences (self-supporting build order)
- v0.4 — Custom boundaries and material cost estimation
- v0.5 — Fantastical structures, gallery of renders

## Key COMPAS Patterns

- Meshes are `compas.datastructures.Mesh` — use `mesh.vertices_attributes('xyz')`, `mesh.edges()`, `mesh.vertices_on_boundary()`, `mesh.faces()`, `mesh.face_vertices(face)`
- FDM solver returns a result object with `.vertices` (numpy array) and `.residuals`
- All coordinates are in meters; vertex indices are integers used as keys throughout
