from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

print(MessageBoxA)

### Create a simple message box with "Hello, World!" text
lpTest = LPCSTR(b"Hello, World!")
lpCaption = LPCSTR(b"Hello")
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001

#MessageBoxA(None, lpTest, lpCaption, MB_OK)

### Get the current user's name using GetUserNameA
GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

buffer_size = DWORD(2) # If DWORDS(8) are used, won't throw an error
buffer = create_string_buffer(buffer_size.value)

GetUserNameA(buffer, byref(buffer_size))
print(buffer.value)

### Check for the buffer size
error = GetLastError()

if error:
    print(error)
    print(WinError(error))


class RECT(Structure):
    _fields_ = [("left", c_long),
                ("top", c_long),
                ("right", c_long),
                ("bottom", c_long)]
rect = RECT()

print(rect.left, rect.top, rect.right, rect.bottom)
rect.left = 10
print(rect.left)

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE, POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left, rect.top, rect.right, rect.bottom)