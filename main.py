import mylib
import dbdb

m_list= mylib.melon()
print(m_list)

#메론에서 가져온 데이터  리스트들을 DB에 넣기 위해
dbdb.save_date(m_list)