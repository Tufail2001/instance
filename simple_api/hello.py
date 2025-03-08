from fastapi import FastAPI
import random

app = FastAPI()

# we will build two simple get enpoints
# side_hustle
# money_quotes
side_hustles =[
    "Freelancing - start offering your services online",
    "Dropshipping - Sell without inventory",
    "Stock Market - Invest and watch your money growth",
    "Affliate Marketing - Earn by promoting products",
    "Crypto Trading - Buy and Sell digital products!",
    "Online Courses - Share your knowledge and earn!",
    "Blogging - Create content and earn by ads and sponsorships!",
    "YouTube Channel - Earn by monetize ads and sposorships!",
    "Social Media Management - Mange accounts for brands and influencers!",
    "App Development - Create mobile and web applications for businesses!"
]

money_qoutes =[
    "Risk comes from not knowing what you're doing. - Warren Buffett",
    "The best investment you can make, is an investment in yourself. The more you learn, the more you’ll earn. - Warren Buffett",
    "Don't count the days, make the days count. - Muhammad Ali",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "The secret of getting ahead is getting started. - Mark Twain",
    "If you don’t build your dream, someone else will hire you to build theirs. - Tony Gaskins",
    "The successful warrior is the average man, with laser-like focus. - Bruce Lee",
    "Do not be afraid to give up the good to go for the great. - John D. Rockefeller",
    "The way to get started is to quit talking and begin doing. - Walt Disney", 
    "I have always been driven to buck the system, to innovate, to take risks—not because I thought it was cool, but because I believed it was the only way to make a difference. - Richard Branson",
    "It's fine to celebrate success but it is more important to heed the lessons of failure. - Bill Gates",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
    "The most dangerous poison is the feeling of achievement. The antidote is to every evening think what can be done better tomorrow. - Ingvar Kamprad ",
    "I knew that if I failed I wouldn’t regret that, but I knew the one thing I might regret is not trying. - Jeff Bezos",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchil"
]

@app.get("/side_hustles")
def get_side_hustles(apiKey: str):
    """Return a random side hustle idea"""
    if apiKey != "123456":
        return {"error": "Invalid API KEY"}
    return {"side hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    """Return Money Quotes"""
    if apiKey != "12345":
        return {'error': "Invalid apikey"}

    return {"money qtotes": random.choice(money_qoutes)}


