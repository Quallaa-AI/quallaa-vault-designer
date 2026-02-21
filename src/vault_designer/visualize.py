"""Rendering helpers for vault visualization."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from vault_designer.voxelize import BrickAssembly, brick_faces


def plot_vault(xyz, mesh, title="Vault", elev=30, azim=-60, color='steelblue', figsize=(14, 10)):
    """Plot a vault surface from vertex coordinates and mesh connectivity.

    Parameters
    ----------
    xyz : numpy.ndarray
        Vertex coordinates (n × 3).
    mesh : compas.datastructures.Mesh
        The mesh providing face connectivity.
    title : str
        Plot title.
    elev : float
        Elevation angle for 3D view.
    azim : float
        Azimuth angle for 3D view.
    color : str
        Face color.
    figsize : tuple
        Figure size.

    Returns
    -------
    tuple
        (fig, ax) matplotlib figure and axes.
    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    face_verts = []
    for face in mesh.faces():
        fv = mesh.face_vertices(face)
        face_verts.append([xyz[v] for v in fv])

    poly = Poly3DCollection(
        face_verts, alpha=0.7,
        facecolor=color, edgecolor='darkslategray', linewidth=0.3,
    )
    ax.add_collection3d(poly)

    ax.set_xlim(xyz[:, 0].min() - 0.5, xyz[:, 0].max() + 0.5)
    ax.set_ylim(xyz[:, 1].min() - 0.5, xyz[:, 1].max() + 0.5)
    ax.set_zlim(-0.5, xyz[:, 2].max() + 1.0)

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.view_init(elev=elev, azim=azim)

    return fig, ax


def plot_vault_colored(xyz, mesh, title="Vault", cmap='viridis', elev=30, azim=-60, figsize=(14, 10)):
    """Plot vault with faces colored by average height.

    Parameters
    ----------
    xyz : numpy.ndarray
        Vertex coordinates (n × 3).
    mesh : compas.datastructures.Mesh
        The mesh providing face connectivity.
    title : str
        Plot title.
    cmap : str
        Matplotlib colormap name.
    elev : float
        Elevation angle for 3D view.
    azim : float
        Azimuth angle for 3D view.
    figsize : tuple
        Figure size.

    Returns
    -------
    tuple
        (fig, ax) matplotlib figure and axes.
    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    face_verts = []
    face_heights = []
    for face in mesh.faces():
        fv = mesh.face_vertices(face)
        polygon = [xyz[v] for v in fv]
        face_verts.append(polygon)
        face_heights.append(np.mean([xyz[v][2] for v in fv]))

    heights = np.array(face_heights)
    norm = plt.Normalize(heights.min(), heights.max())
    colormap = plt.cm.get_cmap(cmap)
    face_colors = [colormap(norm(h)) for h in heights]

    poly = Poly3DCollection(face_verts, alpha=0.85)
    poly.set_facecolors(face_colors)
    poly.set_edgecolor('none')
    ax.add_collection3d(poly)

    ax.set_xlim(xyz[:, 0].min() - 0.5, xyz[:, 0].max() + 0.5)
    ax.set_ylim(xyz[:, 1].min() - 0.5, xyz[:, 1].max() + 0.5)
    ax.set_zlim(-0.5, xyz[:, 2].max() + 1.0)

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.view_init(elev=elev, azim=azim)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=ax, shrink=0.5, label='Height (m)')

    return fig, ax


def plot_bricks(
    assembly: BrickAssembly,
    title: str = "Brick Assembly",
    color_by: str | None = None,
    color: str = "sandybrown",
    cmap: str = "viridis",
    elev: float = 30,
    azim: float = -60,
    figsize: tuple = (14, 10),
    alpha: float = 0.85,
):
    """Plot a brick assembly with all six faces of each brick.

    Parameters
    ----------
    assembly : BrickAssembly
        The brick assembly to render.
    title : str
        Plot title.
    color_by : str or None
        Coloring mode: ``'height'`` colors by brick center Z,
        ``'neighbors'`` colors by neighbor count, or ``None`` for
        uniform *color*.
    color : str
        Uniform face color when *color_by* is None.
    cmap : str
        Matplotlib colormap name (used when *color_by* is set).
    elev : float
        Elevation angle for 3D view.
    azim : float
        Azimuth angle for 3D view.
    figsize : tuple
        Figure size.
    alpha : float
        Face transparency.

    Returns
    -------
    tuple
        (fig, ax) matplotlib figure and axes.
    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    # Collect all face polygons and per-face colors
    all_polys = []
    all_colors = []

    # Compute per-brick scalar values for colormapping
    if color_by == 'height':
        values = assembly.centers[:, 2]
    elif color_by == 'neighbors':
        values = np.array([len(nb) for nb in assembly.neighbors], dtype=float)
    else:
        values = None

    if values is not None:
        norm = plt.Normalize(values.min(), values.max())
        colormap = plt.cm.get_cmap(cmap)

    for i in range(len(assembly)):
        faces = brick_faces(assembly.corners[i])
        if values is not None:
            c = colormap(norm(values[i]))
        else:
            c = color
        for f in faces:
            all_polys.append(f)
            all_colors.append(c)

    poly = Poly3DCollection(all_polys, alpha=alpha)
    poly.set_facecolors(all_colors)
    poly.set_edgecolor('dimgray')
    poly.set_linewidth(0.3)
    ax.add_collection3d(poly)

    # Axis limits from brick corners
    all_pts = assembly.corners.reshape(-1, 3)
    pad = 0.5
    ax.set_xlim(all_pts[:, 0].min() - pad, all_pts[:, 0].max() + pad)
    ax.set_ylim(all_pts[:, 1].min() - pad, all_pts[:, 1].max() + pad)
    ax.set_zlim(-pad, all_pts[:, 2].max() + 1.0)

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.view_init(elev=elev, azim=azim)

    if values is not None:
        label = 'Height (m)' if color_by == 'height' else 'Neighbor count'
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        plt.colorbar(sm, ax=ax, shrink=0.5, label=label)

    return fig, ax
