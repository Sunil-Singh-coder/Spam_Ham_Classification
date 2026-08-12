# (Label, Message)
dataset = [
    ("Ham", "Hey, are we still meeting for lunch today at the cafe?"),
    ("Spam", "Congratulations! You have won a £1000 cash prize. Call now to claim."),
    ("Ham", "Can you send me the presentation before today's meeting?"),
    ("Spam", "You have been selected for a free iPhone. Click the link to claim now."),
    ("Ham", "I will reach the office in about fifteen minutes."),
    ("Spam", "Limited-time offer! Buy one phone and get another absolutely free."),
    ("Ham", "Please remind me to submit the assignment before tonight."),
    ("Spam", "URGENT! Your bank account is blocked. Verify your details immediately."),
    ("Ham", "Let's play cricket this Sunday if the weather is good."),
    ("Spam", "Earn money from home without any investment. Join today!"),
    ("Ham", "Thanks for helping me complete the project yesterday."),
    ("Spam", "You have received an exclusive credit card offer. Reply YES now."),
    ("Ham", "Could you please share the latest source code with me?"),
    ("Spam", "Win a luxury holiday package by texting WIN to 80082."),
    ("Ham", "The meeting has been moved to 3 PM today."),
    ("Spam", "Claim your guaranteed reward before midnight. Offer expires today."),
    ("Ham", "Happy Birthday! Have a wonderful year ahead."),
    ("Spam", "Your PayPal account needs verification. Click here immediately."),
    ("Ham", "I have uploaded the notes to our shared drive."),
    ("Spam", "Congratulations! You are our lucky customer. Get your reward now."),
    ("Ham", "Can we discuss the final project after class?"),
    ("Spam", "Double your income with our secret business plan. Register today."),
    ("Ham", "Please bring your laptop charger to tomorrow's workshop."),
    ("Spam", "Free ringtone and bonus games waiting for you. Subscribe now."),
    ("Ham", "Mom, I will be late today because of extra office work."),
    ("Spam", "Lowest loan interest rates available today. Apply instantly."),
    ("Ham", "Let's watch a movie this weekend if you're free."),
    ("Spam", "Congratulations! Your mobile number has won a brand-new car."),
    ("Ham", "I have completed the documentation and sent it to the team."),
    ("Spam", "Lose weight quickly with our miracle diet pills. Order today!"),
("Ham", "I have reached the library. Let me know when you arrive."),
("Spam", "Exclusive offer! Get 70% off on all products. Shop now before midnight."),
("Ham", "Don't forget to bring your ID card for tomorrow's interview."),
("Spam", "Your mobile number has been selected to receive a brand-new laptop. Click here now."),
("Ham", "Thanks for helping me fix the coding issue yesterday. I really appreciate it."),
("Spam", "Earn £500 every day from home with our proven online system. Register for free today."),
("Ham", "Let's meet after class and complete the remaining project documentation together."),
("Spam", "URGENT! Your account will be suspended within 24 hours unless you verify your details immediately.")
]
new_dataset = [

    # =========================
    # HAM MESSAGES
    # =========================

    ("Ham", "Hello, where are you? I am waiting for you."),
    ("Ham", "Hey, are you coming to class today?"),
    ("Ham", "Can you call me when you reach home?"),
    ("Ham", "I am waiting for you near the main gate."),
    ("Ham", "Let's have tea after the meeting."),
    ("Ham", "What time will you reach the office?"),
    ("Ham", "Please bring your notebook when you come."),
    ("Ham", "I will call you after finishing my work."),
    ("Ham", "Are you free this evening?"),
    ("Ham", "Let's meet tomorrow morning."),
    ("Ham", "I have reached the railway station."),
    ("Ham", "Please send me the notes when you are free."),
    ("Ham", "Did you complete today's assignment?"),
    ("Ham", "I am going to the market. Do you need anything?"),
    ("Ham", "Mom asked me to come home early today."),
    ("Ham", "Can we discuss the project after lunch?"),
    ("Ham", "I forgot my charger at your place."),
    ("Ham", "Please remind me about the meeting tomorrow."),
    ("Ham", "I will be late because of traffic."),
    ("Ham", "Where should we meet for dinner?"),
    ("Ham", "Thanks for sending the documents."),
    ("Ham", "I am studying for tomorrow's exam."),
    ("Ham", "Can you help me with this coding problem?"),
    ("Ham", "Let's go for a walk in the evening."),
    ("Ham", "I reached the college safely."),
    ("Ham", "Please call John and tell him about the meeting."),
    ("Ham", "I will send the project file tonight."),
    ("Ham", "Are you available for a quick call?"),
    ("Ham", "Don't forget to bring your ID card."),
    ("Ham", "I am having lunch with my friends."),
    ("Ham", "What did the teacher say about the assignment?"),
    ("Ham", "I will meet you outside the library."),
    ("Ham", "Can you share the location with me?"),
    ("Ham", "I am feeling tired, so I will rest for a while."),
    ("Ham", "Let's watch a movie this weekend."),
    ("Ham", "Please check your email when you get time."),
    ("Ham", "I have completed my part of the project."),
    ("Ham", "When are you coming back home?"),
    ("Ham", "I am waiting for the bus."),
    ("Ham", "Can you bring some snacks for everyone?"),
    ("Ham", "Good morning, have a nice day."),
    ("Ham", "Happy birthday! I hope you have a great day."),
    ("Ham", "I will talk to you later."),
    ("Ham", "Please let me know when you are ready."),
    ("Ham", "The class will start at ten o'clock."),
    ("Ham", "I am going to the gym after work."),
    ("Ham", "Can you review my resume today?"),
    ("Ham", "I left my keys on the table."),
    ("Ham", "Let's finish the work before going home."),
    ("Ham", "Thank you for helping me yesterday."),


    # =========================
    # SPAM MESSAGES
    # =========================

    ("Spam", "Congratulations! You have won a cash prize. Claim it now."),
    ("Spam", "URGENT! You have been selected for a special reward."),
    ("Spam", "Win a brand new smartphone by entering our lucky draw today."),
    ("Spam", "You have won a free holiday package. Claim your prize now."),
    ("Spam", "Exclusive offer! Get 90 percent discount today only."),
    ("Spam", "Earn thousands of dollars from home with our secret method."),
    ("Spam", "Your account has been selected for a special bonus."),
    ("Spam", "Click now to claim your free gift."),
    ("Spam", "Congratulations! You are today's lucky winner."),
    ("Spam", "Limited offer! Get your reward before midnight."),
    ("Spam", "You have received a free shopping voucher. Claim now."),
    ("Spam", "Win a luxury car in our special competition."),
    ("Spam", "Your number has won a guaranteed cash reward."),
    ("Spam", "Get rich quickly with this amazing investment opportunity."),
    ("Spam", "Exclusive deal! Buy now and receive a huge bonus."),
    ("Spam", "URGENT! Verify your account immediately to avoid suspension."),
    ("Spam", "Your bank account requires immediate verification. Click here."),
    ("Spam", "Congratulations! You have been chosen for a free gift."),
    ("Spam", "Get a free phone by completing this short survey."),
    ("Spam", "Earn money every day without any investment. Join now."),
    ("Spam", "Special discount available for a limited time only."),
    ("Spam", "You are eligible for a guaranteed loan. Apply today."),
    ("Spam", "Claim your free coupon before the offer expires."),
    ("Spam", "You have won a shopping voucher worth 5000. Reply now."),
    ("Spam", "Exclusive lottery result! You are one of the lucky winners."),
    ("Spam", "Get instant cashback by clicking this link now."),
    ("Spam", "Your mobile number has won a brand new laptop."),
    ("Spam", "Congratulations! Your prize is waiting. Claim immediately."),
    ("Spam", "Double your income with our proven online business system."),
    ("Spam", "Free subscription available for selected customers."),
    ("Spam", "Act now! This special offer expires tonight."),
    ("Spam", "You have been selected for a premium membership for free."),
    ("Spam", "Win exciting prizes by texting WIN to our number."),
    ("Spam", "Get 70 percent off your next purchase. Shop now."),
    ("Spam", "Your account is eligible for a special cash bonus."),
    ("Spam", "Earn money from home with no experience required."),
    ("Spam", "Free gift waiting for you. Click the link to receive it."),
    ("Spam", "You are the lucky winner of today's prize draw."),
    ("Spam", "Apply now for an instant loan with zero paperwork."),
    ("Spam", "Your reward will expire today. Claim it immediately."),
    ("Spam", "Get a free recharge by completing our survey."),
    ("Spam", "Congratulations! You have won an exclusive reward."),
    ("Spam", "Special investment opportunity. Double your money quickly."),
    ("Spam", "Your credit card has been selected for a special offer."),
    ("Spam", "Claim your guaranteed reward before midnight."),
    ("Spam", "Free bonus available now. Register immediately."),
    ("Spam", "You have been selected to receive a luxury gift."),
    ("Spam", "Limited-time deal! Order now and get a free bonus."),
    ("Spam", "Click now to unlock your exclusive reward."),
    ("Spam", "URGENT! Confirm your personal details to receive your prize."),
     ("Ham", "Hello Sunil, can you lend me 50 rupees?"),
    ("Ham", "I need to borrow 100 rupees from you."),
    ("Ham", "Can you please lend me some money?"),
    ("Ham", "Could you send me 50 rupees? I will return it tomorrow."),
    ("Ham", "I am short of cash today, can you help me with 100 rupees?"),
    ("Ham", "Can I borrow 200 rupees from you?"),
    ("Ham", "Please lend me 50 rupees, I will give it back later."),
    ("Ham", "I need some money for lunch today."),
    ("Ham", "Can you transfer 100 rupees to me?"),
    ("Ham", "Could you help me with some cash?"),
    ("Ham", "I forgot my wallet, can you lend me some money?"),
    ("Ham", "Please send me 50 rupees when you get time."),
    ("Ham", "I will return the money tomorrow."),
    ("Ham", "Can you lend me 500 rupees until tomorrow?"),
    ("Ham", "I need 100 rupees for the bus fare."),
     # =========================
    # HAM - MONEY / RUPEES / CASH
    # =========================

    ("Ham", "Can you lend me 50 rupees? I will return it tomorrow."),
    ("Ham", "Please send me 100 rupees for the bus fare."),
    ("Ham", "I need 200 rupees for lunch today."),
    ("Ham", "Can I borrow 500 rupees from you until Friday?"),
    ("Ham", "I will transfer your money back tonight."),
    ("Ham", "Please remind me that I owe you 100 rupees."),
    ("Ham", "I have already sent the money to your account."),
    ("Ham", "Can you pay the bill? I will give you the cash later."),
    ("Ham", "I forgot my wallet, could you lend me some money?"),
    ("Ham", "I need some cash to buy groceries."),
    ("Ham", "Please send me the remaining 50 rupees."),
    ("Ham", "I will return the borrowed money after getting my salary."),
    ("Ham", "Can you help me with 300 rupees today?"),
    ("Ham", "I borrowed some money from Rahul yesterday."),
    ("Ham", "Did you receive the money I transferred this morning?"),

    # =========================
    # HAM - WORDS LIKE FREE / OFFER
    # =========================

    ("Ham", "Are you free this evening?"),
    ("Ham", "Let me know when you are free."),
    ("Ham", "I am free after six o'clock."),
    ("Ham", "Are you free tomorrow morning for a meeting?"),
    ("Ham", "The teacher offered to help us with the project."),
    ("Ham", "My friend gave me a free ticket to the movie."),
    ("Ham", "We can have free time after the class."),
    ("Ham", "I am free right now, you can call me."),
    ("Ham", "He offered me his old laptop for the project."),
    ("Ham", "There is no charge because my friend invited me."),

    # =========================
    # HAM - WORDS LIKE ACCOUNT / BANK
    # =========================

    ("Ham", "I checked my bank account this morning."),
    ("Ham", "Please send your account number so I can transfer the money."),
    ("Ham", "I need to update my bank details for my salary."),
    ("Ham", "Did the bank transfer reach your account?"),
    ("Ham", "My account balance is showing the wrong amount."),
    ("Ham", "I will visit the bank after lunch."),
    ("Ham", "Please check whether the payment reached my account."),
    ("Ham", "I forgot my bank password and need to reset it."),
    ("Ham", "The bank called me about my new debit card."),
    ("Ham", "I deposited some money into my savings account."),

    # =========================
    # HAM - NORMAL CONVERSATION
    # =========================

    ("Ham", "Hello, where are you? I am waiting near the cafe."),
    ("Ham", "Can you call me when you reach home?"),
    ("Ham", "I am waiting for you outside the classroom."),
    ("Ham", "Please bring some tea when you come."),
    ("Ham", "What are you doing right now?"),
    ("Ham", "I will meet you after the lecture."),
    ("Ham", "Are we still going to the cricket match tomorrow?"),
    ("Ham", "Please send me the project file when you finish it."),
    ("Ham", "I am running late because there is a lot of traffic."),
    ("Ham", "Let's have dinner together tonight."),


    # =========================
    # SPAM - MONEY / RUPEES
    # =========================

    ("Spam", "Congratulations! You have won 50,000 rupees. Claim now."),
    ("Spam", "Your 1000 rupees reward is waiting. Claim immediately."),
    ("Spam", "You have received a guaranteed cash prize of 5000 rupees."),
    ("Spam", "Win 10,000 rupees today by entering our lucky draw."),
    ("Spam", "Your cash bonus is ready. Click now to receive it."),
    ("Spam", "Claim your free 2000 rupees reward before midnight."),
    ("Spam", "You are eligible for a 5000 rupees cash reward."),
    ("Spam", "Congratulations! Your prize money is waiting for you."),
    ("Spam", "Get instant cash by registering for our special offer."),
    ("Spam", "You have won a guaranteed money reward. Claim today."),

    # =========================
    # SPAM - FREE / OFFER
    # =========================

    ("Spam", "FREE reward waiting for you. Claim it now."),
    ("Spam", "You have been selected for a FREE gift."),
    ("Spam", "Exclusive FREE offer available for you today."),
    ("Spam", "Get a FREE smartphone by clicking this link."),
    ("Spam", "FREE cash bonus available. Register now."),
    ("Spam", "Special offer! Get 90 percent discount today."),
    ("Spam", "Limited offer! Claim your FREE voucher now."),
    ("Spam", "Congratulations! You qualify for a FREE reward."),
    ("Spam", "FREE lottery entry available for selected customers."),
    ("Spam", "Get your FREE gift before this offer expires."),

    # =========================
    # SPAM - BANK / ACCOUNT
    # =========================

    ("Spam", "URGENT! Your bank account will be blocked. Verify now."),
    ("Spam", "Your account has been selected for a cash reward."),
    ("Spam", "Verify your bank account immediately to receive your money."),
    ("Spam", "Your bank account requires urgent verification."),
    ("Spam", "Click here to confirm your account and claim your reward."),
    ("Spam", "Your account is eligible for an exclusive cash bonus."),
    ("Spam", "URGENT! Your account will be suspended within 24 hours."),
    ("Spam", "Confirm your bank details to receive your prize."),
    ("Spam", "Your account has won a special reward. Claim immediately."),
    ("Spam", "Verify your payment details to unlock your cash prize."),

    # =========================
    # SPAM - NORMAL LOOKING BUT PROMOTIONAL
    # =========================

    ("Spam", "Hello! We have a special reward waiting for you today."),
    ("Spam", "Dear customer, your exclusive prize is ready to claim."),
    ("Spam", "You were selected for a special promotion. Register now."),
    ("Spam", "Your number has been chosen for today's lucky draw."),
    ("Spam", "A special bonus has been added to your account. Claim now."),
    ("Spam", "You can receive a large cash reward by joining today."),
    ("Spam", "Your exclusive offer expires tonight. Act now."),
    ("Spam", "Congratulations, you are one of our selected winners."),
    ("Spam", "Your reward is waiting. Click the link to collect it."),
    ("Spam", "Special customer offer! Claim your bonus before midnight."),
("Spam", "Your 1000 RUPEES is waiting."),
("Spam", "You have won 1000 rupees. Claim now."),
("Spam", "Rs 5000 cash reward is waiting for you."),
("Spam", "Your cash prize is ready. Claim it now."),
("Spam", "1000 rupees reward waiting for you."),
("Spam", "You have received a cash bonus."),
("Spam", "Your prize money is waiting."),
("Spam", "Claim your 2000 rupees reward today."),
("Spam", "Congratulations, your cash reward is ready."),
("Spam", "You are eligible for a 5000 rupees bonus."),
("Spam", "Your reward of 1000 rupees is waiting."),
("Spam", "Get your free cash reward now."),
("Spam", "Rs 1000 bonus waiting. Claim immediately."),
("Spam", "Your lucky reward is ready to collect."),
("Spam", "You won 5000 rupees. Claim your money now.")


]
dataset = dataset + new_dataset
import pandas as pd 
ds=pd.DataFrame(dataset,columns=["labels","message"])
# print(ds)

