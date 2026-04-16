import platform

if platform.system() == "Windows":
    import win32file
    def openpipe(pipe_path):
        pipe = win32file.CreateFile(
            pipe_path,
            win32file.GENERIC_READ,
            0, None,
            win32file.OPEN_EXISTING,
            0, None
        )
        return pipe
    def readpipe(pipe,size):
        succes, bytes = win32file.ReadFile(pipe,size)
        if succes == 0:
            return bytes
        else:
            print("pipe error")



if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"

    def openpipe(pipe_path):
        pipe = open(pipe_path, "rb")
        return pipe

    def readpipe(pipe,size):
        bytes = pipe.read(60)
        return bytes
