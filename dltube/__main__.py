from pytube import YouTube
import sys

def main():
	print('Starting Downloads')
	try:
		t = sys.argv[1]
		print('Target URL:',t)
		YouTube(t).streams.first().download()
		print('Success')
	except Exception as e:
		print(f'Fail: {e}')
	print('Download Finished')

if __name__ == "__main__":
    main()
