def inclusive_range(min: int, max: int) -> range:
    off_by_one = 1
    return range(
        min,
        max + off_by_one,
    )
