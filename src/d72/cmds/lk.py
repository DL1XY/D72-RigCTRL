from d72.cmds.attributes import Status, KeyLock

class LK:
    cmd="LK"
    description = "Kez lock"
    # desc, return, format, example response
    getExample= ["Get key lock", "Returns: key lock", "LK", "LK 0,2"]
    # desc, format, example response
    setExample= ["Set key lock", "LK x,y", "LK 0,2"]
    
    status = Status.OFF
    lock = KeyLock.KEY_LOCK

