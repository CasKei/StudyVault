---
aliases: busy waiting
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section problem]]
[[Critical section solutions]]
[[Software spinlocks and mutex locks]]

## Spinlock
Provides [[Mutex]].
> It is simply a variable that can be initialised, e.g. `pthread_spinlock_t` implemented in C library and then obtained or released using 2 **standard** methods like `acquire()` and `release()`.

An attempt to `acquire()` the lock causes a process or thread trying to acquire it to wait in a loop ('spin') while repeatedly checking whether the lock is available.
> Also called **busy waiting**, hence wasting the caller's quantum until the caller acquires the lock and can progress.

E.g. of `acquire` in C lib
```c
acquire() {
   /* this test is performed using atomic test_and_set and busy wait for the process' CS, hardware supported */ 
     while (!available); 
     available = false;
}

release(){
	available = true;
}
```

You can create spinlock using C POSIX lib: `pthread_spin_lock()`
```c
static pthread_spinlock_t spinlock;
pthread_spin_init(&spinlock,0);
pthread_spin_lock(&spinlock); // no context switch, no system call, busy waits if not available
// CRITICAL SECTION ...
pthread_spin_unlock(&spinlock);
// REMAINDER SECTION ...
```

## Busy waiting
Busy waiting **wastes** CPU cycles\
Some other process might use CPU more productively, and it affects efficiency tremendously when a CPU is shared among many processes. The spinning caller will use 100% CPU just waiting, repeatedly checking if a spinlock is available.

> Does it make much sense to use spinlocks in single-core environment? The spinlock polling is blocking the only available CPU core, and as a result no other process can run. Since no other process can run, the lock won’t be unlocked either.

Nevertheless, spinlocks are mostly useful in places where anticipated waiting time is **shorter** than a quantum and that [[Multi-core architecture|multicore]] is present. **No [[Context switch]] is required** when a process must wait on a lock, the calling process simply utilise the special assembly instruction.

