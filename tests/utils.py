from pathlib import PurePosixPath
import random
import string


def random_posix_path(depth=3, name_length=8, include_file=False):
    """
    Generate a random POSIX-style path.

    Args:
        depth (int): Number of path components (directories).
        name_length (int): Length of each directory/file name.
        include_file (bool): Whether to include a file name at the end.

    Returns:
        str: A random POSIX-style path.
    """
    def random_name():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))

    parts = [random_name() for _ in range(depth)]

    if include_file:
        filename = random_name() + random.choice([".txt", ".log", ".csv", ".json", ".py"])
        parts.append(filename)

        return str(PurePosixPath("/".join(parts)))
    else:
        return str(PurePosixPath("/".join(parts)))+"/"