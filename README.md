## TouIST Service (Python)
This basic service allows the user to call the api and use it as a SAT-solver. This uses the tool TouIST.
TouIST is a language for propositional logic and can be used as a SAT-solver : https://touist.github.io/

# Getting Started
## Prerequisites
First of all you need to install the TouIST command-line tool.

I recommand to follow their repo instrutions to install the command-line tool. You might want to install it with opam. As this tool isn't maintained, we can't install it with brew.
https://github.com/touist/touist

As I was on Windows, I personnally installed it with OPAM.

Once installed, you can just run the application.
You will need this to be runned when the epistemic-reasonner is running so he can calls this service.

## Warning for Linux

Installing it with opam, you will probably have to use an environment to use opam and the tools installed on it with the following command :
```
eval $(opam env)
```
So each time you wan't to use Touist, you will have to run this before.
Saying this, you will have to run this eval command every time before running the python server.
Otherwise you will have an error.

## Setting up the application
### 1. Clone the repository
```
git clone https://github.com/Ethavanol/touist-service.git
cd touist-service
```

### 2. Install dependencies
```
pip install Flask flask_cors
```

### 3. Starting the application
```
python -m server
```
