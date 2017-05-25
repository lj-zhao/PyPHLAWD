import tree_reader
import sys
import os

"""
right now this just chooses the longest

BEWARE, this writes over the file
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" table treefile"
        sys.exit(0)
    tab = open(sys.argv[1],"r")
    idn = {}
    for i in tab:
        spls = i.strip().split("\t")
        idn[spls[4].replace(" ","_")] = spls[1]
    tab.close()
    tf = tree_reader.read_tree_file_iter(sys.argv[2]).next()
    for i in tf.iternodes():
        if i.label in idn:
            i.label = idn[i.label]
    print tf.get_newick_repr(True)+";"
