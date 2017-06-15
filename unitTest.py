import unittest
import sys

def getAnswer(filePath):
	with open(filePath,'r') as fr:
		answer=[]
		for line in fr:
			line=line[:-1]
		line=line[1:-1]
		if line.strip() != "": 
                line = line.strip().replace(' ','')
                data = map(int, line.split(','))
                #print(data)
                answers.append(data)
    answers = sorted(answers, key=lambda a: (len(a), a))
    return answers

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("start! ")
    def tearDown(self):
        print("end!  ")
    def test_add(self):
        path = sys.path[0]
        for i in range(0, 16):
            hshresult= getAnswer(path + '/hsh_result/answer'+str(i)+'.txt')
            myresult= getAnswer(path+'/myresult/result_case'+str(i)+'.txt')
            self.assertEqual(myresult, hshresult)

if __name__ == "__main__":
    unittest.main()
