import pickle

class TreeNode():
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            level += 1 
            p = p.parent
        return level
    
    def print_tree(self):
        space = '\t' * self.get_level() * 3
        prefix = space + "|_" if self.parent else ""
        print(prefix+self.data)
        if self.children :
            for child in self.children :
                child.print_tree()
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def save_tree(root, filename):
        with open(filename, 'wb') as file:
            pickle.dump(root, file)

def load_and_print_tree(filename):
        with open(filename, 'rb') as file:
            loaded_root = pickle.load(file)
        loaded_root.print_tree()

root = TreeNode("Rekomendasi Wisata") 

w1 = TreeNode("pantai kenjeran lama")
w2 = TreeNode("pantai trianggulasi")
w3 = TreeNode("kawah ijen")
w4 = TreeNode("hawai waterpark") 


kota1 = TreeNode("Surabaya")
harga1 = TreeNode("15")
rate1 = TreeNode("4.3")
durasi1 = TreeNode("11")
gambar1 = TreeNode("WR1.png")

kota2 = TreeNode("Banyuwangi")
harga2 = TreeNode("20")
rate2 = TreeNode("4.6")
durasi2 = TreeNode("14")
gambar2 = TreeNode("WR2.png")

kota3 = TreeNode("Banyuwangi")
harga3 = TreeNode("5")
rate3 = TreeNode("5.0")
durasi3 = TreeNode("22")
gambar3 = TreeNode("WR3.png")

kota4 = TreeNode("Malang")
harga4 = TreeNode("85")
rate4 = TreeNode("4.5")
durasi4 = TreeNode("8")
gambar4 = TreeNode("WR4.png")

w1.add_child(kota1)
w1.add_child(harga1)
w1.add_child(rate1)
w1.add_child(durasi1)
w1.add_child(gambar1)

w2.add_child(kota2)
w2.add_child(harga2)
w2.add_child(rate2)
w2.add_child(durasi2)
w2.add_child(gambar2)

w3.add_child(kota3)
w3.add_child(harga3)
w3.add_child(rate3)
w3.add_child(durasi3)
w3.add_child(gambar3)

w4.add_child(kota4)
w4.add_child(harga4)
w4.add_child(rate4)
w4.add_child(durasi4)
w4.add_child(gambar4)

root.add_child(w1) 
root.add_child(w2) 
root.add_child(w3) 
root.add_child(w4) 

save_tree(root, 'tree.pickle')

# Load and print the tree structure from the saved file
load_and_print_tree('tree.pickle')