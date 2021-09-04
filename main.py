import argparse
import requests
import threading
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("-d","--download",help="Download URL",required=True)
parser.add_argument("-o","--output",help="Output Location",required=False)
parser.add_argument("-t","--threads",help="Specify number of threads, Default to 5",required=False,default=5)
args = parser.parse_args()

url = args.download
name = args.output
threads = int(args.threads)
def Handler(start, end, url, filename):
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)
def download_file(obj):
    r = requests.head(url)
    file_size = 0
    if name:
        file_name = name
    else:
        file_name = url.split('/')[-1]
    try:
        file_size = int(r.headers['content-length'])
    except:
        print ("Invalid URL")

    part = int(file_size) / int(threads)
    fp = open(file_name, "wb")
    bort = bytes('\0' * file_size,'utf8')
    pickle.dump(bort, fp)

   # fp.write(bytes('\0') * file_size)
   # fp.close()
    for i in range(threads):
        start = int(part * i)
        end = int(start + part)
        t = threading.Thread(target=Handler,kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name})
        t.setDaemon(True)
        t.start()
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s downloaded' % file_name)

if __name__ == '__main__':
    download_file(obj={})