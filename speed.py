def speedtest():
    import speedtest
    from pyfiglet import Figlet
    from colorama import Fore, init

    init()

    yellow = Fore.LIGHTYELLOW_EX
    reset = Fore.RESET

    f = Figlet(font='slant')
    print(yellow + f.renderText('SPEEDTEST') + reset)

    servers = []

    threads = None

    s = speedtest.Speedtest()

    print("[*] Searching server...")

    print("")

    s.get_servers(servers)
    s.get_best_server()

    print(yellow + "[*] Calculating download speed..." + reset)
    print("[*] " + "{:.2f}".format(s.download(threads=threads) / 1000000) + " MBit/s")

    print("")

    print(yellow + "[*] Calculating upload speed..." + reset)
    print("[*] " + "{:.2f}".format(s.upload(threads=threads) / 1000000) + " MBit/s")

    s.results.share()

    print("")

try:

    speedtest()

except ModuleNotFoundError:
    
    import os

    os.system("pip install colorama")
    os.system("pip install pyfiglet")
    os.system("pip install speedtest-cli")

    print()

    speedtest()

