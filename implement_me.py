# Implementation of B+-tree functionality.

from index import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

    # Returns a B+-tree obtained by inserting a key into a pre-existing
    # B+-tree index if the key is not already there. If it already exists,
    # the return value is equivalent to the original, input tree.
    #
    # Complexity: Guaranteed to be asymptotically linear in the height of the tree
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys that already exist in the index.
    @staticmethod


    def InsertIntoIndex( index, key ):
        root = index.root
        root_keys = root.keys.keys
        root_pointers = root.pointers.pointers

        path_nodes = [root]
        fan_out_num = [0]
        

        key_set = []
        key_set = find_all_keys(root, key_set)
        
        
        if root.keys == KeySet():
            root.keys = KeySet([key, None])
            index.root = root
            return index
        elif key in key_set:
            return index
        elif root_keys[1] == None and root_keys[0] > key and type(root_pointers[0]) != Node:
            root_keys[1] = root_keys[0]
            root_keys[0] = key
            return index
        elif root_keys[1] == None and root_keys[0] < key and type(root_pointers[0]) != Node:
            root_keys[1] = key
            return index
    
        
        
        if None not in root_keys and type(root_pointers[0]) != Node:
            root_keys.append(key)
            root_keys.sort()
            root = split_nodes(root, root_keys, path_nodes, fan_out_num) 
            
            return Index(root)
        

    
        while type(root.pointers.pointers[0]) == Node:
            if key < root.keys.keys[0]:
                root = root.pointers.pointers[0]
                path_nodes.append(root)
                fan_out_num.append(0)
            elif root.keys.keys[1] != None:
                if root.keys.keys[0] < key < root.keys.keys[1]:
                    root = root.pointers.pointers[1]
                    path_nodes.append(root)
                    fan_out_num.append(1)
                elif root.keys.keys[1] < key:
                    root = root.pointers.pointers[2]
                    path_nodes.append(root)
                    fan_out_num.append(2)
            else:
                root = root.pointers.pointers[1]
                path_nodes.append(root)
                fan_out_num.append(1)
 
    
        root_keys = root.keys.keys
        root_keys.append(key)
        root_keys.sort()
   
        root = split_nodes(root, root_keys, path_nodes, fan_out_num)
 
        return Index(root)

            
    

        


    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex( index, key ):
        root = index.root
        key_set = []
        key_set = find_all_keys(root, key_set)

        if key in key_set:
            return True

        return False

    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex( index, lower_bound, upper_bound ):
        index_range = []
        root = index.root
        key_set = []
        key_set = find_all_keys(root, key_set)
        for key in key_set:
            if lower_bound <= key < upper_bound:
                index_range.append(key)

        return index_range

def split_nodes(root, keys, path_nodes, fan_out_num):

    num_nodes = len(path_nodes)

    leaf1 = Node()
    leaf1.keys.keys = [keys[1], keys[2]]

    leaf0 = Node()
    leaf0.keys.keys[0] = keys[0]
    leaf0.pointers.pointers[2] = leaf1


    if len(path_nodes) < 2:
        newroot = Node()
        newroot.keys.keys = [keys[1], None]
        newroot.pointers.pointers = [leaf0, leaf1, None]
        return newroot
    else:
        parent = path_nodes[num_nodes - 2]
        fan_num = fan_out_num[num_nodes - 1]

    if parent.keys.keys[1] == None and fan_num != 2 :
        parent.keys.keys.remove(None)
        parent.keys.keys.append(keys[1])
        parent.keys.keys.sort()

        if fan_num == 0:
            parent.pointers.pointers[2] = parent.pointers.pointers[1]
            leaf1.pointers.pointers[2] = parent.pointers.pointers[2]
        else:
            leaf = parent.pointers.pointers[0]
            leaf.pointers.pointers[2] = leaf0
            
        parent.pointers.pointers[fan_num+1] = leaf1
        parent.pointers.pointers[fan_num] = leaf0
        return parent

    elif parent.keys.keys[1] != None :
        parent_pointers = parent.pointers.pointers

        if fan_num > 0:
            node = parent_pointers[fan_num - 1]
            node.pointers.pointers[2] = None

        parent_keys = parent.keys.keys
        parent_keys.append(keys[1])
        parent_keys.sort()

        del path_nodes[num_nodes-2:num_nodes]
        og_path_nodes = []
        for node in path_nodes:
            og_path_nodes.append(node)
        
       

        parent_nodes = []
        newroot, parent_nodes = root_split( parent_keys , path_nodes, parent_nodes)
 
        max_p = 2

        for j in range(len(parent_nodes)):
            parents = parent_nodes[j]

            c = 0
            p = 0
            parent_p = 0 
            d = depth_tree(parent)
            
            for i in range(4):

                new_parent = parents[c]

                if i < fan_num:
                    leaf = parent.pointers.pointers[i]
                    parent_p = parent_p + 1
                elif i == fan_num:
                    leaf = leaf0
                    parent_p = parent_p + 1
                elif i == fan_num + 1:
                    leaf = leaf1
                elif i > fan_num + 1:
                    leaf = parent.pointers.pointers[parent_p]
                    parent_p  = parent_p + 1

                new_parent.pointers.pointers[p] = leaf

                if i > 0 and j < 1:
                    oldleaf.pointers.pointers[2] = new_parent.pointers.pointers[p]
                elif i > 0 and j >= 1:
                    node = new_parent.pointers.pointers[p]

                    for dd in range(d - 2):
                        node = node.pointers.pointers[0]
                    oldleaf.pointers.pointers[2] = node.pointers.pointers[0]

                if j < 1:
                    oldleaf = new_parent.pointers.pointers[p]
                elif j >= 1:

                    node = new_parent.pointers.pointers[p]
                    for dd in range(d - 2):
                        node = node.pointers.pointers[1]
                    oldleaf = node.pointers.pointers[1]

         
                p = p + 1
                
                if num_fan_out(parents[c]) >= max_p:
                    parents[c] = new_parent
                    c = c + 1 
                    p = 0

                if parent_p >= 3 and len(parent_nodes) > 1:
                    fan_l = len(fan_out_num)
                    fan_out_num.pop(fan_l - 1)
                    fan_num = fan_out_num[fan_l - 2]
                    path_l = len(og_path_nodes)
                    if path_l > 0:
                        parent = og_path_nodes[path_l - 1]
                        og_path_nodes.remove(parent)
                    leaf0 = parents[0]
                    leaf1 = parents[1]


        newroot.pointers.pointers = parents
            
        return newroot

        

    return root

