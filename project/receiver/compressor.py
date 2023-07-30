import tarfile    ##from tqdm import tqdm
def compress(members):    # open file for gzip compressed writing
    tar = tarfile.open("compressed.tar.gz", mode="w:gz")
    for member in members:   
        tar.add(member)
    tar.close()
    return "compressed.tar.gz"
def decompress( path, members=None):
    tar = tarfile.open("compressed.tar.gz", mode="r:gz")
    if members is None:
        members = tar.getmembers()
    for member in members:
        tar.extract(member, path=path)

    tar.close()
