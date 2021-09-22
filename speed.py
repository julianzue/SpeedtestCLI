import speedtest

print("SPEEDTEST")
print("=========")

servers = []

threads = None

s = speedtest.Speedtest()

print("[i] Searching server...")

print("")

s.get_servers(servers)
s.get_best_server()

print("[i] Download")
print("[i] " + "{:.2f}".format(s.download(threads=threads) / 1000000) + " MBit/s")

print("")

print("[i] Upload")
print("[i] " + "{:.2f}".format(s.upload(threads=threads) / 1000000) + " MBit/s")

s.results.share()

results_dict = s.results.dict()