def find_all_keys(root, key_set):

    depth = depth_tree(root)
    
    for d in range(depth):
        root = root.pointers.pointers[0]

    while type(root.pointers.pointers[2]) == Node:
        
        for key in root.keys.keys:
            if key != None and key not in key_set:
                key_set.append(key)

        root = root.pointers.pointers[2]
    
    for key in root.keys.keys:
        if key != None and key not in key_set:
            key_set.append(key)
    
    key_set.sort()

    return key_set



def depth_tree(node):

    if type(node.pointers.pointers[0]) != Node:
        return 0
    
    return 1 + depth_tree(node.pointers.pointers[0])

def root_split( keys, path_nodes, parent_nodes):
    path_length = len(path_nodes)

    parent0 = Node()
    parent0.keys.keys = [keys[0], None]
    parent1 = Node()
    parent1.keys.keys = [keys[2], None]
    

    if path_length == 0:
        newroot = Node()
        newroot.keys.keys = [keys[1], None]
        newroot.pointers.pointers = [parent0, parent1, None]
        parent_nodes.append([parent0, parent1, None])

        return newroot, parent_nodes

    elif path_length > 0 :
        newroot = path_nodes[path_length - 1]
        newroot_keys = newroot.keys.keys
        newroot_pointers = newroot.pointers.pointers
        
        if newroot_keys[1] == None:
            if keys[1] < newroot_keys[0]:
                newroot_keys[1] = newroot_keys[0]
                newroot_keys[0] = keys[1]
                newroot_pointers[2] = newroot_pointers[1]
                newroot_pointers[0] = parent0
                newroot_pointers[1] = parent1
                parent_nodes.append([parent0, parent1, newroot_pointers[2]])
                return newroot, parent_nodes
            else:
                newroot_keys[1] = keys[1]
                newroot_pointers[1] = parent0
                newroot_pointers[2] = parent1
                parent_nodes.append([newroot_pointers[0], parent0, parent1])
                return newroot, parent_nodes
        else:
            newroot_keys.append(keys[1])
            newroot_keys.sort()
    
            path_nodes.remove(newroot)
            path_length = len(path_nodes) 
            parent_nodes.append([parent0, parent1]) 
            if path_length == 0:
                return root_split(newroot_keys, path_nodes, parent_nodes)

            else:
                root = path_nodes[path_length - 1]
                newkeys = root.keys.keys
                newkeys.append(keys[1])
                newkeys.sort()
                return  root_split(newkeys, path_nodes, parent_nodes)
                



def num_fan_out(node):
    count = 0

    for pointer in node.pointers.pointers:
        if type(pointer) == Node:
            count = count + 1
    return count

def leaf_num(root):
    count = 0
    depth = depth_tree(root)
    
    for d in range(depth):
        root = root.pointers.pointers[0]
    
    while type(root.pointers.pointers[2]) == Node:
        count = count + 1
        root = root.pointers.pointers[2]
    return count + 1
