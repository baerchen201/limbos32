from tkinter import messagebox


# I added this to use the raw _show function in tkinter.messagebox (it is not normally accessible)


def show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and "icon" not in options:
        options["icon"] = _icon
    if _type and "type" not in options:
        options["type"] = _type
    if title:
        options["title"] = title
    if message:
        options["message"] = message
    res = messagebox.Message(**options).show()
    if isinstance(res, bool):
        if res:
            return messagebox.YES
        return messagebox.NO
    return str(res)
