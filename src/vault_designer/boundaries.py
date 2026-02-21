"""Floor plan boundary definitions for vault form-finding."""

from compas.datastructures import Mesh


def rectangular(dx: float, dy: float, nx: int, ny: int) -> Mesh:
    """Create a rectangular floor plan mesh.

    Parameters
    ----------
    dx : float
        Width in X direction (meters).
    dy : float
        Width in Y direction (meters).
    nx : int
        Number of faces in X direction.
    ny : int
        Number of faces in Y direction.

    Returns
    -------
    Mesh
        A COMPAS mesh with boundary vertices identified.
    """
    return Mesh.from_meshgrid(dx=dx, nx=nx, dy=dy, ny=ny)
