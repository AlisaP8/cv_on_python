key_dict = ['cat', 'dog', 'pig', 'horse']
val_dict = ['white', 'black', 'pink']
# val_dict = ['white', 'black', 'pink', 'orange', 'blue']
new_dict = {}


def test():
    if len(val_dict) < len(key_dict):
        val_dict.append(None)
        print(val_dict)
    else:
        new_dict = {key: val for (key, val) in zip(key_dict, val_dict)}
        return new_dict


test()
print(test())
