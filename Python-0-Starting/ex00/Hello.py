ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

#your code here
# # # BUILT IN DATA TYPES TO STORE COLLECTIONS OF DATA # # #
  # - Used to store multiple items in a single variable
    # # # ---LIST--- # # # 
        # - Lists are created using square brackets
        # - List items are ordered, changeable and allow duplicates
        # - List item are indexed: [0], [1], etc
    # # # ---TUPLES--- # # #
        # - Tuples are created using round brackets
        # - Tuple items are ordered and unchangeable and allow duplicates
        # - Tuple items are indexed: [0], [1], etc
    # # # ---SETS--- # # #
        # - Sets are unordered, unchangeable and unindexed
        # - You can remove items and add new items, no duplicates
        # - You cannot be suere in which order the items will appear
    # # # ---DICTIONARIES--- # # #
        # - Dictionaries are created using curly brackets
        # - Store data in KEY : VALUE pairs
        # - Ordered, changeable, no duplicates

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Austria!")
ft_set.remove("tutu!")
ft_set.add("Vienna!")
ft_dict.update({"Hello":"42Vienna!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


# resource:
# - https://www.w3schools.com/python/python_datatypes.asp
# - https://docs.python.org/3/tutorial/datastructures.html