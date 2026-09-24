def greet(name):
    """Return a greeting for name, trimming surrounding whitespace.

    An empty (or whitespace-only) name greets the world.
    """
    trimmed = name.strip()
    if not trimmed:
        trimmed = "world"
    return "Hello, " + trimmed
