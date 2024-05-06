#####################################################################
# Procesamiento Asíncrono                                           #
#####################################################################

import asyncio

async def main():
    print("async main -> Hola ......")
    await asyncio.gather(func1(), func2(), func3())
    print("async main -> ...... Adios !!!")

async def func1():
    print("async func1 -> Hola 1 ......")
    await asyncio.sleep(5)
    print("async func1 -> ...... Adios 1 !!!")

async def func2():
    print("async func2 -> Hola 2 ......")
    for i in range(11):
        print (f"async func2 - > {i}")
        await asyncio.sleep(0.6)
    print("async func2 -> ...... Adios 2 !!!")


async def func3():
    print("async func3 -> Hola 3 ......")
    for i in range(11):
        print(f"async func3 - > {i}")
        #await asyncio.sleep(0.2)
    print("async func3 -> ...... Adios 3 !!!")

# Hilo principal siempre es Síncrono
print("Inicio Sync")
asyncio.run(main())
print("Fin Sync")
print("")


quit()

#####################################################################
# Procesamiento Síncrono                                            #
#####################################################################

def main():
    print("main -> Hola ......")
    print("main -> ...... Adios !!!")


print("Inicio Sync")
main()
print("Fin Sync")
print("")
