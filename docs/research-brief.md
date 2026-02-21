# Research Brief: Robotic Masonry & Compression Structures

*Last updated: 2026-02-21*

## Current State of Robotic Construction

### 3D Printing (Concrete Extrusion)
- **ICON** (Austin, TX) — largest player. Printed homes in Austin and rural Mexico. Vulcan series printers. $400M+ funding. Limitations: walls only, no structural diversity, limited to single-story, layer-by-layer extrusion constrains geometry.
- **COBOD** (Denmark) — BOD2 printer, deployed globally. Faster but same geometric constraints. Commercial buildings in Germany, Dubai.
- **Mighty Buildings** (Oakland) — 3D-printed ADUs, prefab approach.
- **Apis Cor** — printed a house in 24 hours (Dubai). Mobile printer.

**The gap:** 3D printing is locked into extrusion geometry. You get walls, not structures. No arches, no vaults, no domes. The material is concrete paste — not a structurally optimal form.

### Robotic Bricklaying
- **FBR / Hadrian X** (Australia) — robot arm on a truck lays standard bricks. Fast (1000 bricks/hour claimed) but conventional wall construction. No structural innovation — just automating what a mason does.
- **Construction Robotics / SAM** — semi-automated mason. Collaborative robot, mason still does detail work.

**The gap:** These robots automate conventional construction. They don't unlock new structural forms. A robot that lays bricks in a straight wall is a labor replacement, not a capability expansion.

### Academic Research — Where the Real Work Happens

#### ETH Zurich Block Research Group (BRG)
- Led by Philippe Block. The premier group for computational masonry.
- **COMPAS ecosystem** — open-source Python framework for computational design. MIT-licensed. This project uses it.
- **Key projects:**
  - Armadillo Vault (Venice Architecture Biennale 2016) — unreinforced stone vault, compression-only, no mortar, no tension elements. 399 unique limestone blocks. Proved discrete masonry vaults work.
  - NEST HiLo roof (ETH campus) — thin-shell concrete roof built with cable-net formwork and robotic fabrication.
  - 3D-printed concrete bridge (Venice 2021) — unreinforced, compression-only.
- **Algorithms:** Thrust Network Analysis (TNA), Rigid Block Analysis (RBA), Force Density Method (FDM)
- **Software:** compas, compas_tna, compas_fd, compas_cra, compas_tno — all used in this project

#### Princeton CREATE Lab
- Led by Sigrid Adriaenssens. Form-finding for shells and funicular structures.
- Combines structural optimization with environmental performance.
- Thin shells, gridshells, deployable structures.

#### Other Groups
- **MIT Digital Structures** (Caitlin Mueller) — structural optimization, topology optimization, ML for structural design
- **University of Stuttgart ICD/ITKE** — robotic fiber winding, biomimetic structures
- **Gramazio Kohler Research (ETH)** — robotic fabrication, spatial structures from standard materials

## Masonry Vault History

### Why Vaults?
Compression-only structures are the most material-efficient way to span space. A vault works purely in compression — every piece pushes against its neighbors. No tension, no reinforcing steel, no adhesive required (in theory). The geometry IS the structure.

### Historical Precedents
- **Roman vaults** — concrete with brick formwork. Pantheon dome (43m span, unreinforced, standing for 1900 years)
- **Gothic vaults** — ribbed, pointed arches. Structural expressionism. The ribs carry forces to columns.
- **Guastavino timbrel vaults** — Rafael Guastavino brought Catalan thin-tile vaulting to the US (1880s-1960s). Boston Public Library, Grand Central Terminal, hundreds of buildings. Multiple layers of thin tiles bonded with fast-setting morite. Self-supporting during construction — no formwork.
- **Nubian vaults** — ancient Egyptian technique, still used today (La Voûte Nubienne). Mud brick, built without formwork using leaning arch technique. Each course leans against the previous one.
- **Eladio Dieste** — Uruguayan engineer. Gaussian vaults, double-curved brick shells. Factory buildings spanning 50m+ with just brick and mortar.

### Key Structural Principles
- **Funicular form:** The shape a hanging chain takes under load. Flip it and you get a compression arch. Extend to 2D and you get a vault/dome.
- **Thrust line:** The path of compression force through the structure. If the thrust line stays within the material, the structure stands.
- **Stability, not strength:** Masonry vaults fail by mechanism (moving), not by crushing. The geometry determines stability, not material strength.
- **No tension:** Masonry can't resist tension. The form must ensure all forces resolve in compression.

## The Gap This Project Addresses

### What Exists
- Academic algorithms for form-finding (COMPAS, TNA, FDM)
- Robots capable of placing bricks precisely
- Historical proof that compression vaults work at scale

### What's Missing
1. **Design-to-construction pipeline:** No integrated tool goes from structural form-finding → brick discretization → construction sequence → robot instructions.
2. **Construction sequence planning:** A vault can't be built all at once — you need an order that ensures each partially-built state is stable. This is an unsolved problem for complex geometries.
3. **Unified orchestration:** The robot needs real-time awareness of the structure it's building. Currently there's no system that combines structural analysis, construction planning, and robotic control.
4. **Certification framework:** No standards for validating that a robotically-built masonry structure is safe. No chain of trust from design to occupancy.

### The Quallaa Thesis

The bridge architecture pattern — **signal → AI → device → human oversight** — generalizes:

| Domain | Signal | AI | Device | Oversight |
|--------|--------|-----|--------|-----------|
| Communication | Missed call | Conversation agent | Phone (Twilio/bridge) | Business owner |
| Construction | Design intent | Structural + sequence AI | Robot arm | Engineer/operator |

The certification model also generalizes:
- **Certified Pro** (communication) → trusted to handle customer interactions
- **Certified Partner** (operations) → trusted to manage business workflows
- **Certified Operator** (construction) → trusted to oversee robotic construction

## Key References

See `reading-list.md` for papers, researchers, and companies.
