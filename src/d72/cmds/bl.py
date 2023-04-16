class BL:
    cmd="BL"
    description = "Backlight"
    # desc, return, format, example response
    getExample= ["Get the backlight status", "Returns: backlight status (0:OFF or 1-8)", "BL", "BL 2"]
    # desc, format, example
    setExample= ["Set the backlight status", "BL x", "BL 2"]

    backlightStatus = "0"
