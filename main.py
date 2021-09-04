import argparse
from pySmartDL import SmartDL
parser = argparse.ArgumentParser()
parser.add_argument("-d","--download",help="Download URL",required=True)
parser.add_argument("-o","--output",help="Output Location, DO NOT specify name of file.",required=False)
parser.add_argument("-t","--threads",help="Specify number of threads, Default to 5",required=False,default=5)
args = parser.parse_args()
def file_download():
    url = args.download
    name = args.output
    threads = int(args.threads)

    obj = SmartDL(url, name,threads=threads)
    obj.start()

if __name__ == '__main__':
    file_download()
