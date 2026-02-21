"""Vault surface to discrete brick voxel discretization.

Converts a smooth FDM vault surface into individual brick positions.
Each mesh face becomes a volumetric brick extruded inward along the surface normal.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

if False:  # TYPE_CHECKING
    from compas.datastructures import Mesh


@dataclass
class BrickAssembly:
    """A collection of discrete bricks derived from a vault mesh.

    Parameters
    ----------
    centers : numpy.ndarray
        Brick center positions, shape (n_bricks, 3).
    normals : numpy.ndarray
        Outward-facing unit normals per brick, shape (n_bricks, 3).
    neighbors : list[list[int]]
        Adjacency list — ``neighbors[i]`` is the list of brick indices
        adjacent to brick *i*.
    thickness : float
        Uniform brick depth in meters.
    corners : numpy.ndarray
        Eight corner vertices per brick, shape (n_bricks, 8, 3).
        Indices 0-3 are the outer face, 4-7 are the inner face.
    face_vertices : list[list[int]]
        Original mesh vertex indices for each face (for traceability).
    """

    centers: np.ndarray
    normals: np.ndarray
    neighbors: list[list[int]]
    thickness: float
    corners: np.ndarray
    face_vertices: list[list[int]]

    def __len__(self) -> int:
        return len(self.centers)


def compute_face_normals(xyz: np.ndarray, mesh: Mesh) -> np.ndarray:
    """Compute outward-pointing unit normals for each mesh face.

    Uses the cross product of quad diagonals for each face, then orients
    normals to point away from the vault centroid (outward).

    Parameters
    ----------
    xyz : numpy.ndarray
        Vertex coordinates, shape (n_vertices, 3).
    mesh : compas.datastructures.Mesh
        The mesh providing face connectivity.

    Returns
    -------
    numpy.ndarray
        Unit normals, shape (n_faces, 3).
    """
    centroid = xyz.mean(axis=0)
    normals = []

    for face in mesh.faces():
        fv = mesh.face_vertices(face)
        pts = xyz[fv]
        # Cross product of quad diagonals
        d0 = pts[2] - pts[0]
        d1 = pts[3] - pts[1]
        n = np.cross(d0, d1)
        length = np.linalg.norm(n)
        if length > 1e-12:
            n = n / length
        # Orient outward: normal should point away from vault centroid
        face_center = pts.mean(axis=0)
        if np.dot(n, face_center - centroid) < 0:
            n = -n
        normals.append(n)

    return np.array(normals)


def voxelize(xyz: np.ndarray, mesh: Mesh, thickness: float = 0.2) -> BrickAssembly:
    """Convert a vault surface mesh into discrete bricks.

    Each mesh face becomes a volumetric brick by extruding the face inward
    (opposite to the outward normal) by *thickness*.

    Parameters
    ----------
    xyz : numpy.ndarray
        Vertex coordinates from the FDM solver, shape (n_vertices, 3).
    mesh : compas.datastructures.Mesh
        The mesh providing face/edge connectivity.
    thickness : float
        Brick depth in meters (default 0.2).

    Returns
    -------
    BrickAssembly
        The discrete brick assembly.
    """
    normals = compute_face_normals(xyz, mesh)

    faces = list(mesh.faces())
    n_bricks = len(faces)
    centers = np.zeros((n_bricks, 3))
    corners = np.zeros((n_bricks, 8, 3))
    face_verts_list: list[list[int]] = []

    for i, face in enumerate(faces):
        fv = mesh.face_vertices(face)
        face_verts_list.append(fv)
        pts = xyz[fv]  # (4, 3) for quads

        # Outer face vertices are the original mesh face vertices
        corners[i, :4] = pts
        # Inner face vertices: extrude inward (opposite to outward normal)
        corners[i, 4:8] = pts - thickness * normals[i]

        # Center is midpoint between outer and inner face centers
        centers[i] = pts.mean(axis=0) - 0.5 * thickness * normals[i]

    # Build neighbor adjacency via mesh face neighbors
    face_to_idx = {face: i for i, face in enumerate(faces)}
    neighbors: list[list[int]] = [[] for _ in range(n_bricks)]
    for i, face in enumerate(faces):
        for nb_face in mesh.face_neighbors(face):
            if nb_face in face_to_idx:
                neighbors[i].append(face_to_idx[nb_face])

    return BrickAssembly(
        centers=centers,
        normals=normals,
        neighbors=neighbors,
        thickness=thickness,
        corners=corners,
        face_vertices=face_verts_list,
    )


def brick_faces(corners: np.ndarray) -> list[np.ndarray]:
    """Convert 8 brick corners into 6 quad face polygons.

    Parameters
    ----------
    corners : numpy.ndarray
        Shape (8, 3) — outer face [0:4], inner face [4:8].

    Returns
    -------
    list[numpy.ndarray]
        Six polygons, each shape (4, 3), in order:
        outer, inner, and four side faces.
    """
    # Outer face: 0-1-2-3
    # Inner face: 4-5-6-7 (reversed winding for outward normal)
    # Sides: connecting outer[i] to inner[i]
    return [
        corners[[0, 1, 2, 3]],       # outer
        corners[[7, 6, 5, 4]],       # inner (reversed)
        corners[[0, 1, 5, 4]],       # side 0-1
        corners[[1, 2, 6, 5]],       # side 1-2
        corners[[2, 3, 7, 6]],       # side 2-3
        corners[[3, 0, 4, 7]],       # side 3-0
    ]
