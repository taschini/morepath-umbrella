def top_level_packages(setup):
    """Extract the top-level packages defined in a setup file."""
    packages = sorted(set(setup['packages']) - set(setup.get('namespace_packages', [])))
    i = 0
    while i < len(packages):
        q = packages[i] + '.'
        i += 1
        packages = packages[:i] + [p for p in packages[i:] if not p.startswith(q)]
    return sorted(packages)
