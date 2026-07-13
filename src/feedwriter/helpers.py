def _escape(text: str) -> str:
    map = str.maketrans(
        {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            "'": "&apos;",
            '"': "&quot;",
            "©": "&#xA9;",
            "℗": "&#x2117;",
            "™": "&#x2122;",
        }
    )
    return text.translate(map)
