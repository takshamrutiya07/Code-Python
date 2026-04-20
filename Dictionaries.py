dic = {
    191:"Taksh",
    999:"jon snow",
    898:"Black"
}
print(dic[191])

info = {'name':'Taksh','age':19,'eligible':True}
print(info)
print(info['name'])#if name didn't exists in the dictionary then it gives error
print(info.get('name'))#if name didn't exists in the dictionary then it NULL value

print(info.keys())
print(info.values())
for key in info.keys():
    print(info[key])