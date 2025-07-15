from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID # pointer to a void object

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40 # Enable execution and read/write access to the memory

ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

error = GetLastError()

if error:
    print(error)
    print(WinError(error))

print("VirtualAlloc: ", hex(ptr))

nt = windll.ntdll
NTSTATUS = wintypes. DWORD


### Allocate memory using NtAllocateVirtualMemory
NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
NtAllocateVirtualMemory.restype = NTSTATUS

handle = 0xFFFFFFFFFFFFFFFF  # Use 0xFFFFFFFFFFFFFFFF for the current process
base_address = wintypes.LPVOID(0)
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 12) # Allocate 12 KB

ptr2 = NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr != 0:
    print("error!")
    print(ptr2)

print("NtAllocateVirtualMemory: ", hex(base_address.value))