# First Data Cleaning and prepocessing is very important before going to solve any problem

import joblib
import nltk
import re
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer()
# in this box we process and clean the message by using that we studied till now
corpus=[]
for i in range(len(dataset)):
    words=re.sub('[^a-zA-Z]',' ',dataset[i][1])
    words=words.lower()
    words=words.split()
    words=[wnl.lemmatize(word) for word in words if not word in stopwords.words("english")]
    words=' '.join(words)
    corpus.append(words)

# corpus # output of above code    

# Create a bag of words  ----> Text to vector 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

cv = CountVectorizer(
    max_features=1000,
    ngram_range=(1, 2)
)

x = cv.fit_transform(corpus)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(ds["labels"]) 
spam_detect_models=MultinomialNB()
spam_detect_models.fit(x, y)


joblib.dump(spam_detect_models, "spam_model.pkl")
joblib.dump(cv, "count_vectorizer.pkl")
joblib.dump(le, "label_encoder.pkl")

# User Inputs
msg=input("Enter your message ")
# 0-----> Ham , 1-----> Spam
corpus2=[]
words=re.sub('[^a-zA-Z]',' ',msg)
words=words.lower()
words=words.split()
words=[wnl.lemmatize(word) for word in words if not word in stopwords.words("english")]
words=' '.join(words)
corpus2.append(words)

corpus2 # output of above code  
# msg

# spam
msg_vec=cv.transform(corpus2).toarray()
y_pred2=spam_detect_models.predict(msg_vec)
if(y_pred2):
      print("* This message is spam ")
else:
    print("this message is Ham do not worry about it")
msg_vec = cv.transform(corpus2)


