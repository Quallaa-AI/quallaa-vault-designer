# Iterative Roadmap: Communication to Construction

*Last updated: 2026-02-21*

## The Arc

Quallaa starts with AI communication and extends to robotic construction. Each phase builds on the previous one. The same architectural pattern — signal → AI → device → human oversight — scales from phone calls to physical construction.

---

## Phase 1: Communication (Now)

**What:** AI-powered missed call recovery for service businesses. When a call goes unanswered, AI texts the caller and has real conversations to book jobs.

**Status:** Live. Revenue. Customers.

**Key capabilities built:**
- Real-time AI agent orchestration
- Multi-channel message routing (SMS, iMessage, voice)
- Bridge app architecture (signal relay between devices and AI)
- Escalation and human oversight patterns
- Certification and trust framework

**Why it matters for construction:** The bridge pattern (device ↔ AI ↔ human) is exactly the pattern for robotic control. The certification model (proving a system works, not just saying it does) is exactly what robotic construction needs.

---

## Phase 2: Computational Design (This Project)

**What:** Interactive tools for designing compression-only masonry structures. Vaults, domes, arches — designed as discrete brick assemblies, not smooth surfaces.

**Status:** Starting. This repo.

**Milestones:**
- v0.1 — First vault (FDM form-finding, 3D visualization)
- v0.2 — Brick voxelization (surface → discrete blocks)
- v0.3 — Construction sequences (self-supporting build order)
- v0.4 — Custom boundaries and material cost estimation
- v0.5 — Fantastical structures, gallery of renders

**Key capabilities to build:**
- Force Density Method for compression form-finding
- Vault surface → brick voxel discretization
- Rigid block stability analysis (compas_cra)
- Self-supporting construction sequence planning
- Visualization and rendering pipeline

**Why it matters:** This is the intelligence layer. Before a robot can build a vault, someone has to design it and figure out the construction order. The computational design tool IS the brain.

---

## Phase 3: Physical-World Intelligence (Later)

**What:** Extend the AI's understanding to physical space. Sensor integration, spatial awareness, structural monitoring during construction.

**Not started. Conceptual.**

**Key capabilities to build:**
- Computer vision for construction progress tracking
- Structural sensor integration (strain, displacement)
- Real-time comparison: design model vs. as-built reality
- Anomaly detection during construction

---

## Phase 4: Device Orchestration (Later)

**What:** Control robotic devices using the same patterns used for phone communication. The AI agent receives signals (sensor data, design intent), makes decisions, and sends commands to devices (robot arms, material handlers).

**Not started. Conceptual.**

**Key capabilities to build:**
- Robot arm path planning from construction sequences
- Real-time trajectory adjustment based on sensor feedback
- Multi-device coordination (arm + material feed + curing)
- Safety interlocks and human override

---

## Phase 5: Small-Scale Prototyping (Later)

**What:** Physical proof of concept. Build small-scale masonry structures using the computational design tools and basic robotic/CNC equipment.

**Not started. Conceptual.**

**Possible approaches:**
- Desktop robot arm (UR3e, $25K) placing small blocks
- CNC gantry placing units on a table
- Even manual placement following computed sequences (the human IS the robot)

---

## Phase 6: Full-Scale Robotic Masonry (Far Future)

**What:** Production-scale robotic masonry construction. A certified system where AI designs the structure, plans the construction sequence, and orchestrates robots to build it — with a certified human operator overseeing the process.

**The vision:** A contractor calls (or texts, or just draws a floor plan) and says "build me a vault over this patio." The AI designs it, estimates cost, plans the construction, and a robot builds it. A certified operator oversees the process and signs off.

---

## Why This Order

Each phase is useful on its own AND builds capabilities for the next:

1. **Communication** → agent orchestration, bridge pattern, certification
2. **Computational design** → structural intelligence, construction planning
3. **Physical intelligence** → sensor integration, reality awareness
4. **Device orchestration** → robot control using proven patterns
5. **Small prototyping** → physical proof, iteration
6. **Full scale** → production system

You can't skip phases. The intelligence built in each one is required by the next.
