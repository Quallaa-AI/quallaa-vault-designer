# Reading List

*Last updated: 2026-02-21*

## Foundational Papers

### Force Density Method
- **Schek, H.J. (1974)** — "The force density method for form finding and computation of general networks." *Computer Methods in Applied Mechanics and Engineering.* The original FDM paper.

### Thrust Network Analysis
- **Block, P. & Ochsendorf, J. (2007)** — "Thrust Network Analysis: A new methodology for three-dimensional equilibrium." *Journal of the IASS.* The foundational TNA paper.
- **Block, P. (2009)** — "Thrust Network Analysis: Exploring Three-dimensional Equilibrium." PhD thesis, MIT. Comprehensive treatment.

### Rigid Block Analysis
- **Whiting, E. et al. (2009)** — "Structural Feasibility of Arc-Masonry." *ACM SIGGRAPH.* Stability of masonry arches as rigid block assemblies.
- **Frick, U. et al. (2015)** — "Decomposition of general force networks on masonry vaults." *Structures.* Force decomposition in discrete block vaults.

### Discrete Element Methods
- **Lemos, J.V. (2007)** — "Discrete Element Modeling of Masonry Structures." *International Journal of Architectural Heritage.* DEM applied to historical masonry.

## Researchers

### Philippe Block (ETH Zurich BRG)
- The leading researcher in computational masonry and compression-only structures.
- Developed TNA, led Armadillo Vault, NEST HiLo, and the Venice bridge.
- Lab: [Block Research Group](https://block.arch.ethz.ch/)
- Created the COMPAS ecosystem this project uses.

### Sigrid Adriaenssens (Princeton CREATE Lab)
- Form-finding for shells and funicular structures.
- Combines structural optimization with environmental performance.
- Lab: [CREATE Lab](https://formfindinglab.princeton.edu/)

### Caitlin Mueller (MIT Digital Structures)
- Structural optimization, topology optimization, ML for structural design.
- Bridge between computation and structural engineering education.
- Lab: [Digital Structures](https://digitalstructures.mit.edu/)

### Matthias Kohler & Fabio Gramazio (ETH)
- Pioneers of robotic fabrication in architecture.
- Lab: [Gramazio Kohler Research](https://gramaziokohler.arch.ethz.ch/)

### Tom Van Mele (ETH Zurich BRG)
- Co-developer of COMPAS framework.
- Lead developer of compas_tna, compas_fd.

### John Ochsendorf (MIT → American Academy in Rome)
- Masonry mechanics, historical structures, Guastavino research.
- Key collaborator on TNA development.

## Companies

### Robotic Construction
- **ICON** — 3D-printed homes (concrete extrusion). Austin, TX.
- **COBOD** — 3D printing for construction. Denmark.
- **FBR (Fastbrick Robotics) / Hadrian X** — Robotic bricklaying. Australia.
- **Construction Robotics / SAM** — Semi-automated mason. USA.
- **Mighty Buildings** — 3D-printed prefab ADUs. Oakland, CA.
- **Branch Technology** — Large-scale 3D printing of freeform structures.
- **Apis Cor** — Mobile construction 3D printer.

### Software / Computational Design
- **McNeel & Associates** — Rhino/Grasshopper. Dominant parametric design platform.
- **Autodesk** — Revit, Fusion 360. BIM and engineering.
- **Karamba3D** — Structural analysis plugin for Grasshopper.

## Historical References

### Guastavino Vaulting
- **Ochsendorf, J. (2010)** — *Guastavino Vaulting: The Art of Structural Tile.* Princeton Architectural Press. Definitive book on Guastavino's work.
- Over 600 buildings in the US used Guastavino timbrel vaults (1889-1962). Self-supporting during construction.

### Catalan Vaulting / Timbrel Vaulting
- Thin tile construction. Multiple layers bonded with fast-setting cement. Each course is self-supporting.
- La Voûte Nubienne — modern revival of Nubian vault technique in West Africa. Low-cost, formwork-free.

### Eladio Dieste
- Uruguayan engineer. Gaussian vaults and double-curved reinforced brick shells.
- Showed that brick + geometry can span enormous distances.
- Church of Christ the Worker (Atlántida, 1958) — UNESCO World Heritage Site.

## Open-Source Tools

### COMPAS Ecosystem (MIT License)
- [compas](https://github.com/compas-dev/compas) — Core framework
- [compas_tna](https://github.com/BlockResearchGroup/compas_tna) — Thrust Network Analysis
- [compas_fd](https://github.com/BlockResearchGroup/compas_fd) — Force Density Method
- [compas_cra](https://github.com/BlockResearchGroup/compas_cra) — Coupled Rigid-Block Analysis
- [compas_tno](https://github.com/BlockResearchGroup/compas_tno) — Advanced thrust network solvers

### Other
- [PyVista](https://pyvista.org) — 3D visualization in Python
- [Open3D](http://www.open3d.org) — 3D data processing
- [trimesh](https://trimsh.org) — Triangle mesh processing
