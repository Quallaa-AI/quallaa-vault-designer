"""Vault surface to discrete brick voxel discretization."""

# v0.2 — Convert vault thrust surface into individual brick positions.
# Each face in the mesh becomes a volumetric brick unit with:
# - center position (x, y, z)
# - orientation (normal to the surface at that point)
# - neighbor relationships (which bricks touch which)
# - thickness (brick depth along the normal direction)
