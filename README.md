## TouIST Service (Python)
This basic service allows the user to call the api and use it as a SAT-solver. This uses the tool TouIST.
TouIST is a language for propositional logic and can be used as a SAT-solver : https://touist.github.io/

# Getting Started
## Prerequisites
First of all you need to install the TouIST command-line tool.

I recommand to follow their repo instrutions to install the command-line tool. Especially, if you are on windows, you might want to install it with opam.
https://github.com/touist/touist

As I was on Windows, I personnally installed it with OPAM.

Once installed, you can just run the application.
You will need this to be runned when the epistemic-reasonner is running so he can calls this service.

## Setting up the application
### 1. Clone the repository
```
git clone https://github.com/Ethavanol/touist-service.git
cd touist-service
```

### 2. Install dependencies
```
pip install
```

### 3. Starting the application
```
python -m server
```
