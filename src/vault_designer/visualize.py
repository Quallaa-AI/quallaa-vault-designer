"""Rendering helpers for vault visualization."""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


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
