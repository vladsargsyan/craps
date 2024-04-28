##Installation
1. Clone this repository to your local machine:
git clone https://github.com/vladsargsyan/craps.git

2. Navigate to the project directory:
cd craps

3. Install the required libraries:
pip install -r requirements.txt

##Usage
1. Run the main.py script:
python main.py

##Game rules
The player should roll two dice. If the sum of both of them is 
7 or 11 the player wins. If the sum is 2, 3 or 12 (craps) the 
casino wins. If during the first roll the sum is 4, 5, 6, 8, 9 
or 10, that number becomes the “goal” number. To win, the player 
should roll the dice till they roll the goal number again. 
If the player rolls a 7 before rolling the goal number, they lose.