# # a = float(0.09867)
# a = 0.09504091639351031
# print(round(a,2))
# print(format(a,'.2f'))
#

# def move(n, a, b, c):
#     if n == 1:
#         print(n,'--->',a, '-->', c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(3, 'A', 'B', 'C')


bar = [
  {
      "type": "分区1",
      "sum": 43.9,
      "date": "2019-01"
  },
  {
      "type": "分区2",
      "sum": 80.3,
      "date": "2019-01"
  },

  {
      "type": "分区1",
      "sum": 54.9,
      "date": "2019-02"
  },
  {
      "type": "分区2",
      "sum": 51.2,
      "date": "2019-02"
  },

  {
      "type": "分区1",
      "sum": 80.9,
      "date": "2019-03"
  },
  {
      "type": "分区2",
      "sum": 74.3,
      "date": "2019-03"
  }
]
newbar = []
temp = []
for i in bar:
    if i['type'] not in temp:
        temp.append(i['type'])
        newbar.append({
            'type':i['type'],
            i['date']:i['sum']
        })
    else:
        index = temp.index(i['type'])
        newbar[index][i['date']] = i['sum']
print(newbar)
