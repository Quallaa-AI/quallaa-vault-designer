# CLAUDE.md

## Commands
```bash
pip install -e ".[dev]"   # Install with dev dependencies
jupyter lab                # Launch notebooks
python -m pytest           # Run tests (when added)
```

## What This Is

Interactive tool for designing compression-only masonry structures — vaults, domes, arches — where the structure is composed of discrete brick voxels. Each brick is a volumetric unit in 3D space. The design tool works directly in brick-space: the vault isn't a smooth surface that gets tiled — it IS an assembly of bricks, and the compression geometry ensures the assembly stands.

Minecraft meets structural engineering meets robotics. A robot builds the structure voxel by voxel, and the construction sequence is inherent in the design.

**Stack:** Python, COMPAS ecosystem (TNA, FDM, CRA), Jupyter notebooks, PyVista/matplotlib

## Architecture

| Layer | Tool | Why |
|-------|------|-----|
| Structural math | `compas`, `compas_tna`, `compas_fd` | MIT-licensed, mature BRG tools |
| Visualization | PyVista + matplotlib | 3D rendering in notebooks |
| Interactive exploration | Jupyter notebooks | Fast iteration, visual output |
| Package management | pip | Standard Python packaging |

## Key COMPAS Packages

- `compas` — core framework (geometry, data structures, algorithms)
- `compas_tna` — Thrust Network Analysis (compression-only form-finding)
- `compas_fd` — Force Density Method (constrained form-finding)
- `compas_cra` — Coupled Rigid-Block Analysis (stability, construction sequences)

## Project Structure

- `notebooks/` — Jupyter notebooks, numbered sequentially
- `src/vault_designer/` — Reusable Python module
- `docs/` — Research docs, references, roadmap
- `examples/` — Saved vault designs and renders

## Connection to Quallaa

Part of the Quallaa long-term arc: Communication → Computational Design → Device Orchestration → Robotic Masonry. The bridge architecture (signal → AI → device → human oversight) generalizes from phones to robots. This project is Phase 2: computational design research and experimentation.
