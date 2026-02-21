# TNA & FDM Reference

*Last updated: 2026-02-21*

## Force Density Method (FDM)

### The Core Idea

A network of cables hangs from fixed points under gravity. Each cable has a "force density" q = force / length. Given the force densities, fixed points, and loads, the equilibrium shape can be found by solving a single linear system.

**Why it matters:** The hanging shape is pure tension. Flip it upside down and every force becomes compression. This gives you a vault shape where the material works purely in compression — the most efficient structural form.

### Mathematical Formulation

Given:
- **C** — connectivity matrix (edges × vertices). Row i has -1 at start vertex, +1 at end vertex.
- **Q** — diagonal matrix of force densities (edges × edges)
- **x, y, z** — vertex coordinate vectors
- **px, py, pz** — load vectors (force at each vertex)

The equilibrium equations:

```
C^T Q C x = px
C^T Q C y = py
C^T Q C z = pz
```

Split vertices into free (f) and fixed (d):

```
D_ff x_f = p_xf - D_fd x_d
```

Where `D = C^T Q C` is the force density stiffness matrix.

This is a **linear** system — single solve, no iteration needed. That's the power of FDM: by parameterizing with force density (not force), the nonlinear equilibrium problem becomes linear.

### In COMPAS

```python
from compas_fd.solvers import fd_numpy

result = fd_numpy(
    vertices=[[x, y, z], ...],     # n × 3, initial coordinates
    fixed=[0, 1, 2, ...],          # indices of fixed vertices
    edges=[(0, 1), (1, 2), ...],   # edge connectivity
    forcedensities=[q1, q2, ...],  # one per edge
    loads=[[px, py, pz], ...],     # one per vertex
)

# result.vertices — equilibrium coordinates (n × 3 numpy array)
# result.forces — edge forces
# result.lengths — edge lengths
# result.residuals — residual forces at vertices
```

### Parameter Intuition

| Parameter | Effect |
|-----------|--------|
| Higher q (all edges) | Stiffer net → flatter vault → lower peak height |
| Lower q (all edges) | Looser net → deeper sag → taller vault |
| Higher load | Deeper sag → taller vault |
| Different q per direction | Directional stiffness → barrel vaults, asymmetric forms |
| Non-uniform q | Complex curvature patterns |

### Key Relationship

Force density: **q = f / l**

Where f is the force in the edge and l is the edge length. By prescribing q, you control the ratio — the solver finds the actual force and length.

---

## Thrust Network Analysis (TNA)

### Beyond FDM

TNA (developed by Philippe Block at MIT/ETH) extends the funicular concept to 3D networks. While FDM finds AN equilibrium shape for given force densities, TNA works within the framework of graphic statics to find shapes that satisfy both equilibrium AND geometric constraints.

### Key Concepts

- **Form diagram** — the plan view of the thrust network (the floor plan pattern)
- **Force diagram** — the reciprocal diagram where edge lengths represent forces
- **Thrust network** — the 3D equilibrium shape

The form and force diagrams are reciprocal: corresponding edges are perpendicular, and the ratio of edge lengths gives the force densities.

### TNA vs FDM

| | FDM | TNA |
|---|-----|-----|
| Input | Force densities directly | Force diagram geometry |
| Solution | Linear (single solve) | Iterative (nonlinear constraints) |
| Control | Numerical (q values) | Geometric (diagram manipulation) |
| Intuition | Less visual | More visual (reciprocal diagrams) |
| Best for | Quick exploration, parametric studies | Design refinement, geometric control |

### In COMPAS

```python
from compas_tna.diagrams import FormDiagram, ForceDiagram
from compas_tna.equilibrium import horizontal_nodal, vertical_from_zmax

# Create form diagram from mesh
form = FormDiagram.from_meshgrid(dx=10, nx=10)

# Compute force diagram (horizontal equilibrium)
force = ForceDiagram.from_formdiagram(form)
horizontal_nodal(form, force)

# Find vertical equilibrium for target height
zmax = 3.0  # target peak height
vertical_from_zmax(form, zmax)
```

---

## Rigid Block Analysis

### What It Does

Once a vault is discretized into individual blocks, we need to check: does this assembly actually stand? Rigid Block Analysis (RBA / CRA) checks the stability of assemblies of discrete rigid blocks under gravity and other loads.

### Key Questions RBA Answers

1. **Is the assembly stable?** Do all forces resolve in compression?
2. **Which blocks are critical?** Where are the weakest points?
3. **Is a partial assembly stable?** Can we remove some blocks and have it still stand? (Critical for construction sequencing.)
4. **What are the contact forces?** Forces between each pair of touching blocks.

### In COMPAS

```python
# compas_cra — Coupled Rigid-block Analysis
# Used for checking stability of block assemblies
# and determining construction sequences
```

### Why It Matters for Construction

A robot builds the vault one brick at a time. At every step, the partially-built structure must be stable (or temporarily supported). RBA tells us which construction sequences result in stable intermediate states.

---

## Further Reading

See `reading-list.md` for papers on these methods.
