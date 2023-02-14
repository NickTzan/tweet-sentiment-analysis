import sys
import pickle
import joblib
import re # Regex Library 

def load_model():
	with open(r"./models/vectorizer_tfidf-os.pickle", "rb") as input_file:
		vectorizer = pickle.load(input_file)

	loaded_model = joblib.load('./models/SA_NLP_Model-os.joblib')
	
	return vectorizer, loaded_model

def replace_emoticons(txt):

    # Replace emoticons with a word describing the emoticon
    emoticons_happy = set([':-)', ':)', ':]', ':3', '=]', '=)'])

    emoticons_sad = set([':(',"=[" ,":'(", ':@', ':-(', ':[', ':-[', '>.<', ':-c',':c'])
    
    emoticons_surprised = set([':O', ':o', ':-o', ':-O'])

    words = txt.split()
    new_w = []
    for w in words:
        if w in emoticons_happy:
            new_w.append("happy")
        elif w in emoticons_sad:
            new_w.append("sad") 
        elif w in emoticons_surprised:
            new_w.append("surprised") 
        else:
            new_w.append(w)
    txt = " ".join(new_w)
    return txt


def data_cleaning(txt):
    txt = replace_emoticons(txt)     # replace emoticons with a word describing the emoticon
    txt = re.sub('@[^\\s]+', '', txt) # remove usernames
    txt = re.sub('RT[\\s]+', '', txt) # remove retweet 'RT'
    txt = re.sub('#', '', txt)       # remove '#'
    txt = re.sub('((www\\.[^\\s]+)|(https?://[^\\s]+))', '', txt)  # remove URLs inside the text
    
    return txt



def main():
	

	return

def main():
	args = sys.argv[1:]
	
	with open('./tweet.txt') as f:
 		lines = f.readlines()
	print('The input text is: ', lines[0])

	lines[0] = data_cleaning(lines[0])
		
	vec, model = load_model()
	
	test_vec = vec.transform(lines)
	
	print('The predicted sentiment is:', model.predict(test_vec)[0])
	return
        

if __name__ == "__main__":
 	main()
 	
    
    
