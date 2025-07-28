## TouIST Service (Python)
This basic service allows the user to call the api and use it as a SAT-solver. This uses the tool TouIST.
TouIST is a language for propositional logic and can be used as a SAT-solver : https://touist.github.io/

# Getting Started
## Prerequisites
First of all you need to install the TouIST command-line tool.

We recommand to follow their repo instrutions to install the command-line tool. You might want to install it with opam. As this tool isn't maintained, we can't install it with brew.
https://github.com/touist/touist

We personnally installed it with OPAM on both Windos and Linux.

Once installed, you can just run the application.
You will need this to be runned when the epistemic-reasonner is running so he can calls this service.

## Warning for Linux

Installing it with opam under Linux, you will have to use an environment to run the tools installed on opam.
So each time you want to use an opam-tool you will have to run the following command :
```
eval $(opam env)
```
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
!!!!!!IF ON LINUX and necessary for opam :
```
eval $(opam env)
```

Run the server

```
python -m server
```

### Configurations and Services

A folder cache_touist will be created at execution time.
It stores the constraints TouIST uses to generate the models/set of worlds.
In these files you will be able to see those constraints.