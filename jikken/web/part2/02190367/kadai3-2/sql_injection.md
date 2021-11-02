# SQLインジェクション

## 攻撃方法
- SQLの構文の穴をついたクエリを書いて、認証回避やデータの改ざん・破壊を行う

## weak_sqlite.rbへの攻撃例

```
#coding: utf-8
require 'sqlite3'
db = SQLite3::Database.new("sandbox.db")
id, new_name = gets.chomp.split(",")
str = "UPDATE students SET name = \"#{new_name}\" WHERE student_id = #{id}"
db.execute_batch(str)
db.close
```

new_nameを
new_name="a\" OR 1=1; DROP TABLE students;"
idは適当な値
とすれば,str内でnew_nameが
"UPDATE students SET name = \"a\" OR 1=1; DROP TABLE students;\" WHERE student_id = 適当な値"
と展開され、DBがDROPされる

## 対策
- エスケープ処理を行う
- 入力できる文字を制限する( ', ", '/', '\', ';', '\n')など
- バインド機構（入力値を加工したものをSQL文で使う）
